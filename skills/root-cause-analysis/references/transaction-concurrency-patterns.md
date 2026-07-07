# Transaction And Concurrency Patterns

## Transaction Failures

- partial write before downstream failure
- wrong transaction boundary around retry logic
- async or event handoff escapes transaction expectations

## Concurrency Failures

- duplicate execution under retries
- stale cache after write
- concurrent scheduled job overlap
- race around mutable shared state

## Checks

- transaction scope
- retry idempotency
- async boundaries
- lock / cache / state coordination
