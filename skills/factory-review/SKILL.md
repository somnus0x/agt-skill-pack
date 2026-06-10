---
name: factory-review
description: |
  Cross-model adversarial critique: use a different AI model to review anything your
  primary AI produced — posts, specs, code, research, decisions. Same-model self-review
  falls into local minima; a different model catches different blind spots.
---

# Factory Review — Cross-Model Adversarial Critique

Use a **different AI model** to review anything your primary AI produced. Same-model self-review falls into local minima. A different model catches different blind spots.

## Why

Claude reviewing Claude's output has predictable blind spots. GPT reviewing Claude (or vice versa) catches what the original model was trained to overlook. Two-model review (executor + critic) produces better output than self-play.

## How to use

**Option A — Two chat windows:**
1. Draft something in your primary AI (Claude, GPT, Gemini, etc.)
2. Open a *different* AI in another tab
3. Paste the relevant review prompt below + your draft
4. Read the review, apply what's valid, ignore what's noise

**Option B — CLI tools (advanced):**
If you have access to multiple AI CLIs (Claude Code, Codex, droid, etc.), you can pipe content directly. See the CLI section at the bottom.

## Review Modes

### 1. Content Review (posts, threads, copy, docs)

Paste this into a **different AI** than the one that wrote your draft:

```
You are a critical reviewer for developer-audience content.

Review the following draft. Be adversarial — your job is to find problems, not praise.

Check for:
1. **Unsupported claims** — any numbers, benchmarks, or assertions without evidence?
2. **Missing context** — what would a developer reading this need to know that's not here?
3. **Logical gaps** — does the argument flow? Any leaps?
4. **Shareability blockers** — what would stop someone from sharing this? Too niche? Too vague?
5. **Voice drift** — does anything sound like marketing copy instead of a developer talking to peers?
6. **Factual errors** — any technical claims that are wrong or outdated?

Format your review as:
- VERDICT: [SHIP / REVISE / KILL] with one-line reason
- ISSUES: numbered list, severity (critical/medium/minor) for each
- STRONGEST PART: what works and why
- SUGGESTED FIX: for each critical/medium issue, a concrete rewrite suggestion

DRAFT:
---
[PASTE YOUR CONTENT HERE]
---
```

### 2. Spec / Architecture Review

```
You are a senior systems architect doing a design review. Be adversarial.

Review this specification. Your job is to find what breaks.

Check for:
1. **Unstated assumptions** — what must be true for this to work?
2. **Failure modes** — what happens when X goes wrong? Recovery path?
3. **Scope creep risk** — which parts are MVP-critical vs nice-to-have pretending to be critical?
4. **Missing edge cases** — what scenarios aren't covered?
5. **Scaling bottlenecks** — what breaks at 10x, 100x?
6. **Security surface** — auth boundaries, trust assumptions, external API risks
7. **Dependencies** — what external systems could block or break this?

Format:
- VERDICT: [APPROVE / REVISE / BLOCK] with one-line reason
- ASSUMPTIONS: list every unstated assumption
- FAILURE MODES: numbered, with severity and blast radius
- SCOPE VERDICT: what to cut for MVP
- SUGGESTED CHANGES: concrete, actionable

SPEC:
---
[PASTE YOUR SPEC HERE]
---
```

### 3. Code Review

```
You are a code reviewer. Be thorough and adversarial.

Review the following code changes. Focus on:
1. **Bugs** — logic errors, off-by-ones, race conditions, null derefs
2. **Security** — injection, auth bypass, secret leaks, OWASP top 10
3. **Performance** — unnecessary allocations, N+1 queries, missing indexes
4. **Maintainability** — unclear naming, missing error handling at boundaries, coupling
5. **Edge cases** — what inputs would break this?

Do NOT comment on style, formatting, or naming conventions unless they cause bugs.

Format:
- VERDICT: [APPROVE / REQUEST_CHANGES / BLOCK]
- ISSUES: file:line — description — severity
- APPROVE_IF: conditions for approval

CODE:
---
[PASTE YOUR CODE HERE]
---
```

### 4. Claims / Fact Check

```
You are a fact-checker. Verify the claims in this document.

For each factual claim (numbers, dates, comparisons, market data):
1. Is it verifiable? If yes, is it correct?
2. Is it outdated? What's the current figure?
3. Is it misleading? Technically true but implies something false?
4. Is it fabricated? No evidence this claim exists?

Format:
- VERIFIED: claims that check out
- OUTDATED: claims with newer data (include current figures)
- UNVERIFIABLE: claims you can't confirm or deny
- WRONG: claims that are factually incorrect

DOCUMENT:
---
[PASTE YOUR CONTENT HERE]
---
```

### 5. Quick Review (anything, 30 seconds)

```
Review this and tell me the 3 biggest problems. Be blunt. No praise.

---
[PASTE ANYTHING HERE]
---
```

## The Rule: You Are the Editor, Not the Reviewer

The reviewer model may be wrong. Models hallucinate. Don't blindly accept all feedback.

Your job after getting the review:
- Which points are real issues vs noise?
- Which fixes are worth the effort vs style preferences?
- Is the reviewer too conservative? ("Add more error handling" on internal code = noise)
- Did the reviewer miss the REAL issue while flagging minor ones?

**Example:** "Reviewer flagged 5 issues. #1 and #3 are real — fixing them. #2 is wrong because X. #4 and #5 are style preferences, skipping."

## Model Pairing Guide

| Your primary AI | Good reviewers |
|----------------|---------------|
| Claude | GPT, Gemini, DeepSeek |
| GPT | Claude, Gemini, DeepSeek |
| Gemini | Claude, GPT, DeepSeek |
| Any | Use a *different* model than the one that wrote it |

For **code**: DeepSeek or Claude tend to be strongest.
For **content**: GPT or Gemini catch different voice/logic issues.
For **fact-checking**: Gemini has broadest web knowledge.

## CLI Usage (Advanced)

If you use Claude Code, Codex CLI, or similar tools, you can automate the review:

```bash
# Example: pipe a file to a different AI CLI
cat my-draft.md | codex exec "Review this draft. Be adversarial. List the 3 biggest problems."

# Example: save review output
cat my-spec.md | your-cli-tool "Review this spec" > reviews/2026-05-28-spec-review.txt
```

The specific CLI command depends on your tools. The prompts above work with any model.

---

*From [AGT Skill Pack](https://github.com/somnus0x/agt-skill-pack) — free skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand)*
