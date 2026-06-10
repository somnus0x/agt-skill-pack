---
name: design-taste
description: |
  Pattern-recognition design review: judge whether an interface works before any analysis.
  Use for UI and design reviews, visual hierarchy checks, and 'does this look right'
  calls.
---

# Design Taste

Design taste is the ability to look at an interface and know — before any analysis — whether it works. This skill doesn't teach design rules. It trains the pattern recognition that makes rules unnecessary.

## Start with identity, not a screen

AI-generated UIs look generic because the model starts from zero every time. Ask it for "a nice pricing page" and it converges on the safest, most average answer in its training data. That's why everything looks the same.

The fix is upstream of the screen: **define your design identity first.** Before generating anything, decide what world this product lives in — the tone, the emotional reference, what it should feel like. Pick your own direction (editorial, brutalist, playful, terminal, whatever fits the product). Don't let the model pick a default for you.

Once the identity is set, buttons and layout fall out of it. The same content, gen'd against a defined identity, comes out distinctive instead of average.

**Generic is not a polish problem. It's a starting-point problem.** The four lenses below check whether what you generated matches the identity you decided on.

## The design taste framework

When evaluating any UI — your own, a competitor's, or a reference — run these four lenses. Each one isolates a different axis of quality.

### Lens 1: Squint test

Literally squint at the screen (or blur the screenshot mentally). What do you see?

- **Where does your eye go first?** That's the visual hierarchy. If it goes to the wrong thing (a decorative element, a secondary button, a logo) — the hierarchy is broken.
- **How many distinct zones do you see?** More than 4 zones on one screen = too complex. Reduce.
- **Is there a clear "what do I do here" moment?** If squinting reveals no obvious action — the page has no purpose.

Output: "Eye goes to [X]. [Right/wrong] element. [N] zones visible. Primary action is [clear/unclear]."

### Lens 2: Remove until it breaks

Take the design and mentally delete elements one at a time. Start with decoration — shadows, gradients, icons, borders, background colors.

For each removal, ask: "Does the UI still communicate its purpose?"

When you remove something and the UI breaks — that element was load-bearing. Everything you removed before it was decoration. Good design has very few decorative elements. Every pixel earns its place.

This is the Pareto move: ~80% of what's on a screen carries ~20% of the meaning. Cut the 80% and what's left gets sharp. Remove until removing breaks it — that's where good design lives.

### Lens 3: Copy test

Read every word on the screen. Cover the visuals with your hand and read only the text. Does it make sense? Could you accomplish the task from the text alone?

Then do the reverse — cover the text, look only at the layout, icons, and visual affordances. Can you guess what to do without reading anything?

The best interfaces pass BOTH tests. The text works alone. The visuals work alone. Together they're redundant in the right way.

Bad design: pretty visuals with unclear copy, or clear copy trapped in confusing layout. If the page only works because of the gradient and the animation, the product underneath is thin and the design is just covering for it.

### Lens 4: Emotional register

Every interface has a feeling. Not "makes the user feel good" — that's too vague. Identify the specific emotional register:

- **Confident** — Stripe, Linear. Says "we know what we're doing."
- **Playful** — Figma, Notion. Says "this is fun to use."
- **Urgent** — Trading UIs, dashboards. Says "act now, data is moving."
- **Calm** — iA Writer, Things. Says "take your time."
- **Chaotic** — Most DeFi UIs. Says "we built this in a weekend."

Write the register you want as a word first (fast / trustworthy / fun / refined). Then check: is that the RIGHT register for the product, and does the design actually land it? A finance app with round fonts and pastels reads "toy," not "your money is safe." If the register is wrong, no amount of polish fixes it.

## The order matters more than the lenses

There's a hierarchy to this, and most people start at the wrong end:

1. **Design identity (brandbook)** — decide what the product is. *Before* you generate.
2. **The 4 lenses** — enforce that every screen matches the identity. *While* you generate.
3. **AI slop checklist** — catch the generic defaults before you ship. *Before* you ship.

Most people start at step 3 — they delete gradients and shadows off an AI-gen'd page and call it done. They get an interface that's "not wrong" but has no identity. Removing slop without defining identity just gives you a cleaner version of generic.

Start from the top, not the bottom.

## Design taste exercises

### Exercise 1: Screenshot collection

Save 3 screenshots of UIs you find beautiful this week. Save 3 you find ugly. For each, write one sentence explaining why. After a month, review the collection. Patterns emerge — those patterns are your taste becoming conscious.

### Exercise 2: Redesign in 60 seconds

Take any app you use daily. Mentally redesign one screen — what would you change? Not a full redesign — one change. Practice identifying the single highest-leverage design improvement. This builds the "what's the ONE thing wrong here" instinct.

### Exercise 3: Steal like an architect

Find the best-designed product in your category (Polymarket, Kalshi, Robinhood, whatever). Don't copy their UI. Identify their design DECISIONS:
- Why did they put the primary action there?
- Why that font size for numbers?
- Why that amount of whitespace?
- What did they choose NOT to show?

The decisions are transferable. The pixels aren't.

### Exercise 4: The 5-second test

Show someone your UI for 5 seconds, then close it. Ask: "What was this page about? What would you do next?" If they can't answer both — the design failed. No amount of "but if you look closer..." matters. Five seconds is what you get.

## Design references worth studying

- **Polymarket** — clean information density, confident typography, dark mode done right. Study their market card design — maximum data, minimum decoration.
- **Robinhood** — controversial but effective. Simplified trading to one big green button. Study what they removed, not what they added.
- **Linear** — best-in-class for "confident + fast" register. Study how the emotional register is consistent across every screen.
- **Uniswap** — the gold standard for DeFi UI simplicity. One input, one output, one button. Study the swap card.
- **Twitter/X** — study the composition flow, the reply UX, the card embeds — density and rhythm done at scale.

---

## AI Slop Detection (the bottom layer)

The fingerprint test: if you showed this interface to someone and said "AI made this," would they believe you immediately? If yes, the design has failed. A distinctive interface makes someone ask "how was this made?" not "which AI made this."

These are the tells of 2024-2025 AI-generated frontends. Flag ANY of these during review.

### The AI Color Palette
- Cyan-on-dark, purple-to-blue gradients, neon accents on dark backgrounds
- Gradient text on headings or metrics — decorative, not meaningful
- Dark mode with glowing accents as default (looks "cool" without requiring actual design decisions)
- Pure black (#000) or pure white (#fff) backgrounds — neither exists in nature; always tint

### The AI Layout Template
- Hero metric layout: big number, small label, supporting stats, gradient accent — the "dashboard starter kit"
- Identical card grids: same-sized cards with icon + heading + text, repeated endlessly
- Cards nested inside cards — visual noise, flatten the hierarchy
- Everything centered — left-aligned text with asymmetric layouts feels more designed
- Big rounded icons above every heading — they rarely add value, make sites look templated
- Same spacing everywhere — without rhythm, layouts feel monotonous

### The AI Visual Bag of Tricks
- Glassmorphism everywhere — blur effects, glass cards, glow borders used decoratively rather than purposefully
- Rounded rectangles with generic drop shadows — safe, forgettable, could be any AI output
- Rounded elements with thick colored border on one side — lazy accent, almost never intentional
- Sparklines as decoration — tiny charts that look sophisticated but convey nothing meaningful
- Modals for everything — modals are lazy; there's almost always a better pattern

### The AI Font Choice
- Inter, Roboto, Arial, Open Sans everywhere — invisible defaults
- Monospace typography as lazy shorthand for "technical/developer" vibes
- Too many sizes too close together (14px, 15px, 16px, 18px) — creates muddy hierarchy

### The AI Motion Pattern
- Bounce or elastic easing — trendy in 2015, tacky now; real objects decelerate smoothly
- Animating layout properties (width, height, padding, margin) instead of transform/opacity
- Every button primary — use ghost buttons, text links, secondary styles; hierarchy matters
- Redundant copy — headers that restate the heading, intros that repeat what users can see

---

## Reference: Typography

### Font Selection

Avoid the invisible defaults. Better alternatives:
- Instead of Inter: **Instrument Sans**, **Plus Jakarta Sans**, **Outfit**
- Instead of Roboto: **Onest**, **Figtree**, **Urbanist**
- Instead of Open Sans: **Source Sans 3**, **Nunito Sans**, **DM Sans**
- For editorial/premium: **Fraunces**, **Newsreader**, **Lora**

System fonts are underrated: `-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui` loads instantly and looks native. Good for apps where performance > personality.

You often don't need a second font. One family in multiple weights creates cleaner hierarchy than two competing typefaces. When pairing, contrast on multiple axes (serif + sans, geometric + humanist, condensed + wide). Never pair fonts that are similar but not identical.

### Type Scale

Use fewer sizes with more contrast. A 5-size system covers most needs:

| Role | Size | Use Case |
|------|------|----------|
| xs | 0.75rem | Captions, legal |
| sm | 0.875rem | Secondary UI, metadata |
| base | 1rem | Body text |
| lg | 1.25-1.5rem | Subheadings, lead text |
| xl+ | 2-4rem | Headlines, hero text |

Fluid type via `clamp()` for headings on marketing pages. Fixed `rem` scales for app UIs, dashboards, data-dense interfaces — no major design system uses fluid type in product UI.

### Readability

Line-height should be the base unit for all vertical spacing. If body text has `line-height: 1.5` on 16px (= 24px), spacing values should be multiples of 24px. Use `ch` units for measure (`max-width: 65ch`). Increase line-height for light text on dark backgrounds (add 0.05-0.1).

### CSS Tricks Worth Using

```css
/* Tabular numbers for data alignment — critical in financial UIs */
.data-table { font-variant-numeric: tabular-nums; }

/* Proper fractions */
.fraction { font-variant-numeric: diagonal-fractions; }

/* Small caps for abbreviations */
abbr { font-variant-caps: all-small-caps; }

/* Disable ligatures in code */
code { font-variant-ligatures: none; }

/* Kerning (explicit) */
body { font-kerning: normal; }
```

Check font feature support at [Wakamai Fondue](https://wakamaifondue.com/).

### Font Loading (avoid layout shift)

```css
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2');
  font-display: swap;
}

/* Match fallback metrics to minimize CLS */
@font-face {
  font-family: 'CustomFont-Fallback';
  src: local('Arial');
  size-adjust: 105%;
  ascent-override: 90%;
  descent-override: 20%;
  line-gap-override: 10%;
}
```

---

## Reference: Color

### Use OKLCH, Not HSL

OKLCH is perceptually uniform — equal steps in lightness actually look equal. HSL lies: 50% lightness in yellow looks bright, 50% in blue looks dark.

```css
--color-primary: oklch(60% 0.15 250);       /* Blue */
--color-primary-light: oklch(85% 0.08 250);  /* Same hue, lighter — reduce chroma */
--color-primary-dark: oklch(35% 0.12 250);   /* Same hue, darker */
```

Key insight: as you approach white or black, reduce chroma. High chroma at extreme lightness looks garish.

### Tinted Neutrals

Pure gray has no personality. Add a subtle hint of your brand hue (chroma ~0.01):

```css
/* Warm-tinted */
--gray-100: oklch(95% 0.01 60);
--gray-900: oklch(15% 0.01 60);

/* Cool-tinted */
--gray-100: oklch(95% 0.01 250);
--gray-900: oklch(15% 0.01 250);
```

### The 60-30-10 Rule (Visual Weight)

- **60%**: Neutral backgrounds, white space, base surfaces
- **30%**: Secondary — text, borders, inactive states
- **10%**: Accent — CTAs, highlights, focus states

Accent colors work because they're rare. Overuse kills their power.

### Dangerous Combinations to Flag

- Gray text on any colored background — looks washed out; use a shade of the background color
- Light gray text on white — the #1 accessibility fail
- Red on green (8% of men can't distinguish)
- Blue on red (vibrates visually)
- Thin light text on images (unpredictable contrast)
- Heavy alpha/transparency — usually means incomplete palette

### Dark Mode Is Not Inverted Light Mode

| Light Mode | Dark Mode |
|---|---|
| Shadows for depth | Lighter surfaces for depth (no shadows) |
| Dark text on light | Light text on dark (reduce font weight) |
| Vibrant accents | Desaturate accents slightly |
| White backgrounds | Never pure black — use dark gray (oklch 12-18%) |

---

## Reference: Spacing & Layout

### 4pt Base Grid

8pt is too coarse — you'll constantly need 12px. Use 4pt: 4, 8, 12, 16, 24, 32, 48, 64, 96px. Name tokens semantically (`--space-sm`, `--space-lg`), not by value. Use `gap` instead of margins for sibling spacing.

### Container Queries Over Media Queries

Viewport queries for page layouts. Container queries for components:

```css
.card-container { container-type: inline-size; }

@container (min-width: 400px) {
  .card { grid-template-columns: 120px 1fr; }
}
```

A card in a narrow sidebar stays compact; the same card in main content expands automatically.

### Self-Adjusting Grid

```css
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
```

### Hierarchy Through Multiple Dimensions

Don't rely on size alone. Combine 2-3 at once:

| Tool | Strong | Weak |
|------|--------|------|
| Size | 3:1+ ratio | <2:1 ratio |
| Weight | Bold vs Regular | Medium vs Regular |
| Color | High contrast | Similar tones |
| Position | Top/left | Bottom/right |
| Space | Surrounded by whitespace | Crowded |

### Optical Adjustments

Text at `margin-left: 0` looks indented due to letterform whitespace — use negative margin (`-0.05em`) to optically align. Play icons need to shift right. Geometrically centered icons often look off-center.

### Touch Targets vs Visual Size

Buttons can look small but need 44px minimum touch targets:

```css
.icon-button { width: 24px; height: 24px; position: relative; }
.icon-button::before { content: ''; position: absolute; inset: -10px; }
```

---

## Reference: Motion

### Duration Rules

| Duration | Use Case |
|----------|----------|
| 100-150ms | Instant feedback (button press, toggle) |
| 200-300ms | State changes (menu, tooltip, hover) |
| 300-500ms | Layout changes (accordion, modal, drawer) |
| 500-800ms | Entrance animations (page load, hero) |

Exit animations: ~75% of entrance duration. Don't use `ease` — it's a compromise.

### Easing

```css
--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);   /* Smooth, refined default */
--ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);     /* Snappy, confident */
```

Only animate `transform` and `opacity`. For height animations, use `grid-template-rows: 0fr` to `1fr`.

### Reduced Motion (not optional)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Reference: Interaction Patterns

### Focus Rings

Never `outline: none` without replacement. Use `:focus-visible` for keyboard-only rings:

```css
button:focus { outline: none; }
button:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
```

### Input Method Detection

```css
@media (pointer: coarse) { .button { padding: 12px 20px; } }  /* Touch */
@media (pointer: fine) { .button { padding: 8px 16px; } }      /* Mouse */
@media (hover: none) { /* No hover states — use active instead */ }
```

### Loading States

Skeleton screens > spinners. Optimistic updates for low-stakes actions (likes, follows), never for payments. The 80ms threshold: anything under 80ms feels instant.

### Undo > Confirm

Users click through confirmation dialogs mindlessly. Remove from UI immediately, show undo toast, delete after toast expires. Reserve confirmation for truly irreversible actions.

---

## Optical correction patterns (reference: LiftKit)

LiftKit (github.com/Chainlift/liftkit, ~3k stars) is an open-source UI framework built on golden ratio spacing. Not a dependency — just a reference for optical correction patterns worth stealing:

**Golden ratio scale system.** All spacing derives from a single scale factor (1.618) with musical-interval subdivisions. Sizes cascade: `sm = 1em / 1.618`, `lg = 1em * 1.618`, `xl = lg * 1.618`. The insight: you never pick arbitrary spacing values. Everything is a ratio of everything else.

**Button icon-padding asymmetry fix.** When a button has an icon on one side, equal padding on both sides *looks* unequal because the icon adds visual weight. Reduce padding on the icon side: `padding-icon-side = fontSize / 1.618` vs `padding-text-side = fontSize`. Icons also get a small vertical optical shift to compensate for glyphs sitting high in their bounding box.

**Card top-padding optical correction.** Text inside a card creates extra visual whitespace at the top due to line-height. Compute an offset per text size (`offset = fontSize * (lineHeight / 1.618)`) and subtract it from the top padding. Larger text gets proportionally more correction.

**Practical takeaway:** You don't need to install LiftKit. Define `--scale: 1.618` and derive spacing/type tokens from it. The optical corrections are CSS patterns you can lift directly. The core idea: "equal" padding is a lie — what looks equal requires math that accounts for content shape.

---

## Output format for design reviews

```
DESIGN REVIEW

Identity: [defined / undefined] — [what world is this product in?]
Squint test: Eye goes to [X]. Hierarchy [correct/broken]. [N] zones. Action [clear/unclear].
Remove test: [N] elements are decoration. Load-bearing elements: [list].
Copy test: Text alone [works/fails]. Visuals alone [works/fails].
Register: [current register] → should be [target register].
AI slop check: [pass/fail] — [specific tells if any]

Biggest issue: [1 sentence — the single thing to fix first]
Steal from: [1 reference product and what to take from it]
```

## Reference: Branding Inspiration Sources

When building brand identity, visual language, or moodboards — use these instead of generic Pinterest/Dribbble:

| Site | What it's good for |
|------|--------------------|
| [rebrand.gallery](https://rebrand.gallery/) | Brand redesign case studies — before/after with rationale. Study decisions, not pixels. |
| [visualjournal.it](https://visualjournal.it/) | Curated visual design — editorial, print, identity. High signal-to-noise. |
| [bpando.org](https://bpando.org/) | Design, architecture, art crossover. Good for expanding visual vocabulary beyond screens. |
| [cosmos.so](https://cosmos.so/) | Visual bookmarking and moodboard tool. Better than Pinterest for design research — no recipe noise. |
| [brandarchive.xyz](https://brandarchive.xyz/) | Brand identity archive — logos, guidelines, packaging. How established brands systematize their visual language. |
| [are.na](https://are.na/) | Creative research platform. Follow channels by topic. The thinking person's Pinterest. |
| [abduzeedo.com](https://abduzeedo.com/) | Long-running design inspiration blog. Daily exposure to diverse visual styles. |
| [worldbranddesign.com](https://worldbranddesign.com/) | Packaging and brand design focus. When physical/phygital brand expression matters. |

**How to use these for taste training:** Pick one site per week. Save 5 things you find compelling, write one sentence each about WHY. After a month you'll see patterns in your own taste. Those patterns become your brand's visual DNA.

---

## What this skill is NOT

- Not a design system generator
- Not a component library recommendation engine
- Not a color/font picker
- This is judgment training + anti-pattern detection, not execution tooling

---

*From [AGT Skill Pack](https://github.com/somnus0x/agt-skill-pack) — free skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand)*
