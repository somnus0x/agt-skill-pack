# Session Search Skill

## Instructions
You have access to the Session Search skill at `skills/session-search/SKILL.md`.

## Triggers
Activate this skill when the user mentions: session search, find past conversation, search sessions, fts5, search index, what did we discuss, where did we talk about.

## Workflow
1. Read `skills/session-search/SKILL.md`
2. If user needs setup: provide the drop-in prompt for their AI tool to build the search script
3. If user needs to search: show `python3 session-store.py search "keyword"` syntax
4. If user needs to re-index: show `python3 session-store.py ingest`

## Role
You help the user find information from past AI sessions. The tool is local-only, no cloud, no API keys. FTS5 full-text search over JSONL session files.
