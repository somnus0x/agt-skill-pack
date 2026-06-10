---
name: steal-digest
description: |
  Scan GitHub trending daily and report which repos contain ideas worth stealing for your
  project — patterns, not stars. Use for repo scouting and idea extraction.
---

# Steal Digest — Cherry-Pick Ideas From GitHub Trending

Stop scrolling GitHub trending aimlessly. Let AI scan it daily and tell you which repos have ideas worth stealing for your project.

Not copying code. Stealing ideas — seeing how someone else solved a problem and asking "can I use this pattern?"

## Setup

### Drop-in prompt (copy into your AI tool):

```
ไปดู GitHub trending วันนี้ (https://github.com/trending) เลือก 3-5 repos ที่น่าสนใจสำหรับ stack ของผม [ระบุ stack เช่น: React, Next.js, Python, Go]
แต่ละ repo บอก:
1. ทำอะไร (1 บรรทัด)
2. มี idea/pattern อะไรที่เอามาปรับใช้กับ project ของเราได้
3. ความยากในการ implement (ง่าย/กลาง/ยาก)
ไม่ต้อง copy code ให้บอกแค่ idea + วิธีประยุกต์
ข้ามพวก: awesome lists, tutorial repos, repos ที่ต้องเปลี่ยน stack ทั้งหมด
```

English version:

```
Check GitHub trending today (https://github.com/trending) and pick 3-5 repos relevant to my stack [specify: React, Next.js, Python, Go, etc.]
For each repo:
1. What it does (1 line)
2. What idea/pattern can be adapted for our project
3. Implementation difficulty (easy/medium/hard)
Don't copy code — just describe the idea + how to adapt it.
Skip: awesome lists, tutorial repos, repos requiring full stack migration.
```

## Running as a daily cron (recommended)

The real power is automation. Set up a daily scan that runs every morning:

```bash
# Daily steal digest at 09:00
0 9 * * * cd /path/to/project && claude -p "$(cat steal-digest-prompt.txt)" >> logs/steal-digest.txt
```

Save the prompt above as `steal-digest-prompt.txt` and let it run. Check the output when you have 5 minutes.

## Building a steal backlog (optional)

Track what you've stolen and what's pending:

```markdown
# Steal Backlog

## Queued
- [ ] AI slop detection pattern (from repo X) — adapt for UI review skill
- [ ] Rate limiting middleware (from repo Y) — simpler than current setup

## In Progress
- Product evaluation framework — adapting into Product Taste skill

## Done
- Jina Reader integration — wired into link triage
- twitter-cli — wired into content scouting
```

## What to look for

Good steals have these properties:
- **Solves a problem you already have** — not a solution looking for a problem
- **Can be adapted, not just copied** — the idea transfers even if the code doesn't
- **Doesn't require a full rewrite** — should integrate into existing architecture
- **Has a clear implementation path** — you can see how to build it in your stack

Bad steals:
- Awesome lists (curation, not creation)
- Tutorial/course repos
- Repos requiring a full stack migration
- Things that look cool but don't solve any current problem

## Add to your CLAUDE.md

```markdown
### Steal digest
When asked to run steal digest, check GitHub trending for repos relevant to my stack.
For each candidate: what it does, what to steal, implementation difficulty.
Maintain steal backlog at data/steal-backlog.md.
```

## When to use

- Morning routine — scan trending while drinking coffee
- Before starting a new feature — see if someone already solved the hard part
- Weekly backlog review — which stolen ideas are worth implementing this week
- When you're stuck — sometimes someone else's approach unlocks yours
