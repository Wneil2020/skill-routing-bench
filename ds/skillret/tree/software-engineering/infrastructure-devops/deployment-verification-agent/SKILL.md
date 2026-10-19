---
name: "deployment-verification-agent"
description: "Use when the task involves deploy database: covers deployment, verification, agent, commentary, example"
---

# deployment-verification-agent

Use this agent when a PR touches production data, migrations, or any behavior that could silently discard or duplicate records. Produces a concrete pre/post-deploy checklist with SQL verification queries, rollback procedures, and monitoring plans. Essential for risky data changes where you need a Go
