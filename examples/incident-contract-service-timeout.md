# Example: contract-service Timeout Spike

## Input

- service: `contract-service`
- symptom: API timeout spike after a recent change
- evidence: WARN/ERROR logs showing downstream delay and retry accumulation

## Expected Flow

1. `log-analysis`
   - clusters repeated timeout logs
   - separates noisy retries from root timeout signature
2. `root-cause-analysis`
   - traces request path to downstream Feign call
   - identifies retry amplification and missing guard
3. `code-fix`
   - narrows retry path or adds safe guard
4. `code-review`
   - checks transaction and fallback implications
5. `verification-regression`
   - runs focused timeout-path validation
6. `jira-writer`
   - produces concise incident summary

## Good Output Shape

- summary: timeout spike traced to retry amplification in downstream call path
- evidence: relevant logs, client method, config or callsite
- confidence: high
- next_action: patch and validate timeout-path behavior
- risk: moderate if similar call patterns exist elsewhere
