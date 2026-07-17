---
title: Stakeholder Analysis
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
  - salesforce-quality-engineering/brain/cross-module-map.md
  - salesforce-business-analyst/knowledge/stakeholder-analysis.md
keywords: [stakeholders]
tags: [knowledge, sprint-2]
---

# Stakeholder Analysis (QE Lens)

**Purpose:** Identify stakeholders who affect requirement quality, testability, and sign-off—from a Quality Engineering perspective.

**Scope:** QE-oriented stakeholder questions. Full RACI methodology remains with BA: [BA stakeholder-analysis](../../salesforce-business-analyst/knowledge/stakeholder-analysis.md).

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Stakeholder Types for Requirement Analysis

| Stakeholder | QE interest |
|-------------|-------------|
| Business Owner / PO | Outcome, priority, UAT ownership |
| End User / Persona | Journey realism, usability |
| Business Analyst | AC quality, rules, scope clarity |
| Solution / Technical Architect | Component impact, NFRs, integrations |
| Developer | Build feasibility, technical constraints |
| QE / Test Lead | Testability, environments, evidence |
| Security / Compliance | Access, audit, regulated controls |
| DevOps / Release | Deployability, smoke, rollback |
| Production Support | Operability, known errors |
| Delivery / PM | Dates, dependencies, RAID |

## Analysis Questions

1. Who accepts the story in UAT?
2. Who can clarify business rules within 24–48 hours?
3. Who owns integration contracts?
4. Who grants security design decisions?
5. Who is impacted operationally after go-live?

## Output Shape

```markdown
### Stakeholders
| Role | Name/Team (if known) | Interest | Clarification owner? |
|------|----------------------|----------|----------------------|
| … | … | … | Yes/No |
```

If unknown, generate Critical/High questions via [question-generation-framework.md](question-generation-framework.md).

## Related Documents

- [requirement-analysis.md](requirement-analysis.md)
- [../brain/cross-module-map.md](../brain/cross-module-map.md)

## Future Enhancements

- Persona packs per industry scenario (later)

## Navigation

- **Previous:** [traceability.md](traceability.md)
- **Next:** [business-rules.md](business-rules.md)
- **See Also:** [../brain/cross-module-map.md](../brain/cross-module-map.md)
