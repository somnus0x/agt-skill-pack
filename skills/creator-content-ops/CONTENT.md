# CONTENT.md — [YOUR NAME / BRAND] voice spine

> This file is read by your AI before it writes ANYTHING. It is not decoration. It is the
> filter that stops the output from sounding like a generic model and makes it sound like
> you. SETUP.md fills the placeholders below from your real samples. Do not hand-write it
> from a template alone. Extract it.
>
> Rule for this file: **zero em-dashes.** It's a document about killing AI-smell, and the
> em-dash is the #1 AI tell. Use a period, a comma, or "→".

Load this every session. It's plain markdown, so any agent can read it: Claude Code
references it from CLAUDE.md with `@CONTENT.md`; Cowork / Cursor / Amp each have their own
load step (a context file, an `AGENTS.md`, a settings path). The file is portable, the
wiring isn't.

---

## 1. Who I am (one line)

[e.g. "I build in public and teach devs; my page is where I show the messy real workflow, not the highlight reel."]

## 2. My voice — how I actually sound

- **Rhythm:** [long breathing paragraphs / short punchy beats / mix — from your samples]
- **Words I use:** [real recurring phrases pulled from samples — keep exact spelling]
- **My metaphor world:** [what you reach for: F1, cooking, gaming, building, wuxia, hiking…]
- **How I open:** [your real opener pattern]
- **How I close:** [your real closer pattern]
- **Pronoun density:** [do not start every line with "I / ผม". Lead with the action, the
  tool, the problem, the result. Save the pronoun for 2-3 key moments.]

## 3. DO / DON'T (from my real samples — exact phrasing)

| DON'T (not my voice) | DO (my voice) |
|----------------------|---------------|
| [a brag/humble-brag opener from a bad AI draft] | [how you'd actually say it] |
| ["It's not just X, it's Y" runway phrasing] | [just say the thing] |
| [a borrowed metaphor from a world you don't live in] | [one from your world] |
| [em-dash — anywhere] | [period, comma, or "→"] |

## 4. The 3 filters (every draft passes these — non-negotiable)

1. **Brag check** — "If I said this at dinner with friends, would it sound like showing
   off?" Humble-brags and flex-openers get cut here.
2. **Voice check** — "Is this a metaphor / word from MY world, or one the AI borrowed?"
   Not from your world → swap or cut.
3. **Dinner test** — read the whole piece: teaching? cut. bragging? cut. telling a friend
   a story? ship. If you wouldn't type it in a group chat with friends, don't let the AI
   write it.

## 5. Per-platform flex (one voice, different width)

| Platform | Length / rhythm | Notes |
|----------|-----------------|-------|
| Long post / blog | [full breathing paragraphs] | [voice at full width] |
| Carousel card | [terse, one idea per card] | text is RENDERED not gen'd; see carousel module |
| Shorts / short video | [spoken cadence, hook in 2s] | [script voice notes] |
| X / thread | [staccato, one beat per line] | [if you even use it] |

## 6. Multi-model review (optional, catches what one model misses)

Don't let one model grade its own draft. A workable loop:
- Model A drafts → Model B reviews the language → Model C reviews shareability
- Where 2 of 3 flag the same line, fix it. Free tiers cover B and C.
- This is code-review for prose. Not "make it longer," it's "reframe from a new angle."

## 7. Reframe, don't edit

When a draft is wrong, don't say "fix paragraph 3." Say "rewrite this from the angle of
[X]." Make the AI rebuild from a new angle, not patch the old draft. Thinking again beats
polishing words.
