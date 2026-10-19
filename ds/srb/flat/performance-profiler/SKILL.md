---
name: performance-profiler
description: "Use when Measure API endpoint latency (p50/p95/p99), analyze PostgreSQL slow queries, profile frontend bundle size, and evaluate against SLO targets: covers performance, profiler, 성능, 리뷰, latency"
metadata:
  holon-triggers: |
    latency problems
    slow queries
---

---
name: performance-profiler
description: >-
  Measure API endpoint latency (p50/p95/p99), analyze PostgreSQL slow queries,
  profile frontend bundle size, and evaluate against SLO targets. Use when the
  user asks about performance issues, latency problems, slow queries, bundle
  optimization, or SLO compliance. Do NOT use for database schema design (use
  db-expert), code-level optimization (use backend-expert or frontend-expert),
  or infrastructure scaling review (use sre-devops-expert). Korean triggers:
  "성능", "리뷰", "분석", "설계".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Performance Profiler

Measures and analyzes performance across the full stack — API endpoints, database queries, and frontend assets.

## When to Use

- Investigating latency complaints or slow responses
- Pre-release performance validation against SLO targets
- After schema or query changes to measure impact
- Frontend bundle size monitoring after dependency changes
- As part of the `/incident-response` workflow when the issue is performance-related

## SLO Targets (from docs/08-quality-testing/)

| Metric | Target | Service |
|--------|--------|---------|
| STT latency | p95 < 2s | stt-pipeline (8011) |
| Recommendation latency | p95 < 3s | llm-inference (8014) via orchestration |
| Summary generation | p95 < 10s | summary-crm (8016) |
| API response (general) | p95 < 500ms | all REST endpoints |
| Availability | 99.5% | system-wide |
| WebSocket connection | < 1s | call-manager (8010) |
| Knowledge search | p95 < 2s | rag-engine (8013) |

## Execution Steps

### Step 1: API Endpoint Profiling

Measure response times for critical endpoints. Services must be running locally.

For each endpoint, run N requests and collect timing:

```bash
for i in $(seq 1 20); do
  curl -o /dev/null -s -w "%{time_total}\n" http://localhost:PORT/ENDPOINT
done | sort -n
```

**Critical endpoints to profile:**

| Endpoint | Service | Port | SLO |
|----------|---------|------|-----|
