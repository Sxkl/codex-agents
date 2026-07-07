# Java Spring Review Checklist

Use this checklist when reviewing Java/Spring service changes.

## Correctness

- null handling on request, response, and downstream client objects
- exception mapping matches API behavior
- DTO/entity field mapping remains consistent

## Data Safety

- transaction boundaries are still correct
- updates remain atomic enough for the scenario
- retries do not create duplicates

## Infra and Integration

- Redis lock usage is owner-safe
- Feign timeouts, fallbacks, and null behavior are coherent
- MyBatis SQL still matches filters and schema assumptions

## Operability

- logs include enough context to debug
- failures remain visible without duplicate noise
- patch has a plausible rollback or containment story
