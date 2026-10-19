---
name: terraform-reviewer
description: "Use when Review Terraform modules using terraform validate, terraform plan dry-run, Checkov/tfsec static analysis, and LLM-based HCL review for: covers terraform, reviewer, architected, checkov, hcl"
metadata:
  holon-triggers: |
    review Terraform
    validate Terraform
---

---
name: terraform-reviewer
description: >-
  Review Terraform modules using terraform validate, terraform plan dry-run,
  Checkov/tfsec static analysis, and LLM-based HCL review for security, cost,
  and AWS Well-Architected patterns. Produces a structured pass/fail report.
  Use when the user asks to "review Terraform", "validate Terraform",
  "Terraform security check", "Terraform 리뷰", "테라폼 검증", "terraform-reviewer",
  or any Terraform/IaC quality validation. Do NOT use for Helm chart validation
  (use helm-validator), K8s manifest validation (use k8s-manifest-validator),
  or general infrastructure design (use sre-devops-expert).
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Terraform Reviewer

Review Terraform configurations through a 4-stage pipeline: syntax validation, plan analysis, static security scanning, and LLM-augmented best-practice review.

## When to Use

- Before merging PRs that modify `.tf`, `.tfvars`, or `.terraform.lock.hcl` files
- As part of the `iac-review-agent` unified IaC review pipeline
- When onboarding new Terraform modules or upgrading provider versions
- Security review of infrastructure changes

## Prerequisites

| Tool | Install | Purpose |
|------|---------|---------|
| `terraform` | `brew install terraform` | Validate and plan |
| `checkov` | `pip install checkov` | Static analysis (CIS, SOC2, HIPAA) |
| `tfsec` | `brew install tfsec` | Security-focused static analysis |

Missing tools are reported as `SKIPPED` in the output.

## Workflow

### Step 1: Discover Terraform Roots

Detect Terraform root modules in the target scope:

```bash
find <scope> -name "*.tf" -type f | xargs dirname | sort -u
```

For each root module, run Steps 2-6.

### Step 2: Terraform Validate

Initialize and validate syntax without accessing remote state:

```bash
cd <module-dir>
terraform init -backend=false
terraform validate
```

Capture validation errors (missing variables, type mismatches, syntax errors).

### Step 3: Ter
