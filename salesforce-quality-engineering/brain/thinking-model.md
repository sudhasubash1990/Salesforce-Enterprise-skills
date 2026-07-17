---
title: Thinking Model
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
  - salesforce-quality-engineering/brain/brain.md
  - salesforce-quality-engineering/brain/decision-framework.md
keywords: [thinking-model, stages]
tags: [brain, thinking]
---

# Thinking Model

**Purpose:** Mandatory 30-stage decision flow the AI must complete before generating QE outputs.

**Scope:** Stage catalog and per-stage outcomes. Orchestration of when to pause vs proceed lives in [brain.md](brain.md) and [decision-framework.md](decision-framework.md).

**Owner:** QE Practice Lead

**Version:** 0.2.1

**Status:** Draft (Sprint 1 — modular Brain)

---

## Hard Rule

Before generating any QE output (strategy, plan, scenarios, cases, reports, recommendations), complete the stages below. **Never skip reasoning. Never jump directly into creating test cases.**

## Mandatory 30-Stage Reasoning

| # | Stage | What to establish |
|---|-------|-------------------|
| 1 | Understand Business Context | Industry, program goals, release, stakeholders, constraints |
| 2 | Understand User Story | Persona, goal, benefit, narrative, linked requirements |
| 3 | Validate Requirement Completeness | Gaps in scope, AC, rules, data, permissions, integrations |
| 4 | Identify Business Objectives | Outcomes and success measures the change must support |
| 5 | Identify Business Rules | Explicit and implied rules that constrain behaviour |
| 6 | Identify Functional Scope | In-scope behaviours and user journeys |
| 7 | Identify Out of Scope Items | Explicit exclusions and deferred items |
| 8 | Identify Salesforce Components | Clouds, apps, Lightning pages, Experience sites, OmniStudio |
| 9 | Identify Objects | Standard/custom objects impacted |
| 10 | Identify Fields | Required/optional fields, picklists, formulas, rollups |
| 11 | Identify Relationships | Lookups, master-detail, junctions, hierarchy |
| 12 | Identify Record Types | Record types and page-layout implications |
| 13 | Identify Validation Rules | Declarative validations and error paths |
| 14 | Identify Approval Processes | Approvals, entry criteria, recall/reject paths |
| 15 | Identify Flows | Record-triggered, screen, scheduled, orchestration |
| 16 | Identify Apex | Triggers, classes, batch, queueable, LWC controllers (test impact—not code design) |
| 17 | Identify Integrations | APIs, middleware, MuleSoft, events, files, ETL |
| 18 | Identify Reports | Report types and operational reports affected |
| 19 | Identify Dashboards | Dashboards and KPI surfaces affected |
| 20 | Identify Notifications | Email, custom notifications, Chatter, Omni alerts |
| 21 | Identify Profiles | Profile-level CRUD/FLS and app access (legacy posture) |
| 22 | Identify Permission Sets | Permission sets / groups granting capability |
| 23 | Identify Sharing Rules | OWD, sharing rules, teams, manual sharing impacts |
| 24 | Identify Data Dependencies | Seed data, master data, migration, environments |
| 25 | Identify Risks | Product, process, data, integration, schedule, compliance risks |
| 26 | Identify Assumptions | Labeled assumptions with impact if wrong |
| 27 | Identify Open Questions | Clarifications required before confident delivery |
| 28 | Recommend Testing Approach | Levels, techniques intent, environments, evidence |
| 29 | Recommend Automation Scope | What to automate vs not, and why (purpose-driven) |
| 30 | Recommend Regression Scope | What must re-run; impact-based pack selection |

## Stage Outcomes (Internal Checklist)

For each stage, note:

| Tag | Meaning |
|-----|---------|
| **Known (fact)** | Stated by user or confirmed artifact |
| **Assumed** | Inferred; must appear as `A#` in the response |
| **Unknown / open question** | Must ask or flag as blocker |
| **Risk if wrong** | Impact if the assumption/fact is incorrect |

If stages **3**, **5**, or **27** expose material gaps: **pause deliverable generation**, ask clarification questions, and document assumptions before proceeding. See [decision-framework.md](decision-framework.md).

## Stage Bands (Quick Map)

| Band | Stages | Focus |
|------|--------|-------|
| Context & completeness | 1–7 | Business, story, scope, rules |
| Salesforce impact | 8–24 | Components through data dependencies |
| Uncertainty | 25–27 | Risks, assumptions, questions |
| Recommendations | 28–30 | Testing, automation, regression |

## Related Documents

- [brain.md](brain.md)
- [decision-framework.md](decision-framework.md)
- [skill.md](../skill.md)

## Future Enhancements

- Sprint 2: deeper completeness checks per stage 3
- Sprint 3: map stages 28–30 to test design engine outputs

## Navigation

- **Previous:** [brain.md](brain.md)
- **Next:** [decision-framework.md](decision-framework.md)
- **See Also:** [response-guidelines.md](response-guidelines.md)
