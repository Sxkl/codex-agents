# Benchmarks

## Goal

Show the difference between:

- generic prompting
- role-heavy legacy agent prompting
- workflow-first Codex-native skill execution

## Benchmark 1: Timeout Incident

### Generic Prompt

- often summarizes logs
- may jump to likely causes too early
- weak separation between evidence and speculation

### Workflow-First Skill Pack

- `log-analysis` clusters repeated timeout patterns
- `root-cause-analysis` proves the first causal failure path
- `code-review` and `verification-regression` force risk and validation visibility

### Improvement Signal

- higher evidence density
- lower speculative patching
- clearer residual risk reporting

## Benchmark 2: Feign Null Response

### Generic Prompt

- likely suggests a null check quickly
- may skip similar caller risk and validation depth

### Workflow-First Skill Pack

- explicit root cause chain
- explicit caller adjacency review
- explicit failure-path test expectation

## Benchmark 3: Redis Lock Leak

### Generic Prompt

- may recommend changing lock logic
- may miss owner-safe unlock semantics or retry implications

### Workflow-First Skill Pack

- root-cause isolates lock owner/release semantics
- review checks concurrency and rollback risk
- verification focuses on failure-path lock release

## Key Takeaway

The main gain is not “more words”.

The gain comes from:

- better task boundaries
- better shared assets
- better handoffs
- better validation pressure
