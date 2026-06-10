---
name: link-triage
description: |
  Turn dropped URLs into summarized, categorized entries in a persistent reading queue
  with priority scoring. Use whenever links should be captured, summarized, classified,
  and queued instead of rotting in bookmarks.
---

# Link Triage — AI Reads So You Don't Have To

You save 30 links a day. You read maybe 2. The rest rot in bookmarks until you forget they exist.

Link Triage turns any URL into a 3-5 line summary with key takeaways, category, and relevance score — so you know what's worth your time without reading the full thing.

## Setup

### Drop-in prompt (copy into your AI tool):

```
เมื่อผมส่ง URL มา ให้:
1. อ่านเนื้อหาทั้งหมด
2. สรุปเป็น 3-5 bullet points เน้น key takeaway
3. จัดหมวดหมู่ (tech, business, personal, research)
4. ให้คะแนน relevance 1-5 ว่าเกี่ยวกับงานที่ทำอยู่แค่ไหน
5. ถ้า relevance 4-5 บอกว่าเกี่ยวยังไงและควรอ่านเต็มไหม
```

English version:

```
When I send a URL:
1. Read the full content
2. Summarize in 3-5 bullet points focusing on key takeaways
3. Categorize (tech, business, personal, research)
4. Score relevance 1-5 for how related it is to my current work
5. If relevance 4-5, explain why and whether I should read the full article
```

## What it handles

Works with any content type your AI can access:

- **Articles & blogs** — extract and summarize
- **Tweets & threads** — pull full thread, summarize the argument
- **YouTube videos** — transcript extraction → summary
- **GitHub repos** — README + structure → what it does, why it matters
- **PDFs & research papers** — extract key findings
- **Newsletters** — pull the 2-3 items that matter

## Add to your CLAUDE.md

```markdown
### Link triage
When I send a URL, automatically read the content, summarize in 3-5 bullets,
categorize, and score relevance 1-5 to my current work.
If relevance is 4+, explain why I should care.
```

## Building a reading queue (optional)

If you want to track what you've read and what's pending:

```
เก็บ log ของทุกลิงก์ที่ส่งมาใน reading-queue.md
แต่ละ entry มี: title, URL, summary, category, relevance score, status (unread/read/archived)
เรียงตาม relevance สูงสุดก่อน
```

This gives you a persistent, searchable reading queue that you can review weekly.

## When to use

- Someone sends you a link in chat — triage it before deciding to read
- You're catching up on newsletters — batch triage 10 links in 2 minutes
- You found an interesting thread at midnight — save and triage, read tomorrow
- Weekly reading review — scan your queue, archive what's stale

## Technical notes

- **Works with any AI tool.** Claude Code, Cursor, ChatGPT, Gemini — any tool that can fetch URLs.
- **Accuracy depends on access.** Some sites block AI extraction (paywalled content, JS-heavy pages). The AI will tell you when it can't access something.
- **Relevance scoring improves over time.** The more context your AI has about your work (via CLAUDE.md or hot cache), the better it scores relevance.
