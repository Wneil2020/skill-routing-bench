---
name: swagger-api-doc-generator
description: "Use when Swagger/OpenAPI URL에서 API 명세 문서를 Markdown으로 생성합니다. Swagger URL 제공 시, API 문서화 요청 시, 특정 API 그룹의 명세가 필요할 때 사용합니다. Do NOT use for 코드 생성(fsd-development): covers swagger, api, doc, openapi, fsd"
---

---
name: swagger-api-doc-generator
description: Swagger/OpenAPI URL에서 API 명세 문서를 Markdown으로 생성합니다. Swagger URL 제공 시, API 문서화 요청 시, 특정 API 그룹의 명세가 필요할 때 사용합니다. Do NOT use for 코드 생성(fsd-development), 화면 구현(implement-screen), 또는 화면 기획서 작성(screen-description).
metadata:
  version: 1.1.0
  category: generation
---

# Swagger API Documentation Generator

Swagger/OpenAPI JSON에서 깔끔한 Markdown API 문서를 생성합니다.

## 워크플로우

### Step 1: Swagger JSON 가져오기

```bash
curl -s {SWAGGER_URL} > /tmp/swagger-latest.json
wc -l /tmp/swagger-latest.json
```

### Step 2: API 그룹 확인

사용자가 특정 API를 지정하지 않은 경우, 사용 가능한 태그(그룹) 목록을 보여줌:

```bash
cat /tmp/swagger-latest.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
tags = data.get('tags', [])
for t in tags:
    print(f\"- {t.get('name')}: {t.get('description', '')}\")"
```

### Step 3: 대상 API 경로 추출

```bash
cat /tmp/swagger-latest.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
paths = data.get('paths', {})
keyword = '{KEYWORD}'
filtered = {k: v for k, v in paths.items() if keyword in k}
for path in sorted(filtered.keys()):
    for method in filtered[path].keys():
        summary = filtered[path][method].get('summary', '')
        print(f'{method.upper():7} {path}')
        print(f'        Summary: {summary}')"
```

### Step 4: 스키마 정의 추출

```bash
cat /tmp/swagger-latest.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
definitions = data.get('definitions', {})
keyword = '{KEYWORD}'
filtered = {k: v for k, v in definitions.items() if keyword in k.lower()}
for name in sorted(filtered.keys()):
    print(f'\n=== {name} ===')
    print(json.dumps(filtered[name], indent=2, ensure_ascii=False))"
```

### Step 5: Markdown 문서 생성

문서 저장 위치: `ai-platform/frontend/docs/api/{api-name}/{api-name}-api-spec.md`

상세 템플릿은 [templates.md](templates.md) 참조.

## 문서 구조

```markdown
# {API Name} API Specification

> **Source**: {swagger_url}

## 인증
## API 구조 개요
## 전체 Endpoints 목록
## 각 API 상세
- Request (Path/Query/Body)
- Resp
