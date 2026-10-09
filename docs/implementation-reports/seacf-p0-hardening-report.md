---
title: SEACF P0 Hardening Implementation Report
version: 0.2.0
tags: [framework-core, implementation-report]
status: draft
last_updated: 2026-10-09
---

# SEACF P0 Cross-Module Hardening — Implementation Report

**Date:** 2026-10-09  
**Scope:** P0 Improvements 1–5 (grounding, instruction precedence, prompt-injection defence, tool governance, Responsible AI)  
**Framework Core version:** 0.2.0

## Summary

Tier-0 contracts were added under `framework-core/` without redesigning BA/QE module engines. Depth remains in modules; Core owns normative MUST/MUST NOT/SHOULD/MAY policies, a machine-readable Tier-0 manifest, and contract tests.

## Files created

### Manifest and validation

| Path |
|------|
| `framework-core/tier-0-manifest.yaml` |
| `scripts/framework_core_contract_registry.yaml` |
| `scripts/test_framework_core_contracts.py` |

### Grounding

| Path |
|------|
| `framework-core/grounding/README.md` |
| `framework-core/grounding/grounding-policy.md` |
| `framework-core/grounding/source-authority.md` |
| `framework-core/grounding/evidence-schema.md` |
| `framework-core/grounding/citation-policy.md` |
| `framework-core/grounding/conflict-resolution.md` |
| `framework-core/grounding/retrieval-quality-checklist.md` |
| `framework-core/grounding/examples/claim-classification-brd-snippet.md` |

### Governance / security / tools / RAI

| Path |
|------|
| `framework-core/governance/instruction-precedence.md` |
| `framework-core/security/README.md` |
| `framework-core/security/prompt-injection-defence.md` |
| `framework-core/security/untrusted-content-policy.md` |
| `framework-core/security/secrets-and-data-handling.md` |
| `framework-core/security/adversarial-scenarios.yaml` |
| `framework-core/security/fixtures/brd-ignore-previous-rules.md` |
| `framework-core/security/fixtures/knowledge-reveal-tokens.md` |
| `framework-core/security/fixtures/retrieved-create-work-item.md` |
| `framework-core/security/fixtures/source-claims-system-instruction.md` |
| `framework-core/security/fixtures/encoded-indirect-instruction.md` |
| `framework-core/tools/README.md` |
| `framework-core/tools/tool-governance.md` |
| `framework-core/tools/tool-manifest-schema.yaml` |
| `framework-core/tools/action-risk-model.md` |
| `framework-core/tools/failure-and-retry-policy.md` |
| `framework-core/responsible-ai/README.md` |
| `framework-core/responsible-ai/principles.md` |
| `framework-core/responsible-ai/privacy-and-data-handling.md` |
| `framework-core/responsible-ai/human-oversight.md` |
| `framework-core/responsible-ai/transparency.md` |
| `framework-core/responsible-ai/fairness.md` |
| `framework-core/responsible-ai/prohibited-use-cases.md` |
| `framework-core/responsible-ai/incident-management.md` |
| `docs/implementation-reports/seacf-p0-hardening-report.md` |

## Files modified

| Path | Change |
|------|--------|
| `scripts/retrieve_context.py` | Load `TIER0_CORE` from `tier-0-manifest.yaml` with four-file fallback |
| `scripts/validate_repository.py` | Run Core contract + retriever pytest |
| `framework-core/README.md` | v0.2.0 architecture + folder map |
| `framework-core/MODULE-INTEGRATION.md` | Tier-0 manifest load order; maturity note |
| `framework-core/governance/README.md` | Instruction precedence entry |
| `framework-core/governance/quality-standards.md` | Pointers to grounding, security, precedence, RAI |
| `framework-core/orchestration/context-manager.md` | Tier-0 manifest + untrusted retrieval |
| `framework-core/orchestration/request-router.md` | Precedence before route; T3+ tool note |
| `framework-core/evaluation/README.md` | Adversarial suite pointer; P1 LLM deferred |
| `salesforce-business-analyst/skill.md` | Pre-Execution Gate → manifest |
| `salesforce-business-analyst/brain/anti-hallucination.md` | Tier-0 grounding links |
| `salesforce-business-analyst/brain/validation-framework.md` | Claim classification gate row |
| `salesforce-business-analyst/knowledge/ai-in-business-analysis.md` | Link Core RAI |
| `salesforce-business-analyst/CHANGELOG.md` | Unreleased cross-link note |
| `salesforce-quality-engineering/skill.md` | Pre-Execution Gate → manifest |
| `salesforce-quality-engineering/enterprise-orchestrator/enterprise-orchestrator.md` | Tool governance pointer |
| `salesforce-quality-engineering/enterprise-quality/ai-governance/responsible-ai.md` | Specialization banner |
| `salesforce-quality-engineering/enterprise-quality/ai-governance/README.md` | Tier-0 RAI index row |
| `salesforce-quality-engineering/CHANGELOG.md` | Unreleased cross-link note |
| `.cursor/rules/instructions.mdc` | Precedence section; manifest load |
| `.cursor/rules/indexing.mdc` | Tier-1 Core P0 paths |
| `.cursor/rules/project-context.mdc` | Precedence-aligned hierarchy |
| `.cursor/rules/userstory-generation.mdc` | ADO = T3 write under tool governance |
| `CHANGELOG.md` | Unreleased P0 entry |
| `docs/architecture.md` | Tier-0 paragraph |
| `PROJECT_CONTEXT.md` | Core v0.2.0 status |

## Canonical mapping (no duplication)

| Concern | Canonical | Specialization |
|---------|-----------|----------------|
| Claim accuracy (BA) | `framework-core/grounding/` | `salesforce-business-analyst/brain/anti-hallucination.md` |
| Repo content security | `docs/security-guidelines.md` | Agent secrets: `framework-core/security/secrets-and-data-handling.md` |
| QE Responsible AI advisory | `framework-core/responsible-ai/` | `salesforce-quality-engineering/enterprise-quality/ai-governance/responsible-ai.md` |
| Agentforce product grounding | Core grounding (evidence labels) | `skills/agentforce-testing/knowledge/knowledge-grounding.md` |

## Validations executed

| Check | Result |
|-------|--------|
| `python -m pytest scripts/test_framework_core_contracts.py scripts/test_retrieve_context.py -q` | **21 passed** |
| Manifest path existence | Covered by contract tests |
| Registry MUST/substring/pattern rules | Covered by contract tests |
| Adversarial scenario fixtures + ADV-xxx refs | Covered by contract tests |
| Tool manifest schema required fields | Covered by contract tests |
| `python scripts/validate_metadata.py` | **FAIL (pre-existing)** — hundreds of `examples/` README schema issues unrelated to P0; Framework Core uses light schema (`title`/`version`) |

## Failures

1. **Full-repo metadata validation** fails on pre-existing `examples/` (and similar) documents missing BA Sprint 7 mandatory sections. Not introduced by P0. Framework-core files use `LIGHT_SCHEMA_ROOTS` and are not subject to the nine-section BA contract.
2. Transient **disk full / SQLITE_FULL** during editing delayed some writes; resolved without leaving duplicate Core content.

## Deferred (P1)

| Item | Notes |
|------|-------|
| Context lifecycle (types, expiry, isolation, budgeting) | Extend `context-manager.md` in follow-up |
| Claim verification automation beyond schema | Evidence-backed material claims remain policy + BA/QE gates |
| Agent execution state model | Explicit states / safe transitions |
| Observability / decision-retrieval-tool trace contract | Trace fields referenced; full schema deferred |
| LLM-executed adversarial / red-team regression | Contract fixtures + expectations landed; execution suite deferred to `framework-core/evaluation/` |
| Optional `generate_framework_core.py` stub update | Hand-authored packs; generator not re-run wholesale |

## Acceptance criteria status (P0)

| Criterion | Status |
|-----------|--------|
| BRD can separate requirement-derived vs recommendation | Policy + non-authoritative example in `grounding/examples/` |
| Test strategy must not invent SLA/coverage as evidence | Grounding policy MUST NOT |
| Conflicting requirements → conflict record + escalation | `conflict-resolution.md` |
| Examples/templates not project facts | Grounding MUST NOT + example warning |
| User cannot override Tier-0 safety | Instruction precedence Priority 1–2 |
| BRD-embedded instructions not executable | Precedence Priority 6 + ADV-001 |
| Module specialization only when Core permits | Precedence rule 5 |
| Untrusted content / injection controls | Security pack + ADV-001–005 fixtures |
| Tool risk tiers T0–T4 + manifest schema | Tools pack |
| Consolidated RAI layer | `responsible-ai/` + QE/BA specialization links |

## Navigation

- **Core:** [../../framework-core/README.md](../../framework-core/README.md)
- **Manifest:** [../../framework-core/tier-0-manifest.yaml](../../framework-core/tier-0-manifest.yaml)
