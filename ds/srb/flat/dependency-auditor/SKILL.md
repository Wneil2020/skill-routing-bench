---
name: dependency-auditor
description: "Use when Audit and update Python, Go, and Node.js dependencies — scan for CVEs, classify severity, apply safe patch updates, and generate impact reports for: covers dependency, auditor, 감사, 리뷰, patch"
metadata:
  holon-triggers: |
    audit dependencies
    update packages
---

---
name: dependency-auditor
description: >-
  Audit and update Python, Go, and Node.js dependencies — scan for CVEs,
  classify severity, apply safe patch updates, and generate impact reports for
  major updates. Use when the user asks to audit dependencies, update packages,
  check for vulnerabilities, or run a dependency sweep. Do NOT use for general
  security reviews or threat modeling (use security-expert) or running the full
  CI pipeline (use ci-quality-gate). Korean triggers: "감사", "리뷰", "생성", "체크".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Dependency Auditor

Manages dependencies across the entire polyglot stack (19 Python services, 1 Go service, 1 Node.js frontend).

## When to Use

- Periodic dependency health checks
- After Dependabot PRs to verify compatibility
- Before releases to ensure no known CVEs
- As part of the `/dependency-sweep` workflow (called by mission-control)

## Dependency Map

### Python (20 packages)

| Scope | File | Package Manager |
|-------|------|----------------|
| Shared library | `shared/python/pyproject.toml` | pip / uv |
| 19 services | `services/*/pyproject.toml` | pip / uv |
| Root workspace | `pyproject.toml` | pip / uv |
| Lock file | `uv.lock` | uv |

### Go (1 service)

| Scope | File |
|-------|------|
| call-manager | `services/call-manager/go.mod` |
| Lock file | `services/call-manager/go.sum` |

### Node.js (1 app)

| Scope | File |
|-------|------|
| Frontend | `frontend/package.json` |
| Lock file | `frontend/package-lock.json` |

### Other

| Scope | File |
|-------|------|
| Telephony scripts | `services/telephony-stack/scripts/requirements.txt` |

## Execution Steps

### Step 1: Vulnerability Scan

Run all scanners in parallel (use Task tool subagents):

**Python:**
```bash
pip-audit --strict --desc on 2>&1
```

**Go:**
```bash
cd services/call-manager && go list -m -json all | go run golang.org/x/vuln/cmd/govulncheck@latest ./... 2>&1 || true
```

**Node.js:**
```bash
cd fr
