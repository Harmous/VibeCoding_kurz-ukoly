# Subagenti V Codex Workflow

Subagenti davaji smysl tam, kde lze praci rozdelit na mensi, nezavisle casti. V tomto ukolu jsou pouziti jako soucast nastaveneho workflow, nikoli jako plugin.

## Kdy Pouzit Explorer

Role `explorer` je vhodna pro:

- rychly audit ciziho repozitare
- hledani relevantnich souboru a vstupnich bodu
- overeni, kde je potreba zmeny provest

Priklad zadani pro explorera:

```text
Projdi referencni material a vytahni, co je relevantni pro nastaveni Codex agenta.
```

## Kdy Pouzit Worker

Role `worker` je vhodna pro:

- izolovanou implementaci jedne casti reseni
- pripravu dokumentace nebo konfigurace v oddelenem write scope
- opravy, ktere nejsou na kriticke ceste hlavniho agenta

Priklad zadani pro workera:

```text
Priprav dokument k MCP serverum a uprav jen soubory ve slozce docs/.
```

## Doporucene Rozdeleni Prace

1. Hlavni agent udrzuje plan a integruje vysledky.
2. `explorer` zmapuje referencni material nebo kodovou zakladnu.
3. `worker` zpracuje samostatnou cast reseni s jasne urcenym write scopem.
4. Hlavni agent vysledky overi, otestuje a pripravi finalni odevzdani.

## Pravidla Ktera Se Osvědcila

- nedelegovat bezprostredni blocker, pokud na vysledku stoji dalsi krok
- nedavat dvema workerum stejny write scope
- po navratu workera rychle zkontrolovat diff a zaintegrovat vysledky
- subagenty pouzivat jako zrychleni a nezavisly pohled, ne jako nahradu odpovednosti
