# Axelrod Review Skill

## Instructions
You have access to the Axelrod Review skill at `skills/axelrod-review/SKILL.md`.

## Triggers
Activate this skill when the user mentions: axelrod, tit-for-tat, game theory review, trust score, cooperation score, review loop, auto-correction loop, recurring issues in reviews, review depth adjustment.

## Workflow
1. Read `skills/axelrod-review/SKILL.md`
2. Help the user create `review-trust.json` in their project
3. Determine their review type (content or code) and help define the checklist
4. Provide the drop-in prompt with trust-aware review dynamics
5. Optionally configure the 3-iteration auto-correction loop with model rotation

## Role
You help the user add game theory (tit-for-tat) dynamics to their AI review workflow. The reviewer gets memory of past rounds, adjusts depth based on cooperation score, and catches recurring issues. Based on Robert Axelrod's Evolution of Cooperation — the same strategy that won his 1984 programming tournament.
