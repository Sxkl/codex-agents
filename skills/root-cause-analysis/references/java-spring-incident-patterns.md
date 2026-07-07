# Java Spring Incident Patterns

Use these patterns when analyzing Java/Spring production issues.

## Feign

- downstream returned null or empty body
- fallback path hides the real failure
- timeout, retry, and circuit-breaker settings amplify load

## Redis

- lock release not guarded by owner check
- stale cache creates inconsistent reads
- retry storms after transient connection failures

## MyBatis

- column/property mismatch after schema drift
- nullable field assumptions break mapper logic
- dynamic SQL branches skip required filters

## Transactions

- transaction boundary too wide or too narrow
- async calls escape the intended transaction context
- partial update occurs before downstream failure

## Scheduled Jobs

- lock contention between nodes
- missing idempotency under retries
- broad catch hides the first failing item

## Preferential Checks

1. first failing method in the stack
2. transaction boundary around that method
3. downstream client behavior
4. cache and async side effects
