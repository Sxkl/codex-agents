# Codex Agents

Curated Codex-native skills for incident response, root-cause analysis, code repair, review, verification, and delivery reporting.

This repository is intentionally opinionated:

- fewer skills, stronger boundaries
- workflow-first instead of role-sprawl
- evidence-first outputs
- optimized for Codex default model behavior

## What Changed

This pack is not a raw migration of legacy agents.

It is a curated upgrade with:

- clear trigger boundaries between log analysis, root cause, fix, review, and verification
- consistent output contracts across skills
- a fastlane workflow for production hotfixes
- public-safe packaging with no local-path leakage

## Skills

- `incident-workflow-coordinator`: routes multi-step incident work across the right skills
- `log-analysis`: clusters logs, ranks patterns, and recommends escalation
- `root-cause-analysis`: turns logs and code into an evidence-backed causal chain
- `code-fix`: applies minimal, verifiable patches
- `code-review`: focuses on bugs, regressions, and risk
- `verification-regression`: adds targeted tests and states residual risk
- `jira-writer`: turns technical work into Jira-ready updates
- `hotfix-fastlane`: end-to-end hotfix workflow with explicit handoffs

## Recommended Flow

1. `log-analysis`
2. `root-cause-analysis`
3. `code-fix`
4. `code-review`
5. `verification-regression`
6. `jira-writer`

For fast production work, use `hotfix-fastlane`.

## Repository Layout

```text
skills/
  incident-workflow-coordinator/
  log-analysis/
  root-cause-analysis/
  code-fix/
  code-review/
  verification-regression/
  jira-writer/
  hotfix-fastlane/
docs/
  ARCHITECTURE.md
  ROADMAP.md
scripts/
  migrate_opencode_agents_to_codex.py
```

## Design Goals

- public, portable, and reusable
- easy to extend with service-specific references
- suitable for team workflows, not just solo prompting

## Next Moves

- add service-context loading
- add shared incident output schemas
- add reusable references for Java/Spring, Redis, Feign, MyBatis, and concurrency checks
