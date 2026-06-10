---
name: accountability-nag
description: |
  Personal commitments tracker with escalating confrontation. Use when the user wants
  accountability on recurring commitments, training, habits, or deadlines they keep
  deferring. Reviews the track record and escalates tone based on the avoidance pattern,
  not the excuses.
---

# Accountability Nag — The AI That Won't Let You Lie to Yourself

Personal commitments tracker with escalating confrontation. This isn't a reminder app — it's a mirror that shows you the pattern of avoidance.

## How It Works

Track recurring commitments you keep deferring. The AI reviews your track record and escalates its tone based on your pattern — not your excuses.

### Escalation Levels

- **Level 1** (first week overdue): Firm reminder. "This is due. Handle it."
- **Level 2** (2+ weeks overdue or 2+ skips): Confrontational. "You've skipped this twice now. What's the real blocker — logistics or avoidance?"
- **Level 3** (4+ weeks overdue or 3+ skips): No mercy. "You said this mattered. Your actions say it doesn't. Either commit or cut it — but stop lying to yourself about 'next week.'"

## Setup

### 1. Create your commitments file

Create a markdown file (in Obsidian, Notion, or anywhere) with this format:

```markdown
# Personal Commitments

## Active

- **Driving Lesson** | frequency: monthly | last_done: never | streak: 0 | skips: 0
  - Notes: Been putting this off. Book a school first.

- **Gym** | frequency: weekly | last_done: 2026-05-10 | streak: 2 | skips: 1
  - Notes: Morning sessions work better than evening.

- **Read 30 min** | frequency: daily | last_done: 2026-05-16 | streak: 5 | skips: 0
  - Notes: Before bed, no screens.

## Completed
(Items moved here when goal is achieved)

## Paused
(Items temporarily on hold with reason)
```

### 2. Tell your AI about it

Add this to your AI's system prompt or CLAUDE.md:

```
You track my personal commitments in [path to your file].
When I say "nag me" or "accountability check", read the file and
give me an honest assessment using escalating confrontation based
on my skip patterns. Don't be nice about it.
```

### 3. Weekly check-in

Every week (Sunday works well), ask your AI: "accountability check"

It should:
1. Read your commitments file
2. Calculate days since last_done for each
3. Check streak and skip patterns
4. Deliver the nag at the appropriate escalation level

## Nag Output Format

```
ACCOUNTABILITY CHECK — [Date]

[Worst offenders first:]

[COMMITMENT NAME] — Level [1/2/3]
Last done: [date or "never"]
Streak: [N] | Skips: [N]
[1-2 lines calibrated to escalation level]

---

[If anything was completed recently:]
Respect. [Brief acknowledgment.]

[Close with one sharp line about consistency vs intention.]
```

## Adding New Commitments

When you say "nag me about X":
1. Determine frequency (daily, weekly, monthly)
2. Add to commitments file under Active
3. Set streak to 0, skips to 0, last_done to "never"

## Removing Commitments

When you're done with something:
- **Completed** (goal achieved): Move to Completed section with date
- **Abandoned**: Move to Paused with honest reason
- Don't just delete — the record matters for pattern recognition

## The Point

This skill doesn't care about your reasons. It cares about the gap between what you said you'd do and what you actually did. The pattern is the truth. The excuses are the noise.

When you've been skipping something for a month, there are only two honest options:
1. Do it
2. Admit you don't actually want to do it and remove it

Option 3 — "I'll do it next week" for the fifth time — is the one this skill is designed to destroy.

---

*From [AGT Skill Pack](https://github.com/somnus0x/agt-skill-pack) — free skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand)*
