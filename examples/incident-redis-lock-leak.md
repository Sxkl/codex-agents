# Example: Redis Lock Leak

## Input

- symptom: scheduled job backlog and duplicate work across nodes
- logs: lock acquisition succeeds but release path is inconsistent under failure

## Expected Flow

1. `log-analysis`
   - identifies lock-related failure clusters
2. `root-cause-analysis`
   - traces lock owner and release behavior
3. `code-fix`
   - replaces unsafe unlock with owner-safe release
4. `code-review`
   - checks retry and concurrency implications
5. `verification-regression`
   - validates lock-release behavior under failure path
6. `jira-writer`
   - reports cause, patch, and remaining operational watchpoints
