---
name: agent-boundaries
description: |
  Run multiple AI coding agents in parallel without collisions. Use when setting up
  parallel-agent workflows: defines file boundaries, a written contract between agents,
  and conflict rules so agents stop overwriting each other's work.
---

# Agent Boundaries — Run Many AI Agents Without Them Colliding

Run two or three AI coding agents in parallel and they start stepping on each other. One edits a file, another overwrites it, commits collide. The agents that were supposed to make you 3x faster make you slower — because now you're the traffic cop.

The fix is the same thing that fixes a human team that keeps colliding: **clear boundaries, a written contract, and you stepping out of the bottleneck.** This skill is the drop-in version of that.

## The Problem

You open 3 terminals — backend, frontend, contracts — to work in parallel. Without structure:
- Agent A edits a shared file, Agent B overwrites it
- Two agents touch the same module, commits conflict
- You become the only one who knows what's where — every decision routes through you
- "3 agents" turns into "3 sources of chaos you manage manually"

This isn't an AI problem. It's a **team structure** problem — the same one Conway's Law, Domain-Driven Design, and Team Topologies describe for human teams. The concepts drop straight onto agents.

## Setup: Find Your Boundaries (copy into your AI)

If your project is one big repo, have the AI map the domains *before* you split anything.

### Drop-in prompt (Thai):

```
วิเคราะห์ repo นี้แล้วบอกหน่อยว่าควรแบ่งเป็นกี่ domain
- แต่ละ domain ควรเป็นเจ้าของโฟลเดอร์/ไฟล์ไหนบ้าง
- มีจุดไหนที่ logic พันกันข้าม domain (cross-cutting concern)
  ที่ควรดึงออกมาเป็นส่วนกลาง
- ตั้งชื่อสิ่งเดียวกันให้ตรงกันทุก domain (ubiquitous language)
  มีคำไหนที่เรียกไม่เหมือนกันบ้าง
คืนมาเป็น map: domain → โฟลเดอร์ที่มันเป็นเจ้าของ
```

### Drop-in prompt (English):

```
Analyze this repo and tell me how to split it into bounded domains:
- Which folders/files should each domain own?
- Where is logic tangled across domains (cross-cutting concerns)
  that should be pulled into a shared layer?
- Are the same things named inconsistently (ubiquitous language)?
  List the mismatches.
Return a map: domain -> folders it owns.
```

The output is your boundary map. Each domain becomes one agent's territory.

## Setup: Give Each Agent Its Contract

Each agent (terminal / repo) gets a `CLAUDE.md` that states its boundary. This is the team API — the agent reads it, so you don't have to police it every turn.

### Drop-in CLAUDE.md block (per agent):

```markdown
## Boundary (this agent)
- You own: <folders, e.g. /api>
- You do NOT touch: <other domains' folders>
- Shared/cross-cutting code lives in: <shared path> — propose changes, don't edit silently
- Hand off to another domain by: <interface, e.g. a typed API contract / a PR note>

## Ubiquitous language (same names everywhere)
- "user" = the account holder (NOT "member", NOT "account")
- <add your project's canonical terms>
```

## The Three Moves (what the boundaries actually buy you)

1. **One agent = one domain.** Bounded context. They can't overwrite each other because they don't work in the same place.
2. **The rules live in the file, not your head.** CLAUDE.md is the contract. The agent reads its own boundary — you stop being the reminder.
3. **You stop being the bottleneck.** Agents communicate through the written interfaces (Conway's Law: your file structure becomes their communication path). You watch the whole board instead of refereeing every move — that's the platform role, not the traffic-cop role.

## When to use

- Running 2+ AI agents / terminals in parallel on one project
- Agents keep overwriting each other or producing conflicting commits
- You're the only one who knows what's where, and every decision routes through you
- Splitting a monolith repo into domains before going multi-agent
- Onboarding a new agent and wanting it to stay in its lane

## The concepts (drop these into your own CLAUDE.md)

- **bounded context** (DDD) — 1 agent owns 1 domain, no crossing
- **ubiquitous language** (DDD) — same name for the same thing everywhere; keep a glossary in CLAUDE.md so agents don't drift
- **cross-cutting concern** — logic that spans domains (auth, logging); pull it into a shared layer, don't let each agent reinvent it
- **Conway's Law** — your structure becomes their communication path; structure wrong = they coordinate wrong
- **platform vs stream-aligned** (Team Topologies) — agents do the feature work (stream); you + CLAUDE.md are the platform that lets them flow without asking you every step

## Read deeper

- *Team Topologies* — Skelton & Pais (team shapes, flow, platform thinking)
- *Domain-Driven Design* — Eric Evans (bounded contexts, ubiquitous language)

## Technical notes

- **Tool-agnostic.** Works with Claude Code, Cursor, Aider, Copilot — anything that reads a per-project instruction file.
- **No new tooling.** This is a structure + a contract file, not software to install. The leverage is the boundary, not a binary.
- **Scales down too.** Even one agent benefits from a written boundary map — it stops "helpful" edits outside the task.
