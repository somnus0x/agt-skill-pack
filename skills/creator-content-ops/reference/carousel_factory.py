#!/usr/bin/env python3
"""Faceless Factory — a JSON-driven carousel/card render template.

The point: AI generates the raw material (backgrounds, characters, hero shots),
CODE assembles the deliverable. Text is RENDERED with a real font, never
generated — so it comes out identical every run and Thai never breaks.

This is a template, not a framework. Copy it, point FONT paths at your fonts,
and feed it your own JSON. The three reusable pieces are:
  - dtext()      : mixed Thai/Latin/digit text (the tofu fix)
  - place_shot() : cover-crop + rounded-mask image placement
  - wrap()       : width-aware word wrap
  - brand_bar()  : a bottom brand lockup

Dependencies: Pillow. (`pip install pillow`)

Usage:
    python carousel_factory.py cards.json ./out

where cards.json looks like:
    {
      "size": [1080, 1350],
      "cards": [
        {
          "output": "01-hook.png",
          "shot":   "assets/hero.png",           # optional AI-gen'd raw material
          "shot_box": [0, 0, 1080, 560],
          "shot_darken": 0.3,
          "index": 1, "total": 5,
          "lines": [
            {"xy": [70, 600], "text": "WORKFLOW",           "size": 26, "color": "green"},
            {"xy": [70, 650], "text": "ใช้ AI 3 ตัว ทำงานนึง", "size": 92, "color": "white"}
          ]
        }
      ]
    }
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --- palette (tinted dark, desaturated accent — not neon) --------------------
BG = (15, 17, 22)
BG_HI = (25, 29, 36)
GREEN = (111, 214, 79)
WHITE = (245, 245, 247)
SUB = (188, 193, 202)
DIM = (126, 133, 144)
COLORS = {"bg": BG, "bg_hi": BG_HI, "green": GREEN, "white": WHITE, "sub": SUB, "dim": DIM}

# --- fonts: point these at fonts that ship on your machine -------------------
# Noto Sans Thai + Noto Sans (Latin) are a safe, free default on most Linux.
THAI_B = "/usr/share/fonts/truetype/noto/NotoSansThai-Bold.ttf"
LAT_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"


def F(path: str, sz: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, sz)
    except Exception:
        return ImageFont.load_default()


def _use_latin(ch: str) -> bool:
    # Only Thai-block codepoints (U+0E00..U+0E7F) stay on the Thai font so their
    # combining vowels/tones stack on the base consonant. Everything else —
    # digits, ASCII punctuation, arrows, latin letters — goes to the Latin font,
    # which the Thai font lacks glyphs for (was rendering as tofu boxes).
    return not ("\u0e00" <= ch <= "\u0e7f")


def dtext(d, xy, text, font, fill, latin_font=None):
    """Draw text in runs: consecutive same-font chars render together.

    Thai runs render whole (so combining vowels/tones stack correctly);
    Latin/digit/arrow runs swap to a Latin font (the Thai font lacks those
    glyphs). This is the single most valuable trick in the file.
    """
    if latin_font is None:
        latin_font = F(LAT_B, font.size)
    x, y = xy
    run = ""
    run_latin = None
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


def wrap(draw, text, font, maxw):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= maxw:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def place_shot(img, shot_path, box, darken=0.0, radius=24):
    """Fit an image into box (x, y, w, h): cover-crop, optional darken, round."""
    x, y, bw, bh = box
    s = Image.open(shot_path).convert("RGB")
    sr, br = s.width / s.height, bw / bh
    if sr > br:
        nh, nw = bh, int(bh * sr)
    else:
        nw, nh = bw, int(bw / sr)
    s = s.resize((nw, nh))
    s = s.crop(((nw - bw) // 2, (nh - bh) // 2, (nw - bw) // 2 + bw, (nh - bh) // 2 + bh))
    if darken:
        s = Image.blend(s, Image.new("RGB", s.size, (0, 0, 0)), darken)
    mask = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, bw, bh], radius=radius, fill=255)
    img.paste(s, (x, y), mask)


def brand_bar(d, W, H, brand="Agent Dev Thailand", idx=None, total=None):
    """A bottom brand lockup. Rename `brand` to whatever you're building."""
    y = H - 90
    d.rounded_rectangle([60, y, 110, y + 50], radius=10, fill=GREEN)
    d.text((72, y + 8), brand[:1].upper(), font=F(LAT_B, 34), fill=BG)
    d.text((125, y + 4), brand, font=F(LAT_B, 30), fill=WHITE)
    if idx is not None and total is not None:
        tag = f"{idx} / {total}"
        tw = d.textlength(tag, font=F(LAT_B, 26))
        d.text((W - 60 - tw, y + 8), tag, font=F(LAT_B, 26), fill=DIM)


def render_card(card: dict, W: int, H: int, out_dir: Path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    if card.get("shot"):
        place_shot(
            img, card["shot"], card.get("shot_box", [0, 0, W, H]),
            darken=card.get("shot_darken", 0.0),
        )
        d = ImageDraw.Draw(img)

    for ln in card.get("lines", []):
        color = COLORS.get(ln.get("color", "white"), WHITE)
        font = F(THAI_B, ln.get("size", 40))
        maxw = ln.get("wrap")
        if maxw:
            for i, seg in enumerate(wrap(d, ln["text"], font, maxw)):
                dtext(d, (ln["xy"][0], ln["xy"][1] + i * int(ln.get("size", 40) * 1.5)),
                      seg, font, color)
        else:
            dtext(d, tuple(ln["xy"]), ln["text"], font, color)

    brand_bar(d, W, H, card.get("brand", "Agent Dev Thailand"),
              card.get("index"), card.get("total"))

    out = out_dir / card["output"]
    img.save(out)
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    spec = json.loads(Path(sys.argv[1]).read_text())
    out_dir = Path(sys.argv[2] if len(sys.argv) > 2 else ".")
    out_dir.mkdir(parents=True, exist_ok=True)
    W, H = spec.get("size", [1080, 1350])
    print("RENDERING:")
    for card in spec["cards"]:
        print("  ", render_card(card, W, H, out_dir))


if __name__ == "__main__":
    main()
