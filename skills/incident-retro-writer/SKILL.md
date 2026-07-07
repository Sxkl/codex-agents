---
name: "incident-retro-writer"
description: "Write a concise incident retrospective with cause, response, lessons learned, and follow-up actions."
---

# Incident Retro Writer

Use this skill after incident handling is complete enough to summarize what happened and what should change next.

This skill is optimized for the current Codex session default model.

## Best Fit

- post-incident summary
- short retrospective
- lessons learned draft
- follow-up action capture

## Input

- incident summary
- root cause
- patch or mitigation
- validation performed
- unresolved risk
- timeline if available

## Output Structure

- incident summary
- root cause
- response taken
- what worked
- what was weak
- follow-up actions

## Shared Schema

- Align with `../../shared/output-schemas/incident-report.yaml` when useful.
- Use `../../examples/incident-retro-outline.md` as a concrete structure reference for concise retros.

## Guardrails

- do not turn a retro into a blame document
- separate verified facts from assumptions
- include actionable follow-up items, not generic lessons
