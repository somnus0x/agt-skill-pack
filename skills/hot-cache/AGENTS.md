# Hot Cache Skill

## Instructions
You have access to the Hot Cache skill at `skills/hot-cache/SKILL.md`.

## Triggers
Activate this skill when the user mentions: hot cache, context file, session context, AI doesn't know what I'm working on, pre-load context, briefing file.

## Workflow
1. Read `skills/hot-cache/SKILL.md`
2. If user needs setup: provide the drop-in prompt and CLAUDE.md snippet
3. If user needs refresh: remind them to update before closing session, or set up cron
4. If user asks about pairing with session search: explain present (hot cache) vs past (session search)

## Role
You help the user set up a pre-computed context file so their AI knows the current project state at session start. No database, no service — just a markdown file that gets refreshed.
