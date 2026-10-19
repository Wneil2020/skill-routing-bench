---
name: "phpunit-runner"
description: "Use when the task involves test test_suite: covers phpunit, runner, tests, fix, run"
---

# phpunit-runner

Run PHPUnit tests and fix failures using intelligent agent delegation. Use when user requests to:
- Run tests (full suite, specific path, or single file)
- Fix failing tests
- Analyze test failures
- Check test coverage
Delegates to runner agent (haiku) for execution and fixer agent (sonnet) for fix
