---
name: demo-forge
description: "Use when Auto-generate interactive product demos from recent code changes. Reads git diff, classifies user-facing features, captures browser: covers demo, forge, animations, captures, showcase"
metadata:
  holon-triggers: |
    create demo
    demo forge
---

---
name: demo-forge
description: >-
  Auto-generate interactive product demos from recent code changes. Reads git
  diff, classifies user-facing features, captures browser screenshots of
  before/after states, and produces a shareable HTML demo page with animations
  and annotations — or a video script with timestamps and talking points. Use
  when the user asks to "create demo", "demo forge", "generate demo", "product
  demo", "showcase changes", "데모 생성", "변경사항 데모", "stakeholder demo", "show what
  changed", or wants to present code changes to non-technical stakeholders. Do
  NOT use for static architecture diagrams (use visual-explainer), text-only
  release notes (use pr-review-captain), or video transcription (use
  transcribee).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Demo Forge — Auto-Generate Product Demos from Code Changes

Bridge the gap between "developer changelog" and "stakeholder demo". Turns git diffs into visual, interactive demo pages that non-technical stakeholders can understand.

## Usage

```
/demo-forge                                # demo from uncommitted changes
/demo-forge HEAD~3..HEAD                   # demo from last 3 commits
/demo-forge --branch feature/auth          # demo from branch diff vs main
/demo-forge --mode html                    # interactive HTML page (default)
/demo-forge --mode script                  # video recording script
/demo-forge --mode slides                  # presentation-ready slides HTML
/demo-forge --url http://localhost:3000    # base URL for screenshots
```

## Workflow

### Step 1: Collect Changes

Gather the diff based on user input:

```bash
# Uncommitted changes
git diff HEAD --name-only --stat

# Commit range
git log --oneline $RANGE
git diff $RANGE --name-only --stat

# Branch comparison
git diff main...$BRANCH --name-only --stat
git log main...$BRANCH --oneline
```

Parse commit messages for context (feature descriptions, issue references).

### Step 2: Classify
