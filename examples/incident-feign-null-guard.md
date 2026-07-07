# Example: Feign Null Guard Regression

## Input

- symptom: intermittent NPE after downstream service returns empty body
- stack trace: service method dereferences response directly

## Expected Flow

1. `root-cause-analysis`
   - proves NPE occurs after nullable downstream result
2. `code-fix`
   - adds guard and consistent fallback behavior
3. `code-review`
   - checks whether nearby callers have the same risk
4. `verification-regression`
   - adds failure-path test for null response
5. `jira-writer`
   - documents cause, patch, and residual risk

## Good Output Shape

- summary: missing null guard after Feign response caused intermittent NPE
- evidence: stack frame, service method, failing dereference
- confidence: high
- next_action: deploy targeted fix and monitor similar callsites
- risk: medium if the pattern appears in other clients
