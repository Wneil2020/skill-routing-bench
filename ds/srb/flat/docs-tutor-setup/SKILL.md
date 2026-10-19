---
name: docs-tutor-setup
description: "Use when Transform the project's docs/ markdown files into an Obsidian StudyVault with structured concept notes, practice questions, dashboards, and: covers docs, tutor, setup, 학습 노트, StudyVault 생성"
metadata:
  holon-triggers: |
    generate a study vault
    create study notes from docs
---

---
name: docs-tutor-setup
description: >-
  Transform the project's docs/ markdown files into an Obsidian StudyVault with
  structured concept notes, practice questions, dashboards, and interlinking.
  Use when the user asks to "generate a study vault", "create study notes from
  docs", "docs-tutor-setup", or wants to learn the platform documentation
  systematically. Do NOT use for interactive quizzing (use docs-tutor) or for
  general documentation writing (use technical-writer). Korean triggers: "학습 노트", "StudyVault 생성".
metadata:
  version: "1.0.0"
  category: "learning"
  author: "thaki"
---
# Docs Tutor Setup — Markdown Docs to Obsidian StudyVault

## Scope

Converts markdown files under `docs/` into a structured Obsidian StudyVault at the project root (`StudyVault/`). The vault contains concept notes, practice questions with active recall, a dashboard with MOC, and full interlinking.

## Allowed Tools

Read, Write, Glob, Grep, Shell (for directory listing only), AskQuestion

## Boundary Rules

1. **Source**: Only read from `docs/` and its subdirectories.
2. **Output**: Only write to `StudyVault/` at the project root.
3. **No modifications** to source `docs/` files.
4. **Skip**: `docs/tasks/`, `docs/ai/`, `.git/`, `node_modules/`, any `.tsv` files.

## Selective Scope

The user may specify a target subdirectory. If provided, only process that subdirectory:

```
/docs-tutor-setup                           # all of docs/
/docs-tutor-setup docs/platform-overview    # single section
/docs-tutor-setup docs/infrastructure docs/on-call  # multiple sections
```

If no argument, scan all of `docs/` and present the discovered sections for user confirmation before proceeding.

---

## Phase D1: Source Discovery

1. **Glob** `docs/**/*.md` to find all markdown files.
2. **Group by top-level subdirectory** under `docs/` — each becomes a "section."
   - Nested subdirectories (e.g., `docs/planned/agent-sandbox-platform/`) are treated as a single section with subtopics.
3. *
