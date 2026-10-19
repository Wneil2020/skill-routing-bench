---
name: service-health-doctor
description: "Use when Diagnose and recover the local development stack — check health of all 24+ microservices, detect port conflicts, analyze error logs, and auto-restart: covers service, health, doctor, 리뷰, 분석"
metadata:
  holon-triggers: |
    asks to check health
    needs to troubleshoot the dev stack
---

---
name: service-health-doctor
description: >-
  Diagnose and recover the local development stack — check health of all 24+
  microservices, detect port conflicts, analyze error logs, and auto-restart
  failed services. Use when the user reports service issues, asks to check
  health, or needs to troubleshoot the dev stack. Do NOT use for starting the
  full stack from scratch (use local-dev-runner) or reviewing infrastructure
  configuration (use sre-devops-expert). Korean triggers: "리뷰", "분석", "체크",
  "리포트".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Service Health Doctor

Diagnoses and recovers the local development stack (24 microservices + 5 infrastructure components).

## When to Use

- A service fails to start or returns errors
- The user says "X service is down" or "something is broken"
- As part of the `/incident-response` workflow (called by mission-control)
- After `git pull` or dependency changes that may break services

## Service Registry

5 infrastructure components (Docker) and 24 application services with HTTP `/health` endpoints. For the full registry with ports and tiers, see [references/service-registry.md](references/service-registry.md).

## Execution Steps

### Step 1: Run Status Script

```bash
bash scripts/dev-status.sh
```

Parse the output to categorize services as UP / HEALTHY / STARTING / DOWN.

### Step 2: Diagnose DOWN Services

For each DOWN service, investigate in order:

#### 2a. Port Conflict Detection

```bash
lsof -i :PORT
```

If another process occupies the port, report the PID and process name. Suggest:
- Kill the conflicting process: `kill -9 PID`
- Or use an alternative port

#### 2b. Docker Infrastructure Check

For Docker services (postgres, redis, qdrant, minio):

```bash
docker compose ps
docker compose logs --tail=30 SERVICE_NAME
```

Common issues and fixes:
- **Container not running**: `docker compose up -d SERVICE_NAME`
- **Volume corruption**: `docker compose down -v && docker comp
