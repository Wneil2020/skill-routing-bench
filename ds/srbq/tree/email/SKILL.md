---
name: email
description: "Use when the request concerns the email category of skills: covers email"
---

Grouping node for the 0 skills of the email category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **email-auto-reply** (`email-auto-reply/`): Use when Knowledge-based email draft generation with human approval gate. Reads incoming emails, retrieves relevant context from Cognee knowledge graph: covers email, auto, reply, presents, retrieves
- **email-research-dispatcher** (`email-research-dispatcher/`): Use when Extract research-worthy topics from emails, run web research, and post structured findings to Slack. Bridges the gap between incoming: covers email, research, dispatcher, bridges, worthy

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
