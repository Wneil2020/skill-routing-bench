---
name: jira-linear-adapter
description: "Use when Bidirectional sync adapter between GitHub Issues/Projects and Jira or Linear. Maps fields (status, priority, sprint, assignee) across: covers jira, linear, adapter, assignee, bidirectional"
metadata:
  holon-triggers: |
    sync with Jira
    sync with Linear
---

---
name: jira-linear-adapter
description: >-
  Bidirectional sync adapter between GitHub Issues/Projects and Jira or Linear.
  Maps fields (status, priority, sprint, assignee) across platforms, supports
  both cloud and server Jira, and maintains consistency. Use when the user
  asks to "sync with Jira", "sync with Linear", "Jira 연동", "Linear 동기화",
  "jira-linear-adapter", or needs cross-platform project management sync.
  Do NOT use for GitHub-only project management (use commit-to-issue),
  sprint triage (use sprint-orchestrator), or creating issues from commits
  (use commit-to-issue).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Jira/Linear Adapter

Bidirectional sync between GitHub Issues/Projects and enterprise project management tools (Jira, Linear).

## When to Use

- When enterprise teams use Jira/Linear but development happens on GitHub
- When cross-team visibility requires unified project tracking
- For Samsung and similar enterprises with established Jira workflows

## Supported Platforms

| Platform | API | Auth | Features |
|----------|-----|------|----------|
| Jira Cloud | REST v3 | API token / OAuth 2.0 | Full bidirectional sync |
| Jira Server/DC | REST v2 | Personal access token | Full bidirectional sync |
| Linear | GraphQL | API key | Full bidirectional sync |

## Field Mapping

### GitHub → Jira/Linear

| GitHub Field | Jira Field | Linear Field |
|-------------|------------|-------------|
| Issue title | Summary | Title |
| Issue body | Description | Description |
| Labels | Labels / Components | Labels |
| Assignees | Assignee | Assignee |
| Milestone | Fix Version | Cycle |
| Project Status | Status (mapped) | State (mapped) |
| Project Priority | Priority (mapped) | Priority (mapped) |
| Project Sprint | Sprint | Cycle |
| Project Size | Story Points | Estimate |

### Status Mapping (configurable)

| GitHub Status | Jira Status | Linear State |
|--------------|-------------|-------------|
| Backlog | To Do |
