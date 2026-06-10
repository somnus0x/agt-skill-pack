---
name: product-taste
description: |
  Structured feature evaluation before enthusiasm or inertia makes the decision. Use for
  'should we build this' calls: what to build, what to cut, and the test that separates
  the two.
---

# Product Taste — What to Build, What to Cut

Taste isn't opinion. It's pattern recognition compressed into instinct. This skill builds product taste by forcing structured evaluation before enthusiasm or inertia makes the decision for you.

## The Taste Test

When evaluating a feature, idea, or product decision — run it through five filters in order. Stop at the first filter that kills it.

### Filter 1: Who suffers without this?

Name the specific person. Not "users" — one person with a context and a pain. If you can't name them, the feature is a solution looking for a problem.

Bad: "Users would benefit from group functionality."
Good: "A user who found a hot take on Twitter wants to share it with friends, but can't because the flow only supports solo use."

If the suffering is hypothetical or vague — kill the feature.

### Filter 2: What does this replace?

Every feature competes with doing nothing. The user's current workaround — however ugly — is working. What are they doing today instead? How painful is that workaround?

Rate the workaround pain:
- **Unbearable** → Build it
- **Annoying** → Maybe
- **Fine** → Don't build it

If the workaround is tolerable — the feature is a vitamin, not a painkiller. Vitamins lose to painkillers every time in early-stage products.

### Filter 3: Does this make the core loop stronger?

Every product has one core loop. Define yours first (e.g., discover → create → engage → resolve). Every feature should make one step of this loop faster, easier, or more frequent.

If the feature doesn't touch the core loop — it's a distraction. A settings page, an analytics dashboard, a profile customization system — none of these make more core actions happen.

Ask: "Does this make someone do the core action faster?" If no — cut it or defer it.

### Filter 4: What's the cost of being right?

Assume the feature works perfectly. Users love it. Now what?

- Does it increase surface area you have to maintain?
- Does it add new state to manage?
- Does it create a new failure mode?
- Does it split attention across two things instead of focusing on one?

The best features have low cost-of-being-right. They fold into existing flows without adding new edges. The worst features succeed and then demand permanent maintenance.

### Filter 5: Would you use the product WITHOUT this?

If yes — it's not essential. Ship without it. Add it when someone screams.

The products with the best taste are defined by what they refused to build, not what they shipped.

## Output Format

```
TASTE CHECK — [feature name]

Filter 1 (Who suffers): [pass/fail] — [1 sentence]
Filter 2 (Replaces what): [pass/fail] — workaround pain: [unbearable/annoying/fine]
Filter 3 (Core loop): [pass/fail] — [which step it strengthens, or "none"]
Filter 4 (Cost of being right): [low/medium/high] — [what it adds permanently]
Filter 5 (Ship without it): [yes/no]

Verdict: [BUILD / DEFER / KILL]
[1 sentence — the real reason]
```

## Taste-Building Exercises

### Exercise 1: Teardown

Pick a product you admire. List its features. For each one: "If they removed this tomorrow, would you switch to a competitor?" The features where the answer is "no" reveal what's decoration vs load-bearing.

### Exercise 2: Subtraction Game

Take your current product's feature set. Remove one feature. Which removal hurts users most? That's your most important feature. Keep removing until only the core loop remains. The order of removal IS your priority stack.

### Exercise 3: The "1000 Users" Filter

Imagine your product has exactly 1000 daily active users. Which feature request would 900 of them care about? Which would 50? Build for the 900. The 50 who want niche features are loud but not representative.

### Exercise 4: Study What Ships

Follow 3-5 products in your space. Track what they actually ship each month (not what they announce or roadmap). After 3 months, look at the pattern. What did they prioritize? What did they cut? What does that tell you about what the market actually values?

## What This Skill Is NOT

- Not a prioritization framework (use RICE or ICE for that — this is upstream of frameworks)
- Not a product management process
- Not market research
- This is about developing the INSTINCT that precedes all of those tools

---

*From [AGT Skill Pack](https://github.com/somnus0x/agt-skill-pack) — free skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand)*
