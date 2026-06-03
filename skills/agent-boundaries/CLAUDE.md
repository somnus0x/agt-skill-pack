# Agent Boundaries Skill

You have access to the Agent Boundaries skill at `skills/agent-boundaries/SKILL.md`. Load it when the user says:
- "agents colliding", "agents overwriting each other", "multi-agent", "parallel agents"
- "run multiple terminals", "3 terminals", "agents step on each other"
- "split my repo", "bounded context", "domain boundaries"
- "manage agents like a team", "I'm the bottleneck", "agents conflict"

When triggered, read SKILL.md. If the user needs to find boundaries in a monolith, provide the repo-analysis drop-in prompt. If they need to give an agent its boundary, provide the per-agent CLAUDE.md block. If they want the concepts, give the drop-in vocabulary list (bounded context, ubiquitous language, cross-cutting concern, Conway's Law, platform/stream).
