---
name: ai
description: "Use when the request concerns the ai category of skills: covers ai"
---

Grouping node for the 0 skills of the ai category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **ai-chief-of-staff** (`ai-chief-of-staff/`): Use when Personal AI assistant that combines Gmail, Calendar, and Drive data into actionable briefings via gwcli. Three sub-workflows, Morning Sweep: covers chief, staff, assistant, gwcli, combines
- **ai-quality-evaluator** (`ai-quality-evaluator/`): Use when Score and validate AI-generated financial reports for accuracy, hallucination detection, data consistency, coverage: covers quality, evaluator, actionability, completeness, hallucination
- **ai-workflow-integrator** (`ai-workflow-integrator/`): Use when Design and orchestrate AI-powered stock analysis workflows that chain data ingestion, LLM analysis, report generation, and Slack: covers integrator, ingestion, seamless, stages, composition

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
