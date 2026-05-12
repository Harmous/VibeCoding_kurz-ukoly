# MCP Servery Pro Codex

Tento ukol nepouziva pluginy ani marketplace. MCP servery jsou pripojeny nativne pres `codex mcp`.

## Proc MCP

MCP server dava agentovi pristup k externimu zdroji nebo nastroji pres standardizovane rozhrani. V praxi je to vhodne napriklad pro:

- oficialni dokumentaci
- interni zdroje dat
- lokalni utility dostupne pres stdio

## Overeni Dostupnych Prikazu

Codex CLI podporuje:

```bash
codex mcp list
codex mcp get <name>
codex mcp add <name> --url <url>
codex mcp add <name> -- <command>
```

## Doporuzeny Server 1: OpenAI Developer Docs

Oficialni dokumentacni MCP server pro praci s OpenAI a Codex dokumentaci:

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
```

Overeni konfigurace:

```bash
codex mcp list
codex mcp get openaiDeveloperDocs
```

Odpovidajici zapis v `config.toml`:

```toml
[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

## Doporuzeny Server 2: Lokalni Stdio Server

Codex umi pracovat i se stdio MCP serverem. Vzor registrace:

```bash
codex mcp add localCodex -- codex mcp-server
```

Tento priklad demonstruje stdio variantu registrace bez pluginu. Pro realny projekt lze stejnym zpusobem pripojit vlastni lokalni MCP server nebo tymovou utilitu.

Odpovidajici zapis v `config.toml`:

```toml
[mcp_servers.localCodex]
command = "codex"
args = ["mcp-server"]
```

## Doporucene Pouziti V Praxi

- `openaiDeveloperDocs` pro dohledani aktualni oficialni dokumentace
- lokalni stdio server pro tymove utility, exporty nebo vlastni nastroje

## Co Timto Ukolem Demonstruji

- Codex muze byt rozsireny pres MCP bez pluginu
- konfigurace se da provadet primo pres CLI
- je mozne kombinovat URL server i stdio server
