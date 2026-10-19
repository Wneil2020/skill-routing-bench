---
name: "run-tests"
description: "Use when the task involves test test_suite: covers run, tests, checkpoint_index, docker., eval-snapshot"
---

# run-tests

Run problem tests using eval-snapshot instead of raw pytest. Use this to evaluate solutions against benchmark tests in Docker. Invoke with /run-tests <snapshot_path> <problem_name> <checkpoint_index>.
