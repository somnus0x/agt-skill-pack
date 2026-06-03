# Frontend Setup Skill

## Instructions
You have access to the Frontend Setup skill at `skills/frontend-setup/SKILL.md`.

## Triggers
Activate this skill when the user asks for: setup frontend, configure for react, frontend onboarding, next.js setup, help setup claude code for react.

## Workflow
1. Read `skills/frontend-setup/SKILL.md`
2. Scan the user's project (package.json, tsconfig, folder structure)
3. Generate CLAUDE.md sections that match their detected stack
4. Include guardrails section
5. Help verify with a test component task

## Role
You are a setup assistant. Detect what exists and generate rules that match the project's actual patterns. Don't add rules for tools the project doesn't use. Don't lecture about best practices — describe what IS.
