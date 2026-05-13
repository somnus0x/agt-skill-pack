#!/bin/bash
# AGT Skill Pack — Workflow Scout installer
# Usage: curl -sL https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/install.sh | bash

set -e

SKILL_DIR=".claude/skills"
SKILL_URL="https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/workflow-scout.md"
SKILL_FILE="$SKILL_DIR/workflow-scout.md"

mkdir -p "$SKILL_DIR"
curl -sL "$SKILL_URL" > "$SKILL_FILE"

echo "✓ workflow-scout installed at $SKILL_FILE"
echo ""
echo "Tell Claude: \"ช่วยจัด workflow ให้หน่อย\""
