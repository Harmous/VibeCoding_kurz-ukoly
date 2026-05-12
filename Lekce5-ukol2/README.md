# Nastaveni Kodovaciho Agenta Pro Codex

Toto odevzdani sdili prakticke nastaveni kodovaciho agenta `Codex` bez pouziti pluginu nebo marketplace. Reseni je pripravene jako maly demonstracni projekt se skutecnou Codex strukturou:

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.agents/skills/*/SKILL.md`

Reseni je samostatne. Neobsahuje kurzovni referencni repozitar ani pluginy.

## Obsah Reseni

- `AGENTS.md` - guardrails pro chovani agenta v tomto ukolu
- `.codex/config.toml` - lokalni konfigurace s MCP servery a zapnutym multi-agent workflow
- `.codex/agents/dead-code-analyzer.toml` - ukazka specializovaneho subagenta
- `.agents/skills/vibe-kurz-workflow/SKILL.md` - vlastni skill pro kurzovni workflow
- `docs/mcp-servers.md` - vysvetleni MCP konfigurace
- `docs/subagents.md` - vysvetleni rozdeleni prace mezi subagenty
- `demo-app/` - jednoduchy lokalni projekt pro demonstraci skillu a subagenta
- `demo-prompts.md` - tri konkretni prompty pro MCP, skill a subagenta

## Co Je Timto Ukolem Demonstrovano

1. **AGENTS.md** jako trvala instrukce pro repozitar.
2. **MCP servery** pres nativni `.codex/config.toml` a `codex mcp`.
3. **Skilly** pres lokalni skill v `.agents/skills`.
4. **Subagenty** pres specializovanou konfiguraci v `.codex/agents`.

## Doporuceny Postup Vyzkouseni

1. Spustte Codex v teto slozce:

```bash
cd /home/kali/Documents/VibeCoding-kurz/Repositories/VibeCoding_kurz-ukoly/Lekce5-ukol2
codex
```

2. Otevrete nektery prompt z `demo-prompts.md`.
3. Nechte Codex pracovat s lokalnim `AGENTS.md`, `.codex/config.toml`, `.codex/agents` a `.agents/skills`.

Alternativne lze spustit Codex rovnou z jineho mista:

```bash
codex -C /home/kali/Documents/VibeCoding-kurz/Repositories/VibeCoding_kurz-ukoly/Lekce5-ukol2
```

## Co Pri Vyzkouseni Uvidi Lektor

1. MCP server `openaiDeveloperDocs` je nakonfigurovan v `.codex/config.toml`.
2. Skill `vibe-kurz-workflow` je k dispozici v `.agents/skills`.
3. Subagent `dead-code-analyzer` je pripraven v `.codex/agents`.
4. Demo prompty v `demo-prompts.md` ukazuji jednu samostatnou ukazku pro MCP, skill i subagenta.

## Overeni

Staticke overeni konfigurace:

```bash
cd /home/kali/Documents/VibeCoding-kurz/Repositories/VibeCoding_kurz-ukoly/Lekce5-ukol2
python3 /home/kali/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/vibe-kurz-workflow
python3 - <<'PY'
import pathlib
import tomllib

for path in [
    pathlib.Path(".codex/config.toml"),
    pathlib.Path(".codex/agents/dead-code-analyzer.toml"),
]:
    tomllib.loads(path.read_text())
    print(f"OK {path}")
PY
```

Prakticke overeni v Codexu:

```bash
cd /home/kali/Documents/VibeCoding-kurz/Repositories/VibeCoding_kurz-ukoly/Lekce5-ukol2
codex
```

Potom postupne pouzijte prompty z `demo-prompts.md`.

## Prakticke Poznamky

- Konfigurace nepouziva plugins ani marketplace.
- MCP je demonstrovano pres URL server i stdio server.
- Skill je zamerne jednoduchy a znovupouzitelny pro dalsi kurzovni ukoly.
- Subagent je zamerne read-only, aby ukazka byla bezpecna a stabilni.
