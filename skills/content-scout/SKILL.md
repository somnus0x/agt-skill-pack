---
name: content-scout
series: Claude Code for Everyday Life
description: |
  Pre-publish content intelligence skill for marketing teams and content creators.
  Before drafting any post, scout what's already performing on X/Twitter and across
  platforms. Uses Twitter CLI for real-time data and Manus for cross-platform deep
  research. Returns a structured report: what's trending, what's saturated, where
  the gaps are, and what angle to take.
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

Content Scout uses two tools: **twitter-cli** for X/Twitter data and **Manus** for cross-platform research. No alternatives, no menu. These work. Set them up.

### 1. Twitter CLI — Real-Time X/Twitter Data

[twitter-cli](https://github.com/missuo/twitter-cli) talks to X/Twitter directly. No API key application, no developer portal, no approval wait. Cookie auth from your browser and you're live in 5 minutes.

#### Install

**macOS:**
```bash
brew install go
go install github.com/missuo/twitter-cli@latest
```

**Linux:**
```bash
# Download the latest binary from GitHub releases
curl -L https://github.com/missuo/twitter-cli/releases/latest/download/twitter-cli_Linux_x86_64.tar.gz | tar xz
sudo mv twitter /usr/local/bin/
```

**Windows (WSL):**
```bash
# Use the Linux instructions inside WSL
```

**No Go installed?** Download the pre-built binary from [releases](https://github.com/missuo/twitter-cli/releases) — pick your OS, unzip, move to PATH. Done.

#### Auth Setup

You need two cookies from your X/Twitter session. This takes 60 seconds.

1. Open [x.com](https://x.com) in Chrome and log in
2. Press `F12` (DevTools) → click **Application** tab → **Cookies** → `https://x.com`
3. Find and copy these two values:
   - `auth_token` — long hex string (starts with something like `a1b2c3...`)
   - `ct0` — another long hex string

4. Set them as environment variables:

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc) so they persist:
echo 'export TWITTER_AUTH_TOKEN="paste_your_auth_token_here"' >> ~/.bashrc
echo 'export TWITTER_CT0="paste_your_ct0_here"' >> ~/.bashrc
source ~/.bashrc
```

5. Test it:
```bash
twitter search "Claude Code" --sort top --limit 5 --yaml
```

If you see tweets with engagement numbers — you're live.

#### Troubleshooting

- **"command not found"** → the binary isn't in your PATH. Run `echo $PATH` and move the binary to one of those directories, or add `~/go/bin` to PATH: `export PATH=$PATH:~/go/bin`
- **"unauthorized" or empty results** → your cookies expired. Go back to step 2 and copy fresh ones. Cookies last a few months but X can rotate them.
- **"rate limited"** → wait 15 minutes. Don't run more than ~50 searches per hour.

#### Search Operators

Once you're set up, these operators give you surgical precision:

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

### 2. Manus — Cross-Platform Deep Research (Dead Drop Setup)

[Manus](https://manus.im) is an async browser agent. Twitter CLI handles X/Twitter. Manus handles everything else — LinkedIn, Reddit, newsletters, competitor websites, anywhere that needs a real browser.

You use it as a **dead drop**: drop a task in a shared GitHub repo, Manus picks it up, does the research, commits results. You pull results automatically. No babysitting.

#### Sign Up

1. Go to [manus.im](https://manus.im) and create an account
2. You get a browser-based agent that can execute multi-step research tasks
3. Connect it to your GitHub account (it needs repo access to read tasks and push results)

#### Step 1: Create a shared GitHub repo

```bash
# This is your dead drop — tasks go in, results come out
gh repo create manus-tasks --private
cd manus-tasks
mkdir tasks results tasks/done
```

#### Step 2: Add a CONTEXT.md

Write a `CONTEXT.md` in the repo root. This tells Manus who you are, what you care about, and how to format output. Include:

- Your domain (marketing, dev, crypto, etc.)
- What topics are high/medium/low signal
- Output rules: "never fabricate data, use JSON for data, markdown for analysis"
- The protocol: read from `tasks/`, write to `results/`, move done tasks to `tasks/done/`

This file is Manus's briefing doc. It reads it before every task.

#### Step 3: Drop tasks as markdown files

Create a task brief in `tasks/` and push:

```markdown
# Task: Scout AI marketing content landscape
Type: research
Created: 2026-05-22

## Brief
Find the top-performing posts about AI for marketing teams on X, LinkedIn, and Reddit in the last 7 days. Extract exact text, engagement numbers, author handles.

## Output
JSON to results/ai-marketing-scout_2026-05-22.json
Each post: { author, text, platform, likes, shares, url, angle }

## Context
Planning next week's content. Need to find gaps — what's trending but underserved.
```

```bash
git add tasks/ && git commit -m "task: ai marketing scout" && git push
```

Then open Manus and tell it:

```
Here's my research task repo: https://github.com/[you]/manus-tasks

Read CONTEXT.md for my briefing and output rules.
Check tasks/ for new briefs. Execute them.
Commit results to results/ with message "result: [short description]".
Move completed tasks to tasks/done/.
```

Manus will clone the repo, read your brief, browse the platforms, and push results back. You don't need to be online.

#### Step 4: Set up auto-pull (the sync loop)

On your machine (or a VPS), set up a cron to pull results hourly:

```bash
# crontab -e
0 * * * * cd /path/to/manus-tasks && git pull origin master --quiet
```

Or go further — write a script that:
1. Pulls the repo
2. Checks for new files in `results/` since last check
3. Classifies results by topic
4. Caches them for your next planning session
5. Optionally notifies you (Slack, Telegram, etc.)

```python
# Pseudocode for the check loop
last_commit = read_state_file()
git_pull()
current_commit = get_head()
if current_commit != last_commit:
    changed = git_diff(last_commit, current_commit, path="results/")
    for file in changed:
        content = read(file)
        category = classify(filename)  # "competitors", "market-research", etc.
        cache_for_brief(category, content)
    save_state(current_commit)
```

#### Step 5: Feed results into Content Scout

When Manus drops results, pipe them into the scout workflow:

```
"Read results/ai-marketing-scout_2026-05-22.json and run Content Scout analysis — find the gaps, recommend an angle."
```

The loop: **you drop tasks → Manus researches → results auto-sync → Content Scout analyzes → you draft from a position of knowledge.**

#### Step 6: Auto-Schedule (hands-free scouting)

Two sides to auto-schedule: your cron drops the task, Manus picks it up automatically.

**Manus side — set up recurring execution:**

In Manus, create a scheduled task (or use their API if available):

```
Schedule: Every Friday 00:00 UTC
Repo: https://github.com/[you]/manus-tasks
Instructions: Read CONTEXT.md. Check tasks/ for any unprocessed briefs.
Execute each one. Commit results to results/. Move done tasks to tasks/done/.
If no new tasks, check if last week's scout is >7 days old and re-run it
with fresh data.
```

If Manus doesn't support native scheduling yet, you can trigger it manually each week — or use the cron below to auto-drop tasks so they're waiting whenever you next open Manus.

**Your side — auto-generate the task brief:**

```bash
#!/bin/bash
# drop-content-scout.sh — auto-drop weekly scout task to Manus
# Cron: Thursday 20:00 your timezone — results land by Friday/Saturday

REPO="/path/to/manus-tasks"
TODAY=$(date '+%Y-%m-%d')
NEXT_MON=$(date -d 'next monday' '+%Y-%m-%d')
TASK_FILE="$REPO/tasks/${TODAY}_content-scout-w${NEXT_MON}.md"

# Guard: don't duplicate if already dropped this week
if ls "$REPO/tasks/"*content-scout-w${NEXT_MON}* 2>/dev/null | grep -q .; then
    exit 0
fi

cat > "$TASK_FILE" << HEREDOC
# Task: Weekly Content Scout — Week of $NEXT_MON
Type: research
Created: $TODAY

## Brief
Run a content landscape scout for next week's posts. Research across X/Twitter, LinkedIn, Reddit, and newsletters.

### Track 1: What's Trending (Global)
Search for viral posts about [YOUR TOPICS] in the past 7 days. Extract exact text, engagement numbers, author handles, URLs. Focus on posts with >500 likes.

### Track 2: What's Trending (Local/Niche)
Search your community platforms — Facebook groups, forums, local-language discussions. What questions are people asking? What are they struggling with?

### Track 3: Competitor Watch
Check what your top 3-5 competitor accounts posted this week. What performed? What format? What angle?

### Track 4: Gap Detection
Cross-reference tracks 1-3. Where is there audience interest but few posts? That's the gap.

## Output
Save as: results/content-scout_${TODAY}.md

Include:
- Direct URLs to every source
- Exact engagement numbers
- Final "Top 5 Content Opportunities" section with suggested angles

## Context
[Your page description, audience, what content style works for you]
HEREDOC

cd "$REPO"
git add "tasks/${TODAY}_content-scout-w${NEXT_MON}.md"
git commit -m "task: content scout for week of $NEXT_MON"
git push origin master
```

```bash
# Add to crontab — Thursday evening, research lands by weekend
# crontab -e
0 20 * * 4 /path/to/drop-content-scout.sh
```

The full loop runs on autopilot: **Thursday cron drops task → Manus researches overnight → Friday auto-pull syncs results → you plan next week's content from data, not guesses.**

#### When to use Manus vs Twitter CLI alone
- **Twitter CLI** — quick scout, single platform, 5 minutes
- **Manus** — campaign planning, cross-platform landscape, quarterly strategy, anything that needs a real browser

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
