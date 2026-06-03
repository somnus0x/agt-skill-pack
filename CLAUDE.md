# AGT Skill Pack

You have access to the following skills in the `skills/` directory. Load the relevant skill when the conversation matches.

| Trigger | Skill | File |
|---------|-------|------|
| "review", "cross review", "red team", "stress test", "second opinion", "fact check" | Factory Review | `skills/factory-review/SKILL.md` |
| "workflow", "set up AI", "จัด workflow" | Workflow Scout | `skills/workflow-scout/SKILL.md` |
| "should we build", "is this worth building", "taste check", "what would you cut", "prioritize these", "product review" | Product Taste | `skills/product-taste/SKILL.md` |
| "is this still right", "revisit", "should we reconsider", "has anything changed", "decision review", "decay check" | Decision Decay | `skills/decision-decay/SKILL.md` |
| "nag me", "accountability", "commitment check", "did I do it", "habit tracker" | Accountability Nag | `skills/accountability-nag/SKILL.md` |
| "does this look AI", "slop check", "UI review", "design audit", "AI tells" | AI Slop Detection | `skills/ai-slop-detection/SKILL.md` |
| "setup frontend", "configure for react", "frontend onboarding", "next.js setup" | Frontend Setup | `skills/frontend-setup/SKILL.md` |
| "agents colliding", "agents overwriting", "multi-agent", "parallel agents", "split my repo", "manage agents like a team", "I'm the bottleneck" | Agent Boundaries | `skills/agent-boundaries/SKILL.md` |

When a skill is triggered, read the SKILL.md file and follow its instructions.
