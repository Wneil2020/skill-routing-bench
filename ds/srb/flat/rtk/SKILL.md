---
name: rtk
description: "Use when Manage RTK (Rust Token Killer) CLI proxy for token-optimized command execution. Use when the user asks to \"check token savings\", \"rtk: covers rtk, gain, killer, prefixing, transparently"
metadata:
  holon-triggers: |
    check token savings
    rtk gain
---

---
name: rtk
description: >-
  Manage RTK (Rust Token Killer) CLI proxy for token-optimized command
  execution. Use when the user asks to "check token savings", "rtk gain",
  "optimize tokens", "reduce token usage", "rtk discover", "rtk status", "토큰
  절감", "토큰 사용량", "RTK 상태", "RTK 분석", or wants to view/manage RTK analytics and
  configuration. Do NOT use for general shell commands — the
  rtk-token-optimization rule handles auto-prefixing transparently.
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# RTK — Token Optimization Proxy Management

RTK compresses CLI output before it reaches the LLM context window, reducing token consumption by 60-90%. This skill covers analytics, configuration, and troubleshooting — not command rewriting (handled by the always-on `rtk-token-optimization` rule).

## Workflow

### Step 1: Token Savings Analytics

```bash
rtk gain                    # Summary stats
rtk gain --graph            # ASCII graph (last 30 days)
rtk gain --daily            # Day-by-day breakdown
rtk gain --history          # Recent command history
rtk gain --all --format json  # JSON export for dashboards
```

Present the results in Korean with:
- Total tokens saved (absolute number and percentage)
- Top 5 commands by savings
- Trend over the last 7 days
- Comparison to previous period if data available

### Step 2: Discover Optimization Opportunities

```bash
rtk discover                # Current project
rtk discover --all          # All projects
rtk discover --all --since 7  # All projects, last 7 days
```

For each opportunity found:
1. Show the command that could benefit from RTK
2. Estimate potential token savings
3. Confirm whether the command is already covered by the `rtk-token-optimization` rule

### Step 3: Health Check

Run these commands and report status:

```bash
rtk --version               # Should show rtk 0.27.x
which rtk                   # Should be in PATH
rtk gain                    # Should not error
```

Check c
