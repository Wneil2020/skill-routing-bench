---
name: role-cto
description: "Use when Analyze a given topic from the CTO/technical leadership perspective — architecture impact, tech debt implications, performance/SLO concerns: covers role, cto, CTO 관점, 기술 리더 분석, posture"
metadata:
  holon-triggers: |
    CTO perspective
    CTO 관점
---

---
name: role-cto
description: >
  Analyze a given topic from the CTO/technical leadership perspective — architecture impact,
  tech debt implications, performance/SLO concerns, security posture, and engineering capacity.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes deep-review, backend-expert, sre-devops-expert, security-expert, refactor-simulator,
  workflow-miner, skill-composer, semantic-guard, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "CTO perspective", "CTO 관점", "기술 리더 분석", "architecture impact".
  Do NOT use for hands-on code review (use deep-review), release pipeline execution
  (use release-commander), or incident response (use incident-to-improvement).
  Korean triggers: "CTO 관점", "기술 리더 분석", "아키텍처 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# CTO Perspective Analyzer

Analyzes any business topic from the CTO's technical leadership viewpoint, covering architecture
impact, engineering capacity, tech debt, performance, security, and infrastructure implications.

## Relevance Criteria

Score the topic 1-10 based on overlap with CTO concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Architecture & design | High | microservice, API, system design, scalability, migration |
| Performance & SLO | High | latency, throughput, SLO, p99, monitoring, observability |
| Security & compliance | High | vulnerability, threat, OWASP, compliance, data protection |
| Tech debt & quality | High | refactor, legacy, code quality, maintainability |
| Infrastructure & DevOps | High | K8s, deployment, CI/CD, cloud, GPU cluster |
| Engineering capacity | Medium | team size, hiring, onboarding, skill gaps |
| Product & feature | Medium | new feature, MVP, technical feasibility |
| Strategic & market | Low | market, revenue, competition, pricing |
| HR & organization | Low
