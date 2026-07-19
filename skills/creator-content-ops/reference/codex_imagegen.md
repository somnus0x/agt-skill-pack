# codex_imagegen — headless image generation via Codex CLI

The creative path. Use this for the raw MATERIAL a carousel or cover needs (backgrounds,
hero shots, portraits, diagrams) and for one-off covers where you want creative freedom
over pixel-exactness. For final production covers that must be identical every run, use
`cover_neutral.py` instead. This is the "AI gens the imagination" half of the split.

Generate from the terminal, no browser, no Pillow font pain. gpt-image-2 renders Thai
(and other scripts) correctly, which Pillow struggles with on mixed text.

## Prerequisites

- Codex CLI authed (`/usr/bin/codex --version`). Uses your ChatGPT account, no API key.
- Model `gpt-5.5` (image gen lives here; gpt-5.4 is text-only).
- Sandbox is read-only → images save to `~/.codex/generated_images/<session-id>/`, you
  copy them out.

## The one rule that matters: the forcing clause

`codex exec` is an AGENT, not an image API. Without an explicit directive it improvises:
returns raw SVG, draws with code, or hallucinates an off-brief image. **Always lead AND
close the prompt with the gpt-image-2 directive.** This is not optional polish.

```bash
cat << 'PROMPT' | /usr/bin/codex exec --model gpt-5.5
Generate an image using gpt-image-2 image generation. Do NOT draw with code, SVG, HTML,
or canvas — call the image model directly.

[your detailed description here]

Specs:
- Dimensions: [WxH, e.g. vertical 1080x1350]
- Background: [color / mood]
- Text: [exact text in quotes, or "no text"]
- Style: [flat design, no gradients, no 3D — for diagrams; or your aesthetic]

Generate the image with gpt-image-2 and save it as a PNG.
PROMPT
```

## Locate + copy + verify (per image)

```bash
# newest generated file
find ~/.codex/generated_images/ -type f -name "*.png" -printf '%T@ %p\n' | sort -nr | head -1
# copy to your project
cp ~/.codex/generated_images/<session-id>/<file>.png ./material/hero.png
# verify it actually rendered (a silent SVG/no-file failure looks like success)
python3 -c "from PIL import Image; i=Image.open('./material/hero.png'); print(i.size, i.mode)"
```

**One image per call. Verify each before the next.** Codex backgrounds every `exec`; a
failed gen looks identical to a good one until you open the PNG.

## Neutral templates (fill the brackets)

### Cover (creative path)

```bash
cat << 'PROMPT' | /usr/bin/codex exec --model gpt-5.5
Generate an image using gpt-image-2 image generation (do NOT draw with code, SVG, or
canvas — use the image model directly).

Vertical post cover (1080x1350). [Your background: color / mood / texture].

Main text, upper-left:
Line 1 (large, bold): "[YOUR CLAIM / HOOK]"
Line 2 (smaller, accent color): "[THE GAP OR PAYOFF]"

[Optional: your lockup — small mark + name, bottom.]

Style: [your aesthetic]. No illustrations unless specified. Text-focused.

Generate the image with gpt-image-2 and save it as a PNG.
PROMPT
```

### Diagram / flowchart (below-post)

```bash
cat << 'PROMPT' | /usr/bin/codex exec --model gpt-5.5
Generate an image using gpt-image-2 image generation (do NOT draw with code or SVG).

Technical diagram. [Describe the flow: boxes, arrows, labels — spell out each label,
including exact Thai text in quotes so it renders correctly.]

Specs:
- [background color], 16:9 (1920x1080)
- [accent color] for highlights
- flat design, minimal, clean sans-serif, no gradients, no 3D, no photos

Generate the image with gpt-image-2 and save it as a PNG.
PROMPT
```

### Background / hero material for a carousel

```bash
cat << 'PROMPT' | /usr/bin/codex exec --model gpt-5.5
Generate an image using gpt-image-2 image generation (do NOT draw with code or SVG).

[Describe the scene / texture / subject. NO text baked in — the text gets rendered by
carousel_factory.py on top. Just the raw visual.]

Dimensions: [match your carousel shot_box].

Generate the image with gpt-image-2 and save it as a PNG.
PROMPT
```

## Known limits

- **Dimensions ±5%.** gpt-image-2 approximates size. For exact pixels use the code path.
- **Non-deterministic.** Same prompt, different layout each run. Fine for material and
  one-offs; not for a brand you need identical every time (that's `cover_neutral.py`).
- **Not for multi-region brand boards / swatch grids.** It mangles structured layouts.
  Single subject / single cover / single diagram only.
- **Text can misspell uncommon words.** Always open the PNG and check.
- **~10-30K tokens per call.** Get the prompt right, don't iterate ten times.
