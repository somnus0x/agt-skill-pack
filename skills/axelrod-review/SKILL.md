---
name: axelrod-review
description: |
  Game-theory review loop for AI drafts: tit-for-tat trust tracking across review rounds.
  Review depth adapts to the author's track record of addressing feedback, so clean drafts
  earn lighter reviews and ignored flags trigger deep audits. Use for recurring content or
  code review loops.
---

# Axelrod Review — Game Theory for AI Review Loops

AI reviews are stateless. Same prompt, same depth, every time. Your reviewer doesn't know it flagged the same issue last round. It doesn't know you fixed everything it asked for. It treats every draft like it's meeting you for the first time.

This skill gives your AI reviewer **memory and consequences** — using the same tit-for-tat strategy that won Robert Axelrod's famous computer tournament in 1984.

## The Problem

You run an AI review on your draft. It flags 5 issues. You fix 3 of them (the other 2 were bad suggestions). Next review? Same depth. Same scrutiny. No reward for cooperation.

Worse: if you ignore feedback consistently, nothing changes either. No escalation. No consequences. The reviewer is a broken feedback loop.

## The Fix: Tit-for-Tat Review Dynamics

Track a **cooperation score** between you (the author) and the reviewer. The score adjusts review depth over time.

### How it works

```
cooperation_score = issues_addressed / (issues_found − rejected_with_reason)
                    (rolling avg, last 5 rounds)
```

Every flag gets one of three responses, each priced differently:

- **Fix it** → cooperation
- **Reject it WITH a one-line logged reason** → also cooperation (a wrong flag deserves a documented "no", not silent compliance)
- **Ignore it silently** → defection. Visible in the ledger immediately.

This is the key incentive: rejecting a bad flag costs one written line. Ignoring it costs trust. The cheap path and the honest path become the same path.

- **Score > 0.8 (high trust):** Light review — hook, accuracy, one standout issue only
- **Score 0.5–0.8 (standard):** Full review — all checks, all fixes
- **Score < 0.5 (low trust):** Deep audit — recurring issue tracking, verify every claim, no skimming

### Setup

#### 1. Create the trust ledger

Create `review-trust.json` in your project:

```json
{
  "meta": {
    "strategy": "tit-for-tat",
    "description": "Cooperation tracking for AI review loop",
    "started": "2026-01-01"
  },
  "rounds": []
}
```

#### 2. Define your review checklist

Replace this with whatever you review for. Examples:

**Content review:**
```
1. Language naturalness
2. Brag/ego filter
3. Hook strength
4. Structure (filler sections?)
5. Repetition check
6. Hedge/runway phrases
```

**Code review:**
```
1. Logic correctness
2. Edge cases handled
3. Security (injection, auth boundaries)
4. Performance (unnecessary loops, N+1 queries)
5. Readability (naming, structure)
6. Test coverage
```

#### 3. Drop-in prompt — copy this into your AI tool

```
Before reviewing, read review-trust.json and calculate:
- cooperation_score = avg(issues_addressed / (issues_found - rejected_with_reason))
  from last 5 rounds (rounds without the field: treat rejected as 0)
- recurring_issues = any issue type appearing in 2+ of last 3 rounds
- reviewer precision = (flags - flags_rejected_with_reason) / flags per reviewer,
  rolling last 5 rounds

Then adjust your review based on trust level:

If score > 0.8 AND rounds >= 3:
  "TRUST LEVEL: HIGH. Focus only on: critical issues and anything that breaks
  the output. Skip minor style/structure checks. Be brief."

If score 0.5-0.8 OR rounds < 3:
  "TRUST LEVEL: STANDARD. Full checklist review. Score and give specific fixes."

If score < 0.5:
  "TRUST LEVEL: LOW. Full checklist plus: check if these RECURRING issues are
  still present: [list from trust.json]. Verify every claim. Be harsh. If a
  previous issue reappears, call it out: RECURRING: [issue] was flagged in
  round N and is still here."

Always append to the review prompt:
  "PREVIOUS ROUND: Reviewer flagged [N] issues: [summary]. [X]/[N] were
  addressed. Watch for: [recurring issues or 'no patterns yet']."

If this reviewer's rolling precision < 0.7, also append:
  "CALIBRATION: [X] of your last [N] flags were rejected with documented
  reasons. Flag only what you are confident is wrong. Fewer, better flags."

After the review, judge every flag (fix / reject with reason / never silent),
then log the round to review-trust.json.
```

#### 4. The auto-correction loop (optional, advanced)

Run up to 3 review-fix-review cycles automatically:

```
for iteration in [1, 2, 3]:

  A. REVIEW with trust-aware prompt
     - Rotate models if available (different models catch different things)
     - 15s sleep between calls to avoid rate limits

  B. ASSESS
     - Score >= 9 AND issues <= 1 AND no recurring → EXIT (clean)
     - Iteration == 3 → EXIT (present remaining to human)
     - Otherwise → continue

  C. JUDGE every flag, then fix:
     - VALID → fix it
     - INVALID → reject WITH a one-line reason (logged)
     - Never skip a flag silently — silence is defection and it's visible
     - Two reviewers disagree → side with the one with higher rolling precision

  D. LOG the iteration

  E. RE-INJECT into next iteration:
     "PREVIOUS ITERATION (same draft): flagged [issues], fixed [fixes].
     Verify fixes landed. Watch for: [recurring]."
```

**Exit conditions:**
- **Clean:** score >= 9, issues <= 1, no recurring patterns
- **Max iterations:** 3 rounds done, remaining issues need human judgment
- **Infinite loop guard:** same issue appears in all 3 iterations unchanged → flag as "needs human input"

### Round vs Iteration

- **Iteration** = within-draft correction cycles (1-3 per draft). Short-term memory.
- **Round** = across-draft trust tracking (one per draft). Long-term cooperation score.
- A draft that takes 3 iterations to clean up is still 1 round.
- The round's `issues_found` = iteration 1 count. `issues_addressed` = resolved by final iteration.

### Log format

```json
{
  "round": 2,
  "post": "draft-name",
  "date": "2026-05-28",
  "depth": "standard",
  "iterations": 2,
  "iteration_log": [
    {"iteration": 1, "score": 8.5, "reviewer": "gemini", "issues": 3, "fixes": ["brag removed", "hedge cut", "transition added"]},
    {"iteration": 2, "score": 9.5, "reviewer": "codex", "issues": 0, "fixes": []}
  ],
  "issues_found": 3,
  "issues_addressed": 2,
  "rejected_with_reason": 1,
  "ignored_no_reason": 0,
  "rejection_reasons": [
    "gemini: suggested re-adding a qualifier that was cut on purpose — softens the thesis"
  ],
  "reviewer_flags": {"gemini": 2, "codex": 1},
  "reviewer_rejected": {"gemini": 1, "codex": 0},
  "issue_types": ["brag", "hedge", "structure"],
  "recurring": [],
  "cooperation_score": 1.0,
  "notes": "clean after 2 iterations"
}
```

`cooperation_score` here = 2 / (3 − 1) = 1.0. The rejected flag doesn't count against you — because you paid for the rejection with a reason.

### Reviewer calibration (pricing the other side)

Authors aren't the only players who can defect. A reviewer that flags everything ("looks thorough!") is defecting too — bad flags cost the author judgment time and are free for the reviewer. Price them:

```
precision = (flags − flags_rejected_with_reason) / flags   (rolling, last 5 rounds)
```

- **precision < 0.7** → calibration warning injected into the reviewer's next prompt
- **precision < 0.5** → bench it: rotate to another model for a full window
- **Reviewers conflict** → side with the higher-precision reviewer

Now a junk flag isn't free — every rejected flag follows the reviewer for 5 rounds. Flag-everything stops being the dominant strategy, on both sides of the table.

## Why Tit-for-Tat

Robert Axelrod ran a programming tournament in 1984. Game theorists submitted strategies for the iterated Prisoner's Dilemma. The winner — Anatol Rapoport's tit-for-tat — was also the simplest: 4 lines of code.

It won because of four properties:

- **Nice** — cooperate first, never defect first
- **Retaliatory** — punish defection immediately
- **Forgiving** — after punishment, return to cooperation
- **Clear** — simple enough that the other player can predict your behavior

This skill encodes the same properties:

- **Nice** — first 3 rounds always run at standard depth
- **Retaliatory** — unaddressed issues trigger deeper review next round
- **Forgiving** — one clean round after a bad one resets depth
- **Clear** — the rules are in the prompt, the reviewer sees its own trust level

## When to use

- **Content drafts** — blog posts, documentation, newsletters, social media
- **Code review** — PR reviews, architecture docs, API contracts
- **Any iterative AI review** — anywhere you run the same review prompt repeatedly on different drafts

The key requirement: **repeated interaction with the same reviewer.** Tit-for-tat only works when there's history. One-shot reviews don't benefit from cooperation tracking.

## What you'll see

After a few rounds, patterns emerge from `review-trust.json`:

- Which issue types are recurring (your blind spots)
- Whether your cooperation score trends up or down
- Which reviewer (if rotating models) catches which types of issues
- How many iterations your drafts typically need before they're clean

The trust ledger becomes a mirror. It shows you what you consistently miss and how you respond to feedback.

## Technical notes

- **Everything local.** One JSON file. No cloud, no API, no database.
- **Model-agnostic.** Works with Claude, GPT, Gemini, DeepSeek, Codex — any LLM that can read a file and follow a prompt.
- **Zero dependencies.** No libraries, no install, no build step. Copy the JSON and the prompt.
- **Composable.** Works alongside any existing review workflow. Just add the trust context to your existing prompt.
