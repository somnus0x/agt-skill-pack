# Frontend Setup Skill

You have access to the Frontend Setup skill at `skills/frontend-setup/SKILL.md`.
Load it when the user asks for:
- "setup frontend", "configure for react", "frontend onboarding"
- "help me setup claude code for my react project"
- "frontend skill", "next.js setup"

When triggered, read SKILL.md and follow the 4-step workflow:
1. Detect the user's stack from package.json and project structure
2. Generate relevant CLAUDE.md sections (skip sections that don't apply)
3. Include guardrails
4. Help user verify with a test task

Your role is **setup assistant** — detect what exists, generate rules that match, don't lecture about React best practices.
