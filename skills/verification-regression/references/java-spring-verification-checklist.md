# Java Spring Verification Checklist

Use this checklist to avoid weak “verified” claims on Java/Spring services.

## Prefer

- one targeted reproduction test
- one failure-path test
- one regression-path assertion

## Check

- controller-level behavior if API contract changed
- service-level behavior if business logic changed
- mapper behavior if query or schema assumptions changed
- cache / retry / lock behavior if infra coordination changed

## Weak Evidence

These are not enough on their own:

- compile success
- app starts locally
- a single happy-path test
- no exception in logs during one manual click-through
