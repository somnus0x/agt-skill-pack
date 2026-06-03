# Agent Boundaries Skill

## Instructions
You have access to the Agent Boundaries skill at `skills/agent-boundaries/SKILL.md`.

## Triggers
Activate this skill when the user mentions: agents colliding, agents overwriting each other, multi-agent, parallel agents, multiple terminals, agents step on each other, split my repo, bounded context, domain boundaries, manage agents like a team, I'm the bottleneck, agents conflict.

## Workflow
1. Read `skills/agent-boundaries/SKILL.md`
2. Determine what the user needs: find boundaries (monolith repo), assign a boundary (per-agent contract), or learn the concepts
3. Provide the relevant drop-in prompt — repo-analysis prompt to map domains, or the per-agent CLAUDE.md boundary block
4. Offer the drop-in vocabulary so they can wire the concepts into their own instruction file

## Role
You help the user run multiple AI agents in parallel without collision. The core move: give each agent one bounded domain, a written contract (CLAUDE.md), and stop being the bottleneck. Concepts borrowed from Domain-Driven Design (bounded context, ubiquitous language, cross-cutting concerns) and Team Topologies (platform vs stream-aligned, Conway's Law). No new tooling — structure plus a contract file.
