---
name: content-scout
description: |
  Pre-publish content intelligence skill. Before drafting any post, scout what's already
  performing on X/Twitter and across platforms. Uses Twitter CLI for real-time data and
  Manus for cross-platform deep research. Returns a structured report: what's trending,
  what's saturated, where the gaps are, and what angle to take.
triggers:
  - "scout"
  - "research before posting"
  - "what's trending"
  - "content gaps"
  - "before I post"
---

# Content Scout

Don't post blind. Scout what's already out there, find the gap, then draft from a position of knowledge.

---

## The Stack

Content Scout uses two tools. Set up both.

### 1. Twitter CLI — Real-Time X/Twitter Data

Install a Twitter CLI tool (e.g. [`twitter-cli`](https://github.com/missuo/twitter-cli), `twurl`, or similar). This gives you direct access to X/Twitter data — exact engagement numbers, timestamps, view counts — without a browser.

```bash
# Example: pull a topic's top posts
twitter search "AI marketing" --sort top --limit 20 --yaml
```

Why not browser scraping: CLI is faster, scriptable, and doesn't break when X changes their DOM. If your CLI supports search operators, you get surgical precision:

```
"AI marketing" min_faves:100 -filter:replies filter:blue_verified since:2025-05-15
```

Key operators:
- `min_faves:50` — skip noise, only proven posts
- `-filter:replies -filter:nativeretweets` — original content only
- `filter:blue_verified` — verified accounts only
- `since:YYYY-MM-DD` / `until:YYYY-MM-DD` — time window
- `"exact phrase"` — exact match
- `(A OR B)` — either term

### 2. Manus — Cross-Platform Deep Research

[Manus](https://manus.im) is an async research agent. Use it as a dead drop for large-scale scouting:

1. Drop a task: "Scout what's performing about [topic] on X, LinkedIn, Reddit, and newsletters in the last 7 days"
2. Manus browses all platforms, collects posts, extracts engagement data
3. You get back a structured dataset — posts, numbers, patterns
4. Feed the Manus output into Content Scout for the final intelligence report

When to use Manus vs Twitter CLI alone:
- **Twitter CLI** — quick scout, single platform, 5 minutes
- **Manus** — campaign planning, cross-platform landscape, quarterly strategy

---

## Workflow

### Step 1: Define Your Topic

What are you about to post about? Be specific. "AI" is too broad. "AI agents replacing junior devs" is searchable.

### Step 2: Run the Scout Rounds

Three rounds. Each answers a different question.

**Round 1: What's Performing Right Now**

Pull the top posts on your topic sorted by engagement. Twitter CLI with `--sort top` or Manus with "find highest engagement posts about [topic]."

Extract for each post:
- Author handle and follower range
- The angle they took
- The hook (first 1-2 sentences)
- Likes, RTs, replies, views

**Round 2: What's Fresh (Last 24-48h)**

Filter to recent posts gaining traction. Use `since:` operator or tell Manus "last 48 hours only."

Focus on:
- Emerging angles and debates
- Which posts are accelerating (high engagement relative to post age)
- What the audience is reacting to right now

**Round 3: What the Key Accounts Are Saying**

Filter to verified or high-follower accounts. Use `filter:blue_verified min_faves:100` or tell Manus "only accounts with 10K+ followers."

Focus on:
- What positions the thought leaders hold
- Their framing style
- Where they agree vs disagree with each other

### Step 3: Analyze and Find the Gap

After collecting data from all three rounds, synthesize:

- **What's working** — which angles get the most engagement?
- **What's saturated** — which angles have 20+ posts saying the same thing?
- **Where's the gap** — what has audience interest but few posts?
- **What hooks work** — what first-line patterns drive engagement?

### Step 4: Recommend Your Angle

Based on the gap analysis, recommend a specific angle that:
- Fills an underserved gap
- Matches the poster's voice and expertise
- Takes a position (not a summary)
- Has a proven hook pattern adapted to the new angle

---

## Output: Intelligence Report

```markdown
# Content Scout: [Topic]

## Data Collected
- X/Twitter: [N] posts via Twitter CLI
- Cross-platform: [N] posts via Manus (if used)
- Time range: [dates]

## What's Working
- [Angle 1] — @handle got [N] likes with "[hook excerpt]"
- [Angle 2] — @handle got [N] likes with "[hook excerpt]"

## What's Saturated
- [Angle] — [N] posts in last 48h, engagement declining
- [Angle] — every account saying the same thing

## Content Gaps
- [Gap 1] — audience asking about this in replies, nobody posting about it
- [Gap 2] — adjacent angle with high engagement, untapped variation

## Hook Patterns That Work
- [Pattern]: "[example first line]" — [N] likes
- [Pattern]: "[example first line]" — [N] likes

## Recommended Angle
[Specific position to take, with suggested hook]

## Avoid
- [Overdone angle]
- [Angle with declining engagement]
```

---

## For Marketing Teams

This fits directly into a content calendar:

1. **Monday planning** — scout all topics for the week, identify which gaps to fill which day
2. **Pre-draft checkpoint** — scout the specific angle before anyone writes
3. **Competitor watch** — scout what competitors posted this week, find what they missed
4. **Campaign prep** — scout audience sentiment on your campaign topic before launch

The skill turns "what should we post?" from a brainstorm into a decision backed by data.

---

## Tips

- **Scout the day you post** — content landscapes shift fast, yesterday's gap might be today's noise
- **Adjust thresholds for your niche** — use `min_faves:10` for niche topics, `min_faves:500` for mainstream
- **Use the gaps, not the trends** — the goal isn't to copy what's working, it's to say what nobody else is saying
- **Re-scout after big news** — industry events reset the entire landscape overnight
- **Manus for depth, CLI for speed** — don't over-engineer a quick pre-post check with a full Manus run
