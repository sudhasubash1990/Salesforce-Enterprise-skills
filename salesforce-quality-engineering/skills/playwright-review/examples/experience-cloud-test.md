---
title: Experience Cloud Test
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

# Experience Cloud Test

## Original Implementation

Guest user test with admin storageState.

## Identified Issues

- Wrong persona
- Security false confidence

## Recommended Improvements

- Guest vs member storageState
- Chain PTA
- No admin cookies for public pages

## Refactored Example

```ts
test.use({ storageState: { cookies: [], origins: [] } }); // guest
```

## Best Practices

Persona authenticity matters.

## QA Recommendations

Security + PTA chain.
