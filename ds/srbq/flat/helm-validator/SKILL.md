---
name: helm-validator
description: "Use when Validate Helm charts using helm lint, helm template rendering, kubeconform schema validation, and kube-score/Polaris policy checks: covers helm, validator, kube, polaris, kubeconform"
metadata:
  holon-triggers: |
    validate Helm chart
    lint Helm
---

---
name: helm-validator
description: >-
  Validate Helm charts using helm lint, helm template rendering, kubeconform
  schema validation, and kube-score/Polaris policy checks. Produces a structured
  pass/fail report with fix suggestions. Use when the user asks to "validate
  Helm chart", "lint Helm", "check Helm chart", "Helm 검증", "Helm 차트 린트",
  "helm-validator", or any Helm chart quality/security validation request.
  Do NOT use for general K8s manifest validation without Helm (use
  k8s-manifest-validator), Terraform review (use terraform-reviewer), or
  CI/CD pipeline review (use sre-devops-expert).
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Helm Validator

Validate Helm charts through a 4-stage pipeline: lint, template render, schema validation, and policy checks.

## When to Use

- Before merging PRs that modify `Chart.yaml`, `values.yaml`, or templates
- As part of the `iac-review-agent` unified IaC review pipeline
- When onboarding new Helm charts or upgrading chart versions
- Pre-deployment validation in CI/CD

## Prerequisites

| Tool | Install | Purpose |
|------|---------|---------|
| `helm` | `brew install helm` | Lint and template rendering |
| `kubeconform` | `brew install kubeconform` | Schema validation against K8s OpenAPI |
| `kube-score` | `brew install kube-score` | Best-practice policy checks |

Missing tools are reported as `SKIPPED` in the output.

## Workflow

### Step 1: Discover Charts

Detect Helm charts in the target scope:

```bash
find <scope> -name "Chart.yaml" -type f
```

For each discovered chart directory, run Steps 2-5.

### Step 2: Helm Lint

Run `helm lint` with strict mode to catch template errors and best-practice violations:

```bash
helm lint <chart-dir> --strict --values <chart-dir>/values.yaml
```

Capture exit code and parse warning/error output.

### Step 3: Template Render

Render templates to catch runtime errors that lint misses:

```bash
helm template test-release <chart-dir> --values
