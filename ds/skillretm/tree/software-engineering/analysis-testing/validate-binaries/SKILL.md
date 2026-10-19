---
name: "validate-binaries"
description: "Use when the task involves analyze code: covers validate, binaries, instruction, avx-512, contamination."
---

# validate-binaries

Validate voxtype binaries for CPU instruction contamination. Use when checking release binaries for AVX-512 or GFNI instruction leaks that would crash on older CPUs.
