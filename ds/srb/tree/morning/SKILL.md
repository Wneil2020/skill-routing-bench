---
name: morning
description: "Use when the request concerns the morning category of skills: covers morning"
---

Grouping node for the 0 skills of the morning category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **morning** (`morning/`): Use when Morning routine orchestrator that runs google-daily (calendar briefing, Gmail triage, Drive upload, Slack notification) then: covers morning, notification, sequence, shipping, consolidated
- **morning-ship** (`morning-ship/`): Use when Start-of-day pipeline, git pull all 5 managed repos (ai-platform-webui via tmp branch), run Google Workspace briefing (calendar + Gmail triage): covers morning, ship, pulling, tmp, webui

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
