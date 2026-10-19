---
name: context-engineer
description: "Use when Manage project knowledge architecture — MEMORY.md lifecycle, domain glossary maintenance, context packages per analysis type, knowledge: covers context, engineer, during, done, explaining"
metadata:
  holon-triggers: |
    update context
    refresh MEMORY.md
---

---
name: context-engineer
description: >-
  Manage project knowledge architecture — MEMORY.md lifecycle, domain glossary
  maintenance, context packages per analysis type, knowledge graph updates, and
  AI agent context window optimization. Ensures AI agents always have full
  understanding of the stock analytics domain without re-explaining. Use when
  the user asks to "update context", "refresh MEMORY.md", "build context
  package", "optimize agent context", "context engineer", "컨텍스트 관리",
  "MEMORY 업데이트", "지식 아키텍처", or wants to improve how AI agents
  understand the project.
  Do NOT use for general MEMORY.md updates during task completion (follow
  done-checklist rule directly). Do NOT use for creating new skills (use
  anthropic-skill-creator or create-skill). Do NOT use for prompt optimization
  (use prompt-architect or prompt-transformer).
metadata:
  author: thaki
  version: 1.0.0
  category: generation
---

# Context Engineer

Manage the knowledge architecture that makes AI agents effective collaborators in this stock analytics project. Context engineering ensures every AI interaction starts with the right domain knowledge, project state, and historical context -- eliminating the need to re-explain.

## Knowledge Architecture

The project's context is organized in three tiers:

### Tier 1: Working Memory (always loaded)

| Source | Path | Content |
|--------|------|---------|
| MEMORY.md | `MEMORY.md` | Decisions, tasks, issues, session context |
| Rules | `.cursor/rules/*.mdc` | Persistent behavior rules |
| Skill descriptions | `.cursor/skills/*/SKILL.md` frontmatter | Skill registry (description field only) |

### Tier 2: Domain Knowledge (loaded on demand)

| Source | Path | Content |
|--------|------|---------|
| Skill bodies | `.cursor/skills/*/SKILL.md` | Full skill instructions |
| Skill references | `.cursor/skills/*/references/*.md` | Detailed reference docs |
| Task tracking | `tasks/todo.md` | Current and completed tasks |
| Lessons learned | `t
