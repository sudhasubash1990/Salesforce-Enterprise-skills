---
title: Generate Functional Tests Prompt
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-functional-testing, generate-functional-tests]
---

# Generate Functional Tests

```
Load skills/salesforce-functional-testing/SKILL.md.

Business Scenario: <describe the business process under test>
Cloud(s): <Service Cloud | Sales Cloud | Experience Cloud | multiple>
Personas: <list personas/roles involved>
Objects: <list Salesforce objects in scope>
Configuration: <describe relevant automation, validation rules, approval processes>

Produce all 15 output schema sections:
1. Intent
2. Context
3. Assumptions
4. Scope
5. Risk Assessment
6. Reasoning
7. Cloud Analysis
8. Object/Feature Coverage
9. Test Strategy
10. Test Scenarios (Positive, Negative, Boundary, Permission, Integration, E2E)
11. Business Rule Validation
12. Persona Matrix
13. Quality Gates
14. Dependencies
15. Recommended Next Actions

Chain PTA for permission scenarios.
Chain SOVA for backend verification.
Chain TDG for test data prerequisites.
Do not invent coverage percentages.
All expected results must be measurable.
```

## Required Output Sections

All 15 sections from the output schema in [SKILL.md](../SKILL.md).

## Notes

- Confirm cloud scope before generating scenarios
- Include positive, negative, boundary, and permission paths
- Chain downstream skills rather than duplicating their output
