---
title: Salesforce Console App Test
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

# Salesforce Console App Test

## Original Implementation

Clicks by absolute XPath across console tabs.

## Identified Issues

- Console tab flake
- No tab helper

## Recommended Improvements

- Centralize console navigation helper
- Role-based tab selection

## Refactored Example

```ts
await consoleNav.openTab(page, 'Cases');
await expect(page.getByRole('tab', { name: 'Cases', selected: true })).toBeVisible();
```

## Best Practices

Centralize console helpers.

## QA Recommendations

Salesforce Compatibility Review focus.
