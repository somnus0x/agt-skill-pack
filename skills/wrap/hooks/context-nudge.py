#!/usr/bin/env python3
"""Nudge toward /clear or /compact when context gets expensive.

Two modes, same thresholds:
  (default) UserPromptSubmit hook: one-line systemMessage when
    - the cache has gone cold (idle > TTL) on a big context -> this turn re-writes the whole cache, or
    - context crosses another CTX_STEP tokens (once per step per session).
  --hud  statusline: prints one extra HUD line (via ~/.claude/hooks/statusline.sh, refreshed while idle).
Evidence: a transcript-based spend audit of 12 sessions, Sep-Oct 2026.
"""
import json, os, sys
from datetime import datetime, timezone

COLD_MIN_CTX = 150_000  # below this a cold resume is cheap, stay quiet
CTX_STEP = 250_000      # hook nudges at 250K, 500K, 750K; HUD warns from 250K
CTX_RED = 500_000
# cache-write $/MTok (1.25x input); unknown models fall back to Opus 5
WRITE = {"fable": 12.5, "opus-5-5": 5.0, "opus-5": 6.25, "sonnet": 3.75, "haiku": 1.25}
STATE_DIR = "/tmp/claude-context-nudge"
YEL, RED, DIM, RST = "\033[33m", "\033[31m", "\033[2m", "\033[0m"


def write_price(model):
    for k in ("fable", "opus-5-5", "opus-5", "sonnet", "haiku"):
        if k in (model or ""):
            return WRITE[k]
    return WRITE["opus-5"]


def last_main_usage(path):
    """-> (ctx_tokens, model, last_ts, ttl_seconds) from the latest main-chain response."""
    # Transcripts reach 300MB+; only scan the tail.
    with open(path, "rb") as f:
        f.seek(0, 2)
        f.seek(max(0, f.tell() - 3_000_000))
        lines = f.read().decode("utf-8", "ignore").splitlines()
    found, ttl = None, None
    for line in reversed(lines):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("type") != "assistant" or d.get("isSidechain"):
            continue
        m = d.get("message") or {}
        u = m.get("usage") or {}
        if m.get("model") == "<synthetic>" or not u:
            continue
        if found is None:
            ctx = u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
            found = (ctx, m.get("model"), d.get("timestamp"))
        cc = u.get("cache_creation") or {}
        if cc.get("ephemeral_1h_input_tokens"):
            ttl = 3600
        elif cc.get("ephemeral_5m_input_tokens"):
            ttl = 300
        if found and ttl:
            break
    return found + (ttl or 3600,) if found else None


def idle_minutes(ts):
    return (datetime.now(timezone.utc) - datetime.fromisoformat(ts.replace("Z", "+00:00"))).total_seconds() / 60


def hook(inp):
    path, sid = inp.get("transcript_path"), inp.get("session_id", "x")
    if not path or not os.path.exists(path):
        return
    got = last_main_usage(path)
    if not got:
        return
    ctx, model, ts, ttl = got
    msgs = []

    if ts and ctx >= COLD_MIN_CTX:
        idle = idle_minutes(ts)
        if idle > ttl / 60:
            cost = ctx / 1e6 * write_price(model)
            msgs.append(f"cold cache: idle {idle/60:.1f}h at {ctx//1000}K ctx -> this turn rewrites ~${cost:.0f} of cache. "
                        f"Next time: /wrap then /clear.")

    os.makedirs(STATE_DIR, exist_ok=True)
    state = os.path.join(STATE_DIR, sid)
    step = ctx // CTX_STEP
    try:
        seen = int(open(state).read())
    except (OSError, ValueError):
        seen = 0
    if step > seen:
        open(state, "w").write(str(step))
        msgs.append(f"context at {ctx//1000}K: every call re-reads it. At a project/post boundary, "
                    f"/wrap then /clear (or /compact if mid-task).")

    if msgs:
        print(json.dumps({"systemMessage": "⚠ " + " | ".join(msgs)}))


def hud(inp):
    path = inp.get("transcript_path")
    if not path or not os.path.exists(path):
        return
    got = last_main_usage(path)
    if not got:
        return
    ctx, model, ts, ttl = got
    window = int(os.environ.get("CLAUDE_CODE_AUTO_COMPACT_WINDOW") or (inp.get("context_window") or {}).get("context_window_size") or 1_000_000)

    if ts and ctx >= COLD_MIN_CTX and idle_minutes(ts) > ttl / 60:
        cost = ctx / 1e6 * write_price(model)
        print(f"{RED}⚠ cache cold at {ctx//1000}K → next prompt rewrites ~${cost:.0f}. /wrap, then /clear{RST}")
    elif ctx >= CTX_STEP:
        color = RED if ctx >= CTX_RED else YEL
        left = max(0, window - ctx) // 1000
        print(f"{color}⚠ {ctx//1000}K ctx{RST}{DIM} · auto-compact in ~{left}K · at a boundary: /wrap → /clear · mid-task: /compact{RST}")


if __name__ == "__main__":
    mode = hud if "--hud" in sys.argv else hook
    try:
        mode(json.load(sys.stdin))
    except Exception as e:  # never break the prompt or the HUD; surface the error instead
        if mode is hud:
            print(f"context-nudge error: {e}")
        else:
            print(json.dumps({"systemMessage": f"context-nudge hook error: {e}"}))
