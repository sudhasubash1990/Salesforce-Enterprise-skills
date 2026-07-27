---
title: API Test Review
module: Salesforce Quality Engineering
category: QE Specialized Skill Example
document_type: Example
version: 0.21.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [playwright-review, example]
---

# API Test Review

## Original Implementation

UI login used to seed 50 Accounts before API assert.

## Identified Issues

- Slow
- UI flake coupled to API check

## Recommended Improvements

- request.newContext with OAuth/session
- TDG payloads
- SOVA for verification

## Refactored Example

```ts
const api = await request.newContext({ baseURL, extraHTTPHeaders: { Authorization: `Bearer ${token}` } });
await api.post('/services/data/v59.0/sobjects/Account', { data: { Name: 'TDG API Acc' } });
```

## Best Practices

Keep secrets out of logs.

## QA Recommendations

Chain TDG + SOVA.
