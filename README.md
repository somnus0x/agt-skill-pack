# AGT Skill Pack

Free AI skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand).

[![Facebook](https://img.shields.io/badge/Facebook-Agent%20Dev%20Thailand-1877F2?style=flat&logo=facebook)](https://facebook.com/agentdevthailand)
![Skills](https://img.shields.io/badge/Skills-11-blue)
![Platforms](https://img.shields.io/badge/Platforms-Claude_Code_%7C_Codex_%7C_Cursor-green)

> ฝรั่งแจกพร้อมท์ฟรีกัน ทำไมคนไทยต้องซื้อพร้อมท์

## Quick Start

**Install all skills (Claude Code):**
```bash
curl -sL https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/install.sh | bash
```

**Install one skill:**
```bash
curl -sL https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/install.sh | bash -s factory-review
```

**Clone and go (Claude Code / Codex / Cursor):**
```bash
git clone https://github.com/somnus0x/agt-skill-pack.git
cd agt-skill-pack
# Open in your AI tool and start talking
```

**Any AI chat (Claude.ai / ChatGPT / Gemini):**
Open the skill file, copy the prompt, paste as your first message.

---

## Skills

### Factory Review — Cross-Model Adversarial Critique
> "ผมให้ AI ตัวอื่น review ก่อน deploy ทุกครั้ง"

Use a different AI model to review anything your primary AI produced. Same-model self-review has blind spots — a different model catches what yours missed.

**5 review modes:** Content, Spec/Architecture, Code, Fact-Check, Quick Review

**Try:** `"review this draft"` · `"red team this spec"` · `"sanity check this code"`

📄 [`skills/factory-review/SKILL.md`](skills/factory-review/SKILL.md)

---

### Product Taste — What to Build, What to Cut
> "ก่อน build feature ถามตัวเอง 5 ข้อนี้ก่อน"

5-filter evaluation for product decisions. Runs features through who-suffers, replaces-what, core-loop, cost-of-being-right, and ship-without-it filters. Kills bad ideas before you waste a sprint.

**Try:** `"should we build this?"` · `"taste check"` · `"what would you cut?"`

📄 [`skills/product-taste/SKILL.md`](skills/product-taste/SKILL.md)

---

### Decision Decay — When Past Decisions Go Stale
> "คุณเคยกลับไปดูมั้ยว่า decision เดือนก่อนยังถูกอยู่?"

Re-evaluate past decisions when assumptions change. Scores decay as Fresh, Aging, or Stale. Because a choice that was correct in January may be wrong in March.

**Try:** `"is this still the right call?"` · `"decay check"` · `"revisit our DB decision"`

📄 [`skills/decision-decay/SKILL.md`](skills/decision-decay/SKILL.md)

---

### Accountability Nag — The AI That Won't Let You Lie
> "ให้ AI ไล่ถามว่าทำยัง"

Personal commitment tracker with escalating confrontation. Three levels: firm reminder → confrontational → no mercy. Tracks streaks, skips, and the pattern of avoidance you're pretending doesn't exist.

**Try:** `"nag me about gym"` · `"accountability check"` · `"did I actually do it?"`

📄 [`skills/accountability-nag/SKILL.md`](skills/accountability-nag/SKILL.md)

---

### AI Slop Detection — Does Your UI Look AI-Generated?
> "UI คุณดู AI-generated อยู่มั้ย"

Checklist to identify AI-generated UI patterns. Scores 15 tells across color, layout, visuals, typography, and motion. If your score is 6+, the UI screams "AI made this."

**Try:** `"does this look AI?"` · `"slop check"` · `"design audit"`

📄 [`skills/ai-slop-detection/SKILL.md`](skills/ai-slop-detection/SKILL.md)

---

### Workflow Scout — AI Workflow Architect
> "ช่วยจัด workflow ให้หน่อย"

8-question interview → Workflow Map → AI setup plan → role-specific prompts. Builds your AI workflow from scratch based on your actual work.

**Try:** `"help me set up AI for my work"` · `"ช่วยจัด workflow ให้หน่อย"`

📄 [`skills/workflow-scout/SKILL.md`](skills/workflow-scout/SKILL.md)

---

### Link Triage — AI Reads So You Don't Have To
> "save ลิงก์ไว้ 200 อัน อ่านจริง 3 อัน"

Drop any URL into your AI — get a 3-5 line summary, category, and relevance score. Know what's worth reading without reading everything. Works with articles, tweets, YouTube, GitHub repos, PDFs.

**Try:** `"triage this link"` · `"summarize this URL"` · `"what's this about?"`

📄 [`skills/link-triage/SKILL.md`](skills/link-triage/SKILL.md)

---

### Steal Digest — Cherry-Pick Ideas From GitHub Trending
> "ไม่ได้ก๊อปโค้ด แต่ขโมยไอเดีย"

Daily scan of GitHub trending filtered for your stack. AI picks 3-5 repos with ideas worth stealing — patterns, architectures, and techniques you can adapt for your project. Set it as a cron and it runs every morning.

**Try:** `"steal digest"` · `"what's trending?"` · `"anything worth stealing?"`

📄 [`skills/steal-digest/SKILL.md`](skills/steal-digest/SKILL.md)

---

### X Collect — Scout the Landscape Before You Write
> "ก่อนเขียน ดูก่อนว่าใครเขียนอะไรไปแล้ว"

Research Twitter/X before creating content. Find what's performing, what angles are saturated, and where the content gaps are. Write something new, not something redundant.

**Try:** `"scout this topic"` · `"content gaps for AI tools"` · `"what are people saying about X?"`

📄 [`skills/x-collect/SKILL.md`](skills/x-collect/SKILL.md)

---

### AI Memory — Give Your AI a Past and a Present
> "AI ลืมทุกอย่าง? เพราะคุณไม่เคยสร้างทางให้มันจำ"

Two drop-in prompts that give your AI persistent memory. **Long-term:** FTS5 search over past sessions — find old discussions in milliseconds. **Short-term:** hot cache file so AI knows current project state at session start. No cloud, no API keys.

**Try:** `"set up AI memory"` · `"search past sessions"` · `"AI doesn't remember anything"`

📄 [`skills/ai-memory/SKILL.md`](skills/ai-memory/SKILL.md)

---

### Axelrod Review — Game Theory for AI Review Loops
> "ผมเอา game theory มาใส่ใน AI review — แล้วมันเริ่มทำงานต่างออกไป"

Tit-for-tat cooperation tracking for AI reviews. Your reviewer remembers what it flagged last round, adjusts depth based on your track record, and catches recurring issues by name. Based on the strategy that won Robert Axelrod's 1984 programming tournament.

**3 review depths:** Light (high trust) · Standard · Deep Audit (low trust)
**Auto-correction loop:** 3 iterations, model rotation, self-fixing drafts

**Try:** `"axelrod review"` · `"trust score"` · `"why does it keep flagging the same thing?"`

📄 [`skills/axelrod-review/SKILL.md`](skills/axelrod-review/SKILL.md)

---

## Multi-Platform Support

Each skill works on all major AI coding tools. Clone once, use anywhere.

| Tool | How it works |
|------|-------------|
| **Claude Code** | `curl \| bash` install or clone repo — reads `CLAUDE.md` |
| **Codex CLI** | Clone repo — reads `AGENTS.md` |
| **Cursor** | Clone repo — reads `.cursor/rules/` |
| **Any AI chat** | Copy prompt from `SKILL.md`, paste into chat |

---

## Skill Commands

Available inside any skill session:
- `SKIP` — jump to next section
- `EXPAND [topic]` — go deeper
- `DONE` — summarize with current data
- `REDO` — start over

---

*Skills should be free. Inspired by [dot-skill](https://github.com/titanwings/colleague-skill).*
