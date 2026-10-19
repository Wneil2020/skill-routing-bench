---
name: pm-sentinel
description: "Use when Autonomous PM loop that continuously researches, monitors, and improves the project using a YAML state DB and CLI validation gates. Wakes: covers sentinel, 자율 PM, 무한 루프, exploit, forced"
metadata:
  holon-triggers: |
    start sentinel
    pm sentinel
---

---
name: pm-sentinel
description: >-
  Autonomous PM loop that continuously researches, monitors, and improves the
  project using a YAML state DB and CLI validation gates. Wakes hourly via
  Cursor Automation, picks the next highest-priority mission, executes it
  with evidence-based completion (rejects "done" without proof), and outputs
  forced reminders to exploit LLM recency bias. Composes 12+ existing skills
  across 7 mission domains. Use when the user asks to "start sentinel",
  "pm sentinel", "autonomous loop", "continuous improvement", "무한 루프",
  "자율 PM", "sentinel status", "sentinel report", "seed missions",
  "heartbeat", or wants the project to improve itself without prompting.
  Do NOT use for single-task execution (invoke the specific skill directly),
  interactive debugging (use diagnose), or one-off code review (use simplify
  or deep-review). Korean triggers: "자율 PM", "무한 루프", "센티넬",
  "프로젝트 자동 개선", "하트비트".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "orchestration"
---

# PM Sentinel — Autonomous Project Improvement Loop

An enterprise-grade autonomous PM system that uses YAML state DB + CLI validation gates to ensure AI agents continuously research, improve, and grow the project without human prompting. The CLI enforces evidence-based completion — the AI cannot claim a task is done without providing specific proof.

## Architecture

```
Trigger (hourly cron / manual)
    │
    ▼
CLI: pm-sentinel-cli.py
    │
    ├── Reads sentinel-state.yaml (YAML state DB)
    ├── Resolves next action (priority + dependency ordering)
    ├── Validates evidence (rejects incomplete/empty)
    ├── Updates state atomically
    └── Outputs reminder block (NEXT + WARN + 2 random tips)
         │
         ▼
    Agent executes mission phases using existing skills
         │
         ▼
    CLI validates evidence → updates state → next phase
```

## Prerequisites

- Python 3.10+ with PyYAML (`pip install pyyaml`)
- All files in `.cursor/sentinel/` director
