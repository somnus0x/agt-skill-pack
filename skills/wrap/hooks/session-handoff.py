#!/usr/bin/env python3
"""Session handoff store for the /wrap skill. One canonical path per working directory.

  session-handoff.py --path [cwd]   print where /wrap should write the handoff for cwd
  session-handoff.py                SessionStart hook: on /clear (or a fresh startup within MAX_AGE_H),
                                    inject the cwd's handoff as context, then mark it consumed.
Lives outside repos (~/.claude/session-handoffs/) so it never gets committed.
"""
import json, os, sys, time

DIR = os.path.expanduser("~/.claude/session-handoffs")
MAX_AGE_H = 24  # a startup older than this is a new task, not a continuation


def path_for(cwd):
    slug = os.path.realpath(cwd).strip("/").replace("/", "-") or "root"
    return os.path.join(DIR, slug + ".md")


def main():
    if "--path" in sys.argv:
        args = [a for a in sys.argv[1:] if a != "--path"]
        os.makedirs(DIR, exist_ok=True)
        print(path_for(args[0] if args else os.getcwd()))
        return

    inp = json.load(sys.stdin)
    src = inp.get("source")
    p = path_for(inp.get("cwd") or os.getcwd())
    if src not in ("clear", "startup") or not os.path.exists(p):
        return
    age_h = (time.time() - os.path.getmtime(p)) / 3600
    if src == "startup" and age_h > MAX_AGE_H:
        return
    body = open(p).read()
    os.replace(p, p[:-3] + ".consumed.md")  # keep the last one for reference, never re-inject it
    print(json.dumps({
        "systemMessage": f"↻ loaded /wrap handoff ({age_h:.1f}h old) from {os.path.basename(p)}",
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "Handoff from the previous session in this directory (written by /wrap). "
                                 "Treat it as the starting brief; verify volatile facts against the repo before acting.\n\n" + body,
        },
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # never block session start; surface the error instead
        print(json.dumps({"systemMessage": f"session-handoff hook error: {e}"}))
