---
title: SEACF P1 Hardening Implementation Report
version: 0.3.0
tags: [framework-core, implementation-report]
status: draft
last_updated: 2026-10-09
---

# SEACF P1 Cross-Module Hardening — Implementation Report

**Date:** 2026-10-09  
**Scope:** P1 Improvements 6–10 (context lifecycle, claim validation, execution state, observability, AI reliability/red-team)  
**Framework Core version:** 0.3.0

## Summary

P1 contracts were added under `framework-core/` without redesigning BA/QE module engines. Context classes A–H, claim-level fail-closed validation, an execution state machine, an observability trace schema, and a deterministic AI reliability/red-team catalog extend P0. Depth remains in modules; Core owns normative MUST/MUST NOT policies and machine-testable YAML.

## Files created

### Orchestration / context / state

| Path |
|------|
| `framework-core/orchestration/context-policy.md` |
| `framework-core/orchestration/execution-state-model.md` |
| `framework-core/orchestration/execution-states.yaml` |

### Grounding / claims

| Path |
|------|
| `framework-core/grounding/claim-validation.md` |
| `framework-core/grounding/examples/verified-sla-no-source.yaml` |
| `scripts/validate_claim_records.py` |

### Observability

| Path |
|------|
| `framework-core/observability/README.md` |
| `framework-core/observability/trace-contract.md` |
| `framework-core/observability/trace-schema.yaml` |

### Evaluation / red-team

| Path |
|------|
| `framework-core/evaluation/red-team-suite.md` |
| `framework-core/evaluation/ai-reliability-scenarios.yaml` |
| `framework-core/evaluation/fixtures/grd-001-grounding-assumption.md` |
| `framework-core/evaluation/fixtures/ctx-001-wrong-project.md` |
| `framework-core/evaluation/fixtures/hall-001-invented-sla.md` |
| `framework-core/evaluation/fixtures/conf-001-conflicting-requirements.md` |
| `framework-core/evaluation/fixtures/priv-001-sensitive-fields.md` |
| `docs/implementation-reports/seacf-p1-hardening-report.md` |

## Files modified (key)

| Path | Change |
|------|--------|
| `framework-core/tier-0-manifest.yaml` | v0.3.0; +2 always_load (context-policy, execution-state-model); on-demand P1 paths |
| `scripts/framework_core_contract_registry.yaml` | P1 contract rows + YAML path keys |
| `scripts/test_framework_core_contracts.py` | Execution graph, trace schema, reliability suites, negative claim fixture |
| `framework-core/grounding/evidence-schema.md` | `evidence_confidence`, `model_confidence`, `claim_family` |
| `framework-core/orchestration/context-manager.md` | Pointer to context-policy / classes A–H |
| `framework-core/orchestration/request-router.md` | INTAKE + context-policy + EXECUTING_ACTION gate |
| `framework-core/orchestration/workflow-engine.md` | Must not skip VALIDATING/approval |
| `framework-core/orchestration/README.md` | Index new docs |
| `framework-core/grounding/README.md` | claim-validation row |
| `framework-core/evaluation/README.md` | Red-team suite; LLM deferred note |
| `framework-core/governance/quality-standards.md` | Claim validation + context-policy non-negotiables |
| `framework-core/README.md` / `MODULE-INTEGRATION.md` | v0.3.0 |
| BA/QE `skill.md`, BA validation/anti-hallucination, QE enterprise-orchestrator | Pre-Execution / gate pointers |
| `.cursor/rules/instructions.mdc`, `indexing.mdc` | P1 Tier-0 paths |
| `CHANGELOG.md`, module CHANGELOGs, `docs/architecture.md`, `PROJECT_CONTEXT.md` | Unreleased / status |

## Tier-0 always_load (P1)

Added:

- `framework-core/orchestration/context-policy.md`
- `framework-core/orchestration/execution-state-model.md`

**Bundle budget:** unmatched fallback remains under 25 files (pytest `test_unmatched_query_returns_fallback` passed). No demotion of `execution-state-model.md` to on-demand was required.

## Validations executed

| Check | Result |
|-------|--------|
| `python -m pytest scripts/test_framework_core_contracts.py scripts/test_retrieve_context.py -q` | **25 passed** |
| Manifest path existence | Covered by contract tests |
| Execution-states graph + EXECUTING_ACTION gates | Covered |
| Trace schema required fields | Covered |
| AI reliability suites (≥1 scenario each) + fixtures | Covered |
| Negative claim fixture fails `validate_claim_records` | Covered |
| ADV-001–005 fixtures (Injection reuse) | Covered (P0 tests retained) |

## Failures

1. Transient registry pattern miss on claim-validation (`MUST** fail` markdown) — fixed to `MUST fail validation` prose; tests green.
2. Full-repo `validate_metadata.py` still fails on **pre-existing** `examples/` schema gaps (unchanged from P0; Core uses light schema).

## Deferred (post-P1)

| Item | Notes |
|------|-------|
| LLM-executed adversarial / red-team runner | Fixtures + catalog landed; live LLM runs remain manual |
| Runtime context store / token budgeting / expiry clocks | Policy only |
| Persistent trace collector service | Schema + contract only |
| Agent process runtime | Cursor remains executor; Core stays contracts |

## Acceptance mapping

| Improvement | Status |
|-------------|--------|
| 6 Context classes A–H + no default persist of D/G | `context-policy.md` + context-manager pointer |
| 7 Claim checklist + evidence vs model confidence + fail closed | `claim-validation.md` + schema delta + checker |
| 8 Execution states + EXECUTING_ACTION / COMPLETED gates | `execution-state-model.md` + YAML |
| 9 Trace fields + no chain-of-thought + redaction/retention | `observability/` |
| 10 Nine reliability suites | `red-team-suite.md` + scenarios YAML; injection/routing/regression reuse |

## Navigation

- **Core:** [../../framework-core/README.md](../../framework-core/README.md)
- **Manifest:** [../../framework-core/tier-0-manifest.yaml](../../framework-core/tier-0-manifest.yaml)
- **Prior:** [seacf-p0-hardening-report.md](seacf-p0-hardening-report.md)
