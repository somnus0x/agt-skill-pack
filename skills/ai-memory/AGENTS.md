# AI Memory Skill

## Instructions
You have access to the AI Memory skill at `skills/ai-memory/SKILL.md`.

## Triggers
Activate this skill when the user mentions: AI memory, session search, hot cache, AI doesn't remember, find past conversation, search sessions, pre-load context, fts5, search index, session store.

## Workflow
1. Read `skills/ai-memory/SKILL.md`
2. Determine which part the user needs: long-term (session search), short-term (hot cache), or both
3. Provide the relevant drop-in prompt(s)
4. Show the CLAUDE.md wiring snippet so it works automatically

## Role
You help the user give their AI persistent memory across sessions. Two components: FTS5 search for past sessions (long-term) and hot cache for current state (short-term). Both are local-only, no cloud, no API keys.
