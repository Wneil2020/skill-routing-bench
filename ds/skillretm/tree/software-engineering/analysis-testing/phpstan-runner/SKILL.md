---
name: "phpstan-runner"
description: "Use when the task involves analyze code: covers phpstan, runner, fix, errors, run"
---

# phpstan-runner

Run PHPStan static analysis and fix errors using intelligent agent delegation. Use when user requests to:
- Run static analysis
- Fix PHPStan errors
- Check code quality
- Analyze type errors
Delegates to runner agent (haiku) for execution and fixer agent (sonnet) for fixes.
Automatically cycles bet
