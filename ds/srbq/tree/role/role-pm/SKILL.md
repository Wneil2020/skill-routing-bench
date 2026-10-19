---
name: role-pm
description: "Use when Analyze a given topic from the Product Manager perspective — PRD implications, sprint impact, user story generation, OKR alignment, roadmap changes: covers role, PM 관점, 기획자 분석, story, okr"
metadata:
  holon-triggers: |
    PM perspective
    PM 관점
---

---
name: role-pm
description: >
  Analyze a given topic from the Product Manager perspective — PRD implications, sprint impact,
  user story generation, OKR alignment, roadmap changes, and stakeholder communication.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes pm-execution, kwp-product-management-feature-spec, pm-product-discovery,
  kwp-product-management-roadmap-management, workflow-miner, skill-composer,
  and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "PM perspective", "PM 관점", "기획자 분석", "product impact".
  Do NOT use for writing a full PRD (use pm-execution), sprint planning execution
  (use agency-sprint-prioritizer), or A/B test analysis (use pm-data-analytics).
  Korean triggers: "PM 관점", "기획자 분석", "제품 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# PM Perspective Analyzer

Analyzes any business topic from the Product Manager's viewpoint, covering product requirements,
user impact, sprint/roadmap changes, OKR alignment, and stakeholder communication needs.

## Relevance Criteria

Score the topic 1-10 based on overlap with PM concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Product requirements | High | feature, PRD, spec, user story, acceptance criteria |
| User experience | High | user flow, journey, persona, usability, onboarding |
| Roadmap & planning | High | roadmap, sprint, milestone, priority, backlog |
| Metrics & OKR | High | KPI, OKR, retention, conversion, engagement |
| Stakeholder comms | Medium | update, report, alignment, decision, trade-off |
| Market & competition | Medium | competitor, positioning, market fit, user research |
| Technical feasibility | Medium | API, integration, migration, performance |
| Financial & strategy | Low | revenue, cost, investment, valuation |
| HR & organization | Low | team, hiring, culture |

Score >= 
