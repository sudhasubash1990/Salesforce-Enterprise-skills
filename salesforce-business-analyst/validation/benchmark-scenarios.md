---
title: Validation Benchmark Scenarios
module: Salesforce Business Analyst
category: Validation
document_type: Guide
version: 1.2.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/validation-framework.md, salesforce-business-analyst/brain/anti-hallucination.md]
related_knowledge: [salesforce-business-analyst/knowledge/governance-framework.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/production-readiness-playbook.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/validation/README.md, docs/quality-framework.md, scripts/validate_repository.py]
keywords: [benchmark scenarios]
tags: [benchmark, validation, assessment]
review-cycle: quarterly
---

# Validation Benchmark Scenarios

Anonymized exercises to validate repository health and BA capability. Use for onboarding, certification, and AI agent regression checks.

## Repository Health Benchmarks

| ID | Scenario | Steps | Pass criteria |
|----|----------|-------|---------------|
| RH-01 | Metadata integrity | Run `python scripts/validate_metadata.py` | Exit code 0, all files pass |
| RH-02 | Full repo validation | Run `python scripts/validate_repository.py` | Exit code 0, structure OK |
| RH-03 | Cross-link spot check | Open 5 random knowledge articles | All Related sections populated, links work |
| RH-04 | Skill orchestration | Load `skill.md` + brain loading order for BRD task | Correct module sequence identified |

## BA Capability Benchmarks

| ID | Scenario | Context | Deliverable | Evaluation |
|----|----------|---------|-------------|------------|
| BA-01 | Utilities discovery | [scenarios/utilities/meter-to-cash.md](../scenarios/utilities/meter-to-cash.md) | 3 BR themes + RAID items | Traceable IDs, business outcomes |
| BA-02 | Retail fit-gap | [scenarios/retail/returns.md](../scenarios/retail/returns.md) | Fit-gap table (Standard/Config/Extend/Gap) | Standard-first justification |
| BA-03 | Banking stories | [scenarios/banking/loan-origination.md](../scenarios/banking/loan-origination.md) | 5 INVEST stories + AC | 3+ Given/When/Then per story |
| BA-04 | Healthcare workshop | [scenarios/healthcare/appointments.md](../scenarios/healthcare/appointments.md) | Workshop agenda + minutes | Stakeholder map, decisions logged |
| BA-05 | Insurance traceability | [scenarios/insurance/claims.md](../scenarios/insurance/claims.md) | RTM excerpt (BR → story → test) | Forward/backward trace intact |
| BA-06 | Telecom integration BRD | [scenarios/telecom/order-capture.md](../scenarios/telecom/order-capture.md) | Integration section in BRD | System of record, sync direction, SLAs |

## Interview-Linked Benchmarks

| ID | Scenario | Resource | Pass criteria |
|----|----------|----------|---------------|
| IV-01 | Screening mock | [interview-guide/business-analysis.md](../interview-guide/business-analysis.md) Q1–5 | Structured answers with risks |
| IV-02 | Scenario exercise | [interview-guide/advanced/scenario-questions.md](../interview-guide/advanced/scenario-questions.md) Q1 | Discovery plan + 3 BRs |
| IV-03 | Whiteboard | [interview-guide/advanced/whiteboard-exercises.md](../interview-guide/advanced/whiteboard-exercises.md) Exercise 1 | Process + exception paths |

## Running a Benchmark Session

1. Select benchmark ID aligned to maturity level ([ba-maturity-model.md](../ba-maturity-model.md)).
2. Provide scenario context only — no pre-written answers.
3. Evaluate against pass criteria and [checklists.md](../checklists.md).
4. Record results in [certification-report-template.md](certification-report-template.md).

## Related Brain Modules

- [Validation Framework](../brain/validation-framework.md)
- [Anti Hallucination](../brain/anti-hallucination.md)

## Related Knowledge

- [Governance Framework](../knowledge/governance-framework.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Production Readiness Playbook](../playbooks/production-readiness-playbook.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Interview Index](../interview-guide/interview-index.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Readme](README.md)
- [Quality Framework](../../docs/quality-framework.md)
- [Validate_Repository](../../scripts/validate_repository.py)

## Traceability

**Upstream:** Brain validation, governance | **Downstream:** Certification, maturity assessments | **Validation:** validate_repository.py

## Navigation

- **Previous:** [Readme](README.md)
- **Next:** [Certification Report Template](certification-report-template.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
