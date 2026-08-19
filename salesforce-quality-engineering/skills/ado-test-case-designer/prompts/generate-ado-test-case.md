---
title: Generate ADO Test Case Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [ado-test-case-designer, prompt, generate]
---

# Generate ADO Test Case

## Prompt Pattern

```
Generate ADO test cases for the following requirement:

**Requirement ID:** [BR-XXX / FR-XXX / US-XXX]
**Title:** [Requirement title]
**Description:** [Full requirement text]
**Acceptance Criteria:**
- AC1: Given... When... Then...
- AC2: Given... When... Then...

**Business Rules:**
- BRU-001: [Rule]

**Salesforce Objects:** [Account, Opportunity, etc.]
**Personas:** [Sales Rep, Admin, etc.]
**Environment:** [SIT / UAT]
```

## Expected Output

The skill generates the 10-section output per `SKILL.md > Output Schema`:

1. Intent — restates the test design goal
2. Context — Salesforce cloud, objects, personas
3. Assumptions — labeled with `[ASSUMPTION]`
4. Requirement Analysis — testable conditions extracted
5. Test Design Approach — techniques selected with rationale
6. ADO Test Cases — full test cases in ADO format
7. Traceability Matrix — requirement → test case mapping
8. Quality Gates — checklist status
9. Dependencies — data, environment, integration
10. Recommended Next Actions — follow-ups

## Variations

- **Minimal input:** Provide just a requirement description — the skill will flag assumptions and generate test cases with `[ASSUMPTION]` tags
- **With custom template:** Append "Use this template instead: [template]" — the skill will use the user template
- **Bulk:** Provide multiple requirements — the skill will generate test cases for each and a consolidated traceability matrix

## Quality Rules

- Every expected result must be measurable
- No vague expected results ("Verify it works" → REJECTED)
- All assumptions explicitly labeled
