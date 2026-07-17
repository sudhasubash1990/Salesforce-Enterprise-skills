---
title: Requirement Analysis
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
  - salesforce-quality-engineering/knowledge/requirement-review-framework.md
  - salesforce-quality-engineering/knowledge/requirements-quality-checklist.md
  - salesforce-quality-engineering/skill.md
  - salesforce-quality-engineering/brain/thinking-model.md
keywords: [requirement-analysis, engine]
tags: [knowledge, sprint-2, requirement-analysis]
---

# Requirement Analysis Engine

**Purpose:** Mandatory first-step engine for inspecting, validating, challenging, and enriching Salesforce business requirements before any testing artifacts are created.

**Scope:** Analysis philosophy, 10-step sequence, Salesforce component scan, and mandatory output sections. Does **not** generate test cases, RTM, or templates.

**Owner:** QE Practice Lead

**Version:** 0.3.0

**Status:** Draft (Sprint 2)

---

## Philosophy

Quality Engineering converts BA requirements into **testable scope**. The Requirement Analysis Engine is mandatory before:

Test Strategy · Test Plan · RTM · Test Scenarios · Test Cases · Automation · Regression · UAT · Defect Prevention

**Never jump directly to test cases.** Always analyse first.

Cross-link BA authorship standards; do not rewrite BRDs unless asked:

- [BA skill](../../salesforce-business-analyst/skill.md)
- [BA requirement types](../../salesforce-business-analyst/knowledge/requirement-types.md)

## When to Run

| Trigger | Action |
|---------|--------|
| User pastes story / epic / feature / BRD / FRD excerpt | Run full engine |
| Request for test strategy / plan / scenarios / cases | Run engine first, then proceed (later sprints) |
| Backlog refinement / sprint planning QE support | Run engine |

## Ten-Step Analysis Sequence

| Step | Activity | Detail |
|------|----------|--------|
| 1 | Understand Business Context | Industry, program, release, constraints, clouds |
| 2 | Identify Business Objective | Outcome and success measure |
| 3 | Identify Stakeholders | Who cares, who decides, who tests, who uses |
| 4 | Understand Current Process (As-Is) | Today’s journey and pain |
| 5 | Understand Future Process (To-Be) | Target journey and change |
| 6 | Identify Functional Requirements | Behaviours and journeys in scope |
| 7 | Identify Non-Functional Requirements | Perf, usability, availability, audit, compliance |
| 8 | Identify Business Rules | See [business-rules.md](business-rules.md) |
| 9 | Identify Acceptance Criteria | See [acceptance-criteria.md](acceptance-criteria.md) |
| 10 | Identify Salesforce Components | Metadata impact scan below |

Align with Thinking Model stages 1–27 in [thinking-model.md](../brain/thinking-model.md).

## Salesforce Component Scan (Step 10)

For each item: **Known / Assumed / Unknown / Risk if wrong**.

| Area | Examples |
|------|----------|
| Objects | Standard / custom |
| Fields | Required, picklist, formula, rollup |
| Relationships | Lookup, M-D, junction |
| Flows | Record-triggered, screen, scheduled, orchestration |
| Validation Rules | Error paths |
| Approval Processes | Entry, recall, reject |
| Reports / Dashboards | Ops and KPI surfaces |
| Notifications / Email Templates | Alerts and templates |
| Permission Sets / Profiles | Capability and CRUD/FLS |
| Queues | Assignment / Omni |
| OmniStudio | FlexCards, Omniscripts, DataRaptors, IPs |
| Agentforce | Actions, grounding, guardrails |
| Custom Metadata / Settings | Config-driven behaviour |
| Integrations | APIs, middleware, events, files |
| Apex | Triggers, classes, batch, queueable |
| Platform Events | Pub/sub |
| Scheduled / Batch Jobs | Cadence and failure handling |

## Mandatory Output (When Requirement Provided)

Produce **analysis only**—no test cases:

1. Executive Summary  
2. Business Context  
3. Requirement Summary  
4. Requirement Quality Assessment — [requirements-quality-checklist.md](requirements-quality-checklist.md)  
5. Requirement Gaps  
6. Missing Information  
7. Business Rules  
8. Acceptance Criteria Review  
9. Salesforce Components  
10. Dependencies  
11. Assumptions  
12. Open Questions — [question-generation-framework.md](question-generation-framework.md)  
13. Risks — [requirement-risk-analysis.md](requirement-risk-analysis.md)  
14. Scope — [scope-analysis.md](scope-analysis.md)  
15. Recommended Testing Areas (intent only)  
16. Regression Impact (intent only)  
17. Automation Opportunities (intent only)  
18. Recommendations  
19. Next Steps  

## Related Frameworks

| Topic | Article |
|-------|---------|
| Review workflow | [requirement-review-framework.md](requirement-review-framework.md) |
| Validation defects | [requirement-review-framework.md](requirement-review-framework.md#requirement-validation-catalog) |
| Questions | [question-generation-framework.md](question-generation-framework.md) |
| Risks | [requirement-risk-analysis.md](requirement-risk-analysis.md) |
| Scope | [scope-analysis.md](scope-analysis.md) |
| Traceability | [traceability.md](traceability.md) |
| Stakeholders | [stakeholder-analysis.md](stakeholder-analysis.md) |
| Quality score | [requirements-quality-checklist.md](requirements-quality-checklist.md) |

## Related Documents

- [../skill.md](../skill.md)
- [../brain/brain.md](../brain/brain.md)
- [README.md](README.md)

## Future Enhancements

- Sprint 3: feed Recommended Testing Areas into Test Design Engine
- Sprint 5: bind outputs to templates (not in Sprint 2)

## Navigation

- **Previous:** [README.md](README.md)
- **Next:** [requirement-review-framework.md](requirement-review-framework.md)
- **See Also:** [thinking-model.md](../brain/thinking-model.md)
