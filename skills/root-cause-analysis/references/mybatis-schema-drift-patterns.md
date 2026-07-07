# MyBatis Schema Drift Patterns

## Common Failures

- column rename or alias mismatch
- nullable column becomes required in code
- dynamic SQL misses a branch filter
- mapper XML and DTO drift apart

## Checks

- actual column names
- DTO to SQL field alignment
- mapper XML conditional branches
- nullability assumptions
