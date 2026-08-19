---
title: Generate LWC Tests
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, prompt]
---

# Generate LWC Tests

## Prompt

```
Analyze the LWC component [COMPONENT_NAME] for UI testing using the LFUT skill.

Context:
- Component API name: [API_NAME]
- Org type: [Lightning App / Experience Cloud / Console]
- Parent page: [Record Page / App Page / Home Page]
- Personas: [List personas]
- Key features: [List rendering, interaction, validation features]

Produce a 13-section LWC Test Report covering:
1. Rendering validation (conditional, loading, empty, error states)
2. Interaction testing (inputs, buttons, modals, toasts)
3. Accessibility assessment (keyboard, screen reader, ARIA)
4. Locator strategy (semantic preferred)
5. Error and edge cases

Chain PWR for Playwright automation if automation is needed.
Chain PTA if persona-specific paths exist.
Chain TDG if test data setup is required.
```

## Expected Output

13-section report using [`templates/lwc-test-report.md`](../templates/lwc-test-report.md).

## Related

- [SKILL.md](../SKILL.md)
