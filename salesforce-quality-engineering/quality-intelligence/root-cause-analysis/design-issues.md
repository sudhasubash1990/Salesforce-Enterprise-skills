---
title: Design Issues
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Knowledge Article
version: 0.9.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, root-cause-analysis]
keywords: [design-issues, defect-intelligence, quality-analytics]
---

# Design Issues

**Scope:** Sprint 7 Defect Intelligence & Quality Analytics — prevention-first QE advisor. Reuse Sprint 5/6 defect templates and ADO bug guidance; do not invent metrics without data.

**Version:** 0.9.0

---

## Purpose

Incorrect fit-gap or component design choices.
## Business Context

- Defects consume cost at every escape stage—prevention beats late detection.
- Enterprise governance needs comparable classification, RCA, and trend signals.
## Overview

- Design Issues supports data-driven quality decisions across Salesforce delivery.
- Align with ISTQB Advanced Test Management and TMMi improvement themes.
## Inputs

- Defect records / bug work items
- Requirement and test evidence
- Environment and release context
## Outputs

- Classifications, scores, or analysis narrative
- Preventive / corrective recommendations
## Process

- Gather evidence (do not invent counts)
- Classify and analyse
- Recommend actions with owners
- Feed continuous improvement and predictive risk
## Examples

- Illustrative only — replace with program data
- Always state data period and source system (ADO/Jira/etc.)
## Best Practices

- Separate Severity (impact) from Priority (urgency)
- Link defects to Story/Case IDs
- Prefer prevention actions over retest-only closures
## Common Mistakes

- Inventing coverage or leakage percentages
- RCA that stops at 'developer error' without process cause
- Ignoring environment/config as first-class causes
## Interview Questions

- How would you apply Design Issues on a Salesforce release?
- What data is required before drawing conclusions?
- How does this reduce defect leakage?
## Related Documents

- [QE Brain (Sprint 1)](../../brain/README.md)
- [Requirement Analysis (Sprint 2)](../../knowledge/requirement-analysis.md)
- [Test Design Engine (Sprint 3)](../../knowledge/test-design-engine.md)
- [Platform Foundation 4A](../../knowledge/platform/README.md)
- [Enterprise Knowledge 4B](../../knowledge/clouds/README.md)
- [Documentation Generator (Sprint 5)](../../templates/README.md)
- [ADO Delivery Intelligence (Sprint 6)](../../ado/README.md)
- [Defect Report Template](../../templates/defect-report.md)
- [Defect RCA Template](../../templates/defect-rca-report.md)
- [README.md](README.md)
- [../README.md](../README.md)

## Navigation

- **Previous:** [Requirement Issues](requirement-issues.md)
- **Next:** [Development Issues](development-issues.md)
- **See Also:** [README.md](README.md)

## Future Enhancements

- Deeper Salesforce component pattern catalogs
- Optional metric calculators with validated inputs
