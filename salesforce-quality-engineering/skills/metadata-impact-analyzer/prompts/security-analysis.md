---
title: Security Analysis
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

# Security Analysis

## Purpose

Reusable prompt for structured Metadata Impact Analyzer output.

## Prompt

```
Analyze security impact of the metadata change: CRUD, FLS, sharing, profiles, permission sets, Experience Cloud. Produce Security Impact section plus SOQL validations for access.
```

## Required Output Sections

1. Security Impact
2. Recommended SOQL Validations
3. Recommended Manual Tests
4. Risk Rating

## Quality Gate

- Dependency analysis MUST appear before test recommendations.
- All sections labeled; assumptions explicit.
- No invented coverage %, SLA, or certification levels.

## Related Documents

- [SKILL.md](../SKILL.md)
- [../templates/metadata-impact-report.md](../templates/metadata-impact-report.md)
