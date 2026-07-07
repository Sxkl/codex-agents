---
name: "jira-writer"
description: "Write concise, operator-friendly Jira comments, reports, and closure notes from technical findings and validation."
---

# Jira Writer

Use this skill when the technical work is done and the remaining job is to communicate it clearly.

This skill is optimized for the current Codex session default model.

## Modes

- progress comment
- incident update
- closure note
- short retro

## Writing Rules

- conclusion first
- evidence second
- validation explicit
- unresolved risk visible
- next action or status at the end

## Output Structure

- context
- finding or root cause
- action taken
- validation
- remaining risk
- next step or closure

## Shared Schema

- When a structured incident report is needed, align with `../../shared/output-schemas/incident-report.yaml`.

## Guardrails

- do not claim resolution without validation
- do not invent links, ticket fields, or runtime facts
- keep it scannable for operators
