---
name: design-review
description: "Use when 구현된 코드를 Figma 디자인 및 화면 기획서와 대조하여 시각적 일치도, 기능 커버리지, 품질 표준을 검증합니다. 디자인 리뷰, 피그마 비교, 구현 검증, design review, compare with Figma, implement-screen 완료 후: covers design, review, fsd, tds, figma"
---

---
name: design-review
description: 구현된 코드를 Figma 디자인 및 화면 기획서와 대조하여 시각적 일치도, 기능 커버리지, 품질 표준을 검증합니다. 디자인 리뷰, 피그마 비교, 구현 검증, design review, compare with Figma, implement-screen 완료 후 사용합니다. Do NOT use for 코드 생성(fsd-development, implement-screen), Figma 분석(figma-to-tds), 또는 기획서 작성(screen-description).
metadata:
  version: 1.1.0
  category: review
---

# Design Review

구현된 코드를 Figma 디자인 및 화면 기획서(Screen Spec)와 대조하여 **시각적 일치도**, **기능 커버리지**, **품질 표준 준수**를 검증한다.

## Inputs

| 입력 | 소스 | 필수 |
|------|------|------|
| **구현 파일 경로** | `src/pages/{domain}/`, `src/widgets/` 등 | **필수** |
| **Figma URL** | `https://figma.com/design/...` | 선택 |
| **Screen Spec** | `docs/screens/{domain}/{screen}.md` | 선택 |
| **도메인명** | 사용자 지정 | **필수** |

하나 이상의 비교 기준(Figma 또는 Screen Spec)이 있어야 유의미한 리뷰가 가능.

---

## Workflow

### Step 1 – 컨텍스트 수집

**병렬로 수집**:
1. **구현 코드**: pages, widgets, entities, features 관련 파일
2. **Figma 데이터** (URL 있을 때): `get_design_context` + `get_screenshot`
3. **Screen Spec** (있을 때): `docs/screens/{domain}/{screen}.md`
4. **i18n 파일**: `en/{domain}.json` + `ko/{domain}.json`

### Step 2 – 시각적 일치 검증 (Figma 있을 때)

| 검증 항목 | 심각도 |
|-----------|--------|
| 레이아웃 구조 (flex, 영역 배치) | Critical |
| 간격 (gap, padding → TDS 토큰) | Critical |
| 색상 (시맨틱 토큰 매핑) | Critical |
| 타이포그래피 (폰트 크기, 굵기) | Major |
| 컴포넌트 매핑 (Figma → TDS) | Critical |
| 아이콘 | Major |

### Step 3 – 기능 커버리지 검증 (Screen Spec 있을 때)

- **인터랙션 정의**: 모든 트리거/동작/결과가 구현됨
- **상태별 화면**: 로딩/빈 상태/에러/정상 모두 처리됨
- **API 연동**: 모든 엔드포인트가 Adapter에 정의, Query/Mutation 훅 연결됨

### Step 4 – 품질 표준 검증

**항상 수행** (Figma/Spec 없어도):

- **TDS 컴포넌트**: 동등한 TDS 컴포넌트가 있는데 직접 구현 → Critical
- **스타일링**: Tailwind 기본 색상(`bg-blue-500`), 하드코딩 hex, opacity modifier → Critical
- **i18n**: 하드코딩 텍스트 → Critical, en/ko 불일치 → Critical
- **FSD 아키텍처**: 역방향 의존/형제 import → Critical
- **TypeScript**: `npx tsc --noEmit` 에러 0
- **코드 컨벤션**: `any` 타입 → Critical, `!!` 사용 → Major

### Step 5 – 리포트 생성

```markdown
## Design Review Report

### Summary
- Critical: {N}건
- Major: {N}건

