---
name: qa-test-expert
description: "Use when Design test strategies, generate test code (pytest, Playwright, Vitest), analyze coverage, and plan regression testing. Use when the user asks about: covers test, expert, 테스트, 분석, pytest"
metadata:
  holon-triggers: |
    test generation
    coverage improvement
---

---
name: qa-test-expert
description: >-
  Design test strategies, generate test code (pytest, Playwright, Vitest),
  analyze coverage, and plan regression testing. Use when the user asks about
  test planning, test generation, coverage improvement, or QA strategy. Do NOT
  use for writing or running Playwright E2E tests directly (use e2e-testing) or
  running the full CI pipeline (use ci-quality-gate). Korean triggers: "테스트",
  "분석", "생성", "설계".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# QA / Test Expert

Specialist for testing the FastAPI microservices (pytest + httpx) and React frontend (Vitest + Playwright). Tests at `tests/` (integration), per-service `tests/` dirs, and `frontend/` for E2E.

## Test Strategy

### Test Pyramid

```
        /  E2E  \          — Playwright (frontend flows, 10-20 scenarios)
       / Integration \      — pytest + httpx (API contracts, 50-100 tests)
      /    Unit Tests   \   — pytest / Vitest (functions, models, 200+ tests)
```

### When to Write Which

| Layer | What to test | Tools | Location |
|-------|-------------|-------|----------|
| Unit | Pure functions, Pydantic models, utils | pytest, Vitest | `services/*/tests/`, `frontend/src/**/*.test.ts` |
| Integration | API endpoints, DB queries, service interactions | pytest + httpx + testcontainers | `tests/integration/` |
| E2E | Critical user flows end-to-end | Playwright | `frontend/e2e/` |

## Test Code Generation

### pytest Template (FastAPI endpoint)

```python
import pytest
from httpx import AsyncClient, ASGITransport

@pytest.mark.asyncio
async def test_create_resource(app, db_session):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/resources",
            json={"name": "test", "tenant_id": "t1"},
            headers={"Authorization": "Bearer <test-token>"},
        )
    assert response.status_code == 201
  
