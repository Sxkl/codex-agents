# Architecture

## Principles

- workflow first
- evidence before action
- smallest safe change
- verification before closure
- shared output language across skills
- thin prompts, heavy assets

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

### Shared assets

- `shared/known-services.yaml`
- `shared/severity-matrix.yaml`
- `shared/output-schemas/incident-report.yaml`
- skill-specific `references/`
- skill-specific `workflows/`
- `examples/`

## Why This Shape

Legacy multi-agent systems often overfit to named roles and model choreography. Codex works better when:

- each skill has a narrow trigger boundary
- each handoff is explicit
- each step produces a concrete artifact or decision

The upgrade path in this repository is:

- keep the entry prompts compact
- move domain heft into references and shared assets
- make workflows inspectable
- make outputs reusable by humans and downstream tools

## Output Contract

Every skill should prefer:

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`

Specialized skills may add fields, but they should not omit those concepts.

## Asset Strategy

### SKILL.md

- trigger boundary
- decision rules
- handoff rules

### references/

- stack-specific failure patterns
- review and verification checklists
- domain heuristics

### shared/

- severity, escalation, and output normalization
- service inventory and context hooks

### workflows/

- standard operating sequence
- stop points
- fallback and escalation behavior
