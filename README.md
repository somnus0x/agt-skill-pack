# AGT Skill Pack

Free AI skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand).

[![Facebook](https://img.shields.io/badge/Facebook-Agent%20Dev%20Thailand-1877F2?style=flat&logo=facebook)](https://facebook.com/agentdevthailand)
![Skills](https://img.shields.io/badge/Skills-8-blue)
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

### Session Search — Find What You Already Discussed
> "AI ลืมทุกอย่างที่เคยคุยกัน — เพราะไม่เคยสร้าง search ให้มัน"

Local FTS5 full-text search over all your Claude Code sessions. Drop-in prompt builds the tool for you — one command, then search 800+ sessions in milliseconds. No cloud, no API keys, no vector DB.

**Try:** `"search sessions for auth refactor"` · `"find past conversation about X"` · `"session search"`

📄 [`skills/session-search/SKILL.md`](skills/session-search/SKILL.md)

---

### Hot Cache — AI Knows Today Before You Tell It
> "ทำไม AI ถึงไม่รู้เลยว่าเมื่อวาน ship อะไร"

One markdown file that summarizes your current project state. AI reads it at session start — knows what shipped, what's blocked, and when the deadline is. No more pasting context every morning.

**Try:** `"set up hot cache"` · `"AI doesn't know my context"` · `"pre-load session context"`

📄 [`skills/hot-cache/SKILL.md`](skills/hot-cache/SKILL.md)

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
