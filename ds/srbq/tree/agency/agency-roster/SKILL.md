---
name: agency-roster
description: "Use when Manage and orchestrate 68 Agency AI specialist agents installed as Cursor skills. List agents by division, compose teams for: covers agency, roster, division, overlaps, personalities"
metadata:
  holon-triggers: |
    'list agency agents'
    'agency roster'
---

---
name: agency-roster
description: >-
  Manage and orchestrate 68 Agency AI specialist agents installed as Cursor
  skills. List agents by division, compose teams for scenarios, activate agents,
  and map overlaps with existing project skills. Use when the user asks to 'list
  agency agents', 'agency roster', 'agency team', 'activate agent',
  'agency-roster', 'agency 목록', 'agency 팀', 'agent 활성화', or wants to use
  specialized AI personalities for tasks. Do NOT use for creating new skills
  (use create-skill) or optimizing existing skills (use skill-optimizer).
metadata:
  author: "thaki"
  version: "1.1.0"
  source: "msitarzewski/agency-agents@2293264"
  category: "persona"
---
# Agency Roster

68 specialized AI agents from [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) installed as Cursor skills under `.cursor/skills/agency-*/SKILL.md`. Source commit: `2293264` (2026-03-09).

## How to Activate

Each agent is a skill in `.cursor/skills/agency-{name}/SKILL.md`.

**Single agent**: Read the skill and adopt its persona:
```
Read the agency-frontend-developer skill and use it to review this component.
```

**Multi-agent team**: Read multiple skills and assign roles:
```
Read the agency-frontend-developer and agency-ux-researcher skills, then review this page for both implementation quality and usability.
```

## Agent Roster by Division

### Engineering (10 agents)

| Skill Name | Agent | Specialty |
|-----------|-------|-----------|
| `agency-frontend-developer` | Frontend Developer | React/Vue/Angular, UI, performance optimization |
| `agency-backend-architect` | Backend Architect | API design, database architecture, scalability |
| `agency-mobile-app-builder` | Mobile App Builder | iOS/Android, React Native, Flutter |
| `agency-ai-engineer` | AI Engineer | ML models, deployment, AI integration |
| `agency-devops-automator` | DevOps Automator | CI/CD, infrastructure automation, cloud ops |
| `agency-rapid-prototyper` | Rapid Prototyper 
