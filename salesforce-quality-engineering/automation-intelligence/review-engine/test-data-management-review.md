---
title: Test Data Management Approach Review
version: 0.10.1
tags: [automation-intelligence, sprint-8, review-engine]
---

# Test Data Management Approach Review

## Purpose

Assess how automation creates, isolates, and cleans test data for Salesforce.

## Business Context

Shared mutable data and missing cleanup cause flakes and false failures across sandboxes.

## Architecture

Prefer API/factory seeding; unique dynamic data; cleanup/idempotent teardown; env isolation; masked/synthetic—not production PII.

## Decision Criteria

| Score | Signals |
|-------|---------|
| 5 | API factories; unique keys; cleanup; env-specific config; no PII |
| 3 | Partial seeding; some shared static users/data |
| 1 | Hard-coded record IDs; production-like PII; no cleanup |

## Best Practices

- Create → exercise → assert → delete/archive.  
- Isolate personas and integration stubs per suite where needed.  

## Salesforce Considerations

- Respect validation rules, duplicate rules, and sharing when seeding.  
- Bulk/LDV scenarios need explicit data strategy.  

## Automation Considerations

- Link to [../test-data/README.md](../test-data/README.md).  

## Common Pitfalls

- UI-only data setup for every test.  
- Depending on a single shared Account forever.  

## Examples

`api.createAccount()` + unique suffix + delete in afterAll → 4–5.

## Interview Questions

- How do you review Salesforce test data automation quality?  

## Related Documents

- [../test-data/api-data-creation.md](../test-data/api-data-creation.md)
- [CI/CD Readiness](cicd-readiness-review.md)

## Navigation

- **Previous:** [locator-robustness.md](locator-robustness.md)
- **Next:** [cicd-readiness-review.md](cicd-readiness-review.md)

## Future Enhancements

- Data dependency graph checklist  
