---
name: google-daily
description: "Use when Google Workspace 데일리 자동화, 캘린더 브리핑, Gmail 정리, Drive 업로드, Slack 알림(쓰레드 포함), 메모리 동기화를 순차 실행. /google, \"google daily\", \"구글 데일리\" 등으로 호출. 개별 작업은: covers google, daily, workspace, individual, drive"
---

---
name: google-daily
description: >-
  Google Workspace 데일리 자동화: 캘린더 브리핑, Gmail 정리, Drive 업로드, Slack 알림(쓰레드 포함), 메모리
  동기화를 순차 실행. /google, "google daily", "구글 데일리" 등으로 호출. 개별 작업은 해당 스킬 사용.
  Do NOT use for individual Google Workspace operations (use the specific gws-* skill).
metadata:
  author: "thaki"
  version: "3.0.0"
  category: "execution"
---
# Google Daily Automation

Google Workspace 일일 작업을 순차 파이프라인으로 실행하는 마스터 오케스트레이터.

> **Prerequisites**: `gws` CLI 설치 및 인증 (`gws auth login -s drive,gmail,calendar`). See `gws-workspace` skill.

## Pipeline

```
Calendar → Gmail Triage → Drive Upload → Slack Notify (+ threads) → Memory Sync
```

## Slack Configuration

| Key | Value |
|-----|-------|
| Channel | `#효정-할일` |
| Channel ID | `C0AA8NT4T8T` |
| Decision (Personal) | `#효정-의사결정` |
| Decision (Personal) ID | `C0ANBST3KDE` |
| Decision (Team) | `#7층-리더방` |
| Decision (Team) ID | `C0A6Q7007N2` |

All Slack messages go to `#효정-할일`. Decision items go to their respective channels. Never use DM.

## Phase 1 -- Calendar Briefing

`.cursor/skills/calendar-daily-briefing/SKILL.md` 실행.

```bash
gws calendar +agenda --today
```

1. 이벤트 분류: 면접(HIGH), 외부미팅(HIGH), 팀미팅(MEDIUM), 집중시간(LOW)
2. 한국어 브리핑 생성 + 준비 알림
3. 집중 가능 시간대 계산 (09:00-18:00 기준, 30분 이상 공백)

## Phase 2 -- Gmail Triage

`.cursor/skills/gmail-daily-triage/SKILL.md` 실행.

1. "Low Priority" 라벨 확인/생성
2. 어제 메일 조회: `gws gmail +triage --max 50 --query "after:YYYY/MM/DD before:YYYY/MM/DD" --labels --format json`
3. 분류 및 처리:

| Category | Sender Pattern | Action |
|----------|---------------|--------|
| Spam | 광고, 마케팅 | `messages trash` |
| Notification | Notion, RunPod, GitHub, NotebookLM, Calendar | `messages modify` → Low Priority |
| News | bespin_news@bespinglobal.com | 링크 추출 → 기사 요약 → docx 생성 → AI/GPU Cloud 인사이트 |
| Colleague | @thakicloud.co.kr, @bespinglobal.com | 요약 + 답변 초안 작성 (첨부 있으면 첨부도 요약) |
| Reply Needed | 직접 수신 + 미답장 | 요약 + 액션아이템 → docx 생성 |

4. 생성 문서: `/tmp/reply-needed-YYYY-MM-DD.docx`, `/tmp/bespin-news-YYYY-
