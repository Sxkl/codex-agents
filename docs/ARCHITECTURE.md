# Architecture

## Principles

- workflow first
- evidence before action
- smallest safe change
- verification before closure
- shared output language across skills

## Layering

### Core workflow

- `hotfix-fastlane`
- `incident-workflow-coordinator`

### Specialist analysis

- `log-analysis`
- `root-cause-analysis`

### Change execution

- `code-fix`
- `code-review`
- `verification-regression`

### Reporting

- `jira-writer`

## Why This Shape

Legacy multi-agent systems often overfit to named roles and model choreography. Codex works better when:

- each skill has a narrow trigger boundary
- each handoff is explicit
- each step produces a concrete artifact or decision

## Output Contract

Every skill should prefer:

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`

Specialized skills may add fields, but they should not omit those concepts.
