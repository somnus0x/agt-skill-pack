# Session Search — Find What You Already Discussed

AI doesn't remember past sessions. But it doesn't have to — if you give it a search index.

## Why

Claude Code stores every session as a JSONL file in `~/.claude/projects/`. After a few weeks, you'll have hundreds of sessions containing decisions, bug fixes, prompt iterations, and architecture discussions. But there's no search. No index. Finding that auth discussion from two weeks ago means opening files one by one.

Session Search fixes this: a local SQLite FTS5 full-text search index over all your past sessions. Search by keyword, get results in milliseconds.

## Setup

### Option A: Drop-in prompt (recommended)

Copy this prompt into Claude Code and let it build the tool for you:

```
อ่านไฟล์ JSONL ทุกไฟล์ใน ~/.claude/projects/ ดึงแค่ข้อความ user + assistant ออกมา สร้าง SQLite database ที่มี FTS5 full-text search index ให้ search ด้วย keyword ได้ทันที เขียนเป็น Python script ชื่อ session-store.py ที่รับ command search, ingest, stats
```

Or in English:

```
Read all JSONL files in ~/.claude/projects/ and extract only user + assistant messages. Create a SQLite database with FTS5 full-text search index that can search by keyword instantly. Write it as a Python script called session-store.py that accepts commands: search, ingest, stats
```

One prompt. AI writes the script, runs ingest, and you're ready to search.

### Option B: Manual setup

If you prefer to write it yourself, the key components are:

1. **Parser** — Read JSONL session files, extract `type: "human"` and `type: "assistant"` messages
2. **SQLite + FTS5** — Create a virtual table with `tokenize='unicode61'` for multilingual support
3. **CLI interface** — `search "keyword"`, `ingest` (rebuild index), `stats` (show counts)

The JSONL structure varies by session type. Each line is a JSON object with a `type` field. Look for `type: "human"` (user messages) and `type: "assistant"` (AI responses).

## Usage

```bash
# Search for a keyword across all sessions
python3 session-store.py search "refactor authentication"

# Output:
# [2026-05-10] interactive:a3f2...  (42,318 chars)
#   ...ต้อง refactor authentication flow เพราะ Privy session...
#
# [2026-04-28] interactive:7bc1...  (18,204 chars)
#   ...เปลี่ยน authentication middleware จาก custom เป็น...

# Re-index after new sessions
python3 session-store.py ingest

# Show index stats
python3 session-store.py stats
```

## Add to your CLAUDE.md

```markdown
### Session search
If you need to find information from a past session, use:
python3 session-store.py search "keyword"
This searches across all indexed Claude Code sessions via FTS5.
Run `python3 session-store.py ingest` periodically to index new sessions.
```

## When to use

- "What did we decide about X?" — search for the decision
- "I wrote a good prompt for Y, where is it?" — search for the prompt
- "When did we fix that auth bug?" — search for the fix
- Finding past architecture discussions before making new decisions
- Recovering context that was lost when a session ended

## Technical notes

- **No cloud, no API keys.** Everything runs locally. SQLite FTS5 is built into Python's `sqlite3` module.
- **No embeddings, no vector DB.** Full-text search is simpler, faster, and doesn't need GPU or API calls for this use case.
- **Multilingual.** FTS5 with `unicode61` tokenizer handles Thai, English, and mixed text.
- **Fast.** Searching 800+ sessions (3M+ characters) returns results in milliseconds.
- **Incremental.** Run `ingest` to add new sessions without rebuilding the entire index.
