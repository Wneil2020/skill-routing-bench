---
name: notion-docs-sync
description: "Use when Markdown 문서를 Notion 페이지/DB에 동기화합니다. Notion 동기화, .notion-sync.yaml 설정, 문서를 Notion에 올려줘, Notion 연동, 문서 동기화 요청 시 사용합니다. Do NOT use for 화면 기획서: covers notion, docs, sync, yaml, screen"
---

---
name: notion-docs-sync
description: Markdown 문서를 Notion 페이지/DB에 동기화합니다. Notion 동기화, .notion-sync.yaml 설정, 문서를 Notion에 올려줘, Notion 연동, 문서 동기화 요청 시 사용합니다. Do NOT use for 화면 기획서 작성(screen-description), GitHub 이슈/PR 관리(github-workflow-automation).
metadata:
  version: 1.0.0
  category: execution
---

# Notion 문서 동기화

## 사전 요구사항

프로젝트에 `.notion-sync.yaml`이 없으면 사용자에게 배치할 폴더를 확인한 뒤(기본: 프로젝트 루트) **반드시** `init.sh`를 실행한다.

```bash
SKILL_DIR/scripts/init.sh <target-dir>
```

`init.sh`를 실행해야 하는 이유:
- `.notion-sync.yaml` 템플릿, `NOTION-SYNC.md`(Notion 제약 규칙)를 프로젝트에 복사한다. 이 파일들이 없으면 에이전트가 동기화 설정과 작성 규칙을 참조할 수 없다.
- `spec/`, `guide/` 디렉토리를 생성한다. 문서를 넣을 위치가 없으면 작업을 시작할 수 없다.
- `npm install`로 동기화 스크립트 의존성을 설치한다 (최초 1회). 설치하지 않으면 `sync.mjs` 실행이 실패한다.

요구사항: Node.js 18+

스크립트(`sync.mjs`)는 스킬 디렉토리에 있으며 프로젝트에 복사하지 않는다. `.notion-sync.yaml`의 `file` 경로는 yaml 파일 기준 상대경로이다.

## Notion 동기화

- `docs/` 디렉토리의 `.md` 파일을 `sync.mjs`를 통해 Notion에 동기화한다.
- 문서 메타데이터는 `.notion-sync.yaml`에서 관리한다.
- 동기화 시 페이지 내용을 `erase_content`로 초기화한 뒤 블록을 다시 추가한다.
- 두 가지 동기화 방식을 지원한다:
  - `databases` — Notion DB 소속 문서. `Sync ID`로 페이지를 검색하고, 없으면 새로 생성한다.
  - `pages` — 독립 페이지. `page_id`로 직접 콘텐츠를 동기화한다.

### .notion-sync.yaml 구조

```yaml
databases:
  - database_id: "<Notion DB ID>"
    pages:
      - file: spec/api-design.md
        title: "API 설계 규칙"
        Sync ID: spec-api-design
        Parent: ""

pages:
  - file: guide/quickstart.md
    page_id: "<Notion Page ID>"
```

필드:
- `file` — `docs/` 기준 상대 경로
- `title` — Notion 페이지 제목 (필수). 동기화 시 페이지 제목을 업데이트한다
- `Sync ID` — 고유 식별자. `{분류}-{이름}` 형식 (예: `spec-api-design`, `guide-setup`)
- `Parent` — 상위 문서의 Sync ID. 빈 문자열이면 최상위
- `page_id` — Notion 페이지 ID (`pages` 방식에서만 사용)

예시 설정 파일: [templates/.notion-sync.yaml](templates/.notion-sync.yaml)

### 동기화 실행

`SKILL_DIR`은 이 스킬의 디렉토리 경로이다.

`NOTION_TOKEN` 환경변수가 필요하다. 설정되어 있지 않으면 사용자에게 Notion Integration Token을 요청한다.

```bash
# 전체 동기화 (CWD에 .notion-sync.yaml이 있을 때)
node SKILL_DIR/scripts/sync.mjs

# yaml 경로 지정
node SKILL_DIR/script
