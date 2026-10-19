---
name: local-dev-runner
description: "Use when Start, stop, and manage the full local development environment on macOS. Use when the user asks to run the project locally, start/stop services, or: covers local, dev, runner, 리뷰, diagnosing"
metadata:
  holon-triggers: |
    run the project locally
    start/stop services
---

---
name: local-dev-runner
description: >-
  Start, stop, and manage the full local development environment on macOS. Use
  when the user asks to run the project locally, start/stop services, or set up
  the development stack from scratch. Do NOT use for diagnosing specific service
  failures after startup (use service-health-doctor) or reviewing infrastructure
  configuration (use sre-devops-expert). Korean triggers: "리뷰".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Local Development Runner

로컬 macOS 환경에서 프로젝트 전체 스택을 실행하고 관리하는 스킬.

## Prerequisites

| Tool    | Minimum Version | Check Command          |
|---------|----------------|------------------------|
| Docker  | 20+            | `docker --version`     |
| Node.js | 18+            | `node --version`       |
| npm     | 9+             | `npm --version`        |
| Python  | 3.13+          | `python3 --version`    |
| Go      | 1.22+          | `go version`           |
| uv      | 0.4+           | `uv --version`         |

## Architecture Overview

```
┌─────────────────── Docker (Infrastructure) ───────────────────┐
│  PostgreSQL:5433  PgBouncer:5434  Redis:6379                  │
│  Qdrant:6333,6334  MinIO:9000,9001                            │
└───────────────────────────────────────────────────────────────┘
         ↓                    ↓                    ↓
┌────── Tier 1 (Stateless) ──┐  ┌── Tier 2 (Data) ────────────┐
│ pii-redaction    :8031     │  │ rag-engine           :8013   │
│ nlp-state        :8012     │  │ knowledge-manager    :8015   │
│ analytics        :8022     │  │ memory-service       :8019   │
│ feedback         :8017     │  │ summary-crm          :8016   │
│ routing-engine   :8028     │  └──────────────────────────────┘
└────────────────────────────┘
         ↓                    ↓
┌────── Tier 3 (AI/ML) ─────┐  ┌── Tier 4 (Business) ────────┐
│ llm-inference    :8014     │  │ orchestration        :8020   │
│ stt-pipeline     :8011     │  │ admin          
