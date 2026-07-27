---
title: Flow Review
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

# Flow Review

## Purpose

Reusable prompt for structured Metadata Impact Analyzer output.

## Prompt

```
Review Flow metadata change: entry criteria, versions, subflows, Apex actions, order of execution. Dependency analysis first.
```

## Required Output Sections

1. Dependency Analysis
2. Automation Impact
3. Regression Scope
4. Risk Rating

## Quality Gate

- Dependency analysis MUST appear before test recommendations.
- All sections labeled; assumptions explicit.
- No invented coverage %, SLA, or certification levels.

## Related Documents

- [SKILL.md](../SKILL.md)
- [../templates/metadata-impact-report.md](../templates/metadata-impact-report.md)
