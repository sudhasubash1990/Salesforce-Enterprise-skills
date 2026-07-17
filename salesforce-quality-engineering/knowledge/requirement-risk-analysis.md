---
title: Requirement Risk Analysis
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
  - salesforce-quality-engineering/brain/decision-framework.md
keywords: [risk, requirement-risk]
tags: [knowledge, sprint-2]
---

# Requirement Risk Analysis

**Purpose:** Identify and structure quality risks discovered during requirement analysis.

**Scope:** Risk categories and required fields per risk. Not a full RAID template (later sprint).

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Risk Categories

| Category | Examples |
|----------|----------|
| **Business Risks** | Wrong outcome; regulatory exposure; CX damage |
| **Functional Risks** | Incomplete journey; status holes; edge cases |
| **Technical Risks** | Complex automation; governor limits; brittle design |
| **Testing Risks** | Untestable AC; env gaps; data scarcity |
| **Data Risks** | Migration gaps; poor master data; volume |
| **Security Risks** | Over-permission; sharing leaks; guest access |
| **Integration Risks** | Contract ambiguity; dual write; failure handling |
| **Deployment Risks** | Activation order; feature flag missing |
| **Production Risks** | No monitoring; unclear rollback; support unreadiness |

## Risk Record Format

For each risk generate:

| Field | Guidance |
|-------|----------|
| **ID** | `RISK-001` … |
| **Description** | What could go wrong |
| **Category** | From table above |
| **Impact** | High / Medium / Low (+ brief effect) |
| **Probability** | High / Medium / Low |
| **Mitigation** | Test, clarify, design, or process action |
| **Owner** | BA / Architect / Dev / QE / PM / Support |
| **Priority** | Critical / High / Medium / Low |

## Heuristics

- Untestable AC → Testing Risk (usually High)
- Integration named without contract → Integration Risk
- Persona UI change without security → Security Risk
- High business value + thin AC → Business + Testing Risk

## Related Documents

- [requirement-analysis.md](requirement-analysis.md)
- [requirements-quality-checklist.md](requirements-quality-checklist.md)
- [../brain/decision-framework.md](../brain/decision-framework.md)

## Future Enhancements

- Link to Sprint 7 Defect Intelligence for escaped defects

## Navigation

- **Previous:** [question-generation-framework.md](question-generation-framework.md)
- **Next:** [scope-analysis.md](scope-analysis.md)
- **See Also:** [traceability.md](traceability.md)
