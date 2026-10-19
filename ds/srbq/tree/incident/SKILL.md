---
name: incident
description: "Use when the request concerns the incident category of skills: covers incident"
---

Grouping node for the 0 skills of the incident category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **incident-lifecycle-manager** (`incident-lifecycle-manager/`): Use when --- description, Full incident lifecycle, Slack alert → war-room channel → runbook retrieval from Cognee KG → customer notice draft: covers incident, lifecycle, manager, 인시던트 관리, 인시던트 라이프사이클
- **incident-to-improvement** (`incident-to-improvement/`): Use when Close the loop from production incident to lasting prevention. Orchestrates 7 existing skills in a pipeline, incident triage, root: covers incident, improvement, blameless, closed, lasting

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
