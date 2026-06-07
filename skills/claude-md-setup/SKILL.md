# CLAUDE.md Setup — the rules that stop AI guessing, lying, overreaching, and forgetting

AI doesn't misbehave because the model is bad. It guesses when it doesn't know, says "done" before checking, expands scope past what you asked, and forgets everything the next session — because nobody told it not to. The fix isn't a smarter model. It's a CLAUDE.md that sets the rules once and loads them every session.

This skill gives you a working CLAUDE.md in three layers: **guardrails** (rules that stop the four misbehaviors), **memory** (so it stops repeating mistakes), and **your brain** (so it works the way you do, not the way a generic assistant does).

Everything here is battle-tested — pulled from a setup running daily from morning brief to production deploy. Copy the blocks, wire them, done.

## When to use

Setting up a new project, or fixing an AI that keeps guessing / claiming false completion / scope-creeping / forgetting across sessions.

Say: "setup claude md", "configure my AI rules", "stop AI guessing", "AI keeps forgetting", "claude md template".

## How CLAUDE.md works (30 seconds)

Claude Code reads `CLAUDE.md` from your project root automatically at the start of every session. Whatever's in it becomes standing instruction — no need to repeat yourself. Other agents (Cursor, etc.) have their own equivalent file; the rules below are portable, the filename isn't.

The three layers stack: guardrails are the floor (everyone needs them), memory is the loop (mistakes stop repeating), your-brain is the personalization (it works like you).

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

## Layer 3 — Your brain (so it works like you)

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

1. Create `CLAUDE.md` and `MEMORY.md` in your project root.
2. Paste the **Layer 1 guardrails** block into CLAUDE.md.
3. Add `@MEMORY.md` near the top + the **LEARNING CAPTURE** rule.
4. Run the **Layer 3 extraction prompts**, paste the output (work patterns / voice / skill triggers) into CLAUDE.md.
5. Next session, Claude Code loads all of it automatically. When it slips, tell it to log to MEMORY.md.

That's the full setup: rules that stop the misbehavior, memory that stops the repeat, and your own working pattern so it stops feeling like a generic assistant.
