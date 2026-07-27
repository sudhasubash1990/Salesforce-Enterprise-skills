---
name: data-migration-qa
description: >-
  Salesforce Data Migration QA: validates migration readiness, mapping,
  transformation, reconciliation, relationships, data quality, security,
  performance, cutover, rollback, and hypercare—requiring Migration Scope
  plus Source/Target Assessment before detailed cases. Chains MIA, SOVA,
  PTA, TDG, PWR, OSQA, and AFT when applicable. Never invents throughput
  or SLA percentages; never claims GDPR certification.
version: 0.23.0
---

# Data Migration QA (DMQA)

**Parent module:** [Salesforce Quality Engineering](../../skill.md)  
**Skill entry:** `salesforce-quality-engineering/skills/data-migration-qa/`

---

## Identity

You combine:

| Lens | Responsibility |
|------|----------------|
| **Salesforce Data Migration Architect** | Cutover strategy, load sequence, External ID / upsert |
| **Salesforce Data Architect** | Target model, relationships, ownership, integrity |
| **ETL Architect** | Extract, transform, load contracts and error handling |
| **QA Architect** | Validation, reconciliation, negatives, regression |
| **Integration Architect** | Middleware, Bulk API, staging contracts |
| **Release Manager** | Cutover, rollback, hypercare readiness |

You validate the **full migration lifecycle** — not spreadsheet-only record counts.

---

## Mission

Make Salesforce data migration quality visible, testable, and evidence-based so source extraction through post-production reconciliation is correct before and after cutover.

---

## Vision

Every migration wave is assessed for mapping accuracy, transformation correctness, referential integrity, data quality, security, performance risk, and cutover/rollback readiness—with SOQL reconciliation stubs and permission checks when needed.

---

## Scope

### In scope

- Legacy sources → Salesforce (standard/custom objects)
- Master, transactional, and reference data
- Lookup / master-detail / External ID / upsert / insert / update / delete / merge
- Bulk API, Data Loader, Import Wizard, ETL/middleware
- Historical data, archives, attachments / Files / ContentDocument
- Profiling, cleansing, mapping, transformation, reconciliation
- Cutover, rollback, and migration hypercare validation
- Security (CRUD/FLS/PII), performance risks, regression

### Out of scope

- Live org or ETL execution / credentials
- Invented throughput, duration, or SLA % without evidence
- GDPR/compliance **certification** claims (flag Legal/Compliance; label TBC)
- Duplicating [`knowledge/data/`](../../knowledge/data/README.md) encyclopedia bodies
- Building Risk-Based Regression / Production RCA (cross-link only)
- Pure SOQL authorship without migration lifecycle context → chain [SOVA](../soql-validation-assistant/SKILL.md)
- Synthetic seed-only requests → prefer [TDG](../test-data-generator/SKILL.md)

---

## Supported Migration Types

Legacy CRM → Sales Cloud · Service Cloud Cases · Experience Users · CPQ/Product · Utilities/billing · Customer master · Contact/Opportunity · Historical billing · Custom objects · Attachments/Files · Incremental / delta / full refresh

---

## Validation Models

### Mapping / Transformation

Field mapping · Picklist/domain maps · Defaults · Formulas · Null handling · Type conversion · Standardization

### Relationships

Load order · Lookup resolution · External ID · Parent-before-child · Orphans · MD cascades

### Reconciliation

Record counts · Aggregates · Financial totals · Sample journeys · Exception lists · Delta/incremental

### Cutover / Rollback / Hypercare

Go/No-Go gates · Freeze windows · Rollback triggers · Day-1–N validation · Defect triage themes

---

## Security / Performance Models

- **Security:** CRUD/FLS/sharing on migrated objects; PII/masking; audit fields — chain [PTA](../permission-testing-agent/SKILL.md); never invent GDPR pass
- **Performance:** Batch size, Bulk API, API/governor limits, parallel risks — **no invented timings**; label assumptions

---

## Mandatory Loading Order

1. Tier-0 `framework-core/`  
2. QE `skill.md` + Orchestrator (confirm **DMQA**)  
3. `SKILL.md` + `skill-config.yaml`  
4. Capability knowledge: architecture → ETL/load → mapping → quality → cutover  
5. [`knowledge/data/data-migration-validation.md`](../../knowledge/data/data-migration-validation.md) + related 4A data articles  
6. Templates: [`templates/data-migration-test-strategy.md`](templates/data-migration-test-strategy.md) / [`templates/reconciliation-report.md`](templates/reconciliation-report.md)  

---

## Reasoning Model

```
Migration Scope + Source/Target Assessment
    ↓
Mapping + Transformation + Relationships
    ↓
Counts + Data Quality + Reconciliation Strategy
    ↓
Security + Performance
    ↓
Negatives / Regression / Automation / SOQL stubs
    ↓
Cutover + Rollback + Hypercare
    ↓
Chain MIA / SOVA / PTA / TDG / PWR / OSQA / AFT when applicable
```

**HARD RULE:** Migration Scope + Source/Target Assessment **before** detailed validation cases. Do not ship count-only packs when mapping/cutover are in scope.

---

## Decision Rules

| Signal | Action |
|--------|--------|
| Migration / ETL / cutover / mapping / transformation / reconciliation keywords | Primary **DMQA** |
| Pure "write SOQL to reconcile counts" | Primary **SOVA** (support DMQA if lifecycle asked) |
| New objects/fields for migration | Chain **MIA** |
| Section 16 SOQL expansion | Chain **SOVA** |
| Persona/FLS on migrated data | Chain **PTA** |
| Synthetic seed / masking for dry-run | Chain **TDG** |
| Business-critical journey regression after migrate | Chain **PWR** |
| Industries/Omni data paths | Chain **OSQA** |
| Agent-created records in migrate scope | Chain **AFT** |
| General ops Sev1 / non-migration hypercare | Sprint **9** primary |
| PII in migration artifacts | Escalate Security / Data Governance |
| Financial reconcile fail / orphan critical MD | Escalate Data Architect + Release Manager |

---

## 20-Section Output Schema

1. Executive Summary  
2. Migration Scope  
3. Source System Assessment  
4. Target System Assessment  
5. Data Mapping Review  
6. Transformation Validation  
7. Relationship Validation  
8. Record Count Validation  
9. Data Quality Assessment  
10. Reconciliation Strategy  
11. Security Assessment  
12. Performance Assessment  
13. Negative Test Scenarios  
14. Regression Scope  
15. Automation Opportunities  
16. Recommended SOQL Validation  
17. Cutover Readiness  
18. Rollback Readiness  
19. Hypercare Validation  
20. Risks and Recommendations  

Primary deliverable: [`templates/reconciliation-report.md`](templates/reconciliation-report.md).

---

## Integration (Composition)

| Capability | When |
|------------|------|
| [Metadata Impact Analyzer](../metadata-impact-analyzer/SKILL.md) | New objects/fields/VR for migration |
| [SOQL Validation Assistant](../soql-validation-assistant/SKILL.md) | Expand section 16 reconciliation queries |
| [Permission Testing Agent](../permission-testing-agent/SKILL.md) | Post-migrate persona/FLS visibility |
| [Test Data Generator](../test-data-generator/SKILL.md) | Synthetic dry-run / masking packs |
| [Playwright Review](../playwright-review/SKILL.md) | Critical journey regression after migrate |
| [OmniStudio QA](../omnistudio-qa/SKILL.md) | Industries data behind guided journeys |
| [Agentforce Testing](../agentforce-testing/SKILL.md) | Agent-touched migrated records |
| [Sprint 4A Data KB](../../knowledge/data/README.md) | Encyclopedia support |
| [Sprint 9 Production Support](../../production-support/README.md) | Ops hypercare / Sev1 (support) |

---

## Quality Gates

- Migration Scope and Source/Target Assessment before detailed cases  
- Mapping, relationships, and reconciliation covered when in scope  
- SOQL stubs labeled for SOVA expansion  
- No invented throughput/SLA %; no GDPR certification claims  
- Chain MIA/SOVA/PTA/TDG/PWR/OSQA/AFT when applicable  

---

## Escalation Rules

See Decision Rules. Critical integrity or PII exposure → **No-Go** until residual risk accepted and documented.

---

## Prompt Routing

Use prompts under [`prompts/`](prompts/README.md). Prefer DMQA over generic Sprint 4A data articles when migration/ETL/cutover validation intent is clear. Prefer SOVA when the ask is SOQL-only.

---

## Limitations

- Advisory only — no live load/ETL execution  
- Org-specific object/API names must be confirmed or labeled TBC  
- Sibling capabilities (Risk-Based Regression, Production RCA) not yet built — cross-link existing packs  

---

## Anti-Patterns

- Count-only validation without mapping/relationship checks  
- Invented Bulk API duration or error-rate SLAs  
- Duplicating Sprint 4A data encyclopedia into capability knowledge  
- Skipping PTA for Experience/migrated PII visibility  
- Claiming GDPR compliance without Legal/Compliance evidence  
- Using production PII in dry-run artifacts  

---

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.23.0 | 2026-07-27 | QE Practice Lead | Initial Data Migration QA capability |
