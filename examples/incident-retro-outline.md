# Example: Incident Retro Outline

## Situation

- service: `contract-service`
- incident type: downstream timeout amplification
- resolution: targeted retry-path fix and focused validation

## Good Retro Shape

### Incident Summary

Short description of impact and resolution status.

### Root Cause

Explain the first causal failure, not only downstream symptoms.

### Response

List the actions taken:

- log analysis
- root cause confirmation
- patch
- review
- verification

### What Worked

- useful logs
- narrow patch
- targeted regression coverage

### What Was Weak

- missing context in logs
- weak timeout alerting
- repeated risky pattern in nearby callsites

### Follow-up Actions

- add stronger client timeout observability
- scan similar Feign callsites
- improve service-context references
