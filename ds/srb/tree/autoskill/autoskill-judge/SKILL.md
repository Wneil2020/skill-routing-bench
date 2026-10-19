---
name: autoskill-judge
description: "Use when Evaluate skill candidates produced by autoskill-extractor and decide whether each should be added, merged into an existing skill, or: covers autoskill, judge, discarded, produced, added"
metadata:
  holon-triggers: |
    judge skill candidate
    evaluate extracted skill
---

---
name: autoskill-judge
description: >-
  Evaluate skill candidates produced by autoskill-extractor and decide whether
  each should be added, merged into an existing skill, or discarded. Use when
  processing extracted candidates, when invoked by autoskill-evolve, or when
  the user asks to "judge skill candidate", "evaluate extracted skill",
  "스킬 후보 평가", "autoskill judge". Do NOT use for skill quality auditing
  (use skill-optimizer), creating skills from scratch (use create-skill), or
  general code review.
metadata:
  author: thaki
  version: "0.1.0"
  category: self-improvement
---

# AutoSkill Judge

Evaluate skill candidates produced by autoskill-extractor and decide whether each should be added as a new skill, merged into an existing skill, or discarded. Adapts AutoSkill's P_judge and P_decide methodology for the Cursor ecosystem.

## Instructions

### Input

- A skill candidate JSON from `outputs/autoskill-candidates/` (produced by `autoskill-extractor`)
- Access to the existing skills directory at `.cursor/skills/`

### Decision Process

1. **Retrieve Similar Skills**: Use `scripts/memory/search.py` with hybrid search (BM25 + semantic) to find the top-3 most similar existing skills based on the candidate's name, description, and triggers.

2. **Capability Identity Test**: For each similar skill, evaluate on four axes:
   - **Job-to-be-done**: Do both solve the same core problem?
   - **Deliverable type**: Do both produce the same kind of output?
   - **Hard constraints/success criteria**: Do both enforce similar quality rules?
   - **Required tools/workflow**: Do both use similar tool chains?

3. **Apply Decision Logic**:

   **DISCARD** when:
   - Candidate captures a generic, non-portable task
   - Candidate has confidence < 0.6
   - Candidate duplicates an existing skill with no new constraints
   - Candidate contradicts established project conventions without user confirmation
   - Candidate is too narrow (applies to only one specific file/module)


