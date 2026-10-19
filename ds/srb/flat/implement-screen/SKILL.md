---
name: implement-screen
description: "Use when 화면 기획서와 Figma 디자인을 기반으로 FSD 구조의 프로덕션 코드를 생성하는 마스터 오케스트레이터. 화면 구현, 페이지 만들어줘, 화면 개발, Figma URL + screen spec으로 코드 생성 시 사용합니다. Do NOT use for 기획서만: covers implement, screen, fsd, spec, tds"
---

---
name: implement-screen
description: 화면 기획서와 Figma 디자인을 기반으로 FSD 구조의 프로덕션 코드를 생성하는 마스터 오케스트레이터. 화면 구현, 페이지 만들어줘, 화면 개발, Figma URL + screen spec으로 코드 생성 시 사용합니다. Do NOT use for 기획서만 작성(screen-description), Figma 분석만 수행(figma-to-tds), 또는 디자인 리뷰만 수행(design-review).
metadata:
  version: 1.1.0
  category: orchestrator
---

# Screen Implementation Orchestrator

화면 기획서(Screen Spec)와 Figma 디자인을 기반으로, FSD 구조의 프로덕션 코드를 생성하는 **마스터 워크플로우**. 개별 Skills를 올바른 순서로 체이닝한다.

## Input types

| 입력 | 소스 | 필수 |
|------|------|------|
| **도메인명** | 사용자 지정 (예: `workload`, `template`) | **필수** |
| **화면 기획서** | `docs/screens/{domain}/{screen}.md` | 권장 |
| **Figma URL** | `https://figma.com/design/...` | 선택 |
| **Swagger/API 명세** | URL 또는 문서 | 선택 |

---

## Workflow

### Phase 0 – 입력 수집 및 검증

```
Task Progress:
- [ ] Phase 0: 입력 수집 및 검증
- [ ] Phase 1: 화면 기획서 준비
- [ ] Phase 2: Figma 디자인 분석
- [ ] Phase 3: FSD 코드 생성
- [ ] Phase 4: i18n 다국어 처리
- [ ] Phase 5: 검증 및 마무리
```

1. **도메인명 확인** — 없으면 사용자에게 질문
2. **화면 기획서 확인** — `docs/screens/{domain}/` 경로에서 검색
3. **Figma URL 확인** — 사용자 입력에 URL 포함 여부 확인
4. **기존 코드 확인** — `src/pages/{domain}/`, `src/entities/{domain}/` 존재 여부

**분기 결정**:

| 기획서 | Figma | 행동 |
|--------|-------|------|
| ✅ | ✅ | Phase 2 → 3 → 4 → 5 |
| ✅ | ❌ | Phase 3 → 4 → 5 |
| ❌ | ✅ | Phase 1 → 2 → 3 → 4 → 5 |
| ❌ | ❌ | Phase 1 → 3 → 4 → 5 |

---

### Phase 1 – 화면 기획서 준비

> **Skill**: `screen-description`

기획서가 없거나 불완전한 경우에만 실행. Figma URL/Swagger URL이 있으면 해당 정보를 기획서에 반영.

**산출물**: `docs/screens/{domain}/{screen}.md`

---

### Phase 2 – Figma 디자인 분석

> **Skill**: `figma-to-tds`

Figma URL이 제공된 경우에만 실행. **코드 생성 없이** 분석 결과(컴포넌트 맵, 토큰 맵)만 다음 Phase로 전달.

**산출물** (메모리에 유지): Component Map + Token Map

---

### Phase 3 – FSD 코드 생성

> **Skill**: `fsd-development`
> **Rule**: `03-tds-essentials.mdc`(자동), `04-tds-detail-catalog.mdc`(상세), `07-table-patterns.mdc`

기획서 + Figma 분석 결과를 바탕으로 FSD 레이어 순서대로 코드 생성:

```
shared/constants/query-key → entities → features → widgets → pages → routes
```

**핵심 확인**
