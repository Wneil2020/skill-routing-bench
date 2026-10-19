---
name: role-hr
description: "Use when Analyze a given topic from the HR perspective — organizational impact, hiring needs, change management, training requirements, and people: covers role, HR 관점, 인사 분석, compensation, handbook"
metadata:
  holon-triggers: |
    HR perspective
    HR 관점
---

---
name: role-hr
description: >
  Analyze a given topic from the HR perspective — organizational impact, hiring needs,
  change management, training requirements, and people analytics implications.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes kwp-human-resources-org-planning, kwp-human-resources-people-analytics,
  kwp-operations-change-management, kwp-human-resources-interview-prep,
  workflow-miner, semantic-guard, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "HR perspective", "HR 관점", "인사 분석", "organizational impact".
  Do NOT use for compensation benchmarking (use kwp-human-resources-compensation-benchmarking),
  employee handbook creation (use kwp-human-resources-employee-handbook), or
  recruiting pipeline management (use kwp-human-resources-recruiting-pipeline).
  Korean triggers: "HR 관점", "인사 분석", "조직 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# HR Perspective Analyzer

Analyzes any business topic from the HR team's viewpoint, covering organizational impact,
workforce planning, change management, training needs, and employee experience implications.

## Relevance Criteria

Score the topic 1-10 based on overlap with HR concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Organizational change | High | reorg, restructure, new team, expansion, merger |
| Workforce planning | High | headcount, hiring, skill gap, capacity, staffing |
| Change management | High | rollout, transition, adoption, communication, training |
| Employee experience | Medium | onboarding, retention, engagement, culture, morale |
| Compensation & benefits | Medium | salary, equity, benefits, benchmark, comp review |
| Learning & development | Medium | training, upskilling, certification, workshop |
| Compliance & policy | Medium | labor law, policy, handbook, GDPR (employee data) |
