# SETUP — build your CONTENT.md (the AI runs this interview)

You are setting up a content creator's AI stack. Your job is to interview the user,
collect real material, and write them a `CONTENT.md` that makes every future draft sound
like THEM instead of like a generic model. Do not skip steps. Do not invent a voice from
nothing — extract it from what they hand you.

Run this as a conversation, one block at a time. Wait for each answer before moving on.

---

## Step 0 — check the tools are here

Before the interview, verify what's installed and tell the user what's missing. Do not
assume. Run:

```bash
python3 -c "import PIL; print('Pillow', PIL.__version__)" 2>&1
which ffmpeg 2>&1
codex --version 2>&1                                            # only if using ImageGen
```

**Fonts — find them, don't assume the path.** The render scripts auto-resolve a Thai
and a Latin font across Linux / macOS / Windows, and *fail loud* with a clear message if
none is found (they never silently render tofu boxes). Your job here is to confirm at
least one real Thai font exists on THIS machine and, if the OS isn't Linux, find its
actual path so you can hand it to the script.

If you (the agent) are running inside the user's environment, resolve it yourself:

```bash
# Linux
fc-list :lang=th 2>/dev/null | head
# macOS
ls "/System/Library/Fonts/Supplemental/" 2>/dev/null | grep -iE 'thonburi|noto.*thai|leelawadee'
system_profiler SPFontsDataType 2>/dev/null | grep -iA1 thai | head
# Windows (PowerShell)
# Get-ChildItem C:\Windows\Fonts | Where-Object { $_.Name -match 'leelaw|noto.*thai|tahoma' }
```

Take the real `.ttf` / `.ttc` path you find and pass it via env var (the scripts read
`THAI_FONT` / `LATIN_FONT` and prefer them over the built-in guesses):

```bash
export THAI_FONT="/absolute/path/to/your/thai-font.ttf"
export LATIN_FONT="/absolute/path/to/your/latin-font.ttf"   # optional; a Latin default usually exists
```

If NO Thai font exists, tell the user to install one (free): macOS
`brew install --cask font-noto-sans-thai`, Windows Leelawadee is built in, Linux
`apt install fonts-noto`. Do not proceed to render until a real Thai font resolves.

Report the gaps in plain language: "You have Pillow and a Thai font (Thonburi on your
Mac, wired via THAI_FONT). ffmpeg is missing, so the Shorts module won't run until you
install it. Codex CLI isn't set up, so cover-gen will use the code template only." Do NOT
proceed to write files the user can't run.

---

## Step 1 — collect the voice samples (the load-bearing step)

Say to the user, in their language:

> Hand me 5 to 10 pieces of your writing that you're proud of. Real posts, real
> captions, real threads — the ones that felt like YOU when you wrote them. Paste them or
> give me file paths. The more real the samples, the sharper your voice file. Garbage
> samples in, generic voice out.

Read every sample. Extract, and read back to the user for confirmation:
- **Sentence rhythm** — long breathing paragraphs, or short punchy lines?
- **Recurring words / phrases** they actually use
- **Metaphor world** — what do they reach for? (sport, cooking, gaming, building, film…)
- **How they open** a piece, and how they close it
- **Pronoun density** — do they start every line with "I / ผม"? (a common AI-smell tell)

Do not sanitize. If they write "บอกเลย" or "ngl" or "here's the thing," those ARE the
voice. Keep the exact phrasing.

---

## Step 2 — the no-go list (what is NOT their voice)

Ask:

> Now the opposite. Show me one AI draft of your stuff that felt WRONG, or just tell me:
> what words, tones, or moves are never you? The stuff that makes you go "I'd never say
> that."

Capture concretely. Push for examples, not adjectives. "No corporate tone" is weak;
"never 'unlock', never 'in today's fast-paced world', never a metaphor about hospitals"
is usable. Also flag automatically, because they're near-universal AI tells:
- **em-dash (—)** — the #1 AI signature. Default it to the no-go list.
- humble-brag openers ("I did X without spending a dollar on ads")
- "It's not just X, it's Y" runway phrasing
- borrowed metaphors from a world they don't live in

---

## Step 3 — the channels

Ask which formats they actually ship, and for each, one line of how it differs:

> Which of these do you produce? For each, tell me how the voice shifts.
> - long posts / blog
> - TikTok or IG carousels
> - YouTube Shorts / short video
> - X / threads

Most creators have ONE core voice that flexes per platform (a carousel card is terser
than a blog paragraph). Capture the flex as a row per platform, not a new voice each.

---

## Step 4 — tools & auth (say what stays private)

Ask what they'll use to produce, and be explicit about the boundary:

> What do you generate images/video with? (Codex CLI, an API, Canva, none yet)

Tell them plainly: **the kit renders and composes; it never handles your account
uploads or a private voice model.** If they mention platform auth (YouTube tokens, API
keys), tell them to keep those OUT of the CONTENT.md and out of any repo — the kit
produces the file, they publish it by hand or with their own private step.

---

## Step 5 — write CONTENT.md

Fill the `CONTENT.md` scaffold in this directory with everything above. Rules for the write:

1. **Zero em-dashes in the file itself.** It is a document about killing AI-smell. If it
   contains the #1 AI tell, it fails its own test. Use a period, a comma, or "→" instead.
2. **Use the user's exact words** in the DO/DON'T rows, not a paraphrase. Their language
   is the voice.
3. **Concrete over abstract.** Every rule gets a real example from their samples. "Be
   authentic" is useless. "Cut 'ไม่ได้ run ads สักบาท' → say 'เซ็ตไว้แบบนี้ เอาไปลองได้'" is a rule.
4. **The 3 filters are non-negotiable** — every CONTENT.md ships with them (below). The
   examples get personalized; the filters stay.

Then read the finished file back to the user and ask: "Does this sound like you? What's
wrong?" Iterate until they say yes. A voice file they don't trust is a diary nobody reads.

---

## Step 6 — wire the modules

Point each module at the user's real setup:
- **carousel** / **cover** → do NOT hand-edit font paths in the `.py` files. The scripts
  auto-resolve fonts and honor the `THAI_FONT` / `LATIN_FONT` env vars from Step 0 — set
  those instead (survives updates, doesn't fork the source). Only rename the `brand_bar`
  lockup to their brand. If a render raises a "No thai font found" error, the fix is the
  env var, not a code edit.
- **codex_imagegen** → confirm Codex CLI auth from Step 0; the prompt templates are
  neutral, they fill the text.
- **shorts** → confirm ffmpeg; point at their raw-material folder.

Do a smoke test per wired module (render one card, gen one cover) and show the output.
Do not tell the user it works. Show them the PNG.

---

## The 3 filters (ship in every CONTENT.md — do not omit)

These are the gates every draft passes before it's allowed to ship. They are what catches
AI-smell that a prompt alone never will.

1. **โม้มั้ย? / Brag check** — "If I said this at dinner with friends, would it sound like
   showing off?" Humble-brags and flex-openers get cut here.
2. **เสียงเรามั้ย? / Voice check** — "Is this a metaphor / word from MY world, or one the
   AI borrowed?" If it's not from your world, swap it or cut it.
3. **Dinner test** — read the whole piece and ask: "teaching? → cut. bragging? → cut.
   telling a friend a story? → ship." If you wouldn't type it in a group chat with
   friends, don't let the AI write it.
