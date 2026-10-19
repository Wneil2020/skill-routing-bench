---
name: local
description: "Use when the request concerns the local category of skills: covers local"
---

Grouping node for the 0 skills of the local category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **local-dev-runner** (`local-dev-runner/`): Use when Start, stop, and manage the full local development environment on macOS. Use when the user asks to run the project locally, start/stop services, or: covers local, dev, runner, 리뷰, diagnosing
- **local-dev-setup** (`local-dev-setup/`): Use when Go 백엔드 로컬 개발 환경을 자동 설정합니다. Docker DB/NATS 생성, 마이그레이션 적용, 시드 데이터, RSA 키 생성, 인프라 포트포워딩, .env 업데이트를 순차 수행합니다. 로컬 개발 환경, 로컬 셋업, backend 셋업, 환경 구성, 개발 환경 준비: covers local, dev, setup, nats, rsa

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
