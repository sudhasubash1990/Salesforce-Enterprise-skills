---
title: Generate Apex Test Data Factory
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator, prompt]
---

# Generate Apex Test Data Factory

## Prompt

```
Act as Salesforce Test Data Generator (TDG). Provide Business Scenario, Data Requirements, and Objects/Relationships BEFORE record payloads. Produce all 14 sections per SKILL.md. Synthetic data only; never real PII. Include Cleanup Strategy and SOQL stubs. Label volume assumptions. Context:
[paste]
Focus: Apex factory / @TestSetup stubs; SeeAllData=false.
```

## Required Output Sections

1. Executive Summary
2. Business Scenario
3. Data Requirements
4. Objects Involved
5. Relationship Diagram (logical)
6. Generated Test Data Structure
7. Validation Rule Considerations
8. Security Considerations
9. Data Volume Strategy
10. Automation Opportunities
11. Recommended SOQL Validation
12. Cleanup Strategy
13. Risks
14. QA Recommendations

## Quality Gate

- Business Scenario, Data Requirements, and Objects/Relationships BEFORE payloads.
- Synthetic data only; never real PII.
- Include Cleanup Strategy and SOQL stubs; label volume assumptions.
