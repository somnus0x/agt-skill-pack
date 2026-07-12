---
name: character-lock
description: |
  Keep an AI character's face and voice identical across every clip. Lock the
  identity ONCE (train a face, lock a voice), then reuse it — never re-generate
  the face. Use when a recurring AI character drifts between clips, looks like a
  different person each render, or the brand face is never consistent.
---

# Character Lock — Train the Identity Once, Reuse It Forever

You're making short clips with the same AI character — a mascot, a spokesperson, a recurring face for the brand. Every render, the face shifts: different hairstyle, different age, sometimes a different person entirely. Ten clips look like ten actors. Viewers can't recognize the brand because the face is never the same twice.

The problem isn't that the AI makes ugly faces. It's that it makes a *beautiful* face **every time — a different one.** Each generation starts from zero. It has no memory of who it drew yesterday.

The fix is not "prompt harder" or "gen until it matches." The fix is to **stop generating a new face at all.**

## The core idea

Split the work the same way any production line does: build the identity once, then reuse it.

- **Do once (the identity):** train the character's face, lock the voice. This is the expensive, careful step — get it right, then never touch it again.
- **Do every time (the scene):** put the locked identity into a new scene, new script, new motion. The face and voice come from the lock, not from a fresh roll.

Once the identity is fixed, every clip after the first is a **remix, not a re-creation.** You stop gambling on whether the face comes out right, because it's not being rolled — it's being recalled.

## When to use

Say `/character-lock` or: "my AI character's face keeps changing", "the spokesperson looks different every clip", "how do I keep a consistent AI face", "recurring character drifts between videos", "same voice across all clips".

## The tool that does this today: Higgsfield Soul

The current tool for this is **Higgsfield**, via a feature called **Soul**. Soul trains one character identity ahead of time: you upload a set of stills of the same person (many angles, many lighting conditions), and it learns that face into a reusable Soul. Every clip after that doesn't generate a new face — it pulls the same Soul into a new scene. The face can't drift because it's never re-rolled.

Voice locks the same way: upload a voice sample once, get one voice used across every clip (Thai included). Lock the face and the voice together and the character is genuinely the *same person* every time — not someone who happens to look similar.

This principle outlives any one tool. The tool will change; "lock the identity once, reuse it" won't.

## Steps to apply

1. **Prep the identity set** — gather stills of ONE character: many angles, many lighting setups, varied expressions, but unmistakably the same person. The cleaner and more consistent this set, the more stable the locked identity.
2. **Train the face once** — build the Soul (or your tool's equivalent). One reusable identity, stored, callable forever.
3. **Lock the voice separately** — upload a voice sample. One voice for every clip.
4. **Produce by recall, not by roll** — for each new clip, select the same locked face + same locked voice, then write only the scene and the script. The identity is composited in; you never re-generate it.

## The mistake to avoid

Most people pour their time into making each individual clip beautiful — when the thing that must be done once, well, is the **identity**, not the clip. Pros don't waste time re-generating the character every round. They lock it at step one, and everything after is *copy*, not *create*.

## The one line to remember

Brand consistency doesn't come from generating better. It comes from **not generating again.** Lock the face once, lock the voice once, reuse for everything else.
