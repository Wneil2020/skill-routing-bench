---
name: "release-please-protection"
description: "Use when the task involves review code: covers release, please, protection, version, conventional"
---

# release-please-protection

Detects and prevents manual edits to release-please managed files (CHANGELOG.md,
version fields in package.json, pyproject.toml, Cargo.toml). Provides conventional
commit templates. Use when editing changelogs, version bumps, release files, or
when user mentions "release", "changelog", "version bump
