# Demo Prompts

Tyto prompty demonstruji MCP server, skill a subagenta nad obsahem teto slozky.

## 1. MCP Server

```text
Using the openaiDeveloperDocs MCP server, find how Codex CLI manages MCP servers and summarize the difference between `codex mcp list`, `codex mcp get`, and `codex mcp add`.
```

Co to prokazuje:

- agent pouziva MCP server pro oficialni dokumentaci
- neni potreba plugin ani marketplace

## 2. Skill

```text
Use $vibe-kurz-workflow and review this lesson directory. Tell me whether the deliverable is in the correct folder, whether the setup is documentation-first, and what should be checked before a signed commit.
```

Co to prokazuje:

- agent umi pouzit lokalni skill
- skill meni workflow a checklist odpovedi

## 3. Subagent

```text
Run dead-code-analyzer on ./demo-app and return only a cleanup report.
```

Co to prokazuje:

- hlavni agent umi delegovat specializovanou read-only analyzu na subagenta
- subagent ma vlastni konfiguraci v `.codex/agents`
- v `demo-app/app.js` jsou zamerne ponechane dve nepouzite polozky, aby mel subagent co najit
