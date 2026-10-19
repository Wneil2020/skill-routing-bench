---
name: fe-pipeline
description: "Use when 자연어 한 줄부터 Swagger+Figma 풀세트까지, 프로젝트 내 API·화면 패턴을 자동 발견하여 기획서·Entity·Feature/Widget/Page·i18n·검증을 체크포인트 기반으로 자동 진행합니다. 새 화면 생성뿐 아니라 기존 화면: covers pipeline, widget, swagger, entity, i18n"
metadata:
  holon-triggers: |
    UI 변경 요청 시
---

---
name: fe-pipeline
description: "자연어 한 줄부터 Swagger+Figma 풀세트까지, 프로젝트 내 API·화면 패턴을 자동 발견하여 기획서·Entity·Feature/Widget/Page·i18n·검증을 체크포인트 기반으로 자동 진행합니다. 새 화면 생성뿐 아니라 기존 화면 수정/버그픽스도 기획서 대조 기반으로 처리합니다. Use when 화면 구현해줘, 페이지 만들어줘, 화면 개발, 새 화면 추가, 기존 화면 수정, 버그 수정, UI 변경 요청 시. Do NOT use for 개별 스킬 단독 작업 — API 문서만(swagger-api-doc-generator), 기획서만(screen-description), Figma 분석만(figma-to-tds), 디자인 리뷰만(design-review), Entity만(fsd-development)."
metadata:
  version: "2.0.0"
  category: orchestrator
---

# Frontend Pipeline

자연어 한 줄 → 요청 분류 → 기획서 대조 → 자동 발견 → Entity → Code → i18n → 검증. 체크포인트 기반 자동 진행.

## Inputs

| 입력                          | 필수     | 비고                                           |
| ----------------------------- | -------- | ---------------------------------------------- |
| **도메인명 또는 자연어 설명** | **필수** | `"벤치마크 목록 화면 만들어줘"` 한 줄이면 충분 |
| Swagger URL                   | 선택     | 없으면 프로젝트 내 swagger.json 자동 탐색      |
| Figma URL                     | 선택     | 없으면 기존 유사 화면 패턴으로 대체            |
| 기획서 경로                   | 선택     | 없으면 자동 생성                               |

## Request Classification (최우선)

**모든 요청은 먼저 유형을 분류**한 뒤, 유형에 맞는 플로우를 따른다.

| 유형              | 판단 기준                                      | 플로우                      |
| ----------------- | ---------------------------------------------- | --------------------------- |
| **New Screen**    | "화면 만들어줘", "페이지 추가", 새 도메인      | Full Pipeline (Phase 0 → 7) |
| **Modification**  | "수정해줘", "버그", "추가해줘", 기존 화면 변경 | Modification Flow           |
| **Design Update** | "Figma 업데이트", "디자인 변경" + Figma URL    | Design Update Flow          |

---

## Design Update Flow (Figma 디자인 업데이트)

Figma 디자인이 변경되었을 때, 기존 코드와 기획서를 새 디자인에 맞게 갱신하는 플로우.

```
1. Spec Check ─── docs/screens/{domain}/ 기획서 존재 확인
   ├─ 기획서 있음 → 읽기 → Step 2로
   └─ 기획서 없음 → 기획서 자동 생성:
       1) 기존 코드(pages/{domain}/, widgets/)에서 구조 파악
       2) screen-description 스킬로 기획서 생성
       3) 사용자 알림: "기획서가 없어서 코드 기반으로 생성했습니다."
2. Figma 재분석 ── Phase 3(figma-
