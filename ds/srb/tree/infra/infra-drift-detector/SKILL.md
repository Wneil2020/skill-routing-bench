---
name: infra-drift-detector
description: "Use when Detect infrastructure drift by comparing live cluster state against declared IaC (Helm releases, K8s manifests, Terraform state). Reports: covers infra, drift, detector, cluster, declared"
metadata:
  holon-triggers: |
    check for drift
    infrastructure drift
---

---
name: infra-drift-detector
description: >-
  Detect infrastructure drift by comparing live cluster state against declared
  IaC (Helm releases, K8s manifests, Terraform state). Reports drifts with
  severity and remediation suggestions. Use when the user asks to "check for
  drift", "infrastructure drift", "인프라 드리프트", "상태 비교",
  "infra-drift-detector", or wants to verify infrastructure matches its
  declared state. Do NOT use for IaC code review (use iac-review-agent),
  initial validation (use helm-validator/k8s-manifest-validator), or
  deployment (use sre-devops-expert).
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Infrastructure Drift Detector

Compare live infrastructure state against declared IaC to detect configuration drift, unauthorized changes, and state inconsistencies.

## When to Use

- Periodic drift checks (daily/weekly schedule)
- Before deployments to establish a clean baseline
- After incidents to detect unauthorized changes
- During compliance audits to verify state consistency

## Prerequisites

Requires cluster access (`kubectl` context) and optionally Terraform state access.

## Workflow

### Step 1: Discover Declared State

Identify all IaC sources:

**Helm Releases**:
```bash
helm list -A -o json
```

**K8s Manifests**: Read from `infra/k8s/`, `deploy/` directories.

**Terraform State** (if available):
```bash
terraform show -json
```

### Step 2: Capture Live State

For each declared resource, fetch the live state:

**Helm drift**:
```bash
helm diff upgrade <release> <chart> --values <values> --no-hooks
```

If `helm-diff` plugin not available:
```bash
helm get manifest <release> -n <namespace> > /tmp/declared.yaml
kubectl get <kind> <name> -n <namespace> -o yaml > /tmp/live.yaml
diff /tmp/declared.yaml /tmp/live.yaml
```

**K8s manifest drift**:
```bash
kubectl diff -f <manifest-file> 2>&1
```

**Terraform drift**:
```bash
terraform plan -detailed-exitcode
```
Exit code 2 = drift detected.

### Step 3: Class
