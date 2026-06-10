---
name: ai-slop-detection
description: |
  Detect whether a UI looks AI-generated. Use during design review to run the fingerprint
  test: identifies the default-theme, gradient, and layout tells that make interfaces read
  as AI slop, and how to fix each one.
---

# AI Slop Detection — Does Your UI Look AI-Generated?

The fingerprint test: if you showed your interface to someone and said "AI made this," would they believe you immediately? If yes, the design has failed.

A distinctive interface makes someone ask "how was this made?" — not "which AI made this."

## The Tells

These are the patterns of 2024-2025 AI-generated frontends. Flag ANY of these during review.

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
- Glassmorphism everywhere — blur effects, glass cards, glow borders used decoratively
- Rounded rectangles with generic drop shadows — safe, forgettable, could be any AI output
- Rounded elements with thick colored border on one side — lazy accent
- Sparklines as decoration — tiny charts that look sophisticated but convey nothing
- Modals for everything — modals are lazy; there's almost always a better pattern

### The AI Font Choice
- Inter, Roboto, Arial, Open Sans everywhere — invisible defaults
- Monospace typography as lazy shorthand for "technical/developer" vibes
- Too many sizes too close together (14px, 15px, 16px, 18px) — creates muddy hierarchy

### The AI Motion Pattern
- Bounce or elastic easing — trendy in 2015, tacky now; real objects decelerate smoothly
- Every button primary — use ghost buttons, text links, secondary styles; hierarchy matters
- Redundant copy — headers that restate the heading, intros that repeat what users can see

## How to Use This

### Quick Audit (2 minutes)

Open your UI. Run through this checklist:

```
AI SLOP AUDIT — [project name]

Color:
[ ] Using cyan/purple/neon gradients?
[ ] Gradient text on headings?
[ ] Pure black or pure white background?
[ ] Dark mode with glowing accents?

Layout:
[ ] Hero metric "dashboard starter kit"?
[ ] Identical card grids?
[ ] Everything centered?
[ ] Cards nested inside cards?

Visuals:
[ ] Glassmorphism / glass cards?
[ ] Generic rounded rectangles with shadows?
[ ] Decorative sparklines?

Typography:
[ ] Inter/Roboto/Arial as only font?
[ ] Random monospace for "dev vibes"?
[ ] Muddy size hierarchy?

Motion:
[ ] Bounce/elastic easing?
[ ] Every button looks the same?

Score: [N] / 15 tells detected
```

- **0-2 tells**: You're fine. Ship it.
- **3-5 tells**: Review needed. These are fixable.
- **6+ tells**: The UI screams "AI made this." Redesign before shipping.

### The Fix Pattern

For each tell you find, the fix is usually the opposite:

| AI Slop | Fix |
|---------|-----|
| Gradient text | Solid color, one accent |
| Everything centered | Left-align body, asymmetric layout |
| Glassmorphism | Solid backgrounds, subtle borders |
| Identical card grid | Vary card sizes, break the grid |
| Inter everywhere | Pick one distinctive typeface |
| Bounce easing | Ease-out or custom cubic-bezier |
| All buttons primary | One primary, rest ghost/text |
| Pure black bg | Tinted dark (#0a0a0f, #0d0f0e) |

## The Deeper Point

AI-generated UIs aren't bad because AI made them. They're bad because they're generic. They look like every other AI output because the models converge on the same "safe" patterns from training data.

The fix isn't "don't use AI for UI." The fix is: generate with AI, then apply taste. Remove the tells. Add the one distinctive choice that makes it yours. One unusual color. One unexpected layout break. One typeface nobody else is using.

Generic is the enemy. Distinctive is the goal.

---

*From [AGT Skill Pack](https://github.com/somnus0x/agt-skill-pack) — free skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand)*
