---
title: Changelog
module: Salesforce Quality Engineering
category: Root
document_type: Guide
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-17
last_updated: 2026-08-19
review_cycle: quarterly
related_documents:
  - salesforce-quality-engineering/ROADMAP.md
  - salesforce-quality-engineering/README.md
  - salesforce-quality-engineering/skill.md
  - salesforce-quality-engineering/validation/README.md
  - salesforce-quality-engineering/enterprise-orchestrator/README.md
  - salesforce-quality-engineering/enterprise-quality/README.md
  - salesforce-quality-engineering/production-support/README.md
  - salesforce-quality-engineering/automation-intelligence/README.md
  - salesforce-quality-engineering/quality-intelligence/README.md
keywords: [changelog]
tags: [changelog]
---

# Salesforce Quality Engineering — Changelog

**Purpose:** Module-specific version history.

**Scope:** Releases of the Salesforce Quality Engineering skill module only.

**Owner:** QE Practice Lead

**Version:** 0.25.0

**Status:** Draft (Unified Skills Architecture)

---

## [0.25.0] - 2026-08-19

### Added

- **Salesforce Functional Testing (SFT)** under `skills/salesforce-functional-testing/`:
  - SKILL.md, README.md, skill-config.yaml
  - 6 knowledge articles, 6 playbooks, 5 templates, 5 prompts, 6 examples, 7 test scenarios
  - Service Cloud, Sales Cloud, Experience Cloud functional/E2E testing; chains PTA/SOVA/TDG/PWR
- **LWC & Flow UI Testing (LFUT)** under `skills/lwc-flow-ui-testing/`:
  - SKILL.md, README.md, skill-config.yaml
  - 5 knowledge articles, 5 playbooks, 4 templates, 4 prompts, 5 examples, 6 test scenarios
  - LWC rendering/interaction, Screen Flow UI, Shadow DOM, accessibility; chains PWR/PTA
- **Salesforce PO/UAT Testing (SPUAT)** under `skills/salesforce-uat-po-testing/`:
  - SKILL.md, README.md, skill-config.yaml
  - 4 knowledge articles, 5 playbooks, 4 templates, 4 prompts, 4 examples, 5 test scenarios
  - Product Owner / UAT / business acceptance testing; chains SFT/ATCD/ADL/PTA/TDG
- **ADO Test Case Designer (ATCD)** under `skills/ado-test-case-designer/`:
  - SKILL.md, README.md, skill-config.yaml
  - 4 knowledge articles, 5 playbooks, 4 templates, 4 prompts, 4 examples, 5 test scenarios
  - ADO-default test case generation; custom user template override; traceability chain
- **ADO Defect Logger (ADL)** under `skills/ado-defect-logger/`:
  - SKILL.md, README.md, skill-config.yaml
  - 4 knowledge articles, 5 playbooks, 4 templates, 4 prompts, 4 examples, 5 test scenarios
  - Salesforce defect analysis and ADO-ready bug creation; repro quality gates
- **Salesforce Specialized Testing (SST)** under `skills/salesforce-specialized-testing/`:
  - SKILL.md, README.md, skill-config.yaml
  - 8 knowledge articles, 7 playbooks, 4 templates, 5 prompts, 5 examples, 6 test scenarios
  - Testing dimension orchestrator (security/integration/API/performance/accessibility/mobile/compatibility/regression/release); chains PTA/DMQA/TDG/MIA/RBRR/PWR/SFT/LFUT
- Enterprise Orchestrator — 6 new skill routing rows + priority boosts + examples; COMP-09 through COMP-13 composition patterns
- `skill-config.yaml` — 6 new skill registrations (SFT, LFUT, SPUAT, ATCD, ADL, SST)
- `skills/README.md` — 6 new skill table rows + 15 integration patterns

### Changed

- Module version 0.24.0 → 0.25.0
- `skill.md` — Specialized Skills table, composition, brain loading order, Pre-Execution Gate extended for 6 new skills
- `README.md` — Specialized Skills table, repo tree, version
- `prompts.md` — 6 new specialized-skill prompt sections
- `ROADMAP.md` — Specialized Skills expansion recorded as complete

---

## [0.24.0] - 2026-07-28

### Changed (breaking paths)

- **Unified specialized skills under `skills/`** — retired `capabilities/` namespace
- Module entry remains `skill.md` / `SKILL.md` (same file on Windows case-insensitive FS) + new [`skill-config.yaml`](skill-config.yaml) registry
- Added root [`prompts/README.md`](prompts/README.md) and [`examples/README.md`](examples/README.md) indexes

### Migration map

| Short ID | Old path | New path |
|----------|----------|----------|
| SOVA | `capabilities/soql-validation/` | `skills/soql-validation-assistant/` |
| PTA | `capabilities/permission-testing/` | `skills/permission-testing-agent/` |
| AFT | `capabilities/agentforce-testing/` | `skills/agentforce-testing/` |
| PWR | `capabilities/playwright-review/` | `skills/playwright-review/` |
| OSQA | `capabilities/omnistudio-qa/` | `skills/omnistudio-qa/` |
| DMQA | `capabilities/data-migration-qa/` | `skills/data-migration-qa/` |
| TDG | `capabilities/test-data-generator/` | `skills/test-data-generator/` |
| FSQA | `capabilities/field-service-qa/` | `skills/field-service-testing/` |
| MIA | `skills/metadata-impact-analyzer/` | *(unchanged)* |

- Per-skill entry rename: `CAPABILITY.md` → `SKILL.md`; `capability-config.yaml` → `skill-config.yaml`
- Standard knowledge indexes added: `concepts.md`, `best-practices.md`, `salesforce-reference.md`, `glossary.md` (pointer/index only)

### Added

- **Production RCA (PRCA)** scaffold under `skills/production-rca/`
- **Risk-Based Regression (RBRR)** scaffold under `skills/risk-based-regression/`
- Enterprise Orchestrator routing rows for PRCA/RBRR
- Generator scripts updated to target `skills/` paths

### Removed

- `capabilities/` directory (content migrated)
- One-shot `scripts/migrate_capabilities_to_skills.py` (migration complete; not required for framework consumers)

### Fixed (architecture hardening)

- Repaired broken sibling/MIA relative links under `skills/*/knowledge|playbooks|...`
- Disambiguated PRCA/RBRR routing: Sprint 7/9 and Sprint 3 remain primary; scaffolds compose as support (COMP-08)
- Normalized all `skill-config.yaml` files to top-level `name`/`short_id`/`version`/`entry` (+ `architecture_release: 0.24.0`)
- Replaced residual "QE Capability" frontmatter/category labels with "QE Specialized Skill" / "Specialized Skills"
- Updated root README QE version to 0.24.0; QE ROADMAP; composition-patterns COMP-08

---

## [0.23.0] - 2026-07-27

### Added

- **Data Migration QA (DMQA)** capability under `skills/data-migration-qa/`:
  - `SKILL.md` — Migration lifecycle QA, 20-section output schema
  - `skill-config.yaml` — routing keywords, MIA/SOVA/PTA/TDG/PWR/OSQA/AFT chain rules
  - 19 knowledge articles, 8 playbooks, 9 templates, 10 prompts, 10 examples, 12 test scenarios
  - Generator: `scripts/generate_data_migration_qa_capability.py`
- Parent `skill.md` — DMQA registration, Brain Loading row, Pre-Execution Gate step 26 (response-guidelines → 27)
- Enterprise Orchestrator — DMQA routing + priority boost over generic Sprint 4A; SOVA remains primary for pure SOQL reconciliation
- Cross-links: MIA, SOVA, PTA, TDG, PWR, OSQA, AFT, `knowledge/data/data-migration-validation.md`

### Changed

- Module version 0.22.0 → 0.23.0
- `capabilities/README.md` — DMQA registered; removed Data Migration QA from Future
- Sibling pointers (TDG, OSQA, PWR) updated to reference DMQA

## [0.22.0] - 2026-07-27

### Added

- **OmniStudio QA (OSQA)** capability under `skills/omnistudio-qa/`:
  - `SKILL.md` — Industries/OmniStudio journey QA, 17-section output schema
  - `skill-config.yaml` — routing keywords, MIA/SOVA/PTA/PWR/AFT/TDG chain rules
  - 16 knowledge articles, 8 playbooks, 8 templates, 10 prompts, 10 examples, 11 test scenarios
  - Generator: `scripts/generate_omnistudio_qa_capability.py`
- Parent `skill.md` — OSQA registration, Brain Loading row, Pre-Execution Gate step 25 (response-guidelines → 26)
- Enterprise Orchestrator — OSQA routing + priority boost over generic Sprint 4B when testing intent
- Cross-links: MIA, SOVA, PTA, PWR, AFT, TDG, `knowledge/clouds/omnistudio.md`

### Changed

- Module version 0.21.0 → 0.22.0
- `capabilities/README.md` — OSQA registered; removed OmniStudio QA from Future
- Sibling pointers (FSQA, PWR, TDG) updated to reference OSQA

## [0.21.0] - 2026-07-27

### Added

- **Playwright Review (PWR)** capability under `skills/playwright-review/`:
  - `SKILL.md` — Playwright review reasoning, 18-section output schema
  - `skill-config.yaml` — routing keywords, MIA/SOVA/PTA/AFT/TDG chain rules
  - 22 knowledge articles, 8 playbooks, 8 templates, 10 prompts, 10 examples, 12 test scenarios
  - Generator: `scripts/generate_playwright_review_capability.py`
- Parent `skill.md` — PWR registration, Brain Loading row, Pre-Execution Gate steps 13/24
- Enterprise Orchestrator — PWR routing + priority boost over generic Sprint 8 when Playwright review intent
- Cross-links: MIA, SOVA, PTA, AFT, TDG, Sprint 8 `playwright/` and `review-engine/playwright-framework-review.md`

### Changed

- Module version 0.20.0 → 0.21.0
- `capabilities/README.md` — PWR registered
- Sprint 8 Playwright/review-engine — QE Capability Entry pointers to PWR

## [0.20.0] - 2026-07-27

### Added

- **Test Data Generator (TDG)** capability under `skills/test-data-generator/`:
  - `SKILL.md` — TDM reasoning, 14-section output schema
  - `skill-config.yaml` — routing keywords, MIA/SOVA/PTA/AFT/FSQA chain rules
  - 16 knowledge articles, 8 playbooks, 8 templates, 10 prompts, 12 examples, 11 test scenarios
  - Generator: `scripts/generate_test_data_generator_capability.py`
- Parent `skill.md` — TDG registration, Brain Loading row, Pre-Execution Gate step 23
- Enterprise Orchestrator — TDG routing + priority boost over generic 4A when generation intent
- Cross-links: MIA, SOVA, PTA, AFT, FSQA, `knowledge/data/test-data-management.md`

### Changed

- Module version 0.19.0 → 0.20.0
- `capabilities/README.md` — TDG registered; removed "Test Data Generation (extended)" from Future
- FSQA limitations — point to TDG for seed data

## [0.19.0] - 2026-07-27

### Added

- **Field Service (FSL) QA** capability under `skills/field-service-testing/`:
  - `SKILL.md` — FSL QA reasoning, 18-section output schema
  - `skill-config.yaml` — routing keywords, MIA/SOVA/PTA/AFT chain rules
  - 17 knowledge articles, 9 playbooks, 9 templates, 10 prompts, 10 examples, 12 test scenarios
  - Generator: `scripts/generate_field_service_qa_capability.py`
- Parent `skill.md` — FSQA registration, Brain Loading row, Pre-Execution Gate step 22
- Enterprise Orchestrator — FSQA routing + priority boost over generic 4B when testing intent
- Cross-links: MIA, SOVA, PTA, AFT, `knowledge/clouds/field-service.md`

### Changed

- Module version 0.18.0 → 0.19.0
- `capabilities/README.md` — FSQA registered

## [0.18.0] - 2026-07-27

### Added

- **Agentforce Testing** capability under `skills/agentforce-testing/`:
  - `SKILL.md` — AI QA reasoning, 18-section output schema
  - `skill-config.yaml` — routing keywords, MIA/SOVA/PTA chain rules
  - 20 knowledge articles, 9 playbooks, 9 templates, 10 prompts, 10 examples, 15 test scenarios
  - Generator: `scripts/generate_agentforce_testing_capability.py`
- Parent `skill.md` — AFT registration, Brain Loading row, Pre-Execution Gate step 21
- Enterprise Orchestrator — AFT routing + priority boost over generic 4B when testing intent
- Cross-links: MIA, SOVA, PTA, `knowledge/clouds/agentforce.md`

### Changed

- Module version 0.17.0 → 0.18.0
- `capabilities/README.md` — AFT registered

## [0.17.0] - 2026-07-27

### Added

- **Permission Testing Agent** capability under `skills/permission-testing-agent/`:
  - `SKILL.md` — security reasoning, 19-section output schema
  - `skill-config.yaml` — routing keywords, MIA/SOVA chain rules
  - 21 knowledge articles, 7 playbooks, 8 templates, 10 prompts, 14 examples, 12 test scenarios
  - Generator: `scripts/generate_permission_testing_capability.py`
- Parent `skill.md` — PTA registration, Brain Loading row, Pre-Execution Gate step 20
- Enterprise Orchestrator — PTA routing + MIA→PTA composition
- MIA + SOVA cross-links to PTA; `knowledge/security/README.md` capability entry

### Changed

- Module version 0.16.0 → 0.17.0
- `capabilities/README.md` — PTA registered; removed from future list

## [0.16.0] - 2026-07-27

### Added

- **QE Capabilities** architecture under `capabilities/`
- **SOQL Validation Assistant** capability:
  - `skills/soql-validation-assistant/SKILL.md` — validation reasoning, 14-section output schema
  - `skill-config.yaml` — routing keywords, performance/security gates
  - 15 knowledge articles, 6 playbooks, 6 templates, 10 prompts, 13 examples, 9 test scenarios
  - Generator: `scripts/generate_soql_validation_capability.py`
- Parent `skill.md` — QE Capabilities section, Brain Loading row, Pre-Execution Gate step 19
- Enterprise Orchestrator — SOVA routing + MIA→SOVA composition
- MIA integration cross-links; MIA `soql-validation-report` template → capability pointer
- `knowledge/performance/soql-performance.md` — capability entry link

### Changed

- Module version 0.15.0 → 0.16.0
- `skills/README.md` — points to `capabilities/` namespace

## [0.15.0] - 2026-07-27

### Added

- **Specialized Skills** architecture under `skills/`
- **Metadata Impact Analyzer** specialized skill:
  - `skills/metadata-impact-analyzer/SKILL.md` — identity, reasoning models, 16-section output schema, quality gates
  - `skill-config.yaml` — routing keywords, risk scale, escalation rules
  - 13 skill knowledge articles (cross-link Sprint 4A — no encyclopedia duplication)
  - 5 playbooks, 7 templates, 8 prompts, 10 examples, 6 validation test scenarios
  - Generator: `scripts/generate_metadata_impact_analyzer.py`
- Parent `skill.md` — Specialized Skills section, Brain Loading row, Pre-Execution Gate step 18
- Enterprise Orchestrator — MIA routing row and keyword boost
- Metadata knowledge README + `metadata-impact-analysis.md` — upward link to specialized skill

### Changed

- Module version 0.14.0 → 0.15.0

## [0.14.0] - 2026-07-18

### Added

- Sprint 11 — Enterprise Framework Validation, Certification & Continuous Improvement under `validation/`:
  - `enterprise-validation-engine.md`
  - Domain suites: repository, knowledge, requirement, test-design, documentation, ado, defect, automation, production, enterprise
  - `benchmarking/` (10 industries), `golden-datasets/`, `regression-suite/` (S1–S10)
  - `certification/` (Bronze→Enterprise Certified), `quality-scorecards/`, `test-scenarios/`
  - `continuous-improvement/` including Salesforce release readiness
  - Flat v0.13 files retained as pointers into new folders
  - Generator: `scripts/generate_sprint11_validation.py`
  - skill.md Sprint 11 awareness; prompts.md Sprint 11 prompts; README Sprint 11 overview

## [0.13.0] - 2026-07-18

### Added

- **Validation hub** (`validation/`):
  - Master checklist; repository/knowledge/sprint validations (S2–S10)
  - Advisory + Orchestrator validation
  - E2E industry scenarios (utilities, retail, banking, healthcare, insurance, telecom)
  - `benchmark-scorecard.md`, `regression-suite.md`
  - Generator: `scripts/generate_qe_validation.py`
  - Wired into skill.md Pre-Execution Gate and README

## [0.12.2] - 2026-07-18

### Fixed

- Repository quality audit remediation:
  - Cursor rules Related links (`../../` depth)
  - QE `ado/README.md` and `knowledge/{references,examples,metrics,interview-guide}.md` link depths
  - `skill.md` → `brain/cross-module-map.md`
  - Knowledge root smoke/sanity/regression → `knowledge/release/` pointers
  - Dual `platform-events` → integration canonical
  - Multi-lens pointers for quality-gates, release-readiness, cloud articles
  - Shared consulting-principles as enterprise canonical; BA/QE brain deltas
  - Missing READMEs; BA Cursor skill stub; QE scenarios hub; `knowledge/reports/`
  - Module-root `interview-guide.md` pointer; archived `zzz_ImplmentationGuide/` → `archive/implementation-guide-legacy/`
  - BA `CHANGELOG.md` case normalization
  - [docs/multi-lens-policy.md](../docs/multi-lens-policy.md)

## [0.12.1] - 2026-07-18

### Added

- **Enterprise Orchestrator** (`enterprise-orchestrator/`) — request routing coordinator (not a knowledge pack):
  - `enterprise-orchestrator.md` — intent catalog, routing rules, Sev1 / executive sink rules
  - `capability-routing-table.md` — keyword → sprint capability map
  - `composition-patterns.md` — COMP-01…COMP-07 multi-hop patterns
  - Wired into `skill.md` Pre-Execution Gate, `brain/brain.md` pipeline, README, prompts, Cursor stub
  - Flow: User Request → Orchestrator → Sprints 2|3|5|6|7|8|9 → Sprint 10 Advisory → Executive Recommendations

## [0.12.0] - 2026-07-18

### Added

- Sprint 10 — Enterprise Quality Advisory Platform under `enterprise-quality/`:
  - Quality maturity, project health, portfolio management, delivery governance
  - Architecture quality, AI governance, compliance awareness, quality audits
  - Executive dashboards (CIO→Steering), decision engine, recommendation engine
  - Capability model, generic benchmarking, transformation roadmaps
  - Salesforce enterprise advisory; engine `enterprise-quality-advisory-engine.md`
  - skill.md Enterprise Advisory awareness; prompts.md Sprint 10 prompts
  - Generator: `scripts/generate_sprint10_eq.py`

### Changed

- Module version → 0.12.0; completes CQO-level advisory platform synthesizing Sprints 1–9
- Regression Intelligence deferred to optional continuous evolution

## [0.11.1] - 2026-07-18

### Added

- **Operations Intelligence Engine** under `production-support/operations-intelligence/`:
  - Health scoring, anomaly detection, incident correlation
  - Release risk & SLA breach prediction, support capacity planning, business impact, dependency mapping
  - Operational decision engine (OPS-D-*) and recommendations engine
  - skill.md / prompts.md wiring (`Run Operations Intelligence`, health/risk prompts)

### Changed

- Module version → 0.11.1; Production Support Engine pipeline includes ops intelligence

## [0.11.0] - 2026-07-18

### Added

- Sprint 9 — Production Support, Release Operations & Operational Excellence under `production-support/`:
  - Go-live, hypercare, incident/problem/change, release ops, monitoring, service management, environments
  - Knowledge management, operational excellence, support playbooks, runbook library
  - Salesforce production intelligence, operational analytics, executive reporting
  - Engine: `production-support-engine.md`
  - skill.md Production Support awareness; prompts.md Sprint 9 prompts
  - Generator: `scripts/generate_sprint9_ps.py`

### Changed

- Module version → 0.11.0; Regression Intelligence deferred to Sprint 10

## [0.10.1] - 2026-07-18

### Added

- Automation **Review Engine** under `automation-intelligence/review-engine/`:
  - Nine-dimension scorecard (architecture, POM/Screenplay, locators, data, CI/CD, reporting, flake, governance, security)
  - Maintainability score bands + overrides (Security ≤ 2 ⇒ At Risk)
  - Playwright / Selenium / Cypress review lenses; report template; P0–P3 improvement sequencing
  - skill.md / prompts.md wiring (`Review Existing Automation Framework`, `Score Automation Maintainability`)

### Changed

- Module version → 0.10.1; brownfield assessment path in Automation Intelligence Engine

## [0.10.0] - 2026-07-18

### Added

- Sprint 8 — Automation Intelligence & Test Automation Architecture under `automation-intelligence/`:
  - Strategy, framework design/comparison, patterns, Playwright/Selenium/Cypress/Robot guidance
  - API, mobile, visual, performance advisory; CI/CD; test data; governance; maintenance; metrics
  - Salesforce automation intelligence + Automation Decision Engine
  - Engines: `automation-intelligence-engine.md`, `automation-decision-engine.md`
  - skill.md Automation Intelligence awareness; prompts.md Sprint 8 prompts
  - Generator: `scripts/generate_sprint8_ai.py`
  - `automation/` legacy pointer to canonical `automation-intelligence/`

### Changed

- Module version → 0.10.0; Sprint 8 = architecture/strategy only (no full script generation)

## [0.9.1] - 2026-07-17

### Added

- Quality Intelligence **Rules Engine** under `quality-intelligence/rules/`:
  - Rule schema, evaluation process, recommendation priority
  - Metric threshold, reopen/defect quality, platform hotspot, security/permission, integration/cloud cluster, automation, regression/coverage, release-gate rule packs
  - Canonical rules for leakage → expand regression + coverage review; reopens → defect/data/verification analysis; Flow dominance → Flow suites/automation; permission recurrence → security review; prod cloud/integration clusters → targeted regression + readiness
  - skill.md / prompts.md / defect-intelligence-engine wiring; prompts: Apply Quality Intelligence Rules

### Changed

- Module version → 0.9.1; QI pipeline evaluates rules before action recommendations

## [0.9.0] - 2026-07-17

### Added

- Sprint 7 — Defect Intelligence & Quality Analytics Engine under `quality-intelligence/`:
  - Defect management, RCA methods, defect patterns, quality metrics, risk/trend/predictive analytics
  - Continuous improvement, quality-gate intelligence, Salesforce hotspot KB, executive report standards
  - Engine entry: `defect-intelligence-engine.md`
  - skill.md Defect Intelligence awareness; prompts.md QI prompts (Analyze Defect, RCA, patterns, Fishbone, 5 Whys, release risk, trends, exec reports, preventive actions, lessons learned)
  - Generator: `scripts/generate_sprint7_qi.py`

### Changed

- Module version → 0.9.0; prevention-first Quality Advisor posture; no invented metrics without data

## [0.8.0] - 2026-07-17

### Added

- Sprint 6 — Azure DevOps Delivery Intelligence under `ado/`:
  - Work item folders (epics → bugs, test plans/suites/cases, queries, dashboards, reports, governance, work-items)
  - Relationship model, traceability intelligence, artifact generation, test plan organization
  - Bug intelligence, query strategies (no WIQL files), role-based dashboard designs, governance gates
  - skill.md ADO awareness; prompts.md ADO generation prompts
  - Generator: `scripts/generate_sprint6_ado.py`

### Changed

- Module version → 0.8.0; Sprint 6 is content/intelligence (not REST API publish)

## [0.7.0] - 2026-07-17

### Added

- Sprint 5 — Enterprise Documentation & Deliverable Generator:
  - `templates/` — 40+ consulting-grade QA templates (strategy through KT/hypercare + dashboards)
  - `guidelines/` — document intelligence, deliverable selection, artifact relationships, generation rules, reporting/defect standards
  - `document-generation/` — Strategy, Plan, RTM, Scenario, Case, Defect, Reporting generators
  - `playbooks/` — 10 reusable QE ceremony/gate playbooks
  - skill.md Documentation Intelligence + deliverable loading order
  - prompts.md Sprint 5 generation prompts
  - Generator: `scripts/generate_sprint5_docs.py`

### Changed

- Pre-execution gate allows explicit Sprint 5 deliverable generation after upstream analysis/design
- Module version → 0.7.0

## [0.6.0] - 2026-07-17

### Added

- Sprint 4B — Salesforce Enterprise Business Knowledge:
  - `clouds/` — Sales, Service, Experience, FSL, CPQ, MC, Data Cloud, Agentforce, OmniStudio, FSC/Health/Education/Net Zero/Manufacturing/CG/Utilities
  - `managed-packages/` — full package/upgrade/vendor catalog
  - `integration/` — REST/SOAP/Bulk, events, middleware, OAuth, retries, limits, sync, queues
  - `performance/` — governors through scalability/performance risks
  - `release/` — planning through hypercare + production-readiness (knowledge only)
  - `industry/` — Utilities, Retail, Banking, Insurance, Healthcare, Manufacturing, Telecom, Public Sector, Energy, Consumer Goods
  - Unified 4B documentation standard; generator `scripts/generate_sprint4b_kb.py`
- skill.md Enterprise Business Knowledge awareness; prompts.md 4B templates
- README Sprint 4B overview and enterprise coverage catalogs

### Changed

- Module version → 0.6.0; Salesforce knowledge layer (4A+4B) complete for Sprint 5 readiness

## [0.5.1] - 2026-07-17

### Added

- Sprint 4A — Salesforce Platform Foundation (authoritative):
  - Expanded `platform/` (multi-tenant, metadata-driven, lookup/MD relationships, …)
  - Full `metadata/` catalog (types, impact, deploy, regression, risks, …)
  - Expanded `automation/` (assignment/escalation/auto-response, duplicate/matching, Omni overview)
  - Expanded `security/` (object-level security, territory overview, audit/login/field history)
  - Expanded `data/` (data model, recycle bin, retention, PII, GDPR awareness, integrity, LDV, …)
  - Unified 4A documentation standard (analysis → boundary → regression → defects → interview)
  - Generator: `scripts/generate_sprint4a_kb.py`
- skill.md Platform Foundation awareness; prompts.md 4A templates
- README 4A coverage + Sprint 4B future overview

### Changed

- Clouds/industries/packages treated as Sprint 4B (provisional folders retained)
- Removed out-of-scope/superseded files in 4A folders (e.g. generic `flows.md`, `dynamic-forms.md`)

## [0.5.0] - 2026-07-17

### Added

- Sprint 4 — Salesforce Knowledge Base under `knowledge/`:
  - `platform/`, `metadata/`, `clouds/`, `automation/`, `security/`, `integration/`
  - `data/`, `reporting/`, `release/`, `performance/`, `managed-packages/`, `industry/`
  - Index README per folder; QE-standard article sections (testing, regression, defects, …)
  - Generator: `scripts/generate_sprint4_kb.py`
- skill.md: Salesforce Knowledge Base awareness loading and auto-triggers
- prompts.md: Explain Component, Testing Guidance, Regression/Metadata/Cloud/Integration/Security/Production Risk prompts
- README: Sprint 4 overview, supported clouds/metadata/automation/security/integrations/industries

### Changed

- Module version → 0.5.0; knowledge README indexes Sprint 4 folders

## [0.4.1] - 2026-07-17

### Changed

- Folder structure aligned to lean module layout:
  - Root: `skill.md`, `README.md`, `prompts.md` (+ `CHANGELOG.md`, `ROADMAP.md`)
  - `knowledge/` — analysis + test-design engines and technique articles
  - `templates/` (Sprint 5), `ado/` (Sprint 6), `automation/` (Sprint 8), `scenarios/` (Sprint 4)
  - `brain/` retained (Sprint 1 reasoning — required by orchestrator)
- Moved former `governance/` assets into `knowledge/` (quality-gates, metrics, best-practices, anti-patterns, interview-guide, examples, checklists, references)
- Removed empty `playbooks/`, `governance/`, `reports/`, `examples/`, `interview-guide/`, `assets/` folders
- Navigation links updated across module

## [0.4.0] - 2026-07-17

### Added

- Sprint 3 — Test Design Engine under `knowledge/`:
  - test-design-engine.md, test-design-techniques.md, test-coverage-model.md
  - Technique articles (positive/negative/BVA/EP/decision-table/state-transition/pairwise/exploratory/error-guessing/risk-based)
  - Level/type articles (functional/regression/smoke/sanity/integration/system/uat/security/api)
  - SF-specific articles (sharing/profile/permission-set/validation-rule/flow/report/dashboard/notification)
- skill.md Test Design Engine section; prompts.md Sprint 3 prompt pack
- README Sprint 3 overview

### Notes

- Scenario objectives and coverage only — no detailed test cases, ADO artifacts, or automation scripts

## [0.3.1] - 2026-07-17

### Changed

- Restructured module folders to sprint-aligned layout:
  - `brain/` — Sprint 1 QE Brain modules
  - `knowledge/` — Sprint 2 Requirement Analysis Engine
  - `scenarios/` — Sprint 4+
  - `templates/` / `playbooks/` — Sprint 5
  - `ado/` — Sprint 6
  - `automation/` — Sprint 8
  - `governance/` — Sprint 0 skeletons (gates, metrics, practices, interview, examples)
- Root kept lean: skill, README, prompts, references, checklists (+ CHANGELOG, ROADMAP)
- Removed unused placeholder folders: reports, assets, examples/

## [0.3.0] - 2026-07-17

### Added

- Sprint 2 — Requirement Analysis Engine under `knowledge/`:
  - requirement-analysis.md, requirement-review-framework.md, question-generation-framework.md
  - requirement-risk-analysis.md, scope-analysis.md, traceability.md, stakeholder-analysis.md
  - business-rules.md, acceptance-criteria.md, requirements-quality-checklist.md
- skill.md / brain.md hooks making analysis mandatory before test artifacts
- prompts.md standard prompts for review, story/epic/feature, AC, rules, risk, gaps, questions, scope
- README Sprint 2 overview, capabilities, inputs/outputs

### Notes

- No test cases, RTM, or templates in this release

## [0.2.1] - 2026-07-17

### Changed

- Modularized Quality Engineering Brain into separate files:
  - `skill.md` — master orchestrator
  - `brain.md` — core reasoning engine
  - `thinking-model.md` — 30-stage decision flow
  - `consulting-principles.md` — QE consulting mindset
  - `decision-framework.md` — decision trees
  - `response-guidelines.md` — standard response format
  - `cross-module-map.md` — BA ↔ QE ↔ Architect ↔ DevOps
  - `quality-philosophy.md` — quality engineering principles
- Updated README, prompts, and Cursor discovery stub for modular loading order

## [0.2.0] - 2026-07-17

### Added

- Sprint 1 — Quality Engineering Brain in `skill.md`
- 30-stage Thinking Framework and Decision Framework
- Consulting principles, AI behaviour, response guidelines
- Supported clouds, testing types, deliverables (awareness), roles, responsibilities
- Cross-module collaboration inputs/outputs
- Updated `prompts.md` with reasoning flow, answer structure, clarifications, assumptions, recommendation priority
- Updated `README.md` with philosophy, capabilities, sprint status

### Notes

- No templates, playbooks, test-case libraries, or automation guidance in this release

## [0.1.0] - 2026-07-17

### Added

- Sprint 0 Foundation — module structure, documentation skeletons, and navigation
- Root module at `salesforce-quality-engineering/`
- Cursor discovery stub at `.cursor/skills/salesforce-quality-engineering/SKILL.md`
- Placeholder folders: knowledge, templates, playbooks, scenarios, automation, ado, reports, governance, assets, examples
- Skeleton documents: README, skill, references, prompts, checklists, examples, interview-guide, best-practices, anti-patterns, quality-gates, metrics, ROADMAP, CHANGELOG

### Notes

- No Quality Engineering knowledge, templates, playbooks, techniques, test cases, or automation guidance in this release

---

## Related Documents

- [ROADMAP.md](ROADMAP.md)
- [README.md](README.md)
- [skill.md](skill.md)

## Future Enhancements

- Continue Keep-a-Changelog style entries per sprint release

## Navigation

- **Previous:** [knowledge/metrics.md](knowledge/metrics.md)
- **Next:** [README.md](README.md)
- **See Also:** [ROADMAP.md](ROADMAP.md)
