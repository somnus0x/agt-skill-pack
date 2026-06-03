# AGT Skill Pack

## Available Skills

### Factory Review
- **Triggers:** review, cross review, red team, stress test, second opinion, fact check
- **File:** `skills/factory-review/SKILL.md`
- **Description:** Cross-model adversarial review. Use a different AI to critique what you produced.

### Workflow Scout
- **Triggers:** workflow, set up AI, จัด workflow
- **File:** `skills/workflow-scout/SKILL.md`
- **Description:** 8-question interview that builds your AI workflow from scratch.

### Product Taste
- **Triggers:** should we build, is this worth building, taste check, what would you cut, prioritize these, product review
- **File:** `skills/product-taste/SKILL.md`
- **Description:** 5-filter evaluation for product decisions. Runs features through who-suffers, replaces-what, core-loop, cost-of-being-right, and ship-without-it filters.

### Decision Decay
- **Triggers:** is this still right, revisit, should we reconsider, has anything changed, decision review, decay check
- **File:** `skills/decision-decay/SKILL.md`
- **Description:** Re-evaluate past decisions when assumptions change. Scores decay as Fresh, Aging, or Stale.

### Accountability Nag
- **Triggers:** nag me, accountability, commitment check, did I do it, habit tracker
- **File:** `skills/accountability-nag/SKILL.md`
- **Description:** Personal commitment tracker with escalating confrontation. Three levels from firm reminder to no mercy.

### AI Slop Detection
- **Triggers:** does this look AI, slop check, UI review, design audit, AI tells
- **File:** `skills/ai-slop-detection/SKILL.md`
- **Description:** Checklist to identify AI-generated UI patterns. Scores 15 tells across color, layout, visuals, typography, and motion.

### Frontend Setup
- **Triggers:** setup frontend, configure for react, frontend onboarding, next.js setup
- **File:** `skills/frontend-setup/SKILL.md`
- **Description:** One-time setup that detects your React/Next.js stack and generates CLAUDE.md rules matching your actual project conventions.

### Agent Boundaries
- **Triggers:** agents colliding, agents overwriting, multi-agent, parallel agents, split my repo, manage agents like a team, I'm the bottleneck
- **File:** `skills/agent-boundaries/SKILL.md`
- **Description:** Run multiple AI agents in parallel without collision. One agent owns one bounded domain, rules live in a contract file, you stop being the bottleneck. Concepts from DDD and Team Topologies.

## Instructions
When the user's message matches a trigger, read the corresponding SKILL.md and follow its workflow.
