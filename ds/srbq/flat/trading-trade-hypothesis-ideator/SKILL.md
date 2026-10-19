---
name: trading-trade-hypothesis-ideator
description: "Use when Generate falsifiable trade strategy hypotheses from market data, trade logs, and journal snippets. Use when the user asks to: covers trading, trade, hypothesis, falsifiable, ideator"
metadata:
  holon-triggers: |
    generate trade hypotheses
    rank hypothesis cards
---

---
name: trading-trade-hypothesis-ideator
description: >-
  Generate falsifiable trade strategy hypotheses from market data, trade logs,
  and journal snippets. Use when the user asks to "generate trade hypotheses",
  "rank hypothesis cards", "strategy experiment design", "kill criteria for trades",
  "가설 카드 생성", "트레이드 가설", "실험 설계", or has structured input and wants ranked hypothesis cards with experiment designs and optional strategy.yaml export.
  Do NOT use for strategy backtesting (use trading-backtest-expert). Do NOT use for daily signals (use daily-stock-check).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: research
  source: claude-trading-skills
  api_required: none
---

# Trade Hypothesis Ideator

Generate 1-5 structured hypothesis cards from a normalized input bundle, critique and rank them, then optionally export `pursue` cards into `strategy.yaml` + `metadata.json` artifacts.

## Workflow

1. Receive input JSON bundle.
2. Run pass 1 normalization + evidence extraction.
3. Generate hypotheses with prompts:
   - `prompts/system_prompt.md`
   - `prompts/developer_prompt_template.md` (inject `{{evidence_summary}}`)
4. Critique hypotheses with `prompts/critique_prompt_template.md`.
5. Run pass 2 ranking + output formatting + guardrails.
6. Optionally export `pursue` hypotheses via Step H strategy exporter.

## Scripts

- Pass 1 (evidence summary):

```bash
python3 .cursor/skills/trading-trade-hypothesis-ideator/scripts/run_hypothesis_ideator.py \
  --input .cursor/skills/trading-trade-hypothesis-ideator/examples/example_input.json \
  --output-dir outputs/reports/trading/
```

- Pass 2 (rank + output + optional export):

```bash
python3 .cursor/skills/trading-trade-hypothesis-ideator/scripts/run_hypothesis_ideator.py \
  --input .cursor/skills/trading-trade-hypothesis-ideator/examples/example_input.json \
  --hypotheses outputs/reports/trading/raw_hypotheses.json \
  --output-dir outputs/reports/trading/ \
  --export-strategies
```

## Refer
