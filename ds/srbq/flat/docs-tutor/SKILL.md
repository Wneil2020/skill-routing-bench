---
name: docs-tutor
description: "Use when Interactive quiz tutor for the project's StudyVault. Tracks concept-level proficiency with badges, drills weak areas, and updates a learning: covers docs, tutor, badges, drills, proficiency"
metadata:
  holon-triggers: |
    quiz me
    test my knowledge
---

---
name: docs-tutor
description: >-
  Interactive quiz tutor for the project's StudyVault. Tracks concept-level
  proficiency with badges, drills weak areas, and updates a learning dashboard.
  Use when the user wants to "quiz me", "test my knowledge", "study the docs",
  "docs-tutor", "학습", "퀴즈", "평가", or review specific platform topics. Do NOT use
  for generating the StudyVault (use docs-tutor-setup) or for general
  documentation reading.
metadata:
  version: "1.0.0"
  category: "learning"
  author: "thaki"
---
# Docs Tutor — Interactive Quiz for Platform Knowledge

Quiz-based tutor that tracks what the user knows and doesn't know at the **concept level**. The goal is helping users discover blind spots in their platform knowledge through targeted questions.

## Allowed Tools

Read, Write, Glob, Grep, AskQuestion

## File Structure

```
StudyVault/
├── 00-Dashboard/
│   ├── *study-map*         ← MOC with section map and learning path
│   └── *dashboard*         ← Compact overview: proficiency table + stats
├── 01-<Section>/
│   ├── concept notes...
│   └── practice questions...
├── ...
└── concepts/
    ├── {section-name}.md   ← Per-section concept tracking (attempts, status, error notes)
    └── ...
```

- **Dashboard**: Only aggregated numbers. Links to concept files. Stays small forever.
- **Concept files**: One per section. Tracks each concept with attempts, correct count, date, status, and error notes. Grows proportionally to unique concepts tested (bounded).

---

## Workflow

### Phase 0: Detect Language

Detect user's language from their message → `{LANG}`. All output and file content in `{LANG}`.

### Phase 1: Discover Vault

1. Glob `**/StudyVault/` in project root.
2. List section directories (numbered folders).
3. Glob `**/StudyVault/00-Dashboard/*dashboard*` to find dashboard.
4. If found, read it. Preserve existing file path regardless of language.
5. If not found, create from template (see Dashboard Template below).

If no StudyVault exists, infor
