#!/bin/bash
# claude-hud + one context-nudge line. Wired from settings.json statusLine (refreshInterval keeps it live while idle).
in=$(cat)
cols=${COLUMNS:-}; case "$cols" in ""|*[!0-9]*) cols=$(stty size 2>/dev/null </dev/tty | awk '{print $2}');; esac
case "$cols" in ""|*[!0-9]*) cols=120;; esac
export COLUMNS=$(( cols > 4 ? cols - 4 : 1 ))
plugin_dir=$(ls -d "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"/plugins/cache/*/claude-hud/*/ 2>/dev/null | awk -F/ '{ print $(NF-1) "\t" $(0) }' | grep -E '^[0-9]+\.[0-9]+\.[0-9]+[[:space:]]' | sort -t. -k1,1n -k2,2n -k3,3n -k4,4n | tail -1 | cut -f2-)
printf '%s' "$in" | "/opt/homebrew/bin/node" "${plugin_dir}dist/index.js"
printf '%s' "$in" | /usr/bin/python3 "$HOME/.claude/hooks/context-nudge.py" --hud
