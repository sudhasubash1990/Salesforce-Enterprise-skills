---
title: Page Object Review
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

# Page Object Review

## Original Implementation

God AccountPage with 40 methods and embedded waits.

## Identified Issues

- Low cohesion
- Duplicated waits
- Business assertions inside page

## Recommended Improvements

- Split list/detail/edit pages
- Moves assertions to tests
- Shared wait helpers

## Refactored Example

```ts
export class AccountEditPage {
  constructor(private page: Page) {}
  name = this.page.getByLabel('Account Name');
  async save() { await this.page.getByRole('button', { name: 'Save' }).click(); }
}
```

## Best Practices

Pages = actions/locators; tests = outcomes.

## QA Recommendations

Score POM dimension 2–3 until split.
