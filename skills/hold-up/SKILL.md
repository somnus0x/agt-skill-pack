---
name: hold-up
description: |
  Pump the brakes — clarify before acting. Use when a request is exploratory,
  mid-decision, or underspecified and the AI is about to edit, commit, hand off,
  deploy, or run a workflow on a partial picture. Fires on /hold-up or "just talk",
  "don't action this", "let's think first" — or auto-fires when the AI catches
  discuss-mode cues right as it was about to take a non-trivial action.
---

# Hold Up — Clarify Before You Act

You ask "should we do X?" and the AI has already done X. You think out loud — "i think maybe we move this to a queue" — and it's three files deep into building a queue. You wanted to *talk*; it heard an *order*.

This is the #1 friction of agentic coding: the AI reads exploratory messages as commands, and acts on inferred scope. Hold Up is the brake. It catches the AI mid-sprint, before the wrong action, and trades one clarifying turn for the rework-and-trust cost of building the wrong thing.

## Why

AI coding tools are biased toward **action**. Ambiguity gets resolved by *doing*, not asking — because doing looks helpful. But a question costs one turn; a wrong action costs the rework, the cleanup, and a chunk of your trust that it understood you. The asymmetry is brutal and one-directional.

The failure isn't "the AI is dumb." It's that it can't tell **discuss-mode** from **do-mode**, so it defaults to do. Hold Up installs the missing check: *is this person asking me to act, or thinking out loud?* — run **before** any non-trivial action, not after.

## How it differs from `grill-me` and PLAN mode

- **`grill-me`** = a deliberate, invoked, *exhaustive* interview. You summon it to walk the entire design tree before a big build. Heavyweight, on-demand.
- **PLAN mode** = "design the implementation, don't edit yet." Still assumes you've decided to build.
- **Hold Up** = automatic, reflexive, *one question*. It fires itself when it smells discuss-mode, asks the single thing it needs, and either releases or escalates. Lightweight, always-on.

The chain: **Hold Up** catches "wait, do you even want me to build?" → if yes and it's big → escalate to **`grill-me`** → then build. Hold Up is the front door; grill-me is the interrogation room.

## When to use

### Explicit

Say `/hold-up`, "just talk", "don't action this", "let's think first", "discuss before you build", "wait wait".

### Auto-fire (the real value — add to your CLAUDE.md)

Fire Hold Up automatically when **both** are true:

1. **A non-trivial action is about to happen** — an edit, commit, file creation, handoff, deploy, schema change, or running a workflow/script.
2. **Discuss-mode cues are present:**
   - hedge words: "i think", "maybe", "should we", "wydt", "tbh", "kinda"
   - a question with no imperative verb ("can this be done per-project?" not "do it per-project")
   - the user is mid-decision, weighing options, or thinking out loud
   - no clear "build X" / "fix Y" / "do Z" instruction

**Don't fire for:** a clearly-scoped request with a full picture ("add a unique constraint to the users table"), trivial reversible actions (config tweak, log read, rename), or when the user already said "just do it" / "go" / "quick". Over-firing into clarification-spam is its own failure — the guard against it is this list.

## The brake (run before any non-trivial action)

Four checks, in order:

### 1. Mode — discuss or do?

Scan for the cues above. No imperative verb + a hedge + a question = discuss. A clear "do X" with a full picture = do.

### 2. Picture — full, or am I inferring something load-bearing?

Is there a detail I'd have to *guess* to act — a file path, a target, a value, which-of-three-things-they-mean? If the guess is load-bearing, I don't get to make it silently.

### 3. Asymmetry — when unclear, one question beats one wrong action

A clarifying question costs one turn. A wrong action costs rework + cleanup + trust. Unclear ⇒ ask. Always.

### 4. Keep speed — clear do + full picture ⇒ release immediately

If it's a scoped, reversible "do X" and the picture's complete: **act, no ceremony.** Hold Up is a brake, not a tax. Don't slow down clean requests.

## Output (in hold-up, you produce a READ — never an action)

1. **My read of the ask** — 1–2 lines, what I think you're actually asking
2. **The fork** — the decision as I see it, or 2–3 options
3. **ONE tight question** — the single thing that unblocks (not a questionnaire)
4. **What I'd do once you confirm** — so the release is instant

Then stop. Wait for the go.

## Release

The user gives the go — "go", "yea", "do X", or answers the question → act immediately.
- If the confirmed build is big → escalate into a `grill-me` session.
- If it's just a decision → stay in hold-up, resolve it, move on.

## The honest caveat

A skill is *pulled* — it can't fully catch "I acted before you stopped me," because by the time the skill loads, the action may already be mid-flight. So Hold Up is the **manual brake + self-catch nudge.** The always-on enforcement is the CLAUDE.md rule below — that loads every session with no trigger, so it's the seatbelt, not the airbag.

## Add to your CLAUDE.md

```markdown
### Hold-up reflex
Before any non-trivial action (edit / commit / handoff / deploy / run a workflow),
check the request mode:
- Discuss-mode cues ("i think", "should we", "wydt", "tbh", a question with no
  imperative verb, user mid-decision) → DON'T act. Output: your read of the ask +
  the fork + ONE tight question. Release on the user's go.
- Clear "do X" + full picture + reversible → just do it, no ceremony.
When unclear, one question beats one wrong action — the asymmetry is one-directional.
```

## Output discipline

When fired: the read, the fork, the one question, the what-i'd-do-next. Nothing else. No preamble, no action. The whole point is to *not* do the thing yet.
