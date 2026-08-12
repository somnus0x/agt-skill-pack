---
name: worktree-sessions
description: |
  Give every parallel AI coding session its own checkout with git worktree, so agents
  stop fighting over one working tree, one index, and one branch. Use when running 2+
  agents/terminals on the SAME repo, when agents overwrite each other mid-edit, or when
  one agent's checkout/rebase moves the ground under another. Fires on "git worktree",
  "parallel sessions", "my agents fight over the same branch".
---

# Worktree Sessions — One Checkout Per Agent

You gave each agent a clean boundary. Agent A owns `/api`, Agent B owns `/web`, both read their `CLAUDE.md`, both behave. And they still break each other.

Because the collision isn't in the files. It's underneath them.

Two agents in one checkout share **one working tree, one index, one HEAD**. Agent A runs `git checkout -b feat/x` and Agent B, mid-edit, is suddenly on a different branch. Agent A runs `git add .` and stages half of Agent B's unfinished work. Agent B runs the test suite against a tree that A is rewriting in real time. Both dev servers grab `:3000`.

No `CLAUDE.md` rule fixes this, because no rule is being broken. The agents are obedient. The ground is shared.

## How this differs from `agent-boundaries`

- **`agent-boundaries`** = *who owns what.* Logical split — domains, folders, ubiquitous language, the contract each agent reads. Solves "the agent edited something that wasn't its job."
- **`worktree-sessions`** = *where they stand.* Physical split — one directory, one branch, one index per session. Solves "the agent did its job correctly and still corrupted the other one's state."

Use both. Boundaries without isolation still collide at the git layer. Isolation without boundaries just gives you three agents confidently building the same feature.

## The fix

`git worktree` has shipped with git since 2015 and almost nobody uses it. It gives you multiple checkouts of one repo, each on its own branch, all sharing a single `.git` object store. No second clone, no re-download, no duplicate history.

```bash
# from your main checkout
git worktree add ../myrepo-api  -b feat/api
git worktree add ../myrepo-web  -b feat/web
git worktree add ../myrepo-jobs -b feat/jobs
```

```
myrepo/         ← main checkout. read-only ground truth. nobody works here.
myrepo-api/     ← agent 1 lives here, on feat/api
myrepo-web/     ← agent 2 lives here, on feat/web
myrepo-jobs/    ← agent 3 lives here, on feat/jobs
```

Open one agent per directory. They now cannot touch each other's index, branch, or working tree — not because they were told not to, but because there is nothing to touch.

## The six rules

1. **One session = one worktree = one branch.** Never two agents in one checkout. This is the whole skill; everything else is support.
2. **The main checkout is read-only.** It's where you read history, compare, and merge. No agent gets a terminal there.
3. **Each worktree carries its own boundary block** (see `agent-boundaries`). Isolation stops corruption; boundaries stop duplicated work.
4. **One port per worktree.** Three dev servers will fight over `:3000` and the loser fails in a way the agent will "fix" creatively. Pin the port in each worktree's env file.
5. **Merging is the human gate.** Agents produce branches. You merge. No agent merges, rebases, or deletes another agent's branch — that is the one action that can destroy work outside its own isolation.
6. **Clean up when the session dies.** `git worktree remove ../myrepo-api` then `git worktree prune`. Stale worktrees hold branch locks and confuse the next session.

## Drop-in CLAUDE.md block (one per worktree)

```markdown
## Session isolation
- Your working directory is <ABSOLUTE PATH TO THIS WORKTREE>. Never `cd` above it.
- Your branch is <BRANCH>. Do not checkout, rebase, merge, or delete any other branch.
- Do not run `git add -A` from the repo root. Stage the files you actually changed.
- Dev server port for this worktree: <PORT>. Do not fall back to another port.
- If you need a change in a folder you do not own, write the request to
  ../handoff/<YOUR-BRANCH>.md. Do not edit it yourself.
```

## Handoffs: the part people get wrong

Worktrees share git objects. They do **not** share untracked files. So a `HANDOFF.md` sitting untracked in one worktree is invisible to every other agent, and a committed one drags merge conflicts into every branch.

Put handoffs in a plain directory **outside all the worktrees**:

```
../handoff/feat-api.md      ← "changed the /users response shape, web needs to update the type"
../handoff/feat-web.md
```

Not in git, readable by every agent, zero conflicts. Tell each agent to read the whole `../handoff/` directory before starting and append to its own file when it changes a shared interface.

## Setup prompt (drop into your AI, in the main checkout)

**Thai:**
```
repo นี้กำลังจะรัน AI 3 ตัวพร้อมกัน ช่วยตั้ง git worktree ให้หน่อย
- ดู branch ปัจจุบันกับ domain ใน repo แล้วเสนอว่าควรแยกกี่ worktree แต่ละอันชื่ออะไร branch อะไร
- เขียนคำสั่ง git worktree add ให้ครบทุกอัน (ยังไม่ต้องรัน ให้ผมดูก่อน)
- บอกว่าไฟล์ไหนบ้างที่ไม่ติดไปกับ worktree (พวก .env, node_modules) และต้อง copy อะไรบ้าง
- ตั้ง port ให้แต่ละ worktree ไม่ให้ชนกัน
- เขียน block "Session isolation" ใส่ CLAUDE.md ของแต่ละ worktree ให้ด้วย
```

**English:**
```
This repo is about to run 3 AI sessions in parallel. Set up git worktrees:
- Look at the current branches and domains, propose how many worktrees, with names and branches
- Write out every `git worktree add` command (do not run them yet, show me first)
- List what does NOT come along with a worktree (.env, node_modules, build caches) and what I must copy
- Assign a non-colliding dev server port per worktree
- Write the "Session isolation" block into each worktree's CLAUDE.md
```

## Gotchas (all verified, git 2.43)

- **Untracked files do not come along.** A fresh worktree contains tracked files only. Your `.env`, local certs, and seed data must be copied in. This bites on the first run, every time.
- **`node_modules` is per-worktree.** Each one installs its own. With pnpm the global store makes this cheap; with npm, expect real disk.
- **The same branch cannot live in two worktrees.** Git refuses:
  `fatal: 'feat/api' is already used by worktree at '/path/to/wt-api'`
  That refusal is a feature. It is git enforcing rule 1 for you, for free.
- **Hooks are shared** (they live in the one `.git`), but per-worktree state sits in `.git/worktrees/<name>/`. A hook that assumes it's running in the main checkout will misbehave.
- **Deleting the directory is not removing the worktree.** `rm -rf ../myrepo-api` leaves a stale registration. Use `git worktree remove`, or `git worktree prune` after the fact.

## When NOT to use this

- One agent, one repo. Worktrees add directories and buy you nothing.
- Agents working in genuinely separate repos. They're already isolated; what you need there is handoff, not worktrees.
- A repo whose build cannot tolerate multiple checkouts (absolute paths baked into config, a single shared local DB). Fix the build or accept sequential sessions. Three agents racing one dev database is not an isolation problem, it's a data problem.

## Technical notes

- **Tool-agnostic.** This is git, not an AI feature. Works with Claude Code, Codex, Cursor, Aider, or a human.
- **No new software.** Nothing to install, nothing to pay for, nothing to keep updated.
- **Scales down.** Even solo, one worktree per in-flight branch beats stashing.
- **Scales up honestly.** Large orgs bolt session registries, transcript sharing, and per-principal access on top of this. At one operator, the worktree is the whole win. Take the mechanical half; skip the org half until you have an org.

---

*From [Agent Dev Thailand](https://facebook.com/agentdevthailand) — free skills for people who run AI agents for real.*
