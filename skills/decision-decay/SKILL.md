---
name: decision-decay
description: |
  Detect when past decisions have gone stale because their inputs changed. Use to review a
  decision journal: flags choices whose assumptions the world has moved past, and forces a
  revisit-or-reaffirm call.
---

# Decision Decay — When Past Decisions Go Stale

Decisions are perishable. A choice that was correct in January may be wrong in March — not because the reasoning was flawed, but because the inputs changed. This skill detects when the world has moved and a past decision hasn't moved with it.

## The Decay Model

Every decision rests on assumptions about the world. When those assumptions change, the decision decays.

| Stage | Signal | Action |
|-------|--------|--------|
| **Fresh** | Assumptions still hold. No contradicting evidence. | No action needed. |
| **Aging** | One+ supporting assumptions weakened but not invalidated. | Flag for review within 2 weeks. |
| **Stale** | Core assumption invalidated. Better alternatives exist. Staying costs more than switching. | Active re-evaluation. |

## How to Use

### Step 1: Log your decisions

Keep a simple decision log (Notion, Obsidian, markdown file, whatever you use). Each entry needs:
- **What you decided** and **what you chose it over**
- **Date**
- **Why** — the reasoning at the time
- **Review date** — when to check if it still holds

Example:
```
DEC-001: Use Firebase over Supabase
Date: 2026-01-15
Chose: Firebase over Supabase
Why: Firebase Auth has better mobile SDK, team has Firebase experience, real-time listeners are simpler
Review: 2026-04-15
```

### Step 2: Extract the assumptions

For each decision, identify what had to be true for it to be correct. Usually 2-4 core assumptions.

For the example above:
1. Firebase Auth mobile SDK is better than Supabase Auth
2. Team has Firebase experience (reduces ramp-up)
3. Real-time listeners are simpler in Firebase than Supabase Realtime

### Step 3: Check assumptions against current reality

Use whatever signals you have — ecosystem news, GitHub activity, your own experience, competitor moves.

### Step 4: Score the decay

- All assumptions hold → **Fresh** → No action
- 1+ weakened → **Aging** → Review soon
- Core assumption broken → **Stale** → Re-evaluate now

## Output Format

```
DECISION DECAY REVIEW

DEC-[ID]: [brief title]
Made: [date] ([N] days ago)
Chose: [option A] over [option B]

ASSUMPTIONS AT DECISION TIME:
1. [Assumption] — Status: Fresh / Aging / Stale
   Evidence: [what changed or didn't]
2. [Assumption] — Status: Fresh / Aging / Stale
   Evidence: [what changed or didn't]

OVERALL: [Fresh / Aging / Stale]

[If Aging or Stale:]
WHAT CHANGED:
[Specific developments that weakened or broke the assumptions]

THE CASE FOR RECONSIDERING:
[What would you choose today if making this decision fresh?
What's the switching cost?]

THE CASE FOR STAYING:
[Why the original decision might still be correct.
Sunk cost is NOT a valid reason. Switching cost IS.]

RECOMMENDATION: [Stay / Review within [N] days / Actively reconsider]
```

## Decay Rates by Decision Type

Not all decisions decay at the same rate:

| Decision type | Decay rate | Review cadence |
|--------------|-----------|----------------|
| **Technology choices** (framework, SDK) | Fast | Monthly |
| **Architecture** (monolith vs micro, DB) | Medium | Quarterly |
| **Competitive positioning** | Fast | Monthly |
| **Pricing / business model** | Medium | Quarterly |
| **Team / process** | Slow | Quarterly |
| **Strategic bets** (which market) | Variable | Event-triggered |

## Review Schedule

- **Weekly quick scan** — Check decisions with review dates this week
- **Monthly full scan** — Re-evaluate all logged decisions
- **Event-triggered** — When big news hits your space, check if any decisions rest on assumptions that just changed

## The Hard Truth

The hardest output this skill produces: "This decision was correct when you made it. The world has changed. It's now wrong. Here's what switching costs. Here's what staying costs. Staying costs more."

That's when it earns its keep.

---

*From [AGT Skill Pack](https://github.com/somnus0x/agt-skill-pack) — free skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand)*
