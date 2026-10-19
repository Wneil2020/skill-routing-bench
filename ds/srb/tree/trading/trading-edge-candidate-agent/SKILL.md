---
name: trading-edge-candidate-agent
description: "Use when Generate and prioritize US equity long-side edge research tickets from EOD observations, then export pipeline-ready candidate specs for: covers trading, edge, candidate, finder, observations"
metadata:
  holon-triggers: |
    convert hypotheses to research tickets
    discover edge candidates
---

---
name: trading-edge-candidate-agent
description: >-
  Generate and prioritize US equity long-side edge research tickets from EOD observations,
  then export pipeline-ready candidate specs for trade-strategy-pipeline Phase I.
  Use when the user asks to "convert hypotheses to research tickets", "discover edge candidates",
  "export strategy.yaml", "validate edge-finder-candidate", "에디지 후보 생성", "리서치 티켓 변환", or wants to turn anomalies into reproducible research tickets.
  Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for AlphaEar signal tracking (use alphaear-signal-tracker).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: research
  source: claude-trading-skills
  api_required: none
---

# Edge Candidate Agent

## Overview

Convert daily market observations into reproducible research tickets and Phase I-compatible candidate specs.
Prioritize signal quality and interface compatibility over aggressive strategy proliferation.
This skill can run end-to-end standalone, but in the split workflow it primarily serves the final export/validation stage.

## When to Use

- Convert market observations, anomalies, or hypotheses into structured research tickets.
- Run daily auto-detection to discover new edge candidates from EOD OHLCV and optional hints.
- Export validated tickets as `strategy.yaml` + `metadata.json` for `trade-strategy-pipeline` Phase I.
- Run preflight compatibility checks for `edge-finder-candidate/v1` before pipeline execution.

## Prerequisites

- Python 3.9+ with `PyYAML` installed.
- Access to the target `trade-strategy-pipeline` repository for schema/stage validation.
- `uv` available when running pipeline-managed validation via `--pipeline-root`.

## Output

- `strategies/<candidate_id>/strategy.yaml`: Phase I-compatible strategy spec.
- `strategies/<candidate_id>/metadata.json`: provenance metadata including interface version and ticket context.
- Validation status from `scripts/validate_candidate.py` (pass/fail 
