---
name: "ln-622-build-auditor"
description: "Use when the task involves analyze pipeline: covers build, auditor, errors, deprecation, linter"
---

# ln-622-build-auditor

Build health audit worker (L3). Checks compiler/linter errors, deprecation warnings, type errors, failed tests, build configuration issues. Returns findings with severity (Critical/High/Medium/Low), location, effort, and recommendations.
