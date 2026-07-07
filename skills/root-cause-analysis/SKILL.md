---
name: "root-cause-analysis"
description: "Build an evidence-backed causal chain from error symptoms to the most likely root cause in code."
---

# Root Cause Analysis

Use this skill when the question is not just “what failed” but “why did it fail here?”

This skill is optimized for the current Codex session default model.

## Best Fit

- stack traces
- reproducible runtime failures
- regressions after code changes
- repeated high-value incident patterns

## Workflow

1. Normalize the symptom.
2. Search the repository for exact symbols, messages, endpoints, or field names.
3. Trace the execution path.
4. Build a causal chain:
   `symptom -> trigger -> failing condition -> root cause`
5. Compare at least two plausible hypotheses.
6. State the strongest supported conclusion and its confidence.

## References

- Start with `./references/java-spring-incident-patterns.md` for the broad Java/Spring incident map.
- Read `./references/feign-failure-patterns.md` when the symptom involves downstream RPC, gateway forwarding, deserialization, or null response contracts.
- Read `./references/redis-lock-patterns.md` when the failure may involve distributed locks, TTL handling, idempotency, or retry storms.
- Read `./references/mybatis-schema-drift-patterns.md` when the failure may involve SQL mapping, schema drift, enum/value mismatch, or deployment order.
- Read `./references/transaction-concurrency-patterns.md` when the incident hints at transaction boundaries, duplicate writes, race conditions, or inconsistent reads.

## Output

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`
- `blast_radius`

## Guardrails

- prefer earliest causal failure over downstream noise
- do not jump to patching before the path is credible
- state missing evidence clearly when confidence is low
