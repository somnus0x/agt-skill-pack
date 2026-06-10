---
name: claude-md-setup
description: |
  Set up a CLAUDE.md that stops AI guessing, claiming done without verifying, expanding
  scope past the ask, and forgetting between sessions. Use when configuring Claude Code
  rules for a repo or workspace.
---

# CLAUDE.md Setup — the rules that stop AI guessing, lying, overreaching, and forgetting

AI doesn't misbehave because the model is bad. It guesses when it doesn't know, says "done" before checking, expands scope past what you asked, and forgets everything the next session — because nobody told it not to. The fix isn't a smarter model. It's a CLAUDE.md that sets the rules once and loads them every session.

This skill gives you a working CLAUDE.md in four layers: **guardrails** (rules that stop the four misbehaviors), **memory** (so it stops repeating mistakes), **spec-driven** (so it never loses project state across /clear or /compact), and **your brain** (so it works the way you do, not the way a generic assistant does).

Everything here is battle-tested — pulled from a setup running daily from morning brief to production deploy. Copy the blocks, wire them, done.

## When to use

Setting up a new project, or fixing an AI that keeps guessing / claiming false completion / scope-creeping / forgetting across sessions.

Say: "setup claude md", "configure my AI rules", "stop AI guessing", "AI keeps forgetting", "claude md template".

## How CLAUDE.md works (30 seconds)

Claude Code reads `CLAUDE.md` from your project root automatically at the start of every session. Whatever's in it becomes standing instruction — no need to repeat yourself. Other agents (Cursor, etc.) have their own equivalent file; the rules below are portable, the filename isn't.

The four layers stack: guardrails are the floor (everyone needs them), memory is the loop (mistakes stop repeating), spec-driven is the save point (project state survives any context reset), your-brain is the personalization (it works like you).

---

## Layer 1 — Guardrails (paste as-is)

These four rules stop the four ways AI misbehaves: **เดา / โกหก / ทำเกิน / ลืม** (guess / lie / overreach / forget — the last one is Layer 2). Drop this block straight into CLAUDE.md.

```markdown
## Operating Rules

### NO MAGIC — don't guess
All assumptions explicit. If context is missing, state assumptions.
Don't hallucinate hidden infra or invent unspecified services.
If you don't know where something lives, ask — don't guess the path.

### VERIFY BEFORE DONE — no "done" without evidence
Never claim a change is complete without running verification.
"I edited the file" is not done. "I edited the file and here's the output" is done.
No "should work now." Evidence before assertions, always.

### DISSENT — argue before you commit
Before any major change, surface concerns:
- What's the blast radius if this goes wrong?
- What assumptions are we making?
- What's the reversibility path?
- What are we NOT seeing because of momentum?

### SCOPE DRIFT — flag scope creep
Track stated goals vs actual execution. Flag when:
- "Just one more thing" accumulates
- Nice-to-haves get treated as must-haves
- The ask was "fix bug X" but we're now "refactoring the entire module"

### R0 / R1 / R2 — classify by reversibility
- R0 (irreversible) — STOP. Ask before proceeding.
- R1 (costly to reverse) — Do it, but tell me what and why.
- R2 (easily reversed) — Just do it. No permission needed.
```

Why these four: an AI without rules either asks about everything (slow) or does everything (dangerous). VERIFY is the load-bearing one — AI's default is "answer to completion," so it'll say "done" without running anything. R0/R1/R2 gives it a framework for when to stop vs when to run.

---

## Layer 2 — Memory (so it stops repeating mistakes)

By default AI has no memory across sessions. Teach it something today, it's gone tomorrow — same mistake, next session. Fix: a `MEMORY.md` the AI writes to itself whenever it fails, wired to load every session.

**Step 1 —** Create `MEMORY.md` in your project root.

**Step 2 —** Add this line near the top of CLAUDE.md so the memory loads every session:

```markdown
@MEMORY.md
```

**Step 3 —** Add this rule to the Operating Rules block:

```markdown
### LEARNING CAPTURE — log failures, don't repeat them
When you identify a pattern failure or operational mistake:
1. Log it to MEMORY.md
2. Include three fields: what happened / root cause / correct behavior
3. Make the correct-behavior a command you can follow, not a feeling
```

The three-field schema is the whole trick. "AI messed up X" is useless next session. This is what a real entry looks like:

```markdown
R2 permission-asking (May 29):
- what: asked "should I do 1 and 2?" on an edit that's trivially reversible
- root cause: habit of asking confirm before editing config instead of classifying first
- correct: if it's R2 → just do it, then report. Don't ask.

Read/write pipeline half-wired (May 29):
- what: cron wrote a daily file nobody read
- root cause: built the write side, never wired the read side
- correct: any pipeline with read+write — verify BOTH sides, not just the producer
```

Every failure becomes a line the next session reads before starting. The loop tightens: fail → log → next session reads it → doesn't repeat → fails something new → log. Each turn the circle narrows.

---

## Layer 3 — Spec-driven (so it never loses the plot)

MEMORY.md stops repeated *mistakes*. But there's a second kind of forgetting: every `/clear`, `/compact`, or crash wipes *project state* — and you're back to spending 15-20 minutes explaining "what are we building, how far did we get, what did we agree on." The fix isn't a longer context window. It's a `spec.md` the AI updates itself after every task, so the next session reads one file and continues exactly where the last one stopped.

Context lives in two places: **implicit** (inside the session — the chat history) and **explicit** (a file on disk). Implicit context dies on `/clear` and degrades as token count climbs — like RAM that starts to swap. Explicit context is constant. `spec.md` is your save point: like saving a game before you quit, then reopening and loading the save.

**Step 1 —** Create `spec.md` in your project root with four sections:

```markdown
# [project] — [one-line goal]

## Architecture
What components exist, how they connect, what tech each uses.
The actual current shape of the system, not a wishlist.

## Done
What's built — and the decisions behind it. Not "added auth" but
"added auth via X because Y, rejected Z." The *why* is the part the
next session can't reconstruct.

## Todo / Out of scope
The backlog updated every task. Include what's deliberately NOT being
built, so the AI doesn't helpfully add it.

## Current state
The save point. "What am I doing right now / where am I stuck / what's
the next concrete step." The most important section.
```

The four sections map to the four questions a fresh session always asks: *what is this / what's done and why / what's left / where exactly did we stop.* `Current state` is load-bearing — the difference between "read spec.md and continue" and "let me re-read the whole codebase to figure out where we are."

**Step 2 —** For anything that crosses a component boundary, add a contracts block. New sessions do the most damage here — they can't know what field the frontend sends the backend unless it's written down, so they guess, guess wrong, and you debug what a past session already settled.

```markdown
## Data Contracts
Interfaces between components — the AI may not change these without flagging.

- API response:        { id: string, status: "ok" | "error", data: T }
- Frontend → backend:  { userId: string, amount: number, chain: string }
```

**Step 3 —** Add this rule to the Operating Rules block so the AI maintains the spec itself — you will not remember to say "update spec.md" every time, so make it standing:

```markdown
### SPEC-DRIVEN — the spec is the source of truth, not the chat
At session start: read spec.md before doing anything.
After completing any task:
1. Update spec.md — current state, decisions made, what's next.
2. Update data contracts if any interface changed.
3. Never claim "done" without updating spec.md first.
```

Both halves are required: write-on-finish and read-on-start. A spec nobody reads is a diary; a spec nobody writes goes stale in a day. Wire both sides and `/clear` becomes free — context no longer lives in the session, it lives in a file. Even with infinite context this wins: writing the spec *forces* the AI to organize its understanding instead of just "remembering" the chat. A long chat degrades as it grows; a short spec stays sharp.

---

## Layer 4 — Your brain (so it works like you)

Guardrails are universal. This layer makes the AI think like *you* — your decision style, your voice, your common tasks. You don't write it by hand. You let an AI that already knows you extract it.

Open a chat you've used a lot (Claude, ChatGPT, whatever you talk to often) and run these three prompts. Paste the output into CLAUDE.md.

**Prompt 1 — work patterns:**
```
Analyze all our conversations. Extract my work patterns: how I make
decisions, what I prefer, what I reject, how I communicate. Write it
as a set of rules that another AI can follow.
```

**Prompt 2 — voice:**
```
Analyze how I write messages. What's my tone? What words do I use?
What do I never say? Write a 'Voice' section that another AI can use
to match my communication style.
```

**Prompt 3 — skill triggers:**
```
List the topics I ask about most frequently. Group them into categories.
For each category, write a trigger condition (if user mentions X, do Y).
Format as a table.
```

This beats hand-writing prompts. You're not optimizing one prompt at a time — you're pulling your whole working pattern out in one shot, so every AI you use inherits it. You don't have to be good at prompting. You just have to have talked to it enough that it can see your pattern, then ask it to write that pattern down.

---

## Assembly — the whole setup in order

1. Create `CLAUDE.md`, `MEMORY.md`, and `spec.md` in your project root.
2. Paste the **Layer 1 guardrails** block into CLAUDE.md.
3. Add `@MEMORY.md` near the top + the **LEARNING CAPTURE** rule.
4. Paste the **Layer 3 spec.md scaffold** (four sections + contracts) and add the **SPEC-DRIVEN** rule to the Operating Rules block.
5. Run the **Layer 4 extraction prompts**, paste the output (work patterns / voice / skill triggers) into CLAUDE.md.
6. Next session, Claude Code loads all of it automatically — start with "read spec.md" and it continues where you stopped. When it slips, tell it to log to MEMORY.md.

That's the full setup: rules that stop the misbehavior, memory that stops the repeat, a spec that survives every context reset, and your own working pattern so it stops feeling like a generic assistant.
