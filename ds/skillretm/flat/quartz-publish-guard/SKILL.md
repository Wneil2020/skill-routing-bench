---
name: "quartz-publish-guard"
description: "Use when the task involves configure pipeline: covers quartz, publish, guard, purge, unpublish"
---

# quartz-publish-guard

Manage unpublished content in Quartz static site repos. Use when:
(1) User wants to prevent files without `publish: true` from being committed
(2) User asks about gitignoring based on frontmatter content
(3) User wants to unpublish a note or remove it from git
(4) User wants to purge files from git
