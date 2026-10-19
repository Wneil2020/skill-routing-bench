---
name: fsd-development
description: "Use when AI Platform Frontend의 FSD 변형 구조로 새 도메인을 생성하거나 레거시 코드를 마이그레이션합니다. entities, features, pages, widgets 작업 시, 새 도메인 추가 시, features-legacy에서: covers fsd, development, widgets, legacy, entities"
---

---
name: fsd-development
description: AI Platform Frontend의 FSD 변형 구조로 새 도메인을 생성하거나 레거시 코드를 마이그레이션합니다. entities, features, pages, widgets 작업 시, 새 도메인 추가 시, features-legacy에서 마이그레이션 시 사용합니다. Do NOT use for Figma 분석(figma-to-tds), 화면 기획서 작성(screen-description), 또는 전체 화면 구현 오케스트레이션(implement-screen).
metadata:
  version: 1.1.0
  category: execution
---

# AI Platform FE - FSD 개발 및 마이그레이션

## 핵심 원칙

**의존성 규칙 (단방향)**:

```
shared → entities → features → widgets → pages → app/routes
```

- 하위 레이어는 상위 레이어 참조 불가
- 같은 레이어 내 형제 import 금지

**Export 규칙**:

```typescript
// ❌ export * 금지!
export * from "./Button";

// ✅ 명시적 named export
export { Button } from "./Button";
export type { ButtonProps } from "./Button";
```

---

## 입력 소스 확인

| 소스 | 참조 방법 | 활용 |
|------|-----------|------|
| **화면 기획서** | `docs/screens/{domain}/{screen}.md` 읽기 | API 엔드포인트, 상태 정의, 컴포넌트 구성 |
| **Figma 분석 결과** | 오케스트레이터 Phase 2 산출물 | TDS 컴포넌트 매핑, 토큰 매핑 |
| **TDS 컴포넌트 API** | `03-tds-essentials.mdc`(자동) + `04-tds-detail-catalog.mdc` Rule | Props, variant, 패턴 |
| **테이블 패턴** | `07-table-patterns.mdc` Rule | 목록 페이지 Config/Widget 구조 |

---

## 새 도메인 생성 워크플로우

### 체크리스트

```
[ ] 1. shared/constants/query-key/{domain}.query-key.ts
[ ] 2. entities/{domain}/ (domain, dto, adapter, mapper, types, schema, index)
[ ] 3. features/{domain}/ (service, hooks, index)
[ ] 4. widgets/{type}/{domain}/ (복합 UI)
[ ] 5. pages/{domain}/ ({Domain}Page.tsx, index)
[ ] 6. app/routes/{domain}.route.ts
[ ] 7. 테스트 및 검증
```

### Step 1: Query Key (`shared/constants/query-key/{domain}.query-key.ts`)

```typescript
export const {domain}QueryKeys = {
  all: () => ['{domain}'] as const,
  lists: () => [...{domain}QueryKeys.all(), 'list'] as const,
  list: (params: Record<string, unknown>) => [...{domain}QueryKeys.lists(), params] as const,
  details: () => [...{domain}QueryKeys.all(), 'detail'] as const,
  detail: (id: string) => [...{domain}QueryKeys.details(), id] as const,
};
```

### Step 2: Entity 생성

Domain, DTO, Model(중첩 구조만), Adap
