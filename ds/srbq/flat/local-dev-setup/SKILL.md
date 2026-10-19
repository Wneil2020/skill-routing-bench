---
name: local-dev-setup
description: "Use when Go 백엔드 로컬 개발 환경을 자동 설정합니다. Docker DB/NATS 생성, 마이그레이션 적용, 시드 데이터, RSA 키 생성, 인프라 포트포워딩, .env 업데이트를 순차 수행합니다. 로컬 개발 환경, 로컬 셋업, backend 셋업, 환경 구성, 개발 환경 준비: covers local, dev, setup, nats, rsa"
---

---
name: local-dev-setup
description: Go 백엔드 로컬 개발 환경을 자동 설정합니다. Docker DB/NATS 생성, 마이그레이션 적용, 시드 데이터, RSA 키 생성, 인프라 포트포워딩, .env 업데이트를 순차 수행합니다. 로컬 개발 환경, 로컬 셋업, backend 셋업, 환경 구성, 개발 환경 준비, 로컬 실행 요청 시 사용합니다. Do NOT use for 프론트엔드 개발 환경 설정이나 K8s 클러스터 배포.
---

# Local Development Setup

Go 백엔드(`ai-platform/backend/go`) 로컬 개발 환경 자동 설정.

## Prerequisites

| 도구 | 필수 | 용도 |
|------|------|------|
| `docker` | 항상 | PostgreSQL, NATS 컨테이너 |
| `openssl` | 항상 | RSA 키 생성 |
| `make` | 항상 | 마이그레이션, 서버 실행 |
| `migrate` | 자동 설치 | DB 마이그레이션 CLI |
| `kubectl` | full 모드만 | 포트포워딩 |

## Workflow Checklist

```
- [ ] Step 0: 사용자 입력 수집
- [ ] Step 1: Docker 컨테이너 (PostgreSQL + NATS)
- [ ] Step 2: DB 마이그레이션
- [ ] Step 3: 시드 데이터
- [ ] Step 4: RSA 키 생성
- [ ] Step 5: 포트포워딩 (full 모드)
- [ ] Step 5b: S3 크리덴셜 조회 (full 모드)
- [ ] Step 6: .env 업데이트
```

---

## Step 0: 사용자 입력 수집

AskQuestion 2개로 셋업 모드를 결정합니다.

**Question 1 — 셋업 모드:**

| id | prompt | options |
|----|--------|---------|
| `setup-mode` | 셋업 모드를 선택하세요 | `local-only`: DB + NATS만 (K8s 불필요) / `full`: 원격 K8s 클러스터 연동 포함 |

**Question 2 — KUBECONFIG 경로 (full 모드만):**

| id | prompt | options |
|----|--------|---------|
| `kubeconfig` | KUBECONFIG 파일 경로 | `~/tkai-local.config` / `~/.kube/config` / `직접 입력` |

"직접 입력" 선택 시 자연어로 경로를 재질문합니다.

**Question 3 — K8s 네임스페이스 (full 모드만):**

| id | prompt | options |
|----|--------|---------|
| `namespace` | S3 크리덴셜을 가져올 K8s 네임스페이스 | `ai-platform-stage` / `ai-platform-prod` / `직접 입력` |

"직접 입력" 선택 시 자연어로 네임스페이스를 재질문합니다.

---

## Step 1: Docker 컨테이너

Working directory: 프로젝트 루트

### PostgreSQL

```bash
docker inspect -f '{{.State.Status}}' ai-platform-database 2>/dev/null || echo 'missing'
```

| 출력 | 액션 |
|------|------|
| `missing` | `docker run -d --name ai-platform-database -e POSTGRES_PASSWORD=password -e POSTGRES_DB=ai_platform_db -p 5432:5432 postgres:15-alpine` |
| `exited` | `docker start ai-platform-database` |
| `running` | 스킵 |

### NATS

```bash
docker inspect -f '{{.State.Status}}' ai-platform-n
