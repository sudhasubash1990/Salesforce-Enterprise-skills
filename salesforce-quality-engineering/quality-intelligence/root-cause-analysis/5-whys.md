---
title: 5 Whys
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Knowledge Article
version: 0.9.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, root-cause-analysis]
keywords: [5-whys, defect-intelligence, quality-analytics]
---

# 5 Whys

**Scope:** Sprint 7 Defect Intelligence & Quality Analytics — prevention-first QE advisor. Reuse Sprint 5/6 defect templates and ADO bug guidance; do not invent metrics without data.

**Version:** 0.9.0

---

## Purpose

Use 5 Whys for focused incident RCA.
## Business Context

- Defects consume cost at every escape stage—prevention beats late detection.
- Enterprise governance needs comparable classification, RCA, and trend signals.
## Overview

- Ask why until process/system cause emerges
- Stop at actionable control, not blame
## Inputs

- Defect records / bug work items
- Requirement and test evidence
- Environment and release context
## Outputs

- Classifications, scores, or analysis narrative
- Preventive / corrective recommendations
## Process

- State problem
- Ask why with evidence
- Document chain
- Define CAPA
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

- How would you apply 5 Whys on a Salesforce release?
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
- **Next:** [Fishbone Diagram](fishbone-diagram.md)
- **See Also:** [README.md](README.md)

## Future Enhancements

- Deeper Salesforce component pattern catalogs
- Optional metric calculators with validated inputs
