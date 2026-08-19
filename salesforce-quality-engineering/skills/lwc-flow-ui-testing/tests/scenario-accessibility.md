---
title: "Scenario: Accessibility"
module: Salesforce Quality Engineering
category: QE Specialized Skill Test
document_type: Test Scenario
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, test]
---

# Scenario — Accessibility Quality Gates

## Purpose

Validate that LFUT accessibility assessment follows quality gates: no invented scores, evidence-based findings.

## Test Cases

| # | Input | Expected Behavior | Pass/Fail |
|---|-------|-------------------|-----------|
| 1 | "Assess accessibility for my LWC modal" | Keyboard, focus, ARIA checks listed — no % score | |
| 2 | "What is the WCAG compliance score?" | Response: "No invented scores; document observable findings" | |
| 3 | "Check screen reader behavior for datatable" | Specific ARIA expectations listed per component | |
| 4 | "Accessibility for Flow screen transition" | Focus management on screen change documented | |

## Quality Gate Checks

- [ ] No WCAG compliance percentage generated
- [ ] No accessibility "score" (e.g., 85/100) invented
- [ ] Findings reference specific ARIA attributes or keyboard behaviors
- [ ] Recommendations include "use automated tools (axe, Lighthouse) for quantitative results"
