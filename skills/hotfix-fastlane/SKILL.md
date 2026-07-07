---
name: "hotfix-fastlane"
description: "Run a full hotfix workflow from logs to root cause, patch, review, verification, and Jira-ready reporting."
---

# Hotfix Fastlane

Use this skill for urgent but disciplined production fixes.

This skill is optimized for the current Codex session default model.

## Entry Conditions

Best when you have at least one of:

- logs
- stack trace
- failing endpoint or job
- recent regression context

## Fastlane Steps

1. Run `log-analysis` to cluster the signal.
2. Run `root-cause-analysis` to prove the failure path.
3. Run `code-fix` for the smallest safe patch.
4. Run `code-review` to catch risk.
5. Run `verification-regression` to validate the change.
6. Run `jira-writer` for operator-facing output.

## Required Outputs

- one-line incident summary
- evidence-backed root cause
- patch summary
- validation result
- remaining risk
- next step

## Escalation Rules

- if the failure path is not credible, stop before patching
- if the patch is high blast-radius and weakly verified, surface it as high risk
- if logs are too weak, ask for better data instead of pretending certainty
