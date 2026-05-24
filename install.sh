#!/bin/bash
# AGT Skill Pack — installer
# Usage: curl -sL https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/install.sh | bash
# Install specific skill: curl -sL .../install.sh | bash -s factory-review

set -e

BASE_URL="https://raw.githubusercontent.com/somnus0x/agt-skill-pack/main/skills"
SKILL_DIR=".claude/skills"

install_skill() {
  local skill="$1"
  local dir="$SKILL_DIR/$skill"
  mkdir -p "$dir"
  curl -sL "$BASE_URL/$skill/SKILL.md" > "$dir/SKILL.md"
  echo "  installed: $skill"
}

if [ -n "$1" ]; then
  # Install specific skill
  echo "Installing $1..."
  install_skill "$1"
else
  # Install all skills
  echo "Installing all AGT skills..."
  install_skill "workflow-scout"
  install_skill "factory-review"
  install_skill "product-taste"
  install_skill "decision-decay"
  install_skill "accountability-nag"
  install_skill "ai-slop-detection"
  install_skill "occam"
  install_skill "content-scout"
  install_skill "ai-memory"
  install_skill "link-triage"
  install_skill "steal-digest"
  install_skill "x-collect"
fi

echo ""
echo "Done. Skills installed at $SKILL_DIR/"
echo ""
echo "Try:"
echo "  workflow-scout       → \"help me set up my AI workflow\""
echo "  factory-review       → \"review this draft\" or \"red team this spec\""
echo "  product-taste        → \"should we build this?\" or \"taste check\""
echo "  decision-decay       → \"is this still the right call?\""
echo "  accountability-nag   → \"nag me about gym\""
echo "  ai-slop-detection    → \"does this UI look AI-generated?\""
echo "  occam                → \"is this necessary?\" or \"simpler\""
echo "  content-scout        → \"scout this topic\" or \"what's trending\""
echo "  ai-memory            → \"set up AI memory\" or \"search past sessions\""
echo "  link-triage          → \"triage this link\" or \"summarize this URL\""
echo "  steal-digest         → \"steal digest\" or \"what's trending on GitHub?\""
echo "  x-collect            → \"scout this topic on X\" or \"content gaps\""
