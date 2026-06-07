# Live-Data Brief Setup — stop making AI guess from half-loaded pages

You want AI to summarize live data every morning — market prices, metrics, whatever updates daily. The obvious way is to let it browse and fetch while it writes the summary. That way is wrong, and it's why your numbers come out garbled.

This skill gives you the pattern that fixes it: **separate the fetch from the generation.**

## Why your numbers come out wrong

When you ask AI to "go check the price and summarize," it fetches a page mid-generation, reads whatever loaded, and writes confidently from incomplete data. It doesn't know the page wasn't done loading. So it guesses — yesterday's number, a half-rendered value, or a hallucinated one — and presents it like fact.

The AI isn't dumb. It just has nothing complete to read, so it fills the gap. The fix isn't a smarter model. It's **not asking it to fetch and reason at the same time.**

## The pattern — two beats, never one

**Beat 1 — fetch ahead of time (cron).** Pull each data source, write it to a JSON file. This runs before you (or the AI) need the brief.

**Beat 2 — one prompt reads the files.** The AI never touches the network. It reads the cached files and summarizes. Complete data in, no guessing.

```
cron (fetch) ──> data/*.json ──> one prompt (read + summarize) ──> brief
```

## When to use

Any recurring "summarize live data" job: morning market brief, daily metrics digest, ops dashboard summary, anything where AI reasons over numbers that change.

Say: "setup data brief", "morning brief pipeline", "stop AI guessing numbers", "cron data cache for AI".

## Step 1 — Pick your sources, write fetchers

Start with 2-3 sources. Don't wire ten on day one — most are noise until you know which you actually read.

Each fetcher does one thing: hit the source, write the response to a file. No parsing, no logic.

```bash
mkdir -p data

# free, no key
curl -s 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true' \
  > data/prices.json

# free, no key
curl -s 'https://api.alternative.me/fng/' > data/sentiment.json
```

The rest of your sources follow the identical shape — hit it, write the file. Swap in whatever your domain needs (a metrics API, a status endpoint, a CSV feed).

### Secrets: never hardcode keys

Sources that need a key — read it from the environment, never inline:

```python
import os
API_KEY = os.environ.get("MY_API_KEY", "")   # from .env, not in the code
```

Put the key in `.env`, add `.env` to `.gitignore`, load it before the fetch runs. A key committed to a repo is a key you have to rotate.

## Step 2 — Schedule the fetch

Run the fetchers on cron, before you need the brief. They land in one folder.

```bash
# crontab -e  →  fetch at 06:50, brief reads it after
50 6 * * *  cd /path/to/project && bash fetch-all.sh
```

The fetch and the brief are now decoupled. If a source is down, that one file is stale or empty — it doesn't block the others, and the brief still runs.

## Step 3 — One prompt reads the cache

This is the whole generation step. The AI reads files, summarizes, never fetches.

```
Read every file in data/ :
- prices.json    — price + 24h change
- sentiment.json — sentiment index
[...list each file and what it holds...]

Summarize into a short brief with sections relevant to your data.

If a file is missing or empty, write "n/a" for that item.
Do NOT guess any number. If it's not in the files, it's n/a.
```

The last two lines matter most. **"Do not guess"** is the guardrail — when a feed is down, the AI writes `n/a` instead of inventing a value. That single instruction is the difference between a brief you can trust and one that lies to you on a bad-data day.

## Step 4 — Verify it's not guessing

Test the failure case on purpose: empty one file, run the brief.

```bash
echo '{}' > data/prices.json   # simulate a dead feed
# run the brief prompt
```

The brief should say `n/a` for price, not produce a number. If it invents one, your "do not guess" line is missing or too weak — strengthen it and re-test. A pipeline you haven't tested broken is a pipeline you can't trust.

## Step 5 — Grow one source at a time

Add a source only after you've read the brief enough to know you'd actually use it. Each new source is: a fetcher (Step 1) + a line in the cron + a line in the prompt. Three small additions, no architecture change.

Resist wiring everything up front. A brief with 3 sources you read beats a brief with 15 you skim.

## The principle

The bug was never "AI can't read data." It was "AI fetching while it reasons guesses from incomplete pages." Split the two beats — cache first, read second — and the guessing stops. Not because the model got smarter, but because you stopped asking it to do two things at once.

## Add to your CLAUDE.md

```markdown
### Live-data briefs
When summarizing live data, never fetch during generation.
1. Fetch sources to data/*.json ahead of time (cron)
2. The summary prompt reads files only — no network access
3. Always include "do not guess numbers; missing = n/a" in the prompt
4. Add sources one at a time, only after confirming you read them
```

## Output discipline

When this skill is invoked:
1. Help the user pick 2-3 starting sources (not ten)
2. Write the fetchers (one job each: hit source, write file)
3. Set up the cron schedule
4. Write the read-only summary prompt WITH the "do not guess" guard
5. Test the broken-feed case before calling it done

Don't build the analysis layer for them — that's their domain edge. Ship the pipeline; the judgment on top is theirs.
