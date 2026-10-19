---
name: compliance-gate
description: "Use when Unified compliance quality gate that aggregates secret scanning, SAST (Bandit/Semgrep), dependency CVEs, IaC policy violations, and SBOM: covers compliance, gate, aggregates, bandit, cis"
metadata:
  holon-triggers: |
    run compliance check
    compliance gate
---

---
name: compliance-gate
description: >-
  Unified compliance quality gate that aggregates secret scanning, SAST
  (Bandit/Semgrep), dependency CVEs, IaC policy violations, and SBOM
  generation into a single compliance report with pass/fail per standard
  (SOC2, ISO27001, CIS). Use when the user asks to "run compliance check",
  "compliance gate", "security compliance scan", "컴플라이언스 게이트",
  "보안 컴플라이언스", "compliance-gate", or needs unified compliance
  validation before deployment. Do NOT use for code quality review (use
  deep-review), individual dependency audits (use dependency-auditor),
  or IaC validation only (use iac-review-agent).
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Compliance Gate

Unified compliance validation combining multiple security and policy checks into a single pass/fail report mapped to compliance frameworks.

## When to Use

- Before production deployments (mandatory gate)
- As part of the `release-commander` pipeline
- For periodic compliance audits
- When preparing for SOC2/ISO27001 certification

## Compliance Frameworks Covered

| Framework | Checks | Source |
|-----------|--------|--------|
| SOC2 Type II | Access control, logging, encryption, change mgmt | Checkov, custom rules |
| ISO 27001 | Information security controls | tfsec, KubeLinter |
| CIS Benchmarks | K8s, Docker, AWS/Azure hardening | kube-score, Checkov |
| OWASP Top 10 | Application security vulnerabilities | Semgrep, Bandit |
| Supply Chain | Dependency integrity, SBOM, provenance | Syft, Grype |

## Workflow

### Step 1: Secret Scanning

Scan for exposed secrets in code and configuration:

```bash
gitleaks detect --source . --report-format json --report-path /tmp/secrets.json
```

Checks: API keys, passwords, tokens, private keys, connection strings.

### Step 2: Static Application Security Testing (SAST)

**Python** (Bandit + Semgrep):
```bash
bandit -r . -f json -o /tmp/bandit.json
semgrep scan --config auto --json --output /tmp/semg
