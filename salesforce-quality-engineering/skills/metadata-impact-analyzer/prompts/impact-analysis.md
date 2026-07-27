---
title: Impact Analysis
module: Salesforce Quality Engineering
category: Specialized Skill Prompt
document_type: Prompt
version: 0.15.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [metadata-impact-analyzer, prompt]
---

# Impact Analysis

## Purpose

Reusable prompt for structured Metadata Impact Analyzer output.

## Prompt

```
Analyze the Salesforce metadata change below. Perform complete dependency analysis BEFORE any test recommendations. Produce all 16 sections: Executive Summary, Metadata Changed, Dependency Analysis, Business Impact, Technical Impact, Security Impact, Integration Impact, Automation Impact, Reporting Impact, Regression Scope, Deployment Risk, Risk Rating, Automation Candidates, Recommended SOQL Validations, Recommended Manual Tests, Go/No-Go Recommendation. Label assumptions. Do not invent coverage % or SLA values.
```

## Required Output Sections

1. Executive Summary
2. Metadata Changed
3. Dependency Analysis
4. Business Impact
5. Technical Impact
6. Security Impact
7. Integration Impact
8. Automation Impact
9. Reporting Impact
10. Regression Scope
11. Deployment Risk
12. Risk Rating
13. Automation Candidates
14. Recommended SOQL Validations
15. Recommended Manual Tests
16. Go / No-Go Recommendation

## Quality Gate

- Dependency analysis MUST appear before test recommendations.
- All sections labeled; assumptions explicit.
- No invented coverage %, SLA, or certification levels.

## Related Documents

- [SKILL.md](../SKILL.md)
- [../templates/metadata-impact-report.md](../templates/metadata-impact-report.md)
