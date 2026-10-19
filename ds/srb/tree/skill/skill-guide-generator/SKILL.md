---
name: skill-guide-generator
description: "Use when Scan all installed skills, identify undocumented ones, generate guide documentation following the standard template, and update the README: covers guide, generator, ensure, following, readme"
metadata:
  holon-triggers: |
    document skills
    sync skill guides
---

---
name: skill-guide-generator
description: >-
  Scan all installed skills, identify undocumented ones, generate guide
  documentation following the standard template, and update the README index.
  Use when the user asks to "document skills", "sync skill guides",
  "skill-guide-sync", "find undocumented skills", "update skill docs",
  "스킬 문서화", "스킬 가이드 동기화", "문서화 안 된 스킬", or wants to ensure
  all skills have corresponding guide entries. Do NOT use for creating new
  skills from scratch (use create-skill), optimizing skill quality (use
  skill-optimizer), or writing general documentation (use technical-writer).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Skill Guide Generator

Automate the full skill documentation lifecycle: inventory installed skills, identify gaps, generate guide sections, and update the README index.

## Usage

```
/skill-guide-sync                    # full sync (scan + generate + update README)
/skill-guide-sync --dry-run          # gap analysis only, no file changes
/skill-guide-sync --scope tab-*      # only document skills matching prefix
/skill-guide-sync --readme-only      # only update README.md counts and tables
```

## Pipeline Overview

```
Phase 1: Inventory
  ├─ Glob .cursor/skills/*/SKILL.md → installed skills list
  └─ Grep docs/skill-guides/*.md → documented skills set

    ↓

Phase 2: Gap Analysis
  ├─ Cross-reference → undocumented skills list
  └─ Categorize → existing guide vs new guide file

    ↓

Phase 3: Generation (parallel, max 4 subagents)
  ├─ New guide files → create numbered .md files
  └─ Existing guides → append sections + update summary tables

    ↓

Phase 4: README Update
  ├─ Add/update rows in core skills table
  ├─ Update skill counts and header total
  └─ Update mermaid diagram and workflow commands

    ↓

Phase 5: Report
  └─ Summary of files created, updated, skills documented
```

## Workflow

### Phase 1 — Inventory

1. **Discover installed skills**:

```bash
find .curs
