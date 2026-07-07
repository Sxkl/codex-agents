---
name: "code-review"
description: "Review a diff for correctness, regressions, security, and testing gaps with findings-first output."
---

# Code Review

Use this skill for risk-focused review of changed files or a diff.

This skill is optimized for the current Codex session default model.

## Priorities

- correctness bugs
- regressions
- security issues
- data consistency risks
- transaction and concurrency risks
- missing tests

## Workflow

1. Read the diff first.
2. Reconstruct expected behavior.
3. Check mismatch between intent and implementation.
4. Check edge cases and failure modes.
5. Check what is and is not verified by tests.

## Output

List findings first, ordered by severity. Then optionally add:

- `open_questions`
- `residual_risks`

## Guardrails

- avoid style-only review noise
- prefer concrete issues over speculative ones
- state assumptions when a finding depends on them
