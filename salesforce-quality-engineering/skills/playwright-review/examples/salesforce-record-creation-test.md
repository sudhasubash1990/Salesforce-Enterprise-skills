---
title: Salesforce Record Creation Test
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

# Salesforce Record Creation Test

## Original Implementation

UI-only Account create with CSS selectors and no data cleanup.

## Identified Issues

- Brittle CSS
- No API setup/cleanup
- Asserts only toast text

## Recommended Improvements

- getByLabel for fields
- API create optional; External ID cleanup
- Assert record via UI + SOVA stub

## Refactored Example

```ts
await page.getByLabel('Account Name').fill('TDG Acme Test');
await page.getByRole('button', { name: 'Save' }).click();
await expect(page.getByText('was saved')).toBeVisible();
```

## Best Practices

Prefer TDG External IDs for cleanup.

## QA Recommendations

Recommend SOVA count query; TDG for seed.
