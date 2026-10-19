---
name: pm-execution
description: "Use when Orchestrate product execution workflows, PRDs, OKRs, roadmaps, sprint planning, retrospectives, release notes, stakeholder mapping, user: covers execution, PRD 작성, OKR, 스프린트 계획, dummy"
metadata:
  holon-triggers: |
    write PRD
    plan OKRs
---

---
name: pm-execution
description: >-
  Orchestrate product execution workflows: PRDs, OKRs, roadmaps, sprint
  planning, retrospectives, release notes, stakeholder mapping, user stories,
  job stories, pre-mortems, test scenarios, and prioritization frameworks. Based
  on phuryn/pm-skills. Use when the user asks for "write PRD", "plan OKRs",
  "sprint plan", "retrospective", "release notes", "stakeholder map", "user
  stories", "pre-mortem", "test scenarios", "prioritization", "outcome roadmap",
  "meeting summary", or "dummy dataset". Do NOT use for product discovery (use
  pm-product-discovery), product strategy (use pm-product-strategy), or general
  feature spec (use kwp-product-management-feature-spec). Korean triggers: "PRD 작성", "OKR", "스프린트 계획", "회고", "릴리스 노트", "이해관계자 맵", "유저 스토리", "잡 스토리", "테스트 시나리오", "프리모템", "아웃컴 로드맵", "우선순위 프레임워크", "더미 데이터".
metadata:
  author: "thaki"
  version: "1.0.0"
  upstream: "https://github.com/phuryn/pm-skills"
  category: "product"
---
# PM Execution

Product execution skill orchestrator. Routes user requests to 15 sub-skills for planning, documentation, backlog management, and delivery. Read the matching reference file and follow its instructions.

## Sub-Skill Index

| Sub-Skill | When to Use | Reference |
|-----------|-------------|-----------|
| brainstorm-okrs | Quarterly OKRs, team goals aligned with company strategy | [references/brainstorm-okrs.md](references/brainstorm-okrs.md) |
| create-prd | PRD, product requirements, feature spec | [references/create-prd.md](references/create-prd.md) |
| dummy-dataset | Test data, mock datasets, sample data | [references/dummy-dataset.md](references/dummy-dataset.md) |
| job-stories | JTBD-style backlog items, situations and motivations | [references/job-stories.md](references/job-stories.md) |
| outcome-roadmap | Output→outcome roadmap transformation | [references/outcome-roadmap.md](references/outcome-roadmap.md) |
| pre-mortem | Launch risk analysis, Tigers/Paper Tigers/Elephant
