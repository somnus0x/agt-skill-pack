---
name: x-collect
description: |
  Scout X/Twitter for what's already been said on a topic before writing: what performed,
  what's saturated, what angle is missing. Use for pre-writing research and content gap
  analysis.
---

# X Collect — Scout the Landscape Before You Write

Before writing about any topic, find out what's already been said. What performed? What angle is missing? Where's the gap you can fill?

X Collect scouts Twitter/X for existing content on your topic and gives you a landscape report — so you write something new, not something redundant.

## Setup

### Drop-in prompt (copy into your AI tool):

```
ก่อนเขียนเรื่อง [หัวข้อ] ช่วยหาดูว่าบน Twitter/X มีใครเขียนเรื่องนี้บ้าง
สรุปเป็น:
1. Top 5 posts/threads ที่ได้ engagement สูงสุดเรื่องนี้ (บอก engagement + angle)
2. Angle ที่คนพูดเยอะแล้ว (ควรหลีกเลี่ยงหรือหามุมใหม่)
3. Content gap — angle ที่ยังไม่มีคนพูดถึงแต่น่าสนใจ
4. Hook patterns ที่ perform ดี (คำเปิดแบบไหนที่คนคลิก)
5. แนะนำ 2-3 angle ที่น่าเขียนพร้อมเหตุผล
```

English version:

```
Before writing about [topic], research what's already been said on Twitter/X:
1. Top 5 posts/threads with highest engagement on this topic (include metrics + angle)
2. Angles that are already saturated (avoid or find a new spin)
3. Content gaps — angles nobody's covered yet but would be interesting
4. Hook patterns that perform well (what opening styles get clicks)
5. Recommend 2-3 angles worth writing, with reasoning
```

## How to use

Run X Collect **before** you start drafting. Not after.

```
1. Pick your topic: "AI coding tools" / "startup hiring" / "React performance"
2. Run the prompt with [หัวข้อ] replaced
3. Read the landscape report
4. Pick an angle from the content gaps
5. Now write — with a clear position in an uncrowded space
```

## What it gives you

A landscape report with 5 sections:

- **High performers** — what's already getting engagement, so you know the baseline
- **Saturated angles** — what everyone's already saying, so you don't repeat
- **Content gaps** — what nobody's covered yet, so you can own a position
- **Hook patterns** — what opening styles work for this topic
- **Recommended angles** — specific angles worth writing, with reasoning

## Add to your CLAUDE.md

```markdown
### Content scouting
Before writing any long-form content, run X Collect first:
search Twitter/X for existing content on the topic, identify top performers,
saturated angles, content gaps, and recommend 2-3 angles worth writing.
```

## When to use

- **Before writing a blog post** — find the angle nobody's covered
- **Before creating content for a page** — know what hooks work in this space
- **Before launching a thread** — see what framing gets engagement
- **When planning content calendars** — identify topics with gaps to fill
- **When a topic feels "overdone"** — X Collect shows you the specific sub-angle that isn't

## Tips

- **Specify your audience.** "AI coding tools for Thai developers" gives better results than just "AI coding tools"
- **Run for competitors too.** Search for content by specific creators to see what angles they're using
- **Save the landscape report.** Useful reference while drafting — keeps you from drifting into saturated territory
- **Re-run monthly.** Landscapes shift. What was a gap last month might be saturated now

## Technical notes

- **Accuracy depends on your AI's access to X/Twitter.** Some tools have better access than others. Results may be incomplete.
- **Engagement data is approximate.** AI may not have real-time metrics. Focus on patterns, not exact numbers.
- **Works for any platform.** The prompt says Twitter/X, but you can adapt it for Reddit, LinkedIn, YouTube, or any platform your AI can search.
