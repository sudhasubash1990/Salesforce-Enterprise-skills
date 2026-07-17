---
title: Defect Density
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Knowledge Article
version: 0.9.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, quality-metrics]
keywords: [defect-density, defect-intelligence, quality-analytics]
---

# Defect Density

**Scope:** Sprint 7 Defect Intelligence & Quality Analytics — prevention-first QE advisor. Reuse Sprint 5/6 defect templates and ADO bug guidance; do not invent metrics without data.

**Version:** 0.9.0

---

## Purpose

Define and interpret Defect Density for Salesforce QE governance.
## Business Context

- Defects consume cost at every escape stage—prevention beats late detection.
- Enterprise governance needs comparable classification, RCA, and trend signals.
## Overview

- Defects found relative to size (stories/FP/LOC proxy).
- **Formula (conceptual):** Defects / Size unit
## Inputs

- Defect records / bug work items
- Requirement and test evidence
- Environment and release context
## Outputs

- Classifications, scores, or analysis narrative
- Preventive / corrective recommendations
## Process

- Confirm data source and period
- Compute only with available counts—never invent
- Compare to agreed thresholds; explain drivers
- Recommend actions (test, process, automation, env)
## Examples

- Interpretation guidance for Defect Density must cite numerator/denominator sources
- Thresholds are program-specific—propose bands, do not assert universal SLAs
## Best Practices

- Publish definition beside the number
- Pair with trend, not a single sprint snapshot
- Visualization: trend line + threshold band
## Common Mistakes

- Inventing coverage or leakage percentages
- RCA that stops at 'developer error' without process cause
- Ignoring environment/config as first-class causes
## Interview Questions

- How would you apply Defect Density on a Salesforce release?
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

- **Previous:** [README](README.md)
- **Next:** [Defect Leakage](defect-leakage.md)
- **See Also:** [README.md](README.md)

## Future Enhancements

- Deeper Salesforce component pattern catalogs
- Optional metric calculators with validated inputs
