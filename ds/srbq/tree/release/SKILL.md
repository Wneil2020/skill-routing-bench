---
name: release
description: "Use when the request concerns the release category of skills: covers release"
---

Grouping node for the 0 skills of the release category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **release-commander** (`release-commander/`): Use when Full release lifecycle orchestrator that chains 10 existing skills into a single pipeline, code review, security scan, test validation: covers release, commander, changelog, i18n, split
- **release-ship** (`release-ship/`): Use when Lightweight shipping pipeline, domain-split commits, git push, and PR creation/update in one flow. Use when the user asks to: covers release, ship, included, lightweight, trivial

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
