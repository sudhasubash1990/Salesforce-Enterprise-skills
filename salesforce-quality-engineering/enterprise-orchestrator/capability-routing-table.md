---
title: Capability Routing Table
version: 0.12.1
tags: [enterprise-orchestrator, routing]
---

# Capability Routing Table

## Purpose

Map request signals to sprint capabilities. Used by the Enterprise Orchestrator—**not** a standalone knowledge base.

## Business Context

Agents need a deterministic keyword → engine map so routing stays consistent across sessions.

## Assessment Criteria

Match the **strongest** primary intent; add supporting capabilities only when signals co-occur.

## Inputs / Outputs

- **In:** Request keywords, stated deliverable, audience  
- **Out:** Primary sprint ID + entry path (+ optional supports)

## Evaluation Method

1. Scan keywords (case-insensitive).  
2. Score matches per sprint (count + priority boosts).  
3. Highest primary wins; ties → ask one clarifying question.  
4. Apply composition rules in [composition-patterns.md](composition-patterns.md).

## Decision Framework — Keyword Map

| Keywords / signals | Sprint | Primary entry |
|--------------------|--------|---------------|
| requirement, story, AC, BRD, FRD, testability, gap analysis, clarification questions | **2** | `knowledge/requirement-analysis.md` |
| scenario, coverage matrix, technique, equivalence, boundary, decision table, regression scope, automation candidate (design) | **3** | `knowledge/test-design-engine.md` |
| object, field, Flow, Apex, LWC, sharing, FLS, governor, metadata | **4A** | `knowledge/platform/` (+ metadata/automation/security/data) |
| Sales Cloud, Service Cloud, Experience, OmniStudio, Agentforce, CPQ, integration pattern, industry pack | **4B** | `knowledge/clouds/` (+ packages/integration/…) |
| test plan, test strategy, RTM, checklist, template, QA report, document generation | **5** | `templates/` · `document-generation/` · `guidelines/` |
| Azure DevOps, ADO, work item, Test Plan, Test Suite, bug workflow, WIQL, dashboard | **6** | `ado/README.md` |
| defect, bug, RCA, leakage, reopen, quality gate breach, predictive quality, QI rule | **7** | `quality-intelligence/` (+ `rules/`) |
| automation strategy, Playwright, Selenium, Cypress, CI/CD test, framework review, ROI (indicative), flake | **8** | `automation-intelligence/` (+ `review-engine/`) |
| go-live, hypercare, incident, problem, change, runbook, monitoring, SLA (program-set), ops health | **9** | `production-support/` (+ `operations-intelligence/`) |
| project health, portfolio, maturity, TMMi, audit scorecard, CIO/CTO/CQO dashboard, Proceed/Hold/Escalate, transformation roadmap, architecture quality (exec), AI governance, compliance overview | **10** | `enterprise-quality/enterprise-quality-advisory-engine.md` |
| validate module, certification, benchmark scorecard, skill regression suite, repository validation, golden dataset, improvement backlog, enterprise certified, bronze/silver/gold/platinum | **11 / Validation** | `validation/enterprise-validation-engine.md` |

### Priority boosts

| Signal | Boost |
|--------|-------|
| Sev1 / P1 / outage / production down | Sprint **9** primary |
| “executive”, “steering”, “CIO”, “portfolio” | Add Sprint **10** |
| “do not write scripts” / “design only” | Keep Sprint **8**; forbid script generation |
| “publish to ADO” | Sprint **6** (+ confirm API only if explicitly requested) |

## Examples

| Request snippet | Route |
|-----------------|-------|
| “Are these ACs testable?” | 2 |
| “Build Gherkin scenarios and coverage” | 2→3 |
| “Draft Test Strategy document” | 3 evidence → 5 |
| “Structure ADO Test Suites for Epic X” | 5/6 |
| “Why are Flow defects reopening?” | 7 (+ rules) |
| “Review our Selenium suite maintainability” | 8 review-engine |
| “Hypercare week-1 incident pack” | 9 |
| “Portfolio quality heat map for steering” | 10 (evidence from 7–9) |

## Best Practices

- Prefer explicit deliverable names over vague “help with quality”.  
- When audience is executive **and** work is operational, run ops/QI first, then Sprint 10.

## Common Anti-Patterns

- Treating every request as Sprint 10.  
- Matching “automation” to full script generation.  
- Ignoring Sev1 boost for “dashboard” wording in an outage.

## Interview Questions

1. Which sprint owns “regression scope” vs “release Proceed/Hold”?  
2. How do ADO and document generation interact?

## Related Documents

- [enterprise-orchestrator.md](enterprise-orchestrator.md)
- [composition-patterns.md](composition-patterns.md)

## Navigation

- **Up:** [README.md](README.md)

## Future Enhancements

- Weighted scoring config file for tooling
