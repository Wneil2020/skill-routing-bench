---
name: figma-to-tds
description: "Use when Figma 디자인을 TDS(@thakicloud/shared) 토큰과 컴포넌트로 변환하여 React TSX 코드를 생성합니다. Figma URL 제공 시, 피그마, Figma 구현, 디자인 변환, 레이아웃 구현, 단일 컴포넌트/섹션 구현 시 사용합니다. Do: covers figma, tds, tsx, thakicloud, shared"
---

---
name: figma-to-tds
description: Figma 디자인을 TDS(@thakicloud/shared) 토큰과 컴포넌트로 변환하여 React TSX 코드를 생성합니다. Figma URL 제공 시, 피그마, Figma 구현, 디자인 변환, 레이아웃 구현, 단일 컴포넌트/섹션 구현 시 사용합니다. Do NOT use for 전체 화면 구현 오케스트레이션(implement-screen), 디자인 리뷰(design-review), 또는 기획서 작성(screen-description).
metadata:
  version: 1.1.0
  category: execution
---

# Figma → TDS Code Generator

## Prerequisites

- Figma MCP server 연결 필수
- Figma URL 형식: `https://figma.com/design/:fileKey/:fileName?node-id=1-2`

## Workflow

### Step 0 – 화면 기획서 확인 (선택)

`docs/screens/{domain}/{screen}.md` 경로에서 기획서를 검색. 있으면 인터랙션 정의, 상태별 화면, 컴포넌트 구성 정보를 참고. 없으면 건너뜀.

### Step 1 – Figma URL 파싱 및 디자인 데이터 수집

1. URL에서 `fileKey`와 `nodeId` 추출
2. **반드시 두 MCP 도구를 병렬 호출**: `get_design_context` + `get_screenshot`
3. 응답이 truncated된 경우: `get_metadata`로 구조 파악 → 하위 노드별 개별 호출

### Step 2 – TDS 토큰 매핑

Figma 색상/간격/타이포그래피를 **TDS 시맨틱 토큰**으로 매핑. 상세 테이블은 [token-mapping.md](token-mapping.md) 참조.

**핵심 원칙**:
- Figma hex → 가장 가까운 시맨틱 색상 클래스
- `bg-blue-500` 같은 Tailwind 기본 색상 **절대 금지**
- `bg-primary/10` 같은 opacity modifier **절대 금지**
- 연한 배경 → `bg-success-light`, `bg-error-light`, `bg-warning-light`, `bg-info-light`, `bg-muted-light`
- `bg-primary-light`는 **존재하지 않음**

### Step 3 – TDS 컴포넌트 우선 매칭

| Figma 요소 | TDS 컴포넌트 |
|-----------|-------------|
| 버튼 | `Button` (variant, size, appearance) |
| 입력 필드 | `Input`, `Textarea`, `FormField` |
| 테이블 | `Table`, `SelectableTable` |
| 드롭다운 | `ContextMenu`, `Dropdown` |
| 모달/드로어 | `Overlay` (useOverlay 패턴) |
| 페이지네이션 | `Pagination` |
| 레이아웃 | `Layout.VStack`, `Layout.HStack`, `Layout.Block` |
| 텍스트 | `Typography.Heading`, `Typography.Text` |

TDS에 없는 요소만 시맨틱 토큰 + Tailwind로 직접 구현.

### Step 4 – 코드 생성

**전체 화면 구현** 시에는 `implement-screen` Skill의 Phase 3 사용 권장. 이 Step은 **단일 컴포넌트/섹션** 구현 시에 사용.

**코드 생성 규칙**:
- Arrow function 컴포넌트
- Props는 `interface` 사용
- 모든 텍스트 `t()` i18n 처리
- 시맨틱 컬러만 사용 (Tailwind 기본 색상 금지)
- TDS 컴포넌트 Props는 `04-tds-detail-catalog.mdc` 참조 (필수 규칙은 `03-tds-essentials.mdc` 자동 적용)

### Step 5 
