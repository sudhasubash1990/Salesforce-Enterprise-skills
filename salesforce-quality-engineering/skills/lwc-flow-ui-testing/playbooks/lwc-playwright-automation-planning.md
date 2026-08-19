---
title: LWC Playwright Automation Planning
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, playbook]
---

# LWC Playwright Automation Planning

## When to Use

Preparing to chain LFUT test scenarios to [Playwright Review (PWR)](../../playwright-review/SKILL.md) for automation scripting.

## Steps

1. **Complete LFUT analysis first** — Rendering, interaction, accessibility, locator strategy must be defined
2. **Export locator map** — Document semantic locators, test IDs, and shadow DOM considerations
3. **Identify sync patterns** — Wire adapter waits, spinner removal, toast assertions, navigation waits
4. **Map test data needs** — Chain TDG for required records; document data setup/teardown
5. **Define page object boundaries** — One POM per component or logical page area
6. **Hand off to PWR** — Provide: locator map, sync patterns, test scenarios, data dependencies
7. **PWR produces** — Playwright test structure, fixtures, assertions, CI config

## Boundaries

| LFUT Produces | PWR Produces |
|---------------|-------------|
| Test scenarios and expected behavior | Playwright test scripts |
| Locator strategy and sync patterns | Page objects and fixtures |
| Accessibility test criteria | Accessibility automation (axe integration) |
| Component analysis | Framework config and CI pipeline |

**HARD RULE:** Do not generate Playwright code in LFUT. Provide the test design; PWR handles automation.

## Related Documents

- [SKILL.md](../SKILL.md)
- [Playwright Review](../../playwright-review/SKILL.md)
