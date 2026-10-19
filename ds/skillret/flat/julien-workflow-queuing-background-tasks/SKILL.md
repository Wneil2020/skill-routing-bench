---
name: "julien-workflow-queuing-background-tasks"
description: "Use when the task involves orchestrate pipeline: covers julien, workflow, queuing, background, tasks"
---

# julien-workflow-queuing-background-tasks

Queue long-running tasks (transcoding, API calls, batch processing) to run in background at low priority when user is active, normal priority when idle. Use when scripts take minutes/hours and shouldn't impact PC performance during active use.
