---
name: portfolio-report-generator
description: "Use when Generate cross-project portfolio reports aggregating weekly status from all managed projects into an executive view with: covers portfolio, report, generator, aggregating, repositories"
metadata:
  holon-triggers: |
    portfolio report
    cross-project summary
---

---
name: portfolio-report-generator
description: >-
  Generate cross-project portfolio reports aggregating weekly status from all
  managed projects into an executive view with project health, blockers, and
  resource allocation. Use when the user asks to "portfolio report",
  "cross-project summary", "포트폴리오 리포트", "프로젝트 전체 현황",
  "portfolio-report-generator", or needs a unified view across multiple
  repositories. Do NOT use for single-project weekly reports (use
  weekly-status-report), daily activity digests (use github-sprint-digest),
  or release pipeline (use release-commander).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Portfolio Report Generator

Cross-project executive portfolio report: aggregate status from all managed projects into a unified health dashboard.

## When to Use

- Weekly executive reporting across all managed projects
- Sprint retrospectives spanning multiple repositories
- Resource allocation reviews
- Stakeholder presentations on overall program health

## Managed Projects

| Project | Repository | Type |
|---------|-----------|------|
| AI Platform WebUI | ThakiCloud/ai-platform-webui | Main platform |
| TKAI Deploy | ThakiCloud/tkai-deploy | Deployment tooling |
| TKAI Agents | ThakiCloud/tkai-agents | Agent framework |
| Business Automation | ThakiCloud/thaki-business-automation | Business team tools |
| Research | ThakiCloud/research | R&D projects |

## Workflow

### Step 1: Collect Per-Project Data

For each managed project, gather weekly metrics:

```bash
for repo in ai-platform-webui tkai-deploy tkai-agents thaki-business-automation research; do
  gh issue list --repo ThakiCloud/$repo --state all --json number,state,labels,closedAt \
    --search "updated:>=$(date -v-7d +%Y-%m-%d)"
  gh pr list --repo ThakiCloud/$repo --state all --json number,state,mergedAt \
    --search "updated:>=$(date -v-7d +%Y-%m-%d)"
done
```

### Step 2: Calculate Health Scores

Per-project health score (0-100) based on:


