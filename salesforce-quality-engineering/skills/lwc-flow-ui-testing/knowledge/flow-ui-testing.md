---
title: Flow UI Testing
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [lwc-flow-ui-testing, knowledge]
---

# Flow UI Testing

## Purpose

Define the testing model for Screen Flow and Flow UI: navigation, input screens, conditional visibility, decision outcomes, fault paths, and persona behavior.

## Screen Flow Navigation

| Action | What to Test |
|--------|-------------|
| Next | Advances to correct screen; validates required fields before proceeding |
| Back | Returns to previous screen; preserves entered data |
| Cancel | Confirms cancel dialog (if configured); exits flow cleanly |
| Resume | Paused flow resumes at correct screen with prior data intact |
| Finish | Final screen renders success message; record created/updated as expected |

## Input Screen Testing

- Required fields block Next until populated
- Picklist/radio choices drive conditional visibility on same or subsequent screens
- Default values render correctly on first load
- Input validation messages display inline (not toast)
- Multi-column layout renders correctly at different widths

## Conditional Visibility

- Components show/hide based on choice selections or formula conditions
- Visibility changes are immediate (no page reload)
- Hidden components do not submit values

## Decision Outcomes

- Each decision branch routes to the correct screen
- All branches are reachable (no dead paths in test plan)
- Complex decision matrices documented with expected outcomes

## Fault Paths

- DML failures surface user-friendly fault message
- Apex action exceptions caught by fault connector → error screen
- Network timeout or governor limit produces meaningful feedback
- Fault screen allows retry or navigation back

## Persona-Specific Behavior

- Profile-based record type assignment affects picklist values
- Permission set assignment controls Flow entry (run-time visibility)
- FLS restrictions hide fields within Flow screens
- Chain [PTA](../../permission-testing-agent/SKILL.md) for permission matrix

## Success and Completion

- Success screen displays correct confirmation message
- Record ID or link provided for created/updated record
- Post-flow redirect navigates to expected page

## Cross-Links

- [LWC UI Testing](lwc-ui-testing.md)
- [Accessibility Testing](accessibility-testing.md)
- [SKILL.md](../SKILL.md)

## Related Documents

- [SKILL.md](../SKILL.md)
- [Permission Testing Agent](../../permission-testing-agent/SKILL.md)
