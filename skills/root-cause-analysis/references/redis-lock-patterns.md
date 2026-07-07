# Redis Lock Patterns

## Common Failures

- unlock without owner verification
- lock TTL too short or too long
- retries create duplicate work after lock failure
- exception path skips release

## Checks

- owner-safe release
- failure-path release
- retry interaction
- multi-node contention
