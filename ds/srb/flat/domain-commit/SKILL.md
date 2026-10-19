---
name: domain-commit
description: "Use when Run pre-commit hooks, fix lint errors, and create domain-split git commits from uncommitted changes. Use when the user asks to commit local changes: covers domain, commit, 커밋, 생성, trivial"
metadata:
  holon-triggers: |
    commit my changes
    domain commit
---

---
name: domain-commit
description: >-
  Run pre-commit hooks, fix lint errors, and create domain-split git commits
  from uncommitted changes. Use when the user asks to commit local changes, run
  pre-commit, split commits by domain, clean up the working directory, or says
  "commit my changes", "domain commit", "split commits". Do NOT use for
  single-file trivial commits, git push/pull/merge operations, or branch
  management. Korean triggers: "커밋", "생성", "수정".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "execution"
---
# Domain-Split Commit

Automates the full pre-commit + lint-fix + domain-split commit workflow for this project.

## Prerequisites

- Pre-commit hooks installed (`.pre-commit-config.yaml`)
- Commit message format per `CONTRIBUTING.md`: `[TYPE] Summary` (50 char max, English imperative)

## Workflow

### Step 1: Analyze uncommitted changes

```bash
git status --short | wc -l
git status --short | sort
```

If working directory is clean, stop and inform the user.

### Step 2: Categorize files into domains

Group files by directory prefix into commit batches. For the full domain-to-path mapping and commit type assignments, see [references/hooks-and-domains.md](references/hooks-and-domains.md).

Skip empty domains. Combine small domains if fewer than 3 files.

### Step 3: Commit each domain

For each domain batch:

1. **Stage**: `git add <files>`
2. **Commit** with HEREDOC message:

```bash
git commit -m "$(cat <<'EOF'
[TYPE] English summary (max 50 chars)

- Korean or English detail bullet 1
- Korean or English detail bullet 2
EOF
)"
```

3. **If pre-commit fails**:
   - `git reset HEAD <files>` to unstage
   - Read the error output and identify the failing hook
   - For hook-specific remediation steps, see [references/hooks-and-domains.md](references/hooks-and-domains.md)
   - Re-stage and commit again (new commit, never amend failed commits)

4. **If pre-commit modifies files** (black/ruff auto-fix): add modified files and create a n
