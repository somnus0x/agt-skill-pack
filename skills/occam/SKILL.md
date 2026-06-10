---
name: occam
description: |
  The simpler-thing test: before a fix ships, prove the smaller version doesn't work. Use
  when code feels overbuilt, when complexity needs challenging, or when asking 'is this
  necessary'.
---

# Occam — The Simpler-Thing Test

You proposed a fix. Before it ships, prove the smaller version doesn't work.

## Why

AI coding tools are biased toward comprehensive solutions. You ask for a bug fix, you get a new service with 10 columns, 3 methods, and wiring at 12 call sites. The bug needed one database constraint.

Occam forces a checkpoint: show the minimum version, the proposed version, and the overbuilt version side by side. Then justify why you're not shipping the smallest one.

**This is NOT a veto.** Some complexity is correct. The point is to make the trade explicit before you commit.

## When to use

### Explicit

Say `/occam` or "is this necessary", "feels complex", "simpler", "why is this so much code", "in my head it's just X".

### Auto-fire (add to your CLAUDE.md)

Tell your AI to fire Occam automatically before finalizing any plan that introduces:

- A new database table or column whose only purpose is the current bug
- A new service, module, or provider
- A new helper class wrapping a single existing call
- A new background worker, cron, or scheduled job
- A new event type, queue, or pub/sub channel
- A new feature flag with only one consumer
- A function longer than ~60 lines that's mostly defensive branches
- Any abstraction justified by "we might need this later"

**Don't fire for:** one-line fixes, renames, test additions, config changes, following an existing pattern, or when you've explicitly said "go ahead, full version."

## The four questions

Run in order. Show your work.

### 1. Restate the user-visible bug in one sentence

What does the user see today that they shouldn't? If you can't say it in one sentence, the fix scope is too broad.

> Example: "When a user submits a form once, two identical records appear."

### 2. What is the minimum change that closes that exact sentence?

Often: one DB constraint, one early-return, one config flip, one bug fix in a single function. Resist the urge to refactor surrounding code.

> Example: "Add a UNIQUE constraint. INSERT-or-skip on every request. ~30 LOC, no new module."

### 3. What does the proposed (larger) version cover that the minimum doesn't?

List the extra failure modes. Be specific. "Future-proofing" is not a failure mode — name the actual scenario.

> Example: "The proposed version adds: pod-crash recovery via lease reclaim, in-flight observability via status field, full audit trail with error reasons."

### 4. Are those extra failure modes actually present today?

For each extra failure mode:

- **Has it happened in the last 30 days?**
- **What's the user-visible cost if it happens once?**
- **Can it be added later without a rewrite?**

If speculative OR cheap to lose once OR can be grown additively later → minimum wins.
If happening NOW and costs real money/trust → larger version wins.

## Output format

Three columns, then a verdict:

| | Minimum | Proposed | Could go further |
|---|---|---|---|
| **What** | The 1-sentence fix | The version under review | The maximally-defensive version |
| **LOC** | estimate | estimate | estimate |
| **Covers** | which failure modes | + extra failure modes | + everything imaginable |
| **Leaves** | what's unprotected | what's still unprotected | nothing (in theory) |

```
Verdict: <Minimum | Proposed | Further>

Reason: <one sentence tying the verdict to question 4>

If wrong: <what evidence would change this verdict>
```

The "if wrong" line is the most important part. It names the condition that would upgrade the verdict — so the decision is reversible without re-running the full audit.

## When NOT to apply

- **Real-money paths with no rollback.** Contract state, balance flows, anything irreversible → default to maximum defensive.
- **User explicitly named the failure mode.** They said "I want crash recovery" — don't re-litigate.
- **Following a binding spec.** If the spec mandates the larger version, don't undermine it.
- **One-shot operations.** Migrations, backfill scripts — defensive correctness is cheap when the code runs once and gets deleted.

## Add to your CLAUDE.md

```markdown
### Occam checkpoint
Before finalizing any plan that introduces a new table, service, module, worker,
queue, feature flag, or abstraction — run the Occam audit:
1. Restate the bug in one sentence
2. Show the minimum fix
3. Show what the proposed version adds
4. Ask: are those extra failure modes real, today, in production?
Output: three-tier comparison + verdict + "if wrong" condition.
```

## Output discipline

When invoked:

1. The one-sentence bug restatement
2. The three-column comparison
3. The verdict + reason + "if wrong" condition
4. Nothing else

Keep it short. The longer the audit, the more it becomes part of the complexity it's auditing.
