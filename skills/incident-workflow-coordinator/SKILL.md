---
name: "incident-workflow-coordinator"
description: "Coordinate incident work across log analysis, root cause analysis, code fix, review, verification, and reporting."
---

# Incident Workflow Coordinator

Use this skill when a request spans multiple incident-response phases and needs deliberate routing instead of a single-pass answer.

This skill is optimized for the current Codex session default model.

## Best Fit

- production issues
- hotfix planning
- “find, fix, verify, and summarize” requests

## Workflow

1. Start with `log-analysis` if logs are broad or noisy.
2. Route to `root-cause-analysis` when a concrete failure path must be proven.
3. Route to `code-fix` only after the failure path is credible.
4. Route to `code-review` after the patch exists.
5. Route to `verification-regression` before closure.
6. Route to `jira-writer` for operator-facing output.

## Guardrails

- do not skip evidence-building
- do not widen scope during incident handling
- surface blockers early when required data is missing
