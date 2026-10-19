---
name: infra-runbook-generator
description: "Use when Generate infrastructure runbooks from Helm charts, K8s manifests, monitoring configs, and alert rules. Produces structured runbooks with: covers infra, runbook, generator, configs, paths"
metadata:
  holon-triggers: |
    generate runbook
    create runbook
---

---
name: infra-runbook-generator
description: >-
  Generate infrastructure runbooks from Helm charts, K8s manifests, monitoring
  configs, and alert rules. Produces structured runbooks with overview,
  prerequisites, step-by-step procedures, rollback plans, and escalation
  paths. Output as .md + .docx with Cognee indexing. Use when the user asks
  to "generate runbook", "create runbook", "런북 생성", "인프라 런북",
  "infra-runbook-generator", or needs operational runbooks for infrastructure
  components. Do NOT use for incident response (use incident-to-improvement),
  general documentation (use technical-writer), or reviewing existing
  runbooks (use sre-devops-expert).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Infrastructure Runbook Generator

Transform infrastructure code into operational runbooks, reducing runbook creation from 3 days to 15 minutes.

## When to Use

- When deploying a new service/component that needs operational documentation
- When infrastructure code changes require runbook updates
- As part of the release pipeline (post-code-review, pre-deployment)
- When onboarding new SRE/ops team members

## Workflow

### Step 1: Analyze Infrastructure Context

Read and analyze the target infrastructure component:

**Helm Charts** (if present):
- `Chart.yaml`: name, version, dependencies
- `values.yaml`: configurable parameters, defaults
- `templates/`: resource types, labels, selectors
- `README.md`: existing documentation

**K8s Manifests** (if present):
- Deployments, StatefulSets, DaemonSets
- Services, Ingresses, NetworkPolicies
- ConfigMaps, Secrets references
- PVCs, StorageClasses

**Monitoring Config** (if present):
- Prometheus rules, Grafana dashboards
- AlertManager routes and receivers
- SLO definitions

**Docker Config** (if present):
- Dockerfile: build process, dependencies, ports
- docker-compose: service dependencies, volumes, networks

### Step 2: Identify Runbook Scope

Determine which runbook types are need
