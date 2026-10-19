---
name: k8s-manifest-validator
description: "Use when Validate Kubernetes manifests using kubeconform schema validation, KubeLinter policy checks, and kubectl dry-run server-side validation: covers k8s, manifest, validator, kubectl, kubelinter"
metadata:
  holon-triggers: |
    validate K8s manifests
    check Kubernetes YAML
---

---
name: k8s-manifest-validator
description: >-
  Validate Kubernetes manifests using kubeconform schema validation, KubeLinter
  policy checks, and kubectl dry-run server-side validation. Produces a
  structured pass/fail report. Use when the user asks to "validate K8s
  manifests", "check Kubernetes YAML", "K8s 매니페스트 검증", "쿠버네티스 검증",
  "k8s-manifest-validator", or any Kubernetes manifest quality/security
  validation. Do NOT use for Helm chart validation (use helm-validator),
  Terraform review (use terraform-reviewer), or infrastructure design review
  (use sre-devops-expert).
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# K8s Manifest Validator

Validate raw Kubernetes manifests (non-Helm YAML files) through a 4-stage pipeline: schema validation, policy checks, dry-run validation, and LLM-augmented review.

## When to Use

- Before merging PRs that modify files in `infra/k8s/`, `deploy/`, or any directory containing K8s manifests
- As part of the `iac-review-agent` unified IaC review pipeline
- When migrating between Kubernetes versions (API deprecation checks)
- Security review of workload configurations

## Prerequisites

| Tool | Install | Purpose |
|------|---------|---------|
| `kubeconform` | `brew install kubeconform` | OpenAPI schema validation |
| `kube-linter` | `brew install kube-linter` | Security and best-practice linting |
| `kubectl` | `brew install kubectl` | Dry-run server-side validation |

Missing tools are reported as `SKIPPED` in the output.

## Workflow

### Step 1: Discover Manifests

Find Kubernetes manifest files in the target scope:

```bash
find <scope> -name "*.yaml" -o -name "*.yml" | \
  xargs grep -l "^kind:" 2>/dev/null
```

Filter out Helm templates (files containing `{{ }}` Go template syntax) — those go to `helm-validator`.

### Step 2: Schema Validation (kubeconform)

Validate each manifest against the target K8s version OpenAPI schema:

```bash
kubeconform -kubernetes-version <target-version> -summ
