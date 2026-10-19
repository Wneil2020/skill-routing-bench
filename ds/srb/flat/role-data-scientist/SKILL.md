---
name: role-data-scientist
description: "Use when Analyze a given topic from the Data Scientist perspective — data pipeline impact, ML model implications, statistical methodology, data: covers role, data, scientist, 데이터 사이언티스트 관점, DS 분석"
metadata:
  holon-triggers: |
    data scientist perspective
    데이터 사이언티스트 관점
---

---
name: role-data-scientist
description: >
  Analyze a given topic from the Data Scientist perspective — data pipeline impact, ML model
  implications, statistical methodology, data quality requirements, and visualization needs.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes kwp-data-data-exploration, kwp-data-statistical-analysis, kwp-data-data-visualization,
  kwp-data-data-validation, kwp-data-sql-queries, hf-model-trainer, hf-evaluation, hf-datasets,
  workflow-miner, skill-composer, semantic-guard, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "data scientist perspective", "데이터 사이언티스트 관점", "DS 분석", "data impact analysis".
  Do NOT use for running data exploration directly (use kwp-data-data-exploration),
  model training execution (use hf-model-trainer), or dashboard building (use kwp-data-interactive-dashboard-builder).
  Korean triggers: "데이터 사이언티스트 관점", "DS 분석", "데이터 영향 분석".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "role-analysis"
---

# Data Scientist Perspective Analyzer

Analyzes any business topic from the Data Scientist's viewpoint, covering data pipeline impact,
ML model requirements, statistical methodology, data quality, feature engineering, and
visualization needs.

## Relevance Criteria

Score the topic 1-10 based on overlap with data science concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Data analysis & exploration | High | dataset, EDA, profiling, distribution, outlier, correlation |
| ML model development | High | model, training, fine-tuning, inference, prediction, classification |
| Data pipeline & ETL | High | pipeline, ETL, ingestion, transformation, batch, streaming |
| Statistical methods | High | hypothesis, regression, significance, confidence, A/B test |
| Data visualization | High | chart, dashboard, plot, visualization, Plotly, matplotlib |
| Da
