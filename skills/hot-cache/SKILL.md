# Hot Cache — AI Knows Today Before You Tell It

Every new session starts blank. AI doesn't know what you shipped yesterday, what's blocked, or when your deadline is. You paste context manually, every morning, every session.

Hot cache fixes this: one markdown file that summarizes your current state. AI reads it at session start and knows everything.

## Why

Without hot cache, every session starts with:
- "What are we working on?" — you explain
- "What's the current status?" — you paste notes
- "What did we decide about X?" — you dig through files

With hot cache, the AI reads one file and already knows: what shipped, what's blocked, who's waiting on what, and when the deadline is.

## Setup

### Option A: Drop-in prompt (recommended)

Copy this prompt into Claude Code and let it build the file for you:

```
อ่านไฟล์พวกนี้: [standup log, decisions.md, schedule.env, tester-gate.md] สรุปให้เหลือแค่ข้อมูลที่จำเป็น — เมื่อวาน ship อะไร, blocker ตอนนี้คืออะไร, deadline เมื่อไหร่, decision ไหนยัง active — save เป็น hot-cache.md
```

Or in English:

```
Read these files: [standup log, decisions.md, schedule.env, project-status.md] and summarize into only the essential information — what shipped yesterday, current blockers, upcoming deadlines, which decisions are still active — save as hot-cache.md
```

Replace the file list with whatever files contain your project state. Common sources:
- Git log (`git log --oneline -10`)
- TODO files, kanban boards
- Decision journals
- Sprint/milestone trackers
- Open PRs (`gh pr list`)

### Option B: Manual template

Create `hot-cache.md` with this structure:

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

## Keeping it fresh

### Manual refresh
Before closing a session, tell the AI: "update hot-cache.md with what we did today."

### Automated refresh (cron)
Set up a cron job to rebuild hot cache periodically:

```bash
# Every 4 hours during work hours
0 */4 * * * cd /path/to/project && claude -p "Read [your source files]. Update hot-cache.md with current status." >> /dev/null 2>&1
```

## Add to your CLAUDE.md

```markdown
### Session context
Before starting work, read data/hot-cache.md to understand:
- What shipped recently
- Current blockers and who owns them
- Upcoming deadlines
- Active decisions that affect today's work
```

This is the key step — it makes the AI read the cache automatically at every session start.

## When to use

- Any project with state that changes daily
- Multi-day tasks where context carries over
- Team projects where decisions and blockers shift
- Solo projects with multiple workstreams

## How it pairs with Session Search

Hot cache handles the **present** — what's happening now.
Session Search handles the **past** — finding old discussions.

Together:
```markdown
Before starting work:
1. Read data/hot-cache.md for current context (blockers, decisions, deadlines)
2. If you need info from a past session, use: python3 session-store.py search "keyword"
```

## Technical notes

- **Just a markdown file.** No database, no service, no dependencies.
- **AI-readable.** Markdown is the native format for LLM context.
- **Compact.** A good hot cache is ~100-200 lines. If it's longer, you're including too much.
- **Disposable.** It gets overwritten every refresh. No history to maintain.
- **Universal.** Works with any AI tool that reads files: Claude Code, Cursor, Copilot, Windsurf, Aider.
