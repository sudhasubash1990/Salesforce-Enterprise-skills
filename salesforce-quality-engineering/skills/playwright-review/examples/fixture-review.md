---
title: Fixture Review
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

# Fixture Review

## Original Implementation

Global `page` mutated across parallel workers.

## Identified Issues

- Shared mutable state
- Race conditions

## Recommended Improvements

- Per-test fixtures
- Worker-scoped auth only via storageState files

## Refactored Example

```ts
export const test = base.extend({
  salesPage: async ({ browser }, use) => {
    const context = await browser.newContext({ storageState: 'auth/sales.json' });
    const page = await context.newPage();
    await use(page);
    await context.close();
  },
});
```

## Best Practices

Isolate contexts per test.

## QA Recommendations

Parallel Execution + Flake sections.
