---
title: Login Test Review
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

# Login Test Review

## Original Implementation

```ts
test('login', async ({ page }) => {
  await page.goto(process.env.SF_URL!);
  await page.fill('#username', process.env.SF_USER!);
  await page.fill('#password', process.env.SF_PASS!);
  await page.click('#Login');
  await page.waitForTimeout(10000);
});
```

## Identified Issues

- Hard sleep after login
- Credentials from env OK but no storageState reuse
- No assertion of landing page

## Recommended Improvements

- Use storageState fixture per persona
- Replace sleep with expect(home locator)
- Keep secrets in CI secret store

## Refactored Example

```ts
test.use({ storageState: 'auth/sales.json' });
test('home loads', async ({ page }) => {
  await page.goto('/lightning/page/home');
  await expect(page.getByRole('heading', { name: /Home/i })).toBeVisible();
});
```

## Best Practices

Never commit storageState with live cookies.

## QA Recommendations

Chain PTA for persona matrix; score Security and Sync.
