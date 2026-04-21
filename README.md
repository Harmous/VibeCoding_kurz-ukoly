# VibeCoding_kurz-ukoly

Řešení úkolu pro vibe coding kurz je ve složce [`Lekce1`](./Lekce1).

## Run

```bash
cd Lekce1
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

Před spuštěním je potřeba doplnit `OPENAI_API_KEY` do `Lekce1/.env`.
