---
name: "external-system-safety"
description: "Use when the task involves orchestrate agent_skill: covers external, system, safety, confirmation, linear"
---

# external-system-safety

Enforces confirmation workflow for EXTERNAL system writes (Jira, Confluence, BitBucket, Slack) ONLY. NEVER activates for Linear operations (Linear is internal tracking). Auto-activates when detecting potential writes to external PM systems (status updates, page creation, PR posts, notifications). Bl
