---
name: air-gap-orchestrator
description: "Use when Air-gap compatible pipeline orchestrator that routes LLM calls to on-premises endpoints, manages approval gates, provides audit logging, and: covers air, gap, orchestrator, compatible, prem"
metadata:
  holon-triggers: |
    run in air-gap mode
    on-prem pipeline
---

---
name: air-gap-orchestrator
description: >-
  Air-gap compatible pipeline orchestrator that routes LLM calls to on-premises
  endpoints, manages approval gates, provides audit logging, and supports
  model fallback chains. Use when the user asks to "run in air-gap mode",
  "on-prem pipeline", "에어갭 모드", "온프레미스 파이프라인",
  "air-gap-orchestrator", or needs pipeline execution in secure/isolated
  environments. Do NOT use for standard cloud pipeline execution (use
  mission-control), general orchestration without air-gap requirements (use
  mission-control), or LLM API configuration (configure directly).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Air-Gap Orchestrator

Pipeline orchestration middleware for air-gapped and on-premises environments. Ensures all LLM calls route through approved on-prem endpoints with audit logging and approval gates.

## When to Use

- When deploying the "One Person, Six Teams" pipeline in enterprise environments
- When running pipelines in air-gapped networks (no internet access)
- When compliance requires all AI processing to stay on-premises
- For Samsung and similar enterprise deployments with strict data governance

## Configuration

### Environment Variables

```bash
# LLM routing
AIRGAP_MODE=true                          # Enable air-gap mode
LLM_PROVIDER=on-prem                      # on-prem | cloud | hybrid
LLM_BASE_URL=https://llm.internal:8443    # On-prem LLM endpoint
LLM_MODEL=thaki-32b                       # Default on-prem model
LLM_FALLBACK_MODEL=thaki-8b              # Fallback if primary unavailable

# Approval gates
APPROVAL_REQUIRED=true                    # Require human approval for actions
APPROVAL_CHANNEL=#approvals               # Slack channel for approval requests
APPROVAL_TIMEOUT=300                      # Seconds to wait for approval

# Audit
AUDIT_LOG_PATH=/var/log/ai-pipeline/      # Audit log directory
AUDIT_LEVEL=full                          # full | summary | minimal
```

