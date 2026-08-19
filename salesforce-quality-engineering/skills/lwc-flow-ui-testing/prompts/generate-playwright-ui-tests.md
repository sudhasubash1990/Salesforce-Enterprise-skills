---
title: Generate Playwright UI Tests
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

# Generate Playwright UI Tests

## Prompt

```
I have completed LFUT analysis for [COMPONENT_OR_FLOW_NAME].
Chain to PWR (Playwright Review) to generate automation test scripts.

Handoff includes:
- Locator map: [semantic locators, test IDs, shadow DOM notes]
- Sync patterns: [wire waits, spinner removal, toast assertions]
- Test scenarios: [list from LFUT 13-section report]
- Data dependencies: [TDG requirements]
- Page object boundaries: [component/page groupings]

Use PWR skill to produce Playwright test structure, page objects, fixtures, and CI config.
```

## Expected Output

PWR produces Playwright automation artifacts. LFUT provides the test design input.

## Boundaries

- LFUT: test scenarios, locators, sync patterns, accessibility criteria
- PWR: Playwright scripts, POM, fixtures, config, CI pipeline

## Related

- [SKILL.md](../SKILL.md)
- [Playwright Review](../../playwright-review/SKILL.md)
