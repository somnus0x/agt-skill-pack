---
name: ai-memory
description: |
  Give your AI long-term and short-term memory: keyword-searchable session history (FTS5
  index) plus a hot cache of current project state loaded at session start. Use when AI
  should remember past sessions and know project state without re-explaining.
---

# AI Memory — Give Your AI a Past and a Present

AI doesn't remember anything between sessions. Every new chat starts blank — no history, no context, no idea what you shipped yesterday.

This skill gives your AI two things it's missing:
1. **Long-term memory** — search past sessions by keyword (FTS5 index)
2. **Short-term memory** — know current project state at session start (hot cache)

## The Problem (two sides)

**Side 1: Can't find the past.**
You discussed an auth refactor two weeks ago. Made a decision. Wrote a great prompt. Now it's gone — buried in hundreds of session files with no search, no index.

**Side 2: Doesn't know the present.**
What shipped yesterday? What's blocked? When's the deadline? AI has no idea until you paste context manually. Every session. Every morning.

## Setup: Long-Term Memory (Session Search)

### Drop-in prompt (copy into Claude Code):

```
อ่านไฟล์ JSONL ทุกไฟล์ใน ~/.claude/projects/ ดึงแค่ข้อความ user + assistant ออกมา สร้าง SQLite database ที่มี FTS5 full-text search index ให้ search ด้วย keyword ได้ทันที เขียนเป็น Python script ชื่อ session-store.py ที่รับ command search, ingest, stats
```

English version:

```
Read all JSONL files in ~/.claude/projects/ and extract only user + assistant messages. Create a SQLite database with FTS5 full-text search index that can search by keyword instantly. Write it as a Python script called session-store.py that accepts commands: search, ingest, stats
```

One prompt. AI writes the script, runs ingest, ready to search.

### Usage

```bash
# Search across all sessions
python3 session-store.py search "refactor authentication"

# Output:
# [2026-05-10] interactive:a3f2...  (42,318 chars)
#   ...ต้อง refactor authentication flow เพราะ Privy session...

# Re-index after new sessions
python3 session-store.py ingest

# Show index stats
python3 session-store.py stats
```

### Manual setup (if you prefer)

Key components:
1. **Parser** — Read JSONL session files, extract `type: "human"` and `type: "assistant"` messages
2. **SQLite + FTS5** — Virtual table with `tokenize='unicode61'` for multilingual support
3. **CLI** — `search "keyword"`, `ingest` (rebuild index), `stats` (show counts)

No cloud, no API keys, no vector DB, no embeddings. FTS5 is built into Python's `sqlite3`.

## Setup: Short-Term Memory (Hot Cache)

### Drop-in prompt (copy into Claude Code):

```
อ่านไฟล์พวกนี้: [standup log, decisions.md, schedule.env, tester-gate.md] สรุปให้เหลือแค่ข้อมูลที่จำเป็น — เมื่อวาน ship อะไร, blocker ตอนนี้คืออะไร, deadline เมื่อไหร่, decision ไหนยัง active — save เป็น hot-cache.md
```

English version:

```
Read these files: [standup log, decisions.md, schedule.env, project-status.md] and summarize into only the essential information — what shipped yesterday, current blockers, upcoming deadlines, which decisions are still active — save as hot-cache.md
```

Replace the file list with whatever holds your project state: git log, TODO files, kanban boards, decision journals, sprint trackers, open PRs.

### What hot-cache.md looks like

```markdown
# Hot Cache — 2026-05-24

## Last Standup
- feature X ✅ shipped
- feature Y BLOCKED on [person]
- feature Z IN PROGRESS

## Active Decisions
- Auth approach: social-first (Privy) — active
- Deployment: Cloud Run — decided, not revisiting

## Deadlines
- Launch: June 2
- Demo: May 28

## Recently Modified Files (last 24h)
- src/auth/privy.ts
- contracts/Parimutuel.sol
```

### Keeping it fresh

- **Manual:** Before closing a session, tell the AI: "update hot-cache.md with what we did today."
- **Automated:** Set up a cron to refresh periodically:
```bash
0 */4 * * * cd /path/to/project && claude -p "Read [source files]. Update hot-cache.md." >> /dev/null 2>&1
```

## Wire It Up — Add to CLAUDE.md

This is the key step. Add these lines to your CLAUDE.md (or your AI tool's instruction file):

```markdown
Before starting work:
1. Read data/hot-cache.md for current context (blockers, decisions, deadlines)
2. If you need info from a past session, use: python3 session-store.py search "keyword"
```

Now every session starts with context and has access to history. No manual pasting.

## When to use

- "What did we decide about X?" — search past sessions
- "I wrote a good prompt for Y" — search and recover it
- "What shipped yesterday?" — hot cache knows
- Starting a new session on a multi-day task — hot cache has continuity
- Before making architectural decisions — search for past discussions on the topic

## Technical notes

- **Everything local.** No cloud, no API keys, no external services.
- **No vector DB.** FTS5 full-text search handles keyword lookup without embeddings.
- **Multilingual.** FTS5 `unicode61` tokenizer works with Thai, English, and mixed text.
- **Fast.** 800+ sessions (3M+ chars) searched in milliseconds.
- **Universal.** Works with Claude Code, Cursor, Copilot, Windsurf, Aider — any tool that reads files.
