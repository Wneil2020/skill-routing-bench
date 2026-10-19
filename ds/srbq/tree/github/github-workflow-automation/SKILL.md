---
name: github-workflow-automation
description: "Use when ai-platform-webui 레포지토리의 GitHub 워크플로우를 자동화합니다. 변경사항 확인, 이슈 생성, 브랜치 생성, 커밋, 푸시, PR 생성/업데이트, 이슈 코멘트까지 전체 흐름 처리. 이슈 만들어줘, 커밋해줘, PR 생성해줘, 변경사항: covers github, automation, webui, fsd, implement"
---

---
name: github-workflow-automation
description: ai-platform-webui 레포지토리의 GitHub 워크플로우를 자동화합니다. 변경사항 확인, 이슈 생성, 브랜치 생성, 커밋, 푸시, PR 생성/업데이트, 이슈 코멘트까지 전체 흐름 처리. 이슈 만들어줘, 커밋해줘, PR 생성해줘, 변경사항 정리해줘, 깃 워크플로우 요청 시 사용합니다. Do NOT use for 코드 생성(fsd-development), 화면 구현(implement-screen), Notion 문서 동기화(notion-docs-sync), 또는 디자인 리뷰(design-review).
metadata:
  version: 1.1.0
  category: execution
---

# GitHub 워크플로우 자동화

## 워크플로우 개요

```
변경사항 확인 → 적합한 브랜치인가?
    ├── YES (issue/XXX 브랜치) → Step C → Step D
    └── NO → Step A → Step B → Step D
```

상세 명령어: [references/workflow-commands.md](references/workflow-commands.md)

---

## Step 0: 현재 상태 확인

```bash
git branch --show-current  # 브랜치
git status                 # 변경사항
git log --oneline -5       # 히스토리
```

**분기**:
- `issue/{NUMBER}-{SUMMARY}` → 기존 이슈 브랜치 → **Step C**
- `dev`, `main`, 기타 → **Step A**

## Step A: 이슈 생성

1. `gh issue create --title "..." --body "..." --assignee @me`
2. `gh project item-add 5 --owner ThakiCloud --url [이슈URL]`
3. 프로젝트 필드 설정 (Priority/Size/Estimate/Sprint)

**필드 규칙**:
- **Priority**: P0 (기본), Epic 하위면 상속
- **Size**: XS/S/M/L/XL (변경 규모 기반)
- **Estimate**: 피보나치 (0.5~8), 1일 = 1 기준
- **Sprint**: 오늘 날짜 기준 현재 활성 스프린트

상세 GraphQL: [references/workflow-commands.md](references/workflow-commands.md) Step A 참조

## Step B: 브랜치 생성

```bash
git checkout dev && git pull origin dev
git checkout -b issue/{ISSUE_NUMBER}-{summary}
```

## Step C: 이슈 업데이트 (기존 브랜치)

브랜치명에서 이슈 번호 추출 → `gh issue view` → 변경사항 반영 → `gh issue edit`

## Step D: Pre-commit → 커밋 → 푸시 → PR

### D-0. Pre-commit (필수)

```bash
pre-commit run --all-files
# 실패 → git add . → 재실행 반복. 통과까지 커밋 금지.
```

### D-1. 커밋

**형식**: `<type>: <summary>` (50자 이내, 영어 소문자 명령문, 마침표 없음)

| 타입 | 설명 |
|------|------|
| `feat` | 새 기능 | `fix` | 버그 수정 | `docs` | 문서 | `refactor` | 리팩토링 |
| `style` | 포맷팅 | `perf` | 성능 | `test` | 테스트 | `chore` | 기타 |

scope 선택: `auth`, `api`, `ui`, `kfp`, `storage`, `inference`, `ml-studio`, `pipeline`

### D-2. 푸시

`git push -u origin $(git bra
