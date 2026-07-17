---
title: Salesforce Quality Intelligence
module: Salesforce Quality Engineering
category: Quality Intelligence
document_type: Knowledge Article
version: 0.9.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
tags: [quality-intelligence, sprint-7, knowledge-base]
keywords: [salesforce-quality-intelligence, defect-intelligence, quality-analytics]
---

# Salesforce Quality Intelligence

**Scope:** Sprint 7 Defect Intelligence & Quality Analytics — prevention-first QE advisor. Reuse Sprint 5/6 defect templates and ADO bug guidance; do not invent metrics without data.

**Version:** 0.9.0

---

## Purpose

Identify recurring defect areas across VR, Flows, Apex, security, integrations, packages, OmniStudio, Agentforce, industry clouds.
## Business Context

- Defects consume cost at every escape stage—prevention beats late detection.
- Enterprise governance needs comparable classification, RCA, and trend signals.
## Overview

- Scan defects against Salesforce component tags
- Prioritize prevention for high-frequency + high-impact components
- Ground specifics in 4A/4B knowledge articles
## Inputs

- Defect records / bug work items
- Requirement and test evidence
- Environment and release context
## Outputs

- Classifications, scores, or analysis narrative
- Preventive / corrective recommendations
## Process

- Tag defects by component family
- Rank by frequency × severity × business criticality
- Recommend targeted tests, reviews, and automation
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

- How would you apply Salesforce Quality Intelligence on a Salesforce release?
- What data is required before drawing conclusions?
- How does this reduce defect leakage?
## Related Documents

- [../../knowledge/automation/README.md](../../knowledge/automation/README.md)
- [../../knowledge/security/README.md](../../knowledge/security/README.md)
- [../../knowledge/clouds/README.md](../../knowledge/clouds/README.md)
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
- **Next:** [Quality Health Report](quality-health-report.md)
- **See Also:** [README.md](README.md)

## Future Enhancements

- Deeper Salesforce component pattern catalogs
- Optional metric calculators with validated inputs
