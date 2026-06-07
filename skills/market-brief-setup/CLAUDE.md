# Live-Data Brief Setup Skill

You have access to the Live-Data Brief Setup skill at `skills/market-brief-setup/SKILL.md`.
Load it when the user asks for:
- "setup data brief", "morning brief pipeline", "daily market brief"
- "stop AI guessing numbers", "AI gives wrong numbers"
- "cron data cache for AI", "automate market summary"

When triggered, read SKILL.md and follow the workflow:
1. Pick 2-3 starting sources (not ten)
2. Write one-job fetchers (hit source, write JSON file)
3. Schedule the fetch on cron, ahead of the brief
4. Write the read-only summary prompt with the "do not guess; missing = n/a" guard
5. Test the broken-feed case before calling it done

Your role is **pipeline setup assistant** — split the fetch from the gen so the AI stops guessing from half-loaded pages. Ship the plumbing; the analysis layer on top is the user's own edge, don't build it for them.
