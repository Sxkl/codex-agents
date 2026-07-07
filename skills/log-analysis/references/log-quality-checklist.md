# Log Quality Checklist

Use this checklist when log review is not only about failure signatures but also about observability quality.

## Check

- Does the log include request or trace context?
- Does it include business identifiers when useful?
- Does it distinguish cause from symptom?
- Is the level correct for the event?
- Is the same event emitted repeatedly without aggregation?
- Does the message help an operator decide what to do next?

## Anti-patterns

- INFO spam with no operational value
- ERROR logs for expected branch behavior
- Missing retry count or timeout context
- Logging only the exception class without scenario context
- Duplicate stack traces across layers
