---
title: Knowledge — README
module: Salesforce Quality Engineering
category: Knowledge
document_type: Guide
version: 0.6.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/README.md
  - salesforce-quality-engineering/skill.md
  - salesforce-quality-engineering/brain/README.md
keywords: [knowledge]
tags: [knowledge, sprint-2, sprint-3, sprint-4a, sprint-4b]
---

# Knowledge

**Purpose:** Quality Engineering knowledge base — analysis engines, test design, Platform Foundation (4A), and Enterprise Business Knowledge (4B).

**Scope:** Sprint 2–3 engines · Sprint **4A** platform · Sprint **4B** enterprise business layer.

**Owner:** QE Practice Lead

**Version:** 0.6.0

**Status:** Draft (Sprint 4B)

## Sprint 4A — Platform Foundation

| Folder | Focus |
|--------|-------|
| [platform/](platform/README.md) | Architecture, objects, fields, relationships, UI, formulas, CMDT |
| [metadata/](metadata/README.md) | Types, impact, deploy, regression, risks |
| [automation/](automation/README.md) | VR, Flows, Apex async, events, rules |
| [security/](security/README.md) | Profiles, sharing, OWD, MFA, audit |
| [data/](data/README.md) | Model, quality, migration, integrity, LDV, privacy awareness |

## Sprint 4B — Enterprise Business Knowledge

| Folder | Focus |
|--------|-------|
| [clouds/](clouds/README.md) | Sales, Service, Experience, FSL, CPQ, Agentforce, OmniStudio, industry clouds, … |
| [managed-packages/](managed-packages/README.md) | Managed/unlocked, upgrades, packaged metadata, vendor coordination |
| [integration/](integration/README.md) | REST/SOAP/Bulk, events, middleware, OAuth, retries, API limits, sync |
| [performance/](performance/README.md) | Governors, SOQL, LDV, locking, Flow/report/integration performance |
| [release/](release/README.md) | Deploy, smoke/sanity, readiness, Go/No-Go, cutover, hypercare, production readiness |
| [industry/](industry/README.md) | Utilities → Consumer Goods industry starters |

Cross-link Sprint 3 technique articles — do not duplicate. Reuse 4A for platform internals.

## Index — Requirement Analysis Engine (Sprint 2)

| Article | Role |
|---------|------|
| [requirement-analysis.md](requirement-analysis.md) | Engine entry |
| Supporting analysis articles | review, questions, risk, scope, traceability, stakeholders, rules, AC, quality score |

## Index — Test Design Engine (Sprint 3)

| Article | Role |
|---------|------|
| [test-design-engine.md](test-design-engine.md) | Engine entry |
| Techniques / levels / SF-specific testing | Articles at knowledge root |

## Index — Support & governance

| Article | Role |
|---------|------|
| [references.md](references.md) · [checklists.md](checklists.md) | References / checklists |
| [quality-gates.md](quality-gates.md) · [metrics.md](metrics.md) | Gates / metrics (skeleton) |
| [best-practices.md](best-practices.md) · [anti-patterns.md](anti-patterns.md) | Practice guidance |

## Related Brain

- [../brain/README.md](../brain/README.md)

## Related Documents

- [../skill.md](../skill.md)
- [../README.md](../README.md)

## Future Enhancements

- Sprint 5: Documentation Generator / Enterprise QA Deliverables
- Expand `scenarios/` linked to industry + cloud packs

## Navigation

- **Previous:** [../brain/README.md](../brain/README.md)
- **Next:** [platform/README.md](platform/README.md)
- **See Also:** [clouds/README.md](clouds/README.md) · [test-design-engine.md](test-design-engine.md)
