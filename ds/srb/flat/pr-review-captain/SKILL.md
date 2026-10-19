---
name: pr-review-captain
description: "Use when Summarize pull request changes, assess risks, generate review checklists, and produce release notes. Use when the user asks for a PR summary: covers review, captain, 리뷰, 생성, checklists"
metadata:
  holon-triggers: |
    a PR summary
    change risk assessment
---

---
name: pr-review-captain
description: >-
  Summarize pull request changes, assess risks, generate review checklists, and
  produce release notes. Use when the user asks for a PR summary, change risk
  assessment, review checklist, or release note generation. Do NOT use for
  committing local changes (use domain-commit) or writing ADR/operational
  documentation (use technical-writer). Korean triggers: "리뷰", "생성", "체크", "커밋".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# PR Review Captain

Coordinate code reviews and release documentation for pull requests. Works alongside the existing PR commands (`pr-review.md`, `pr-create.md`).

## Change Summary

When reviewing a PR, produce a concise summary:

1. **Read the diff** using `gh pr diff <number>` or `git diff <base>...HEAD`
2. **Categorize changes** by type:
   - Feature (new functionality)
   - Enhancement (improvement to existing)
   - Bug fix
   - Refactor (no behavior change)
   - Infrastructure / config
   - Documentation
3. **Identify affected services** from file paths (`services/<name>/`)
4. **Note migration/schema changes** if any files in `db/migrations/` are modified

## Risk Assessment

### Risk Matrix

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Scope | Single file/function | Multiple files in one service | Multiple services |
| Data | No schema changes | Additive migration | Destructive migration |
| Security | No auth/PII changes | Auth logic modified | New auth flow / PII handling |
| Dependencies | No dep changes | Patch/minor updates | Major version bump |
| Reversibility | Easily reverted | Needs coordination | Requires data migration to revert |

### Assessment Process

1. Score each factor (1=Low, 2=Medium, 3=High)
2. Overall risk = max(individual scores)
3. If overall >= High, recommend phased rollout or feature flag

## Review Checklist

Generate a checklist tailored to the PR content:

### Always Check

- [ ] PR title follows format: `#<IS
