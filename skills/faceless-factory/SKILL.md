---
name: faceless-factory
description: |
  Split AI content into two layers — AI generates raw material (backgrounds, characters,
  clips), code assembles the deliverable (text, layout, render). Use when AI-generated
  carousels/cards come out inconsistent, Thai fonts break, or every re-gen is a gamble.
---

# Faceless Factory — AI Makes Raw Material, Code Assembles

Every time you gen a full carousel with AI, it comes out beautiful one round and broken the next: characters drift, colors shift, Thai fonts shatter into tofu. That's not a prompt problem. It's a job-assignment problem.

## The core idea

You're using a tool that **guesses every time** to do work that needs to be **the same every time**. Split it into two layers:

- **Top layer (expensive, AI-gen):** backgrounds, characters, opening clips. These are *raw material*. Gen once, keep it, reuse it. Randomness is fine — even wanted — here.
- **Bottom layer (cheap, code):** text, layout, composition, final render to file. **Never let AI gen this.** Code does it, deterministically, for free.

The insight most people miss: the part everyone thinks they must pay the most for (the gen) is the *least* important. The part that makes it shippable — the assembly — is plain code that runs for free, identically, forever.

## When to use

Say `/faceless-factory` or: "my AI carousel is inconsistent", "Thai fonts keep breaking", "every gen is a gamble", "how do I make repeatable content with AI", "the faces/colors drift between slides".

## Why code, not AI, for the bottom layer

The bottom-layer work — JSON, render scripts, ffmpeg — is "boring but must be exact." It doesn't need imagination. It needs to come out **pixel-identical every run**, which is exactly what AI gen *cannot* do and code does for free.

Concrete payoffs once you split:
- **Thai text never breaks again** — it isn't *generated*, it's *rendered* with a real font.
- **Gen the background once, render N cards for $0** — no paying again to remake the same thing.
- **No more gacha** — you stop lucking into a good result.

## The two-tool division of labor (agent workflow)

If you drive this with coding agents, split the roles:

- **The code-writer agent** builds the machine: a render script (PIL for images, ffmpeg for video) that reads one JSON file and draws the deliverable.
- **The pipeline-runner agent** runs the line: invokes the script, checks the JSON is complete, keeps a manifest so nothing double-renders, and QAs the final files.

One builds the machine, the other runs the belt.

## The hard part: Thai + Latin in one string

The single most valuable trick in the render script is drawing mixed Thai/Latin/digit text correctly. Naively drawing a Thai string with a Thai font renders digits, arrows, and Latin letters as tofu boxes; drawing it with a Latin font detaches Thai combining vowels/tones from their base consonant.

The fix: **split the string into runs by script**, render each run with the right font, advance the x-cursor by the measured width of each run. Thai runs stay whole (so vowels/tones stack); everything else swaps to a Latin font.

See [`reference/carousel_factory.py`](reference/carousel_factory.py) for a working, dependency-light implementation of:

- `dtext()` — run-splitting Thai/Latin text renderer (the tofu fix)
- `wrap()` — width-aware word wrap
- `place_shot()` — cover-crop + rounded-mask image placement
- `brand_bar()` — a bottom brand lockup

It's a template, not a framework. Copy it, point the font paths at your fonts, feed it your JSON.

## Steps to apply

1. **List your content** — put every slide's text, image path, and layout into one JSON file. One source of truth.
2. **Separate the layers** — decide what is raw material (gen once) vs assembly (render every time).
3. **Gen the raw material once** — backgrounds, characters, hero shots. Save them.
4. **Write the render script** — reads JSON, draws text with a real font, composites the images, exports the file. No AI in this step.
5. **Run and QA** — render all cards, eyeball the output, iterate on the JSON (not the pixels).

## The one line to remember

Don't ask AI to gen the whole thing. Split first: **what's raw material, what's the assembly line.** Raw material → AI. Assembly line → code. Then you stop gambling every time you hit generate.
