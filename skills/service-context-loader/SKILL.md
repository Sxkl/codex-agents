---
name: "service-context-loader"
description: "Load service-specific context such as stack traits, likely failure patterns, and analysis priorities before deeper incident work."
---

# Service Context Loader

Use this skill when the service name is known and you want to avoid rebuilding technical context from scratch.

This skill is optimized for the current Codex session default model.

## What It Loads

- stack traits
- likely incident families
- review priorities
- verification priorities
- context hints for downstream skills

## Shared Assets

- `../../shared/known-services.yaml`

## Workflow

1. Match the requested service name to the known service inventory.
2. Extract stack and trait information.
3. Surface likely incident patterns.
4. Recommend which downstream skills should emphasize which checks.

## Output

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`
- `service_profile`

## Guardrails

- if the service is unknown, fall back to stack-level heuristics instead of inventing details
- separate confirmed service facts from inferred likely patterns
