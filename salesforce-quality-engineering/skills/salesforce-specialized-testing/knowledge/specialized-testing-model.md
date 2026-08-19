---
title: Specialized Testing Model
module: Salesforce Quality Engineering
category: QE Specialized Skill Knowledge
document_type: Knowledge Article
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, orchestration-model]
---

# Specialized Testing Model

## Purpose

Orchestration model for determining which specialized testing dimensions are required for a given Salesforce implementation or change.

## Dimension Selection Decision Tree

```
Implementation Context
│
├─ Security model changes (profiles, PSs, sharing, OWD, roles)?
│   └─ YES → Security Testing → Chain PTA
│
├─ External system connectivity (API, middleware, events)?
│   └─ YES → Integration Testing + API Testing
│
├─ Data changes (migration, ETL, new objects, field changes)?
│   └─ YES → Data Testing → Chain DMQA / TDG
│
├─ Performance-sensitive (bulk data, concurrent users, SLA)?
│   └─ YES → Performance Advisory (no invented metrics)
│
├─ UI components (LWC, Experience Cloud, custom pages)?
│   └─ YES → Accessibility Testing + Compatibility Testing
│
├─ Mobile requirements (Salesforce Mobile, FSL, responsive)?
│   └─ YES → Mobile Testing
│
├─ Existing functionality impacted by changes?
│   └─ YES → Regression Testing → Chain RBRR
│
└─ Deployment to target environment?
    └─ YES → Release Testing → Chain MIA
```

## Dimension Applicability Matrix

| Trigger | Security | Integration | Data | API | Performance | Accessibility | Mobile | Compat | Regression | Release |
|---------|----------|-------------|------|-----|-------------|---------------|--------|--------|------------|---------|
| New custom object | ✓ | — | ✓ | — | — | — | — | — | ✓ | ✓ |
| New integration | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ |
| Permission changes | ✓ | — | — | — | — | — | — | — | ✓ | ✓ |
| Experience Cloud site | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Data migration | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ |
| LWC component | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Flow automation | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ |
| Bulk API usage | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ |

## Chain Rules

1. **Never duplicate** a downstream skill's detailed analysis
2. SST produces the **assessment** — downstream skill produces the **test scenarios**
3. If a dimension is "Not Required," skip its detailed section but note rationale in the dimension matrix
4. Performance dimension is **advisory only** — measurements come from performance engineering

## Related

- [SKILL.md](../SKILL.md)
- [PTA](../../permission-testing-agent/SKILL.md)
- [DMQA](../../data-migration-qa/SKILL.md)
- [MIA](../../metadata-impact-analyzer/SKILL.md)
- [RBRR](../../risk-based-regression/SKILL.md)
