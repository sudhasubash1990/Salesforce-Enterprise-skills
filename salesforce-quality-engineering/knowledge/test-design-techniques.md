---
title: Test Design Techniques
module: Salesforce Quality Engineering
category: Knowledge
document_type: Knowledge Article
version: 0.4.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-07-17
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/knowledge/test-design-engine.md
  - salesforce-quality-engineering/knowledge/requirement-analysis.md
keywords: [test-design-techniques]
tags: [knowledge, sprint-3, test-design]
---

# Test Design Techniques

**Purpose:** Catalog of enterprise test design techniques and when to select them.

**Scope:** Selection guidance. Deep articles linked below. Aligns to ISTQB-style black-box techniques plus Salesforce validation themes.

**Owner:** QE Practice Lead

**Version:** 0.4.0

**Status:** Draft (Sprint 3)

---

## Technique Selection Decision Framework

| If you see… | Prefer |
|-------------|--------|
| Clear happy path AC | [positive-testing.md](positive-testing.md) |
| Rules, rejects, invalid input | [negative-testing.md](negative-testing.md) |
| Numeric/date/string limits | [boundary-testing.md](boundary-testing.md) + [equivalence-partitioning.md](equivalence-partitioning.md) |
| Combinations of conditions → actions | [decision-table-testing.md](decision-table-testing.md) |
| Status / lifecycle objects | [state-transition-testing.md](state-transition-testing.md) |
| Many independent parameters | [pairwise-testing.md](pairwise-testing.md) |
| Thin AC / high uncertainty | [exploratory-testing.md](exploratory-testing.md) + [error-guessing.md](error-guessing.md) |
| Limited time / uneven risk | [risk-based-testing.md](risk-based-testing.md) |
| CRUD on objects | CRUD Validation |
| Business rules / VR / Flow decisions | Business Rule Validation |
| Personas / FLS / sharing | [security-testing.md](security-testing.md) |
| APIs / middleware | [integration-testing.md](integration-testing.md) + [api-testing.md](api-testing.md) |
| Seed / mandatory / formats | Data Validation |
| Layouts / Lightning UX | UI Validation |
| Multi-browser / a11y / L10n | Awareness only unless in scope |

## Enterprise Technique Catalog

| Technique | Article / note |
|-----------|----------------|
| Positive Testing | [positive-testing.md](positive-testing.md) |
| Negative Testing | [negative-testing.md](negative-testing.md) |
| Boundary Value Analysis | [boundary-testing.md](boundary-testing.md) |
| Equivalence Partitioning | [equivalence-partitioning.md](equivalence-partitioning.md) |
| Decision Table Testing | [decision-table-testing.md](decision-table-testing.md) |
| State Transition Testing | [state-transition-testing.md](state-transition-testing.md) |
| Error Guessing | [error-guessing.md](error-guessing.md) |
| Exploratory Testing | [exploratory-testing.md](exploratory-testing.md) |
| Risk-Based Testing | [risk-based-testing.md](risk-based-testing.md) |
| Pairwise Testing | [pairwise-testing.md](pairwise-testing.md) |
| CRUD Validation | Create/Read/Update/Delete (+ undelete if used) per object/persona |
| Business Rule Validation | Map each rule to at least one scenario |
| Security Validation | [security-testing.md](security-testing.md) |
| Integration Validation | [integration-testing.md](integration-testing.md) |
| Data Validation | Formats, mandatory, referential integrity, volumes |
| UI Validation | Visibility, requiredness, inline edit, messages |
| API Validation | [api-testing.md](api-testing.md) |
| Cross Browser Testing | Only if Experience/Lightning browser matrix in scope |
| Accessibility Awareness | Flag if Experience/public UI; do not invent WCAG claims |
| Localization Awareness | Flag if multi-locale; confirm with BA |

## Related Documents

- [test-design-engine.md](test-design-engine.md)
- [functional-testing.md](functional-testing.md)

## Navigation

- **Previous:** [test-design-engine.md](test-design-engine.md)
- **Next:** [test-coverage-model.md](test-coverage-model.md)
