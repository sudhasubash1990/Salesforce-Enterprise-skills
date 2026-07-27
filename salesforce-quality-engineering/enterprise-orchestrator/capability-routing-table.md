---
title: Capability Routing Table
version: 0.24.0
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
| metadata impact, dependency analysis, deployment review, package.xml, change set, deploy impact, regression impact, perm set, profile change, validation rule deploy, flexipage, record type deploy | **MIA** (Specialized Skill) | `skills/metadata-impact-analyzer/SKILL.md` (+ Sprint **4A** support; Sprint **3** after analysis) |
| SOQL, data validation, backend validation, reconciliation, duplicate detection, bulk validation, migration validation, query review, optimize SOQL, report validation, dashboard validation, aggregate query | **SOVA** (Specialized Skill) | `skills/soql-validation-assistant/SKILL.md` (+ `knowledge/performance/`, `knowledge/data/`, security) |
| permission, profile, permission set, CRUD, FLS, sharing, OWD, role hierarchy, record access, Experience Cloud, guest user, security testing, API access, restriction rule, deployment security | **PTA** (Specialized Skill) | `skills/permission-testing-agent/SKILL.md` (+ `knowledge/security/`, MIA/SOVA chain) |
| Agentforce, AI agent, prompt template, topic classification, agent action, guardrails, grounding, hallucination, Copilot, Einstein agent, LLM, RAG, conversation test, tool invocation, AI validation | **AFT** (Specialized Skill) | `skills/agentforce-testing/SKILL.md` (+ `knowledge/clouds/agentforce.md`, AI governance; MIA/SOVA/PTA chain) |
| Field Service, FSL, Work Order, Service Appointment, Service Resource, Service Territory, scheduling, Dispatcher Console, optimization, Field Service Mobile, offline, technician, crew, van stock, inventory, Maintenance Plan, Service Report, Work Type, skills | **FSQA** (Specialized Skill) | `skills/field-service-testing/SKILL.md` (+ `knowledge/clouds/field-service.md`, mobile-testing; MIA/SOVA/PTA/AFT chain) |
| Test Data, Sample Data, Test Records, Seed Data, Data Factory, Test Setup, UAT Data, SIT Data, Regression Data, Mock Data, Bulk Test Data, Data Masking, Synthetic Data, Sandbox Refresh, External ID, Data Loader, Bulk API, Apex Test Factory, CSV Test Data | **TDG** (Specialized Skill) | `skills/test-data-generator/SKILL.md` (+ `knowledge/data/`, Sprint 5/8 test-data; MIA/SOVA/PTA/AFT/FSQA chain) |
| Playwright, Playwright Test, locator, POM, Page Object, fixtures, flaky, Trace Viewer, storageState, playwright.config, getByRole, automation code review (Playwright) | **PWR** (Specialized Skill) | `skills/playwright-review/SKILL.md` (+ Sprint 8 review-engine/playwright; MIA/SOVA/PTA/AFT/TDG chain) |
| OmniStudio, OmniScript, FlexCard, Integration Procedure, DataRaptor, Calculation Procedure, Calculation Matrix, Decision Matrix, Decision Table, Expression Set, Industries, Vlocity, Guided Flow, Service Process, Digital Journey, CPQ, EPC, Product Configuration, Remote Action, HTTP Action, Data JSON, Context Variables | **OSQA** (Specialized Skill) | `skills/omnistudio-qa/SKILL.md` (+ `knowledge/clouds/omnistudio.md`; MIA/SOVA/PTA/PWR/AFT/TDG chain) |
| Data Migration, ETL, Data Conversion, Legacy System, Cutover, Data Load, Bulk API, Data Loader, Migration Validation, Data Quality, Reconciliation, Data Mapping, Transformation, Duplicate Records, Record Counts, Data Integrity, Data Cleansing, Post Migration Validation, External ID, Upsert, Lookup Resolution, Incremental Load, Delta Migration, Rollback, migration Hypercare | **DMQA** (Specialized Skill) | `skills/data-migration-qa/SKILL.md` (+ `knowledge/data/`; MIA/SOVA/PTA/TDG/PWR/OSQA/AFT chain) |
| production RCA, root cause analysis report, incident RCA, defect RCA, production defect postmortem, 5 whys production, fishbone production | **PRCA** (Specialized Skill — scaffold) | `skills/production-rca/SKILL.md` — **support/compose with Sprint 7 + 9**; do not replace Sprint 7/9 primary for generic defect/incident |
| risk-based regression, prioritized regression scope, regression risk ranking | **RBRR** (Specialized Skill — scaffold) | `skills/risk-based-regression/SKILL.md` — **support/compose with Sprint 3 + MIA**; generic “regression scope” stays Sprint **3** |
| Sales Cloud, Service Cloud, Experience, OmniStudio, Agentforce, CPQ, integration pattern, industry pack | **4B** | `knowledge/clouds/` (+ packages/integration/…) |
| test plan, test strategy, RTM, checklist, template, QA report, document generation | **5** | `templates/` · `document-generation/` · `guidelines/` |
| Azure DevOps, ADO, work item, Test Plan, Test Suite, bug workflow, WIQL, dashboard | **6** | `ado/README.md` |
| defect, bug, RCA, leakage, reopen, quality gate breach, predictive quality, QI rule | **7** | `quality-intelligence/` (+ `rules/`) |
| automation strategy, Selenium, Cypress, CI/CD test strategy, ROI (indicative), general framework selection | **8** | `automation-intelligence/` (+ `review-engine/` for Selenium/Cypress) |
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
| “metadata impact”, “deployment review”, “dependency analysis”, “what breaks if we deploy” | **MIA** primary → `skills/metadata-impact-analyzer/SKILL.md` |
| Agentforce + (test OR validate OR prompt OR guardrail OR hallucination OR grounding) | **AFT** primary over Sprint **4B** |
| Field Service / FSL / Work Order / Service Appointment + (test OR validate OR scheduling OR dispatch OR mobile OR inventory) | **FSQA** primary over Sprint **4B** |
| Test data / seed / sample / factory / UAT data / SIT data / masking / synthetic / sandbox refresh + (generate OR create OR setup OR bulk) | **TDG** primary over Sprint **4A** data articles |
| “SOQL”, “backend validation”, “data reconciliation”, “duplicate detection SOQL”, “validate migration data” | Prefer **DMQA** when mapping/cutover/lifecycle present; else **SOVA** primary → `skills/soql-validation-assistant/SKILL.md` |
| “permission test”, “CRUD matrix”, “FLS validation”, “sharing test”, “profile change security”, “guest user access” | **PTA** primary → `skills/permission-testing-agent/SKILL.md` |
| MIA output includes Recommended SOQL Validations | **MIA** then chain **SOVA** for full 14-section query packs |
| MIA/security metadata change (profile, perm set, sharing, FLS) | **MIA** then chain **PTA** for permission validation report |
| MIA new required field / validation rule / record type | **MIA** then chain **TDG** for compliant synthetic payloads |
| “Agentforce test”, “validate prompt”, “hallucination”, “grounding”, “guardrail”, “conversation test”, “tool invocation” | **AFT** primary → `skills/agentforce-testing/SKILL.md` (prefer over generic 4B when testing intent) |
| Agentforce action mutates CRM / exposes sensitive fields | **AFT** then chain **MIA** / **SOVA** / **PTA** as applicable |
| “FSL test”, “validate scheduling”, “Work Order lifecycle”, “offline sync”, “Dispatcher Console”, “van stock”, “Service Appointment” | **FSQA** primary → `skills/field-service-testing/SKILL.md` (prefer over generic 4B when testing intent) |
| FSL metadata deploy / WO-SA-inventory proof / tech-dispatcher access / agent booking | **FSQA** then chain **MIA** / **SOVA** / **PTA** / **AFT** as applicable |
| “generate test data”, “seed UAT”, “data factory”, “synthetic data”, “Data Loader CSV”, “bulk test records”, “mask sandbox data” | **TDG** primary → `skills/test-data-generator/SKILL.md` (prefer over generic 4A when generation intent) |
| TDG post-gen proof / persona sharing / agent or FSL seed | **TDG** then chain **SOVA** / **PTA** / **AFT** / **FSQA** as applicable |
| Playwright + (review OR optimize OR flaky OR locator OR POM OR fixture OR CI) | **PWR** primary over Sprint **8** |
| “review Playwright”, “optimize locators”, “flaky Playwright”, “Playwright POM”, “storageState review”, “Playwright Azure DevOps” | **PWR** primary → `skills/playwright-review/SKILL.md` |
| MIA FlexiPage / LWC / UI layout change with Playwright suite | **MIA** then chain **PWR** for locator impact |
| PWR needs backend proof / persona UI / Agentforce UI / seed gaps | **PWR** then chain **SOVA** / **PTA** / **AFT** / **TDG** as applicable |
| Selenium or Cypress estate review | Sprint **8** review-engine (not PWR) |
| OmniStudio / Industries / OmniScript / FlexCard / DataRaptor / IP + (test OR validate OR journey OR DataRaptor OR FlexCard OR OmniScript) | **OSQA** primary over Sprint **4B** |
| “validate OmniScript”, “DataRaptor mapping”, “Integration Procedure test”, “FlexCard QA”, “Utility Move In OmniScript”, “Industries journey test” | **OSQA** primary → `skills/omnistudio-qa/SKILL.md` |
| MIA OmniStudio metadata / package deploy | **MIA** then chain **OSQA** for journey QA |
| OSQA needs CRM/JSON proof / FLS/Experience / UI automation / agent journey / seed JSON | **OSQA** then chain **SOVA** / **PTA** / **PWR** / **AFT** / **TDG** as applicable |
| Data Migration / ETL / cutover / mapping / transformation + (validate OR reconcile OR readiness OR rollback OR hypercare) | **DMQA** primary over Sprint **4A** data articles |
| Full migration lifecycle (mapping + cutover + reconcile) vs pure SOQL | **DMQA** primary; pure “write SOQL to reconcile counts” stays **SOVA** |
| “validate migration mapping”, “ETL cutover readiness”, “External ID upsert validation”, “migration reconciliation strategy”, “rollback readiness” | **DMQA** primary → `skills/data-migration-qa/SKILL.md` |
| MIA new objects/fields/VR for migration | **MIA** then chain **DMQA** for migration lifecycle QA |
| DMQA needs reconciliation queries / persona FLS / synthetic dry-run / journey regression / Industries data | **DMQA** then chain **SOVA** / **PTA** / **TDG** / **PWR** / **OSQA** / **AFT** as applicable |
| Synthetic seed / factory without migration validation intent | **TDG** (not DMQA) |
| General ops Sev1 / non-migration hypercare | Sprint **9** primary (DMQA support only if data-migration caused) |

| "production RCA", "incident RCA", "defect RCA", "postmortem" | Prefer Sprint **7**/**9** primary; chain **PRCA** scaffold for structured RCA report outline only |
| "risk-based regression", "prioritized regression scope" | Prefer Sprint **3** (+ MIA if deploy-driven); chain **RBRR** scaffold when explicit risk-ranking deliverable requested |
| Generic "RCA" / "root cause" without production/postmortem framing | Sprint **7** primary (not PRCA) |
| Generic "regression scope" without risk-based framing | Sprint **3** primary (not RBRR) |

## Examples

| Request snippet | Route |
|-----------------|-------|
| “Are these ACs testable?” | 2 |
| “Build Gherkin scenarios and coverage” | 2→3 |
| “Draft Test Strategy document” | 3 evidence → 5 |
| “Structure ADO Test Suites for Epic X” | 5/6 |
| “Why are Flow defects reopening?” | 7 (+ rules) |
| “Review our Selenium suite maintainability” | 8 review-engine |
| “Review our Playwright Salesforce login and POM structure” | PWR (+ Sprint 8 playwright/review-engine) |
| “Validate Utility Move In OmniScript and DataRaptor mapping” | OSQA (+ clouds/omnistudio; SOVA/TDG chain) |
| “Validate legacy CRM Account migration mapping and reconciliation” | DMQA (+ knowledge/data; SOVA/PTA chain) |
| “What is the impact of deploying this package.xml?” | MIA (+ 4A) |
| “Write SOQL to verify closed cases have resolution code” | SOVA (+ data/security) |
| “Validate sales user cannot edit peer Opportunities” | PTA (+ security) |
| “Test Agentforce service agent grounding and guardrails” | AFT (+ clouds/agentforce) |
| “Validate Field Service scheduling and offline sync for Work Orders” | FSQA (+ clouds/field-service) |
| “Generate UAT seed data for Account–Contact–Opportunity with sharing personas” | TDG (+ data knowledge; PTA for sharing) |
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
