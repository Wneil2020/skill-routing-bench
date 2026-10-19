---
name: backend-expert
description: "Use when Design and review FastAPI microservices, Pydantic models, async patterns, error handling, and observability. Use when the user asks about: covers backend, expert, 백엔드, 리뷰, observability"
metadata:
  holon-triggers: |
    service architecture
    error models
---

---
name: backend-expert
description: >-
  Design and review FastAPI microservices, Pydantic models, async patterns,
  error handling, and observability. Use when the user asks about backend API
  design, service architecture, error models, or observability setup. Do NOT use
  for database schema design or migration review (use db-expert),
  deployment/infrastructure concerns (use sre-devops-expert), or frontend code
  (use frontend-expert). Korean triggers: "백엔드", "리뷰", "배포", "설계".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Backend Expert

Specialist for the FastAPI + Python 3.11+ microservices platform. The repo has 19 Python services under `services/` plus 1 Go service (`services/call-manager/`). Shared library at `shared/python/` (`agent-assist-common`).

## Service Inventory

19 Python services + 1 Go service (`call-manager`) under `services/`. For the full service list with ports, see [references/service-inventory.md](references/service-inventory.md).

## API Design Review

### Checklist

- [ ] RESTful resource naming (plural nouns, no verbs in paths)
- [ ] Pydantic v2 models for request/response with `model_config`
- [ ] Proper HTTP status codes (201 for create, 204 for delete, 409 for conflict)
- [ ] Pagination via `limit`/`offset` or cursor-based for large collections
- [ ] API versioning strategy consistent across services
- [ ] Request validation via Pydantic (not manual checks)
- [ ] Response envelope: `{"data": ..., "meta": {...}}` or direct model

### Error Model

Use the shared error model from `agent-assist-common`:

```python
# Standard error response
{
    "error": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "Human-readable description",
        "details": [...]  # optional field-level errors
    }
}
```

- Map domain exceptions to HTTP codes in exception handlers
- Never leak stack traces to clients
- Include `request_id` in error responses for tracing

## Async Patterns

- [ ] All I/O operations use `
