---
name: "verification-regression"
description: "Add focused tests and run the smallest useful validation to prove a change and state residual risk."
---

# Verification And Regression

Use this skill after a patch or review cycle when confidence must come from targeted verification, not explanation alone.

This skill is optimized for the current Codex session default model.

## Workflow

1. Identify the exact behavior to verify.
2. Reproduce the failing scenario if possible.
3. Add or update the smallest useful tests.
4. Run the narrowest meaningful command.
5. Report what remains unverified.

## Coverage Targets

- happy path
- failure path
- regression trigger
- one nearby edge case when cheap

## Output

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`
- `commands_run`

## Guardrails

- do not confuse compile success with regression coverage
- do not generate broad speculative suites
- report test-environment blockers explicitly
