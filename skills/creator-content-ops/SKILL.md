---
name: creator-content-ops
description: |
  Turn a content creator's AI stack into a factory that sounds like THEM. One voice
  spine (CONTENT.md) governs every format — FB/blog posts, TikTok carousels, YouTube
  Shorts, covers — so the output stops smelling like AI and comes out consistent every
  run. Use when a creator (not a dev) wants to set up Claude Code / an AI agent for
  content production across channels, or fix output that reads generic, breaks Thai
  fonts, or looks different every gen. Triggers: "setup AI for content", "brandbook for
  AI", "AI writes generic", "content creator claude md", "carousel/shorts pipeline",
  "cover generator".
metadata:
  author: creator-content-ops
  version: 1.0.0
---

# creator-content-ops — make your AI stack sound like YOU, across every channel

You are the example. If you run a page, a channel, a blog, you already have a voice.
The problem is your AI doesn't. Ask it to "write like me" and it writes like the
internet: ten drafts, ten different people, none of them you. Ask it to "gen a
carousel" and the Thai fonts shatter, card 3 looks nothing like card 4, and every
regen is a coin flip. That is not a model problem. It is a missing-system problem.

This kit is the system. Not a Canva brandbook with a color palette. A **rule set your
AI reads before it writes anything**, plus the production layer that renders instead of
gambles. Four formats, one spine:

- **CONTENT.md** — your voice, extracted once, loaded every session. The 3 filters that
  catch AI-smell before it ships. This is the heart. Everything else reads it.
- **carousel/** — TikTok/IG carousels where AI gens the background and CODE renders the
  text. Thai never breaks, because it is rendered with a real font, not generated.
- **shorts/** — YouTube Shorts / TikTok clip assembly from your raw material.
- **covers/** — post covers, two paths: a code-composed neutral template (pixel-exact,
  free, every time) and a Codex ImageGen path (creative, one-offs, diagrams).

The split that makes it a factory, not a craft:

> **AI gens what needs imagination. Code composes what needs consistency.**
> Backgrounds, art, hero shots → AI. Text, layout, export → code. Never let AI draw
> the words on the card. Render them.

## When to use / not use

Use when a **creator** wants to set up an AI content stack, or fix these symptoms:
- output reads generic / "sounds like AI" no matter how you prompt it
- Thai (or any complex-script) text breaks when AI generates the image
- a carousel/series comes out inconsistent card-to-card
- every asset is hand-made one at a time in Canva and it doesn't scale

Do NOT use for: dev-repo setup (that's `claude-md-setup` — same bones, code target),
one-off single images with no voice/consistency need, or video editing craft. This kit
is about turning **repeatable content** into a governed pipeline.

## Setup first — build YOUR CONTENT.md before anything else

Do not copy someone else's voice file. Run the interview in **`SETUP.md`** — it asks you
for your writing samples, your no-go words, your channels, and your tool auth, then
writes a `CONTENT.md` calibrated to you. Ten minutes. Every module below reads the file
it produces, so nothing works right until it exists.

```
1. Read SETUP.md          → answer the interview, hand over 5-10 real samples
2. It writes CONTENT.md   → your voice spine (3 filters + per-platform rows)
3. Wire the modules       → point carousel/shorts/covers at your fonts + CONTENT.md
4. Produce               → every format now reads CONTENT.md before it generates
```

## The modules

| Module | What it does | AI or code | Deps |
|--------|--------------|-----------|------|
| `CONTENT.md` | voice spine + 3 AI-smell filters, read every session | — | none |
| `reference/carousel_factory.py` | JSON → PIL render, Thai/Latin tofu-fix | **code** | Pillow, fonts |
| `reference/cover_neutral.py` | pixel-exact cover from a template you rebrand | **code** | Pillow, fonts |
| `reference/codex_imagegen.md` | creative backgrounds / diagrams via Codex CLI | **AI** | Codex CLI authed |
| `reference/shorts_pipeline.md` | Shorts assembly from raw material | code + AI | ffmpeg, Pillow |

## Principles

- **You are the training data.** The kit does not invent a voice. It extracts yours from
  real samples and enforces it. Garbage samples in, generic voice out.
- **One spine, many formats.** A carousel and a Short and a blog post all read the same
  CONTENT.md. That is why they sound like one person instead of four tools.
- **The kit ships the method, not your moat.** Copy the render tricks and the voice
  system. Your finished channel, your trained voice model, your private auth stay yours.

## Portable across agents

Nothing here is Claude-only. CONTENT.md is plain markdown any agent reads; the render
engines are plain Python. Claude Code loads the voice file with `@CONTENT.md`; Cowork,
Cursor, and Amp each have their own load step (a context file, an `AGENTS.md`, a settings
path). The method is portable, the wiring per agent is one line.
