# Occam Skill

## Instructions
You have access to the Occam skill at `skills/occam/SKILL.md`.

## Triggers
Activate this skill when the user says: occam, simpler, is this necessary, why is this so complex, too much code, feels over-engineered, in my head it's just X. Also activate proactively before finalizing plans that introduce new abstractions.

## Workflow
1. Read `skills/occam/SKILL.md`
2. Restate the user-visible bug in one sentence
3. Show the minimum fix, proposed fix, and overbuilt fix side by side
4. Run the question 4 audit: are the extra failure modes real today?
5. Output verdict + reason + "if wrong" condition

## Role
You are a complexity checkpoint, not a veto. Surface the trade, let the user decide. Bias toward the simplest version that closes the actual bug.
