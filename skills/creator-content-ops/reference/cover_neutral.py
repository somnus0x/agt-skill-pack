#!/usr/bin/env python3
"""cover_neutral.py — a NEUTRAL, code-composed post cover generator.

No brand baked in. You set the colors, the two headline lines, and your own
lockup. Text is RENDERED with a real font (never generated), so it is
pixel-exact every run and Thai never breaks. This is the deterministic path;
for creative/one-off covers use the Codex ImageGen method instead.

The two headline lines are the whole cover: line 1 is the claim/hook, line 2 is
the gap or payoff. A cover that just describes a topic dies. A cover that takes
a position or names a problem travels.

Dependencies: Pillow. (`pip install pillow`)

Usage:
    python cover_neutral.py cover.json out.png

where cover.json looks like:
    {
      "size": [1080, 1350],
      "bg": [15, 17, 22],
      "accent": [111, 214, 79],
      "line1": "your claim / hook",
      "line2": "the gap or the payoff",
      "brand": "Your Name",
      "handle": "@yourhandle"
    }
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --- fonts: resolved per-OS so this works on Mac/Windows/Linux, not just Linux.
# Set THAI_FONT / LATIN_FONT env vars to override with your own.
import os

_THAI_CANDIDATES = [
    os.environ.get("THAI_FONT"),
    "/usr/share/fonts/truetype/noto/NotoSansThai-Bold.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansThai-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Thonburi.ttc",
    "/Library/Fonts/NotoSansThai-Bold.ttf",
    "/System/Library/Fonts/Thonburi.ttc",
    "C:/Windows/Fonts/Leelawad.ttf",
    "C:/Windows/Fonts/leelawui.ttf",
    "C:/Windows/Fonts/tahoma.ttf",
]
_LATIN_CANDIDATES = [
    os.environ.get("LATIN_FONT"),
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/arial.ttf",
]


def _resolve(candidates: list, label: str) -> str:
    for p in candidates:
        if p and Path(p).exists():
            return p
    raise FileNotFoundError(
        f"No {label} font found. Tried: {[c for c in candidates if c]}. "
        f"Install one, or set the {label.upper()}_FONT env var to a .ttf/.ttc path. "
        f"Recommended free option: Noto Sans Thai + Noto Sans."
    )


THAI_B = _resolve(_THAI_CANDIDATES, "thai")
LAT_B = _resolve(_LATIN_CANDIDATES, "latin")
WHITE = (245, 245, 247)
DIM = (126, 133, 144)


def F(path: str, sz: int) -> ImageFont.FreeTypeFont:
    # Paths are pre-resolved above; never mask a failure with load_default()
    # (a bitmap font with no Thai glyphs → silent tofu).
    return ImageFont.truetype(path, sz)


def _use_latin(ch: str) -> bool:
    # Thai-block codepoints (U+0E00..U+0E7F) stay on the Thai font so combining
    # vowels/tones stack on the base consonant. Everything else (digits, ASCII,
    # latin) goes to the Latin font, which the Thai font lacks glyphs for.
    return not ("\u0e00" <= ch <= "\u0e7f")


def dtext(d, xy, text, font, fill, latin_font=None):
    """Mixed Thai/Latin text: render in same-font runs so nothing turns to tofu."""
    if latin_font is None:
        latin_font = F(LAT_B, font.size)
    x, y = xy
    run, run_latin = "", None
    for ch in text:
        want = _use_latin(ch)
        if run and want != run_latin:
            f = latin_font if run_latin else font
            d.text((x, y), run, font=f, fill=fill)
            x += d.textlength(run, font=f)
            run = ""
        run += ch
        run_latin = want
    if run:
        f = latin_font if run_latin else font
        d.text((x, y), run, font=f, fill=fill)


def _is_thai_combining(ch: str) -> bool:
    # Thai above/below vowels + tone marks — must stay glued to their base
    # consonant; a break before one orphans the mark and corrupts the syllable.
    o = ord(ch)
    return o == 0x0E31 or 0x0E34 <= o <= 0x0E3A or 0x0E47 <= o <= 0x0E4E


def _cluster_wrap(draw, token, font, maxw):
    """Break an unspaced token (Thai) at safe character boundaries."""
    lines, cur = [], ""
    for ch in token:
        if _is_thai_combining(ch):
            cur += ch
            continue
        if cur and draw.textlength(cur + ch, font=font) > maxw:
            lines.append(cur)
            cur = ch
        else:
            cur += ch
    if cur:
        lines.append(cur)
    return lines


def wrap(draw, text, font, maxw):
    """Wrap on spaces (Latin) and fall back to Thai-safe cluster breaking for
    any single token that overflows (unspaced Thai). Fixes the right-edge clip."""
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= maxw:
            cur = test
            continue
        if cur:
            lines.append(cur)
            cur = ""
        if draw.textlength(w, font=font) > maxw:
            parts = _cluster_wrap(draw, w, font, maxw)
            lines.extend(parts[:-1])
            cur = parts[-1] if parts else ""
        else:
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render_cover(spec: dict, out: Path):
    W, H = spec.get("size", [1080, 1350])
    bg = tuple(spec.get("bg", [15, 17, 22]))
    accent = tuple(spec.get("accent", [111, 214, 79]))
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    # corner brackets (neutral decoration; delete if you don't want them)
    d.line([(60, 60), (140, 60)], fill=accent, width=4)
    d.line([(60, 60), (60, 140)], fill=accent, width=4)
    d.line([(W - 140, H - 60), (W - 60, H - 60)], fill=accent, width=4)
    d.line([(W - 60, H - 140), (W - 60, H - 60)], fill=accent, width=4)

    # line 1 (claim) white, line 2 (gap/payoff) accent
    y = 300
    for seg in wrap(d, spec.get("line1", ""), F(THAI_B, 92), W - 200):
        dtext(d, (100, y), seg, F(THAI_B, 92), WHITE)
        y += 130
    y += 30
    for seg in wrap(d, spec.get("line2", ""), F(THAI_B, 72), W - 200):
        dtext(d, (100, y), seg, F(THAI_B, 72), accent)
        y += 100

    # your lockup — rename freely
    brand = spec.get("brand", "Your Name")
    handle = spec.get("handle", "@yourhandle")
    by = H - 100
    d.rounded_rectangle([100, by, 150, by + 50], radius=10, fill=accent)
    d.text((112, by + 8), brand[:1].upper(), font=F(LAT_B, 34), fill=bg)
    dtext(d, (165, by + 4), brand, F(LAT_B, 30), WHITE)
    hw = d.textlength(handle, font=F(LAT_B, 26))
    d.text((W - 100 - hw, by + 10), handle, font=F(LAT_B, 26), fill=DIM)

    img.save(out)
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    spec = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "cover.png")
    print("RENDERED:", render_cover(spec, out))


if __name__ == "__main__":
    main()
