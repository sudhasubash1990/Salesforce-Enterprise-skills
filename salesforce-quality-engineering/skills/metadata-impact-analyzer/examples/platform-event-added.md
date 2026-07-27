---
title: Platform Event Added
module: Salesforce Quality Engineering
category: Specialized Skill Example
document_type: Example
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, example]
---

# Platform Event Added

## Input

**Change:** New Platform Event `Order_Shipped__e` published from Flow; external subscriber via Event Relay.

Flow `Fulfillment_Complete` publishes event. MuleSoft subscriber in lower env only.

## Expected Analysis (Dependency First)

- Publish/subscribe contract versioning.
- Event fields must match subscriber schema.
- High volume — governor and replay ID considerations.

## Expected Regression

| Scope | Rationale |
|-------|-----------|
| In | Flow publishes event on fulfillment |
| Conditional | Subscriber receipt in integrated env |
| Out | Unrelated order flows |

## Expected Risk

**Rating:** High

## Expected SOQL Validations

```sql
SELECT Id, ReplayId, CreatedDate FROM Order_Shipped__e ORDER BY CreatedDate DESC LIMIT 5
```

## Related Documents

- [SKILL.md](../SKILL.md)
- [examples/README.md](README.md)
