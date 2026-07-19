# shorts_pipeline — assemble Shorts from raw material (method, not a black box)

The same split as everything else in this kit: **AI gens the raw material, code composes
the deliverable.** For Shorts that means AI/stock supplies the visual loop and the audio,
and ffmpeg assembles the 1080x1920 vertical with your overlays. The text on screen is
rendered (Pillow), never generated, so it never breaks and never drifts between clips.

This is a method doc on purpose. Shorts pipelines are the most channel-specific thing you
own (your loop style, your audio, your lower-thirds), so the kit ships the PATTERN and you
wire your own assets. Your finished channel pipeline and your platform upload auth stay
yours and out of any repo.

## The pipeline shape

```
raw material            compose (ffmpeg + Pillow)           output
─────────────           ─────────────────────────           ──────
visual loop  ─┐
(AI / stock)  ├─→  1. enhance the loop (grain, drift,   ─→  1080x1920.mp4
audio bed    ─┘       light sweep — optional polish)         (ready to upload
overlay text ─────→  2. render text overlays with a          BY HAND / your
(from CONTENT.md)     real font (Pillow → PNG w/ alpha)       own private step)
                   3. ffmpeg: scale/pad to 1080x1920,
                      burn overlays, mux audio, trim
```

## Step 1 — raw material

- **Visual:** a short loop. Generate it (Codex ImageGen for stills you animate, or your
  video model) or use stock. Keep it longer than your target so you can trim.
- **Audio:** a bed you have the rights to. The kit does not supply audio.
- **Copy:** the on-screen text. Write it through CONTENT.md so the hook sounds like you,
  not like a generic Shorts script. Hook lands in the first 2 seconds or the view is gone.

## Step 2 — optional polish on the loop

A raw loop reads flat. Cheap ffmpeg polish that reads "produced":
- film grain (`noise` filter), subtle Ken-Burns drift (slow `zoompan`), a light sweep, a
  vignette pulse. Keep it subtle. Over-polished reads as fake.

Reference ffmpeg skeleton (adjust filters to taste):

```bash
ffmpeg -i loop.mp4 \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,\
noise=alls=8:allf=t,vignette=PI/5" \
  -t 30 -c:v libx264 -pix_fmt yuv420p enhanced.mp4
```

## Step 3 — render the text overlays (do NOT gen them)

Same principle as the carousel: text is rendered with a font, transparent PNG, then burned
on. This is why Thai never breaks in your Shorts. Reuse the `dtext` tofu-fix from
`carousel_factory.py` — draw onto an RGBA canvas, save PNG, then:

```bash
ffmpeg -i enhanced.mp4 -i overlay.png \
  -filter_complex "[0][1]overlay=0:0" \
  -i audio.mp3 -shortest -c:v libx264 -c:a aac out_1080x1920.mp4
```

## What the kit deliberately leaves to you

- **Platform upload.** No account tokens, no OAuth, no auto-publish. The kit produces the
  finished MP4; you upload it by hand or with your own private step. Keep any platform
  auth out of CONTENT.md and out of any repo.
- **Your signature loop / audio / lower-third style.** That IS your channel. The kit gives
  the assembly pattern, not your look.

## Deps

- `ffmpeg` (assembly + polish)
- `Pillow` (text overlays, shares the tofu-fix with the carousel module)
