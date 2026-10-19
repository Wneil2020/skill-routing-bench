---
name: planning
description: "Use when the request concerns the planning category of skills: covers planning"
---

Grouping node for the 0 skills of the planning category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **planning-meeting-sentinel** (`planning-meeting-sentinel/`): Use when --- description, Cursor Automation that polls Notion meeting DB every 30 min, auto-runs meeting-digest on new entries, extracts decisions: covers planning, meeting, sentinel, 회의 감시, 자동 다이제스트
- **planning-weekly-pulse** (`planning-weekly-pulse/`): Use when --- description, Weekly Cursor Automation that queries Notion project DBs, diffs against last snapshot, generates "what changed this week": covers planning, weekly, pulse, 주간 현황, 위클리 펄스

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
