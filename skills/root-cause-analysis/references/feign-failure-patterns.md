# Feign Failure Patterns

## Common Patterns

- null or empty downstream body
- fallback swallows the real failure
- timeout plus retry amplification
- HTTP error mapped to success-like wrapper

## Checks

- callsite null guard
- timeout and retry configuration
- fallback behavior visibility
- caller-side exception mapping

## Frequent False Shortcut

Adding a null check may stop the exception but still hide the real downstream failure mode.
