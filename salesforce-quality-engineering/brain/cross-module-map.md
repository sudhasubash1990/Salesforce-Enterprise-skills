---
title: Cross Module Map
module: Salesforce Quality Engineering
category: Brain
document_type: Framework
version: 0.2.1
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/skill.md
  - salesforce-business-analyst/skill.md
  - shared/glossary.md
keywords: [cross-module, collaboration]
tags: [brain, collaboration]
---

# Cross Module Map

**Purpose:** Define how Quality Engineering interacts with BA, Architecture, Development, DevOps, and delivery roles—inputs and outputs for each relationship.

**Scope:** Collaboration contracts only. Do not duplicate BA/architect skill content; link instead.

**Owner:** QE Practice Lead

**Version:** 0.2.1

**Status:** Draft (Sprint 1 — modular Brain)

---

## Value Chain

```
BA (requirements → stories → AC)
        ↓ handoff (testability, RTM, UAT planning)
QE (reason → strategy/plan intent → design → gates → release quality)
        ↓ feedback (defects, coverage gaps, production signals)
BA / Architect / Dev / DevOps / Delivery (updates, build, deploy, go-live)
```

## Partner Map

| Partner | Inputs from them | Outputs to them |
|---------|------------------|-----------------|
| **Business Analyst** | BRD/FRD, stories, AC, process, RAID | Testability gaps, AC improvements, UAT scenario intent, coverage feedback |
| **Solution Architect** | Solution options, integration design, NFRs | Verification focus, risk questions, environment needs |
| **Technical Architect** | Data model, security model, limits | Permission/sharing test intent, governor-risk flags |
| **Developer** | Build notes, technical constraints | Clear scenarios/cases intent, defect quality expectations |
| **DevOps** | Pipeline, environments, release train | Smoke/regression pack intent, deploy validation checks |
| **Project Manager** | Dates, scope cuts, RAID | Quality risks, readiness status, estimation inputs |
| **Delivery Manager** | Governance cadence, steering needs | Executive quality narrative, Go/No-Go inputs |
| **Production Support** | Incidents, known errors, monitoring | Production validation checks, escape RCA inputs |

## BA ↔ QE Rules

| Rule | Detail |
|------|--------|
| Do not duplicate | BA templates, playbooks, knowledge—cross-link |
| UAT ownership | BA owns UAT process playbooks; QE supplies scenario/readiness intent |
| Conflicts | Surface as open questions; do not silent overwrite |
| Canonical BA skill | [../salesforce-business-analyst/skill.md](../../salesforce-business-analyst/skill.md) |

## Architect ↔ QE Rules

- Ask impact questions; do not produce detailed technical design unless asked.
- Flag verification needs for integrations, security, and NFRs.
- Escalate multi-cloud or licensing-impact decisions as open questions.

## Dev / DevOps ↔ QE Rules

- Provide clear, testable intent—not Apex/LWC implementation by default.
- Align smoke/regression packs to release train and environments.
- Never fabricate pipeline or environment state.

## Shared Assets

- [glossary](../../shared/glossary.md)
- [output-standards](../../shared/output-standards.md)
- [capability map](../../shared/salesforce-capability-map.md)

## Related Documents

- [skill.md](../skill.md)
- [consulting-principles.md](consulting-principles.md)
- [../salesforce-business-analyst/skill.md](../../salesforce-business-analyst/skill.md)

## Future Enhancements

- Cross-skill RTM (requirement → design → test) when repo Phase 3 lands

## Navigation

- **Previous:** [response-guidelines.md](response-guidelines.md)
- **Next:** [skill.md](../skill.md)
- **See Also:** [README.md](../README.md)
