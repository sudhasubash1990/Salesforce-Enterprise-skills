---
title: Regression Analysis
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

# Regression Analysis

## Purpose

Reusable prompt for structured Metadata Impact Analyzer output.

## Prompt

```
Given the metadata impact analysis below, produce regression scope (In/Out/Conditional), automation candidates, and manual test priorities. Dependency analysis must be referenced.
```

## Required Output Sections

1. Regression Scope
2. Automation Candidates
3. Recommended Manual Tests
4. Assumptions

## Quality Gate

- Dependency analysis MUST appear before test recommendations.
- All sections labeled; assumptions explicit.
- No invented coverage %, SLA, or certification levels.

## Related Documents

- [SKILL.md](../SKILL.md)
- [../templates/metadata-impact-report.md](../templates/metadata-impact-report.md)
