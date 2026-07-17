---
title: Test Design Engine
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
keywords: [test-design-engine]
tags: [knowledge, sprint-3, test-design]
---

# Test Design Engine

**Purpose:** Mandatory engine that decides WHAT to test and WHY before HOW (detailed cases later).

**Scope:** 10-step design sequence, scenario objectives, coverage, regression, automation readiness. Does **not** generate detailed test cases, ADO artifacts, or automation scripts.

**Owner:** QE Practice Lead

**Version:** 0.4.0

**Status:** Draft (Sprint 3)

---

## Philosophy

Test design turns analysed requirements into a **coverage strategy**. Cases and scripts come later.

**Prerequisites:** Run [requirement-analysis.md](requirement-analysis.md) first when a requirement is provided. Do not design tests on unanalysed, blocked Critical gaps without labeling assumptions.

## When to Run

| Trigger | Action |
|---------|--------|
| After Requirement Analysis (or sufficient quality band) | Run Test Design Engine |
| Request for scenarios / coverage / regression / automation candidates | Run engine |
| Request for detailed test cases | Produce scenarios + techniques first; defer case steps to later sprint |

## Ten-Step Sequence

| Step | Activity | Output |
|------|----------|--------|
| 1 | Understand Requirement | Context from analysis / story |
| 2 | Identify Business Goal | Outcome under test |
| 3 | Identify Salesforce Components | Impacted metadata |
| 4 | Identify Testable Features | Behaviours that can fail observably |
| 5 | Identify Risks | Links to [risk-based-testing.md](risk-based-testing.md) |
| 6 | Select Test Design Technique(s) | [test-design-techniques.md](test-design-techniques.md) |
| 7 | Identify Test Scenarios | Objectives only — see below |
| 8 | Determine Test Coverage | [test-coverage-model.md](test-coverage-model.md) |
| 9 | Determine Regression Scope | [regression-planning.md](regression-planning.md) |
| 10 | Recommend Automation Candidates | Readiness only — no scripts |

## Test Scenario Generation Framework

For every requirement, identify **scenario objectives** (not steps):

| Scenario type | Intent |
|---------------|--------|
| Business | Outcome / journey value |
| Functional | Core behaviour vs AC |
| Negative | Invalid / rejected paths |
| Exception | System / timeout / lock failures |
| Validation | Field / VR / rule enforcement |
| Permission | Persona allowed / denied |
| Integration | Upstream / downstream contracts |
| Data | Seed, mandatory, migration edge |
| Regression | Neighbor features at risk |
| Automation Candidates | High-ROI repeatable checks |

## Risk Priority Labels

| Priority | Use when |
|----------|----------|
| **Business Critical** | Customer, revenue, safety, compliance, go-live blocker |
| **High** | Core AC / primary persona / primary integration |
| **Medium** | Important variants, secondary personas |
| **Low** | Cosmetic, rare edge, deferred |

Explain **why** each scenario gets its priority ([risk-based-testing.md](risk-based-testing.md)).

## Automation Readiness Assessment

| Classification | Meaning |
|----------------|---------|
| Suitable for Automation | Stable, repeatable, high regression value |
| Manual Only | Exploratory, subjective UX, unstable UI, one-off |
| API Automation | Data/API contract better than UI |
| UI Automation | User-path confidence needed |
| Regression Automation | Pack candidate for every release |
| Smoke Automation | Build/deploy confidence |

Explain reasoning. **No scripts** in Sprint 3.

## Quality Coverage Matrix (Reusable)

Map each row:

```
Requirement → Business Rule → Salesforce Component → Test Scenario
  → Testing Technique → Priority → Automation Recommendation → Regression Scope
```

| Column | Guidance |
|--------|----------|
| Requirement | Story/AC/BR ID |
| Business Rule | Rule ID or implied |
| Salesforce Component | Object/field/Flow/… |
| Test Scenario | Objective ID `TS-###` |
| Testing Technique | From techniques catalog |
| Priority | Business Critical / High / Medium / Low |
| Automation Recommendation | Classification above |
| Regression Scope | In / Out / Conditional |

## Mandatory Output (Sprint 3)

When designing tests for a requirement, produce:

1. Design summary (goal, components, risks)
2. Selected techniques + rationale
3. Test scenarios (objectives by type)
4. Quality Coverage Matrix (table)
5. Coverage assessment + gaps ([test-coverage-model.md](test-coverage-model.md))
6. Regression scope recommendation
7. Automation readiness recommendations
8. Assumptions / open questions
9. Next steps (e.g., case authoring in later sprint)

**Do not** output detailed Given/When/Then test case steps unless the user explicitly insists—and still prefer scenarios first.

## Salesforce-Specific Design Areas

When selecting scenarios, consider components listed in Step 3 and deep-dive articles: objects, fields, relationships, validation rules, record types, page layouts, Lightning pages, Flows, approvals, reports, dashboards, permission sets, profiles, sharing, queues, email alerts, scheduled/batch jobs, platform events, custom metadata/settings, Experience Cloud, OmniStudio, Agentforce, CPQ, Field Service.

## Related Documents

- [test-design-techniques.md](test-design-techniques.md)
- [test-coverage-model.md](test-coverage-model.md)
- [requirement-analysis.md](requirement-analysis.md)
- [../skill.md](../skill.md)

## Future Enhancements

- Sprint 5: bind matrix to templates
- Later: detailed test case generation

## Navigation

- **Previous:** [requirement-analysis.md](requirement-analysis.md)
- **Next:** [test-design-techniques.md](test-design-techniques.md)
- **See Also:** [test-coverage-model.md](test-coverage-model.md)
