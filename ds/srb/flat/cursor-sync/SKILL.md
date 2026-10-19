---
name: cursor-sync
description: "Use when N-repo bidirectional sync of .cursor/ assets (commands, skills, rules) across all 5 ThakiCloud repositories. Research acts as the merge hub, pull: covers cursor, sync, absorbs, acts, newest"
metadata:
  holon-triggers: |
    sync skills
    sync commands across projects
---

---
name: cursor-sync
description: >-
  N-repo bidirectional sync of .cursor/ assets (commands, skills, rules) across
  all 5 ThakiCloud repositories. Research acts as the merge hub: pull phase
  absorbs changes from all 4 target repos using newest-wins (-u flag), then
  push phase distributes the merged result to all targets. Any .cursor/ change
  in any repo propagates to all others in one run. Use when the user runs
  /cursor-sync, asks to "sync skills", "sync commands across projects", or
  "push cursor config to other repos". Do NOT use for syncing non-.cursor
  files, deploying code, or general file copy operations.
metadata:
  author: thaki
  version: 2.0.0
---

# Cursor Sync — N-Repo .cursor/ Asset Synchronization

Research는 5개 레포의 `.cursor/` 에셋 **머지 허브**입니다. 5개 레포 중 어디서 변경이 발생하든, research에서 `/cursor-sync`를 한 번 실행하면 모든 레포에 전파됩니다.

- **Pull Phase**: 4개 타겟 레포 → research (`rsync -au`, 최신 파일 우선)
- **Push Phase**: research → 4개 타겟 레포 (`rsync -ac`, checksum 기반)

## 흐름 다이어그램

```
[github-to-notion-sync]        ─┐
[ai-platform-webui]            ─┼─ rsync -au ──▶ [research] ─── rsync -ac ──▶ [github-to-notion-sync]
[ai-model-event-stock-analytics]─┤  (Pull Phase)   (허브)    (Push Phase)     [ai-platform-webui]
[ai-template]                  ─┘                                             [ai-model-event-stock-analytics]
                                                                              [ai-template]
```

## Platform Note: macOS openrsync

macOS에 내장된 `/usr/bin/rsync`는 **openrsync** (protocol v29) 이며, GNU rsync와 다릅니다:

- `-i` (itemize-changes): `>f+++++++` 형태의 per-file 출력을 하지 않음
- `-v` (verbose): 개별 전송 파일 목록을 출력하지 않음
- `--dry-run`: 변경 파일 목록을 보여주지 않음 (바이트 요약만 출력)

따라서 이 스킬은 **`comm` 기반 diff 비교**로 새 파일을 감지하고, rsync는 **전송 전용**으로만 사용합니다.

## Configuration

- **Hub (source of truth after merge)**: `/Users/hanhyojung/thaki/research/.cursor/`
- **Sync directories**: `commands/`, `skills/`, `rules/`
- **Target projects**: See [references/sync-targets.md](references/sy
