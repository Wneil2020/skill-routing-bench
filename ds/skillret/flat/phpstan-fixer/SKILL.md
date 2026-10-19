---
name: "phpstan-fixer"
description: "Use when the task involves debug code: covers phpstan, fixer, errors, logs, says"
---

# phpstan-fixer

Analyze existing PHPStan error logs without running analysis. Use when:
- User says "fix the phpstan errors" (after manually running PHPStan)
- User says "what phpstan errors do I have?"
- User points to specific log file
- PHPStan was run outside Claude's context
Delegates to fixer agent (sonnet) t
