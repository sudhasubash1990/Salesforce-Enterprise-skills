---
title: Validation Rule Review
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

# Validation Rule Review

## Purpose

Reusable prompt for structured Metadata Impact Analyzer output.

## Prompt

```
Review Validation Rule change: formula dependencies, API save paths, bulk impact, integrations.
```

## Required Output Sections

1. Dependency Analysis
2. Technical Impact
3. Integration Impact
4. Recommended Manual Tests

## Quality Gate

- Dependency analysis MUST appear before test recommendations.
- All sections labeled; assumptions explicit.
- No invented coverage %, SLA, or certification levels.

## Related Documents

- [SKILL.md](../SKILL.md)
- [../templates/metadata-impact-report.md](../templates/metadata-impact-report.md)
