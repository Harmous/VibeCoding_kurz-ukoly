# Lekce 1

Python demonstrace OpenAI Responses API s function callingem. Skript předá modelu lokální tool `convert_unit`, provede převody jednotek v Pythonu a výsledek vrátí zpět modelu pro finální odpověď.

## Requirements

- Python 3.10+
- OpenAI API key

## Project Files

- `main.py` - vstupní skript
- `requirements.txt` - Python dependencies
- `.env.example` - vzor lokální konfigurace

## Configuration

Vytvořte lokální `.env` ze vzoru a doplňte platný API klíč:

```bash
cp .env.example .env
```

```env
OPENAI_API_KEY=vloz_svuj_api_klic
```

Skript načítá proměnnou `OPENAI_API_KEY` ze souboru `.env` umístěného ve stejné složce jako `main.py`.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Volitelně lze předat vlastní prompt:

```bash
python main.py "Převeď 42 kilometrů na míle a 80 Fahrenheit na Celsius."
```

## Behavior

Bez argumentu skript odešle výchozí demo prompt. Pokud je předán vlastní prompt, použije se ten. Model má k dispozici tool `convert_unit`, který slouží jako lokální funkce pro samotný převod jednotek; LLM rozhoduje, kdy ho zavolat, a po vrácení výsledku vytvoří finální textovou odpověď v češtině.
