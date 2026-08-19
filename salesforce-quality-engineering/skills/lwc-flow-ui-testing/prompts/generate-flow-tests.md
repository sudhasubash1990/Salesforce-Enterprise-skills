---
title: Generate Flow Tests
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

# Generate Flow Tests

## Prompt

```
Analyze the Screen Flow [FLOW_NAME] for UI testing using the LFUT skill.

Context:
- Flow API name: [API_NAME]
- Flow type: Screen Flow
- Entry point: [Record Page / Button / Quick Action / URL]
- Screens: [Count and names]
- Decision elements: [Count and branching logic]
- Personas: [List personas with different behavior]

Produce a 13-section Flow UI Test Report covering:
1. Screen-by-screen input and rendering validation
2. Navigation paths (next, back, cancel, resume, finish)
3. Decision branch routing
4. Fault path and error scenarios
5. Persona-specific behavior
6. Accessibility on screen transitions

Chain PTA for permission-based Flow visibility.
Chain TDG for prerequisite test records.
```

## Expected Output

13-section report using [`templates/flow-ui-test-report.md`](../templates/flow-ui-test-report.md).

## Related

- [SKILL.md](../SKILL.md)
