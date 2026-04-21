from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent
MODEL = "gpt-4.1-mini"
DEMO_PROMPT = (
    "Převeď 5 kilometrů na míle, 10 kilogramů na libry a 25 stupňů Celsia "
    "na Fahrenheit. Odpověz stručně česky."
)
SYSTEM_PROMPT = (
    "Jsi užitečný asistent pro převody jednotek. "
    "Když uživatel chce převod mezi podporovanými jednotkami, vždy použij tool "
    "`convert_unit`. Výsledky shrň stručně a česky."
)


def load_dotenv_file(path: Path | None = None) -> None:
    # Load local configuration from the project directory so the script works
    # the same way regardless of the current working directory.
    env_path = path or (BASE_DIR / ".env")
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        os.environ.setdefault(key, value)


def normalize_unit(unit: str) -> str:
    return unit.strip().lower().replace(" ", "_")


def convert_unit(value: float, from_unit: str, to_unit: str) -> dict[str, Any]:
    from_unit = normalize_unit(from_unit)
    to_unit = normalize_unit(to_unit)

    if from_unit == to_unit:
        result = value
    elif {from_unit, to_unit} == {"km", "miles"}:
        result = value * 0.621371 if from_unit == "km" else value / 0.621371
    elif {from_unit, to_unit} == {"kg", "lb"}:
        result = value * 2.20462 if from_unit == "kg" else value / 2.20462
    elif {from_unit, to_unit} == {"celsius", "fahrenheit"}:
        if from_unit == "celsius":
            result = (value * 9 / 5) + 32
        else:
            result = (value - 32) * 5 / 9
    else:
        raise ValueError(
            "Unsupported conversion. Use only km<->miles, kg<->lb, or "
            "celsius<->fahrenheit."
        )

    return {
        "status": "ok",
        "value": value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "result": round(result, 4),
    }


def execute_tool_call(tool_call: Any) -> str:
    if tool_call.name != "convert_unit":
        return json.dumps(
            {
                "status": "error",
                "message": f"Unknown tool: {tool_call.name}",
            },
            ensure_ascii=False,
        )

    try:
        arguments = json.loads(tool_call.arguments)
        result = convert_unit(**arguments)
    except ValueError as error:
        result = {"status": "error", "message": str(error)}
    except (TypeError, json.JSONDecodeError) as error:
        result = {"status": "error", "message": f"Invalid tool arguments: {error}"}

    return json.dumps(result, ensure_ascii=False)


def build_tools() -> list[dict[str, Any]]:
    return [
        {
            "type": "function",
            "name": "convert_unit",
            "description": (
                "Convert values between supported units. "
                "Supported pairs are km<->miles, kg<->lb, and "
                "celsius<->fahrenheit."
            ),
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "Numeric value to convert.",
                    },
                    "from_unit": {
                        "type": "string",
                        "enum": ["km", "miles", "kg", "lb", "celsius", "fahrenheit"],
                        "description": "Unit of the input value.",
                    },
                    "to_unit": {
                        "type": "string",
                        "enum": ["km", "miles", "kg", "lb", "celsius", "fahrenheit"],
                        "description": "Target unit for the conversion.",
                    },
                },
                "required": ["value", "from_unit", "to_unit"],
                "additionalProperties": False,
            },
        }
    ]


def run_demo() -> str:
    prompt = " ".join(sys.argv[1:]).strip() or DEMO_PROMPT
    load_dotenv_file()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Set it in the environment or create a .env file."
        )

    client = OpenAI(api_key=api_key)
    tools = build_tools()
    # First request: give the model the user prompt and the tool definition.
    response = client.responses.create(
        model=MODEL,
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        tools=tools,
        parallel_tool_calls=False,
    )

    for _ in range(5):
        tool_outputs = []

        for item in response.output:
            if item.type != "function_call":
                continue

            # Execute the requested tool locally and send the structured result
            # back to the model in the next Responses API call.
            tool_outputs.append(
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": execute_tool_call(item),
                }
            )

        if not tool_outputs:
            return response.output_text

        response = client.responses.create(
            model=MODEL,
            input=tool_outputs,
            previous_response_id=response.id,
            tools=tools,
            parallel_tool_calls=False,
        )

    raise RuntimeError("Model exceeded the tool-calling iteration limit.")


def main() -> int:
    try:
        prompt = " ".join(sys.argv[1:]).strip() or DEMO_PROMPT
        final_answer = run_demo()
        print("Prompt:")
        print(prompt)
        print("\nOdpověď modelu:")
        print(final_answer)
        return 0
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
