---
name: ct
description: "Commit and tag in one step, with the SemVer bump read off your own commit messages. Use when the user says 'ct', '/ct', 'commit and tag', 'commit tag', or wants to cut a release. Supports /ct (auto-detect), /ct patch|minor|major (force bump), /ct alpha|beta|rc (pre-release). Never pushes: it prints the push command."
---

# CT — Save Points For Code You Already Shipped

Production breaks at 4pm. The first question is not "what version is this", it's **"what's the last point I can get back to."** If you can't answer that, you're reading `git log` backwards with shaking hands, which is the worst possible time to be reading `git log`.

If you ship many times a day, a tag is not a release ceremony. It's a save point. Same idea as saving before you close the game: cheap to make, and the only thing that matters is that one exists near where you are.

`/ct` is one command: commit, name the save point by reading your own commits, cut an annotated tag carrying what's inside it, print the push command, stop.

The version number is just the naming scheme. It sorts, and it hints at what changed between two points. Nobody is auditing whether your MINOR was truly a MINOR.

## Why nobody makes save points

Skipping it never produces an error. Everything still works. The entire cost arrives at once, three weeks later, on the worst day. So it's the first thing dropped when you're moving fast, which is exactly when you're generating the most to roll back through.

AI makes that worse in a straightforward way: commits per day go up three or four times, and a ritual that was survivable at 8 commits a day is not survivable at 30.

## Why the bump is auto-detected, not asked

If the AI asks "patch, minor, or major?" you will answer patch every time, because patch is the answer that ends the conversation. Ask enough times and you stop making save points at all.

So `/ct` doesn't ask. It reads the commit subjects since the last tag and applies the rule:

- `BREAKING CHANGE:` in a footer, or `!` after the type (`feat!:`, `fix(api)!:`) → **MAJOR**
- `feat:` → **MINOR**
- `fix:` / `perf:` → **PATCH**
- only `docs:` / `chore:` / `ci:` / `style:` / `test:` / `refactor:` → **PATCH**

Highest level wins. `feat:` plus `fix:` is a MINOR.

**The 0.x rule:** while the major version is `0`, a breaking change bumps MINOR instead of MAJOR. In 0.x everything is allowed to break, and burning v1.0.0 on a rename you made in week two is a version number you can't get back.

The upshot: the discipline moves to where it belongs. Write honest commit messages and your version numbers are correct for free.

## Setup: pick your branch flow

Set this once, in your `CLAUDE.md` / `AGENTS.md`. Two shapes cover almost everyone.

**Single branch (most repos, and the default if you set nothing):**
```markdown
## Release flow
- Work and commit on: main
- Tag on: main
```

**Three branches (dev → staging → main):**
```markdown
## Release flow
- Work and commit on: development (or feature/*)
- Merge to and tag on: staging
- Never commit directly on staging or main
```

The rest of the skill reads whatever you wrote there. If you set nothing, it commits and tags in place on your current branch.

## The steps

### 0. Branch check
Read the release flow. If the current branch is one the flow marks as commit-forbidden (`staging`, `main`), **STOP** and say so:
`git stash && git checkout development && git stash pop`

### 1. Stage
`git add -A`, then explicitly unstage `.env*`, credential files, service account keys, and debug logs, and warn if any were found. Nothing staged means nothing to do: say so and stop.

### 2. Gather context (all in parallel)
```bash
git diff --staged --stat
git log --oneline -5
git tag --sort=-v:refname | head -1     # PREV_TAG
git log ${PREV_TAG}..HEAD --oneline     # commits since the last tag
```
No tags in the repo yet? `PREV_TAG` is empty and the first tag is `v0.1.0`.

### 3. Bump level
Forced by an argument if one was given. If the current tag is a pre-release and no argument was given, this is a **finalize**: strip the suffix (`v0.2.0-rc.1` → `v0.2.0`) and skip the bump. Otherwise auto-detect using the rules above.

### 4. Next version
Parse `PREV_TAG` as `vMAJOR.MINOR.PATCH[-prerelease.N]`.

Normal: `v0.1.19` → patch `v0.1.20` / minor `v0.2.0` / major `v1.0.0`

Pre-release:
- same type as current → increment: `v0.2.0-alpha.1` → `v0.2.0-alpha.2`
- different type → graduate, keep the base: `v0.2.0-alpha.2` → `v0.2.0-beta.1`
- current is a normal release → apply the bump first, then the suffix: `v0.1.19` + minor + alpha → `v0.2.0-alpha.1`

Then `git tag -l <NEW_TAG>`. If it exists, **STOP**. Never move an existing tag.

### 5. Commit message
Match the repo's existing style, read from the last five commits. Conventional commits if that's the pattern there. One subject line, optional short body.

### 6. Commit
```bash
git commit -m "$(cat <<'EOF'
<message>
EOF
)"
```

### 7. Merge to the tag branch
Only if your flow has one:
```bash
git checkout staging && git merge development
```

### 8. Annotated tag with real release notes
```bash
git tag -a <NEW_TAG> -m "$(cat <<'EOF'
Release <NEW_TAG>

Changes since <PREV_TAG>:
- <commit subject 1>
- <commit subject 2>
EOF
)"
```
Annotated, never lightweight. A lightweight tag is a bare name with no author, no date, and no message. On the bad day it hands you `v0.2.0 v0.2.1 v0.2.2` and tells you nothing about which one to go back to. The annotated tag carries its own contents, so the save point is readable without archaeology. Cap the list around 12 entries and add `... and N more commits`.

### 9. Back to the work branch
```bash
git checkout development
```

### 10. Output, and nothing more
```
Bump:  MINOR (feat: detected in 3 commits)
Tag:   v0.1.19 → v0.2.0
Push:  git push origin development && git push origin staging --tags
```

## It does not push, on purpose

The command is printed, not run. Commits and tags are local and cheap to undo; a pushed tag is public and people build against it. That is the line worth keeping a human on, and it costs you one paste.

## The rules it will not break

- Never commit on a branch your flow marks as protected
- Always annotated tags, never lightweight
- Never move or overwrite an existing tag: duplicate means stop
- Never `--no-verify`, hooks exist for a reason
- Never stage `.env*` or credentials, warn when it sees them
- Never push
- In 0.x, breaking changes bump MINOR
- Nothing to commit means stop, not an empty commit

## Try it

```
/ct                 # auto-detect the bump
/ct minor           # force minor
/ct rc              # cut a release candidate
/ct minor alpha     # force minor, alpha pre-release
/ct                 # on an rc, this finalizes it
```

## Pairs with

- **`hold-up`** for the moment before a big action, when you meant to talk, not ship.
- **`guard`-style reversibility thinking:** a local tag is easy to delete, a pushed tag is not. `/ct` stops exactly at that line.

---

*From [Agent Dev Thailand](https://facebook.com/agentdevthailand) — free skills for people who run AI agents for real.*
