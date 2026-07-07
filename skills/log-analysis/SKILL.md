---
name: "log-analysis"
description: "Analyze logs by clustering repeated patterns, ranking operational impact, and recommending escalation."
---

# Log Analysis

Use this skill for broad log review, log health analysis, and first-pass incident triage.

This skill is optimized for the current Codex session default model.

## Best Fit

- SLS or exported application logs
- repeated WARN or ERROR spikes
- noisy logs that hide real failures
- deciding what deserves deeper investigation

## Workflow

1. Group logs by level, component, and signature.
2. Collapse duplicates into clusters.
3. Separate:
   - critical failure patterns
   - noisy warnings
   - weak observability
   - low-signal spam
4. Rank findings by operational impact.
5. Recommend one next action per cluster:
   - ignore
   - monitor
   - fix logging
   - escalate to root cause analysis

## Output

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`
- `clusters`

## Guardrails

- do not claim code root cause from logs alone
- prefer clusters over raw dumps
- keep escalation recommendations explicit
