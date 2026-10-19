---
name: "create-worktree"
description: "Use when the task involves configure project: covers create, worktree, ado, branch, slug"
---

# create-worktree

Create a new git branch and worktree from context. Use when starting work on a task - given an ADO Work Item URI, ADO comment, or freetext description, auto-selects branch prefix (feature/bugfix/experiment) based on context, creates branch like feature/<username>/<slug>, and sets up worktree at ../<
