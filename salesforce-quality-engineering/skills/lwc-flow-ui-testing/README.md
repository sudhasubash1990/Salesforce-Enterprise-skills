---
title: LWC & Flow UI Testing — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing]
---

# LWC & Flow UI Testing (LFUT)

## Purpose

Enterprise **LWC and Flow UI testing** capability for Salesforce QE. Validates component rendering, interaction, visibility, accessibility, Screen Flow navigation, input validation, fault paths, and persona-specific behavior — producing evidence-based test analysis without invented scores.

Playwright automation architecture lives in:

- [`../playwright-review/`](../playwright-review/SKILL.md) — chain for script generation and framework review

This pack holds **LWC/Flow UI testing reasoning models** and the **13-section** deliverable.

## Capabilities

- LWC component rendering, interaction, and validation analysis
- Screen Flow navigation and input screen testing
- Shadow DOM, dynamic rendering, async UI assessment
- Accessibility evaluation (keyboard, screen reader, ARIA, focus)
- Semantic locator strategy recommendation
- Flow fault path and negative scenario coverage
- Persona-specific Flow behavior analysis
- Experience Cloud LWC testing context

## Supported Components

**LWC:** `lightning-input` · `lightning-combobox` · `lightning-datatable` · `lightning-record-edit-form` · `lightning-record-view-form` · `lightning-button` · `lightning-modal` · `lightning-card` · `lightning-accordion` · `lightning-tab` · Custom LWC · Nested/composed LWC

**Flows:** Screen Flow · Auto-launched (UI entry) · Record-triggered (UI side-effects)

## Folder Structure

```
skills/lwc-flow-ui-testing/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 5 reasoning articles
├── playbooks/       ← 4 playbooks
├── templates/       ← 3 templates
├── prompts/         ← 3 prompts
├── examples/        ← 4 examples
└── tests/           ← 5 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Component name or Flow API name | Yes |
| Component metadata (fields, events, wire adapters) | Recommended |
| Org context (Lightning, Experience, Console) | Recommended |
| Persona / profile | When permission-sensitive |
| FlexiPage layout | When rendering context needed |

## Outputs

| Deliverable | Template |
|-------------|----------|
| LWC Test Report (13 sections) | [`templates/lwc-test-report.md`](templates/lwc-test-report.md) |
| Flow UI Test Report | [`templates/flow-ui-test-report.md`](templates/flow-ui-test-report.md) |
| Accessibility Checklist | [`templates/lwc-accessibility-checklist.md`](templates/lwc-accessibility-checklist.md) |

## Sample Prompt

> Analyze the `customerSearchLWC` component for rendering, interaction, and accessibility. The component uses `lightning-input`, `lightning-datatable`, and communicates via Lightning Message Service. Target org uses Service Cloud console.

## Best Practices

- Always identify component metadata before writing test scenarios
- Prefer semantic locators over CSS/XPath
- Cover conditional rendering paths (if:true/lwc:if)
- Validate async behavior after wire adapter refresh
- Test Flow navigation in both happy and fault paths
- Chain PWR for Playwright automation — do not generate scripts here

## Limitations

- Advisory only — no live execution
- No invented accessibility scores or WCAG compliance percentages
- Playwright scripts require chaining to PWR
- Backend Flow logic out of scope unless UI-visible

## Related

| Link | Purpose |
|------|---------|
| [Playwright Review](../playwright-review/SKILL.md) | Automation scripts |
| [Permission Testing Agent](../permission-testing-agent/SKILL.md) | Persona paths |
| [Test Data Generator](../test-data-generator/SKILL.md) | Test data seeding |
| [Metadata Impact Analyzer](../metadata-impact-analyzer/SKILL.md) | Metadata change impact |

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.25.0 | 2026-08-19 | QE Practice Lead | Initial LWC & Flow UI Testing capability |
