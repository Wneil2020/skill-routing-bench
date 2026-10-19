---
name: mission
description: "Use when the request concerns the mission category of skills: covers mission"
---

Grouping node for the 0 skills of the mission category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **mission-control** (`mission-control/`): Use when Orchestrate multi-skill autonomous workflows — decompose high-level goals into sub-tasks, delegate to specialist skills via subagents, aggregate: covers mission, control, 감사, 리뷰, alone
- **mission-control-copy** (`mission-control-copy/`): Use when Orchestrate multi-skill autonomous workflows — decompose high-level goals into sub-tasks, delegate to specialist skills via subagents: covers mission, control copy, 감사, 리뷰, delegate

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
