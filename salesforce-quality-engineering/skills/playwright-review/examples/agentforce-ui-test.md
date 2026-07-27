---
title: Agentforce UI Test
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

# Agentforce UI Test

## Original Implementation

Clicks Agentforce chat send; asserts any response text.

## Identified Issues

- No grounding/guardrail evaluation
- UI-only

## Recommended Improvements

- Chain AFT for AI QA sections
- UI checks for panel open/send only
- Do not invent accuracy %

## Refactored Example

```ts
await expect(page.getByRole('textbox', { name: /message/i })).toBeVisible();
// Delegate response quality to AFT
```

## Best Practices

Separate UI shell vs AI quality.

## QA Recommendations

Mandatory AFT cross-link.
