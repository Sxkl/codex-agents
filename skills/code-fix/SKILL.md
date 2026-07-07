---
name: "code-fix"
description: "Apply the smallest safe patch for a known issue and document the verification scope and residual risk."
---

# Code Fix

Use this skill after the bug or failure mode is understood well enough to change code.

This skill is optimized for the current Codex session default model.

## Workflow

1. Restate the target behavior.
2. Prefer test-first when practical.
3. Apply the smallest coherent patch.
4. Check nearby risk:
   - nullability
   - retries
   - transactions
   - logging
   - backward compatibility
5. Run focused validation.
6. State residual risk.

## Output

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`
- `files_changed`

## Guardrails

- avoid unrelated refactors
- avoid silent scope growth
- say explicitly when verification is incomplete
