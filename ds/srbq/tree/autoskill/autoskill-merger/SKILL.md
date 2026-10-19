---
name: autoskill-merger
description: "Use when Merge a skill candidate into an existing skill with semantic union of constraints, triggers, and tags. Use when autoskill-judge returns a: covers autoskill, merger, tags, union, candidate"
metadata:
  holon-triggers: |
    merge skill candidate
    update skill with new constraints
---

---
name: autoskill-merger
description: >-
  Merge a skill candidate into an existing skill with semantic union of
  constraints, triggers, and tags. Use when autoskill-judge returns a merge
  decision, when the user asks to "merge skill candidate", "update skill with
  new constraints", "스킬 병합", "autoskill merge", or when invoked by
  autoskill-evolve. Do NOT use for creating new skills (use create-skill),
  skill quality auditing (use skill-optimizer), or manual skill editing.
metadata:
  author: thaki
  version: "0.1.0"
  category: self-improvement
---

# AutoSkill Merger

Merge a skill candidate into an existing skill, producing an improved version with a patch version bump. Performs semantic union of constraints, triggers, and tags while preserving the existing skill's identity. Adapts AutoSkill's P_merge methodology for the Cursor SKILL.md format.

## Instructions

### Input

- The existing SKILL.md file path (from `autoskill-judge` decision's `target_skill_id`)
- The skill candidate JSON (from `autoskill-extractor`)

### Merge Process

1. **Read Existing Skill**: Parse the target SKILL.md file including frontmatter metadata and body content.

2. **Apply Merge Principles**:

   - **Shared Intent**: Preserve the existing skill's core capability identity
   - **Diff-Aware**: Import only unique, non-conflicting constraints from the candidate
   - **Semantic Union**: Combine constraints by meaning, not raw concatenation
   - **Recency Guard**: When conflicts arise, prefer the candidate's recent-topic intent
   - **Anti-Duplication**: Never duplicate section headers, bullets, or blocks

3. **Field-Level Merge Rules**:

   | Field | Merge Strategy |
   |-------|---------------|
   | `name` | Keep existing unless candidate is clearly more specific |
   | `description` | Keep existing structure, add new scope if candidate expands usage |
   | `prompt` / body | Semantic union of Goal, Constraints, Workflow sections |
   | `triggers` | Union + deduplicate, max 8 |
   | 
