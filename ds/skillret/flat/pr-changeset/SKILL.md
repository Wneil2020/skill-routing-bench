---
name: "pr-changeset"
description: "Use when the task involves generate pipeline: covers changeset, package, changes, minor, requested."
---

# pr-changeset

Create changesets for package changes in pull requests. Use whenever you modify code in any package (packages/*). Required before committing changes to packages. Handles versioning with patch for bug fixes, minor for features, and major only when explicitly requested.
