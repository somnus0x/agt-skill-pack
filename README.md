# AGT Skill Pack

Free AI skills from [Agent Dev Thailand](https://facebook.com/agentdevthailand).

[![Facebook](https://img.shields.io/badge/Facebook-Agent%20Dev%20Thailand-1877F2?style=flat&logo=facebook)](https://facebook.com/agentdevthailand)

> ฝรั่งแจกพร้อมท์ฟรีกัน ทำไมคนไทยต้องซื้อพร้อมท์

## Workflow Scout

Workflow Architect that helps you set up AI to match your actual work. Works with Claude, ChatGPT, Gemini, or any AI chat.

### Quick Start

**Claude Code:**
```bash
curl -sL https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/install.sh | bash
```
Then tell Claude: `ช่วยจัด workflow ให้หน่อย`

**Claude.ai / ChatGPT / Gemini:**
Copy the prompt from the "Copy-Paste Version" section in [`workflow-scout.md`](workflow-scout.md) and paste it as your first message.

### What it does

1. Asks 8 structured questions about your work
2. Outputs a Workflow Map with AI migration opportunities
3. Gives you a concrete AI setup plan (system prompts, context files, output formats)
4. Recommends role-specific prompts (max 5) mapped to your actual pain points
5. Provides search paths so you can keep finding good prompts yourself

### Commands

Type these anytime during the interview:
- `SKIP` — jump to next section
- `EXPAND [topic]` — go deeper
- `DONE` — summarize with whatever data is available
- `REDO` — start over

---

Inspired by [dot-skill](https://github.com/titanwings/colleague-skill) which distills a colleague's workflow. This does the opposite — builds *your own* from scratch.
