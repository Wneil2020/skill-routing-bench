---
name: kwp-data-interactive-dashboard-builder
description: "Use when Build self-contained interactive HTML dashboards with Chart.js, dropdown filters, and professional styling. Use when creating dashboards, building: covers kwp, data, interactive, 데이터, 빌드"
metadata:
  holon-triggers: |
    creating dashboards
    building interactive reports
---

---
name: kwp-data-interactive-dashboard-builder
description: >-
  Build self-contained interactive HTML dashboards with Chart.js, dropdown
  filters, and professional styling. Use when creating dashboards, building
  interactive reports, or generating shareable HTML files with charts and
  filters that work without a server. Do NOT use for tasks outside the data
  domain. Korean triggers: "데이터", "빌드", "리포트".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Interactive Dashboard Builder Skill

Patterns and techniques for building self-contained HTML/JS dashboards with Chart.js, filters, interactivity, and professional styling.

## HTML/JS Dashboard Patterns

### Base Template

Every dashboard follows this structure:

For base template, see [references/code-block-1.md](references/code-block-1.md).


### KPI Card Pattern

```html
<div class="kpi-card">
    <div class="kpi-label">Total Revenue</div>
    <div class="kpi-value" id="kpi-revenue">$0</div>
    <div class="kpi-change positive" id="kpi-revenue-change">+0%</div>
</div>
```

For code block, see [references/code-block-2.md](references/code-block-2.md).


### Chart Container Pattern

```html
<div class="chart-container">
    <h3 class="chart-title">Monthly Revenue Trend</h3>
    <canvas id="revenue-chart"></canvas>
</div>
```

## Chart.js Integration

### Line Chart

For line chart, see [references/code-block-3.md](references/code-block-3.md).


### Bar Chart

For bar chart, see [references/code-block-4.md](references/code-block-4.md).


### Doughnut Chart

For doughnut chart, see [references/code-block-5.md](references/code-block-5.md).


### Updating Charts on Filter Change

```javascript
function updateChart(chart, newLabels, newData) {
    chart.data.labels = newLabels;

    if (Array.isArray(newData[0])) {
        // Multiple datasets
        newData.forEach((data, i) => {
            chart.data.datasets[i].data = data;
        });
    } else {
        chart.data.datasets[0
