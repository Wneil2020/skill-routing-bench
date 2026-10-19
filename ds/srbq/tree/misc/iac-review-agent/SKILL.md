---
name: iac-review-agent
description: "Use when Unified Infrastructure-as-Code review agent that detects IaC file types in diffs (Helm, Terraform, K8s manifests) and routes to the: covers iac, review, diffs, appropriate, manifest"
metadata:
  holon-triggers: |
    review infrastructure code
    IaC review
---

---
name: iac-review-agent
description: >-
  Unified Infrastructure-as-Code review agent that detects IaC file types in
  diffs (Helm, Terraform, K8s manifests) and routes to the appropriate
  validator. Orchestrates helm-validator, terraform-reviewer, and
  k8s-manifest-validator into a single review pass. Use when the user asks to
  "review infrastructure code", "IaC review", "validate infra changes",
  "인프라 코드 리뷰", "IaC 검증", "iac-review-agent", or any unified IaC
  validation. Do NOT use for application code review (use deep-review),
  CI/CD pipeline review (use sre-devops-expert), or single-tool validation
  (use the specific validator skill directly).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# IaC Review Agent

Unified orchestrator for Infrastructure-as-Code review. Detects IaC file types in the change set, routes to specialized validators, aggregates results, and optionally posts as PR review comments.

## When to Use

- As the 5th agent in the `deep-review` pipeline (alongside Frontend, Backend, Security, Test Coverage)
- Before merging any PR that touches infrastructure files
- As a standalone IaC quality gate in CI/CD

## Workflow

### Step 1: Detect IaC Files in Scope

Classify changed files by IaC type:

| Pattern | Type | Router Target |
|---------|------|---------------|
| `Chart.yaml`, `templates/*.yaml`, `values*.yaml` in chart dirs | Helm | `helm-validator` |
| `*.tf`, `*.tfvars`, `*.terraform.lock.hcl` | Terraform | `terraform-reviewer` |
| `*.yaml`/`*.yml` with `kind:` field (non-Helm) | K8s Manifest | `k8s-manifest-validator` |
| `docker-compose*.yml`, `Dockerfile*` | Docker | LLM review only |
| `.github/workflows/*.yml` | CI/CD | LLM review only |

If no IaC files are detected, report "No IaC files in scope" and exit.

### Step 2: Launch Parallel Validators

For each detected IaC type, launch the corresponding validator as a subagent:

```
Subagent 1 (if Helm files):      helm-validator
Subagent 2 (if Terraform 
