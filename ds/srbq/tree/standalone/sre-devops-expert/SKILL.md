---
name: sre-devops-expert
description: "Use when Design and review CI/CD pipelines, Helm charts, Kubernetes manifests, Docker Compose configs, runbooks, SLO definitions, and rollback procedures. Use when: covers sre, devops, expert, 리뷰, 배포"
metadata:
  holon-triggers: |
    infrastructure
    operational readiness
---

---
name: sre-devops-expert
description: >-
  Design and review CI/CD pipelines, Helm charts, Kubernetes manifests, Docker
  Compose configs, runbooks, SLO definitions, and rollback procedures. Use when
  the user asks about deployment, infrastructure, runbooks, alerting, or
  operational readiness. Do NOT use for running CI locally (use
  ci-quality-gate), managing the local dev stack (use local-dev-runner), or
  backend API code review (use backend-expert). Korean triggers: "리뷰", "배포",
  "설계", "파이프라인".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# SRE / DevOps Expert

Specialist for the infrastructure at `infra/` (Helm/K8s), `docker-compose.yml` (local infra), `docker-compose.services.yml` (app services), `.github/workflows/` (CI/CD), and `Makefile`.

## Infrastructure Inventory

| Component | Location | Technology |
|-----------|----------|-----------|
| Local infra | `docker-compose.yml` | PostgreSQL 16, PgBouncer, Redis 7, Qdrant, MinIO |
| App services | `docker-compose.services.yml` | 14 Python + 1 Go + 1 React containers |
| Helm charts | `infra/helm/` | Kubernetes deployment (primary) |
| K8s manifests | `infra/k8s/` | Supplementary raw manifests |
| Observability | `infra/observability/` | Prometheus, Grafana, Loki, OTel, Alertmanager |
| CI/CD | `.github/workflows/` | GitHub Actions |
| Scripts | `scripts/` | Build, deploy, utility scripts |

## CI/CD Pipeline Review

### Checklist

- [ ] Lint → Test → Build → Push → Deploy stages in order
- [ ] Tests run in parallel where independent
- [ ] Docker images tagged with git SHA (not just `latest`)
- [ ] Multi-stage Dockerfiles (builder + runtime for small images)
- [ ] Secret management via GitHub Secrets or external vault (not hardcoded)
- [ ] Branch protection: main requires passing CI + review
- [ ] Caching: pip/npm/go module caches in CI
- [ ] Security scan: container image scanning (Trivy, Snyk)

## Docker / Compose Review

### Checklist

- [ ] Base images pinned to specific v
