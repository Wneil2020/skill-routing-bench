---
name: e2e-testing
description: "Use when Write, run, and debug Playwright E2E tests for the frontend application. Use when the user asks to create E2E tests, run E2E tests, debug test failures: covers e2e, testing, 테스트, 생성, debug"
metadata:
  holon-triggers: |
    create E2E tests
    run E2E tests
---

---
name: e2e-testing
description: >-
  Write, run, and debug Playwright E2E tests for the frontend application. Use
  when the user asks to create E2E tests, run E2E tests, debug test failures, or
  automate browser-based testing scenarios. Do NOT use for test strategy
  planning, coverage analysis, or unit test generation (use qa-test-expert).
  Korean triggers: "테스트", "생성", "계획", "디버깅".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# E2E Testing Skill

Playwright 기반 E2E 테스트 작성, 실행, 디버깅 가이드.

## Project Context

- **Test dir**: `frontend/e2e/`
- **Config**: `frontend/playwright.config.ts`
- **Base URL**: `http://localhost:5173`
- **Framework**: Playwright `^1.58.2`
- **Browser**: Chromium only
- **Runner**: `pnpm test:e2e` (또는 `make test-e2e`)

## Prerequisites

E2E 테스트 실행 전 필수 환경:

```bash
# 1. 인프라 시작 (postgres, redis, pgbouncer, qdrant, minio)
make dev-infra   # 또는 docker compose up -d

# 2. DB 마이그레이션 + 시드 데이터
make db-migrate && make db-seed

# 3. 백엔드 서비스 시작 (최소: admin:8018, call-manager:8010)
docker compose -f docker-compose.yml -f docker-compose.services.yml up -d

# 4. 프론트엔드 (자동 시작됨 — playwright.config의 webServer)
cd frontend && pnpm dev
```

**Redis 참고**: `global-setup.ts`가 `autopilot-dev-redis` 또는 `aa-redis` 컨테이너의 rate-limit 키를 플러시함.

## Test File Structure

```
frontend/e2e/
├── {feature}.spec.ts      # 테스트 파일
├── global-setup.ts        # Rate-limit flush
└── helpers/
    ├── auth.ts            # loginAs() 헬퍼
    └── setup.ts           # 커스텀 fixture 확장점
```

## Writing Tests

### 1. 기본 구조

```typescript
import { test, expect } from "@playwright/test";
import { loginAs } from "./helpers/auth";

test.describe("Feature Name", () => {
  test.beforeEach(async ({ page }) => {
    await loginAs(page);  // 인증 필요 시
  });

  test("should do something", async ({ page }) => {
    await page.goto("/route");
    await expect(page.getByRole("button", { name: /action/i })).toBeVisible();
  });
});
```

### 2. 인증 패턴

```typescript
// 로그인 (기본: m
