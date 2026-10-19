---
name: role-developer
description: "Use when Analyze a given topic from the Developer perspective — implementation complexity, code impact, testing requirements, documentation needs: covers role, developer, 개발자 관점, 구현 영향, diagnosis"
metadata:
  holon-triggers: |
    developer perspective
    개발자 관점
---

---
name: role-developer
description: >
  Analyze a given topic from the Developer perspective — implementation complexity, code impact,
  testing requirements, documentation needs, and CI/CD implications.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes deep-review, test-suite, diagnose, technical-writer, refactor-simulator,
  workflow-miner, skill-composer, semantic-guard, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "developer perspective", "개발자 관점", "구현 영향 분석", "implementation impact".
  Do NOT use for hands-on code review (use deep-review), bug diagnosis (use diagnose),
  or test generation (use test-suite).
  Korean triggers: "개발자 관점", "구현 영향", "코드 영향 분석".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# Developer Perspective Analyzer

Analyzes any business topic from the Developer's viewpoint, covering implementation complexity,
codebase impact, testing strategy, documentation requirements, and CI/CD pipeline changes.

## Relevance Criteria

Score the topic 1-10 based on overlap with developer concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Implementation | High | code, implement, build, develop, API endpoint, module |
| Code impact | High | refactor, migration, breaking change, dependency, import |
| Testing | High | test, coverage, regression, E2E, unit test, edge case |
| CI/CD & tooling | High | pipeline, build, deploy, lint, pre-commit, GitHub Actions |
| Documentation | Medium | docs, README, ADR, API docs, changelog |
| Performance | Medium | latency, memory, optimization, profiling, bundle size |
| Security | Medium | vulnerability, auth, input validation, secret |
| Product & UX | Low | user flow, design, wireframe, persona |
| Strategy & finance | Low | market, revenue, investment, competition |

Score >= 5 → produce full analysis. Score < 5 → retur
