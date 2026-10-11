---
name: wrap
description: Write a compact session handoff so you can /clear and continue in a fresh, cheap context — the new session auto-loads it via a SessionStart hook. Use when the user says "wrap", "wrap up", "handoff and clear", "fresh session", "clear context", "reset context", or after the context-nudge HUD/hook warns (≥250K context or cold cache) at a natural boundary (post/feature/project done).
argument-hint: [focus for the next session]
---

# Wrap — handoff, then /clear

Why: a long main loop re-reads its whole context every call, so a short reply typed into a huge
chat after an idle gap costs the same as a long one. One cold resume at 800K context runs $5–10
at list price. A ~50-line brief carries what matters at a fraction of that.

You cannot run `/clear` yourself — your job is to make clearing lossless, then tell the user to
type it.

## Steps

1. **Path:** `python3 ~/.claude/hooks/session-handoff.py --path` → the one handoff file for this
   cwd. Overwrite it; never write elsewhere (never into the repo).
2. **Gather receipts, not memory** (one batch of read-only calls): `git status --short`,
   `git branch --show-current`, `git log --oneline -5`, branches ahead of origin — skip if not a
   git repo. Re-read any file you are about to cite.
3. **Write the brief** — terse, ≤ 60 lines, only what the next session can't cheaply re-derive
   from the repo:

```markdown
# Wrap — <cwd basename> — <YYYY-MM-DD HH:MM>
**Next:** <the single next action; use $ARGUMENTS if given>

## State
- Doing: <task in 1-2 lines>  · Branch: <b> · Uncommitted: <files or "clean">
- Done this session: <bullets, each with file:line or commit sha>

## Decisions (locked — don't relitigate)
- <decision> — because <why>

## Open
- <question / blocker / thing the user still has to decide>

## Gotchas
- <non-obvious things that cost time this session: wrong turns, corrected facts, tool quirks>

## Resume
- Files to read first: <paths>
- Commands: <exact commands to re-run / verify>
```

   Rules: corrected facts go in Gotchas (e.g. "the staging DB is NOT a copy of prod"). No
   secrets, no key values. Don't paste code — point to file:line. Don't restate CLAUDE.md.
4. **Surface stranded work:** if this session created/modified files that are uncommitted, or a
   branch is ahead of origin, say so in one line — don't commit unless asked.
5. **Hand over** — reply with exactly:
   - the handoff path and line count,
   - `Type /clear — the next session loads this automatically.` (also loads on a fresh `claude`
     start in this directory within 24h),
   - if the next task is a taste/design call, suggest `/model` *after* the clear; otherwise stay
     on the default.

If the user wants to keep going in the same session instead, suggest `/compact` with the **Next**
line as the focus.

---

## Install the other half

The skill writes the brief. A **SessionStart hook** is what loads it back after `/clear` — without
it you get a note that never returns. `install.sh` only copies this file, so fetch the three
scripts yourself:

```bash
mkdir -p ~/.claude/hooks
BASE=https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/skills/wrap/hooks
curl -sL $BASE/session-handoff.py -o ~/.claude/hooks/session-handoff.py
curl -sL $BASE/context-nudge.py   -o ~/.claude/hooks/context-nudge.py
curl -sL $BASE/statusline.sh      -o ~/.claude/hooks/statusline.sh
chmod +x ~/.claude/hooks/statusline.sh
```

Then merge into `~/.claude/settings.json`:

```json
{
  "env": { "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "400000" },
  "hooks": {
    "UserPromptSubmit": [{ "hooks": [{ "type": "command",
      "command": "python3 ~/.claude/hooks/context-nudge.py", "timeout": 5 }] }],
    "SessionStart": [{ "matcher": "clear|startup", "hooks": [{ "type": "command",
      "command": "python3 ~/.claude/hooks/session-handoff.py", "timeout": 5 }] }]
  },
  "statusLine": { "type": "command",
    "command": "~/.claude/hooks/statusline.sh", "refreshInterval": 30 }
}
```

What each piece does:

- `session-handoff.py` — SessionStart hook. On `/clear` (or a fresh start in the same directory
  within 24h) it injects the brief as context, then renames it `.consumed.md` so it never loads
  twice. Handoffs live in `~/.claude/session-handoffs/`, outside any repo.
- `context-nudge.py` — UserPromptSubmit hook plus a HUD line. Warns when the cache has gone cold
  at ≥150K context (*this turn rewrites ~$X*) and once per 250K step.
- `statusline.sh` — **optional, and Mac-shaped.** It chains the `claude-hud` plugin and then
  appends the nudge line, with a hardcoded Homebrew node path. If you don't use claude-hud,
  replace the first half with your own statusline command, or point `statusLine` straight at
  `python3 ~/.claude/hooks/context-nudge.py --hud`.

`CLAUDE_CODE_AUTO_COMPACT_WINDOW` is the part that works without you. It compacts before the main
loop passes 400K, so the habit doesn't have to hold.
