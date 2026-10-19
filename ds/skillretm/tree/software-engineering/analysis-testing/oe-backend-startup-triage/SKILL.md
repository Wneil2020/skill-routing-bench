---
name: "oe-backend-startup-triage"
description: "Use when the task involves debug api: covers backend, startup, triage, ports, bytecode"
---

# oe-backend-startup-triage

Debug âbackend wonât start / first request 500 / ports stuckâ quickly. Use when uvicorn reload behaves strangely, ports 8000/3000 are blocked, or you see first-request errors like âunexpected keyword argumentâ due to stale bytecode caches.
