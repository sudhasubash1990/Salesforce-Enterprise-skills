---
title: Dynamic Locator Review
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

# Dynamic Locator Review

## Original Implementation

`page.locator('div.slds-truncate:nth-child(3)')` for related list.

## Identified Issues

- Position-based CSS
- Breaks on column reorder

## Recommended Improvements

- Role/name within related list
- data-testid if product allows
- Chain MIA on FlexiPage change

## Refactored Example

```ts
page.getByRole('link', { name: 'Case 00001234' })
```

## Best Practices

Avoid nth-child for Lightning.

## QA Recommendations

Locator Review Fail until hardened.
