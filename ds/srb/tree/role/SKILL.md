---
name: role
description: "Use when the request concerns the role category of skills: covers role"
---

Grouping node for the 0 skills of the role category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **role-ceo** (`role-ceo/`): Use when Analyze a given topic from the CEO/executive perspective — strategic impact, market positioning, stakeholder communication, and investment: covers role, ceo, CEO 관점, 경영진 분석, comms
- **role-cso** (`role-cso/`): Use when Analyze a given topic from the CSO (Chief Strategy Officer) perspective — market sizing, competitive positioning, GTM strategy, business model: covers role, cso, CSO 관점, 전략 분석, officer
- **role-cto** (`role-cto/`): Use when Analyze a given topic from the CTO/technical leadership perspective — architecture impact, tech debt implications, performance/SLO concerns: covers role, cto, CTO 관점, 기술 리더 분석, posture
- **role-data-scientist** (`role-data-scientist/`): Use when Analyze a given topic from the Data Scientist perspective — data pipeline impact, ML model implications, statistical methodology, data: covers role, data, scientist, 데이터 사이언티스트 관점, DS 분석
- **role-developer** (`role-developer/`): Use when Analyze a given topic from the Developer perspective — implementation complexity, code impact, testing requirements, documentation needs: covers role, developer, 개발자 관점, 구현 영향, diagnosis
- **role-dispatcher** (`role-dispatcher/`): Use when Cross-role mission control that dispatches a given topic to all 12 role-perspective analyzer skills in parallel batches, collects results: covers role, dispatcher, 직무별 분석, 종합 분석, batches
- **role-finance** (`role-finance/`): Use when Analyze a given topic from the Finance perspective — financial impact, budget variance, ROI analysis, cash flow implications, and: covers role, finance, 재무 관점, 재무 분석, reconciliation
- **role-hr** (`role-hr/`): Use when Analyze a given topic from the HR perspective — organizational impact, hiring needs, change management, training requirements, and people: covers role, HR 관점, 인사 분석, compensation, handbook
- **role-pm** (`role-pm/`): Use when Analyze a given topic from the Product Manager perspective — PRD implications, sprint impact, user story generation, OKR alignment, roadmap changes: covers role, PM 관점, 기획자 분석, story, okr
- **role-sales** (`role-sales/`): Use when Analyze a given topic from the Sales perspective — sales enablement impact, competitive battlecard needs, customer outreach implications, pipeline: covers role, sales, 영업 관점, 영업 분석, effects
- **role-security-engineer** (`role-security-engineer/`): Use when Analyze a given topic from the Security Engineer perspective — threat modeling (STRIDE), vulnerability assessment (OWASP Top 10): covers role, security, engineer, 보안 관점, 보안 엔지니어 분석
- **role-trading-expert** (`role-trading-expert/`): Use when Analyze a given topic from the Trading Expert perspective — market environment impact, technical analysis, strategy validation, risk: covers role, trading, expert, 트레이딩 전문가 관점, 매매 전문가 분석
- **role-ux-designer** (`role-ux-designer/`): Use when Analyze a given topic from the UX Designer perspective — user experience impact, accessibility concerns, design system consistency, user: covers role, designer, UX 관점, 디자이너 분석, critique

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
