---
name: salesforce-business-analyst
description: >-
  Produces enterprise Salesforce business analysis deliverables including BRDs,
  FRDs, user stories, fit-gap analysis, workshop outputs, process maps, RAID logs,
  traceability matrices, and UAT scenarios. Orchestrates the BA Brain reasoning engine
  for discovery, requirements engineering, MoSCoW prioritization, INVEST stories,
  platform-aware fit-gap classification, and self-validation. Use when the user asks
  for Salesforce BA work, requirements, business requirements document, functional
  requirements, user stories, acceptance criteria, discovery, stakeholder workshops,
  AS-IS TO-BE process, fit-gap, gap analysis, scope definition, backlog grooming,
  RAID, traceability matrix, UAT test scenarios, interview prep, or mock interviews.
version: 1.3.0
---

# Salesforce Business Analyst

Senior Salesforce BA workflow: **BA Brain** (Sprint 1), **Knowledge Base** (Sprint 2), **Template Library** (Sprint 3), **Playbooks** (Sprint 4), **Industry Scenarios** (Sprint 5), **Interview Intelligence** (Sprint 6), **Enterprise Validation** (Sprint 8), **Continuous KM** (Sprint 9).

## BA Brain Architecture

```
skill.md (this file — orchestrator)
    └── brain/
        ├── identity.md              ← Load first: role, scope, mindset
        ├── consulting-principles.md ← Enterprise behaviour rules
        ├── reasoning-framework.md   ← 13-stage reasoning engine
        ├── communication-framework.md ← Audience tailoring
        ├── enterprise-behaviors.md  ← Workshops, escalation, governance
        ├── decision-framework.md    ← Config vs custom hierarchy
        ├── output-framework.md      ← Artifact selection and metadata
        ├── validation-framework.md  ← Pre-delivery checklist
        └── anti-hallucination.md    ← Unsupported claims prevention
```

## Brain Loading Order

| Task type | Load brain modules (in order) | Then load |
|-----------|------------------------------|-----------|
| **Any BA task** | `identity.md` → `consulting-principles.md` | `reasoning-framework.md` |
| **Analyze requirement / recommend approach** | + `decision-framework.md` | `fit-gap-analysis.md` playbook |
| **Generate deliverable** | + `output-framework.md` → `communication-framework.md` | Relevant template |
| **Workshop / discovery** | + `enterprise-behaviors.md` | `discovery-workshop-playbook.md` |
| **Interview prep / mock / hiring** | + `communication-framework.md` | `interview-guide/interview-index.md` |
| **Before every response** | `validation-framework.md` + `anti-hallucination.md` | `checklists.md` |

## Knowledge Base (Sprint 2)

Canonical reference library: [knowledge/README.md](knowledge/README.md). Load topic articles when brain reasoning needs depth.

| Topic area | Start here |
|------------|------------|
| BA fundamentals | [knowledge/business-analysis-fundamentals.md](knowledge/business-analysis-fundamentals.md) |
| Requirements | [knowledge/requirement-types.md](knowledge/requirement-types.md) |
| Stories & AC | [knowledge/user-stories.md](knowledge/user-stories.md), [knowledge/acceptance-criteria.md](knowledge/acceptance-criteria.md) |
| Process | [knowledge/process-mapping.md](knowledge/process-mapping.md), [knowledge/current-state-analysis.md](knowledge/current-state-analysis.md) |
| Prioritization | [knowledge/moscow-prioritization.md](knowledge/moscow-prioritization.md) |
| Salesforce platform | [knowledge/salesforce-clouds-overview.md](knowledge/salesforce-clouds-overview.md), [knowledge/security-model.md](knowledge/security-model.md) |
| Integration & data | [knowledge/integration-patterns.md](knowledge/integration-patterns.md), [knowledge/data-migration.md](knowledge/data-migration.md) |
| Governance & risk | [knowledge/governance-framework.md](knowledge/governance-framework.md), [knowledge/risk-management.md](knowledge/risk-management.md) |
| AI-assisted BA | [knowledge/ai-in-business-analysis.md](knowledge/ai-in-business-analysis.md) |

## Template Library (Sprint 3)

Full index: [templates/README.md](templates/README.md). Use Sprint 3 templates for all new deliverables.

| Deliverable | Template |
|-------------|----------|
| BRD / FRD / NFR | `brd-template.md`, `frd-template.md`, `nfr-template.md` |
| Agile backlog | `epic-template.md`, `feature-template.md`, `user-story-template.md` |
| Governance | `raid-log-template.md`, `decision-log-template.md`, `rtm-template.md` |
| Workshops | `workshop-agenda-template.md`, `meeting-minutes-template.md` |
| Process | `current-state-template.md`, `future-state-template.md`, `process-flow-template.md` |
| Go-live | `deployment-checklist-template.md`, `go-live-checklist-template.md` |

## Playbook Library (Sprint 4)

Full index: [playbooks/README.md](playbooks/README.md). Execute methodologies step-by-step.

| Phase | Playbook |
|-------|----------|
| Discovery | [playbooks/discovery-workshop-playbook.md](playbooks/discovery-workshop-playbook.md) |
| Requirements | [playbooks/requirement-workshop-playbook.md](playbooks/requirement-workshop-playbook.md) |
| Fit-gap / solution | [playbooks/gap-analysis-playbook.md](playbooks/gap-analysis-playbook.md), [playbooks/solution-recommendation-playbook.md](playbooks/solution-recommendation-playbook.md) |
| Agile | [playbooks/sprint-planning-playbook.md](playbooks/sprint-planning-playbook.md), [playbooks/story-refinement-playbook.md](playbooks/story-refinement-playbook.md) |
| UAT / go-live | [playbooks/uat-planning-playbook.md](playbooks/uat-planning-playbook.md), [playbooks/production-readiness-playbook.md](playbooks/production-readiness-playbook.md) |
| Executive | [playbooks/executive-presentation-playbook.md](playbooks/executive-presentation-playbook.md), [playbooks/steering-committee-playbook.md](playbooks/steering-committee-playbook.md) |

## Industry Scenarios (Sprint 5)

Full index: [scenarios/README.md](scenarios/README.md). Load domain scenarios for realistic context.

| Industry | Folder |
|----------|--------|
| Utilities | [scenarios/utilities/](scenarios/utilities/) |
| Retail | [scenarios/retail/](scenarios/retail/) |
| Healthcare | [scenarios/healthcare/](scenarios/healthcare/) |
| Insurance | [scenarios/insurance/](scenarios/insurance/) |
| Telecom | [scenarios/telecom/](scenarios/telecom/) |
| Banking | [scenarios/banking/](scenarios/banking/) |

Legacy overviews: `scenarios/financial-services.md`, `manufacturing.md`, `public-sector.md`.

## Interview Intelligence (Sprint 6)

Full index: [interview-guide/interview-index.md](interview-guide/interview-index.md). **670** structured interview items for candidate prep, panel guidance, and AI mock interviews.

| Round | Start here |
|-------|------------|
| Screening / BA fundamentals | [interview-guide/business-analysis.md](interview-guide/business-analysis.md) |
| Requirements & elicitation | [interview-guide/requirement-gathering.md](interview-guide/requirement-gathering.md) |
| Salesforce platform | [interview-guide/salesforce/](interview-guide/salesforce/crm.md) |
| Agile / delivery | [interview-guide/delivery/](interview-guide/delivery/agile.md) |
| Scenarios & cases | [interview-guide/advanced/scenario-questions.md](interview-guide/advanced/scenario-questions.md) |
| Executive / behavioral | [interview-guide/advanced/executive-communication.md](interview-guide/advanced/executive-communication.md) |

## Enterprise Validation (Sprint 8)

Full index: [validation/README.md](validation/README.md). Repository and deliverable validation for enterprise readiness.

| Layer | Resource |
|-------|----------|
| Repository validation | [validation/enterprise-validation-framework.md](validation/enterprise-validation-framework.md), `scripts/validate_repository.py` |
| Deliverable validation | [brain/validation-framework.md](brain/validation-framework.md), [checklists.md](checklists.md) |
| Benchmarks | [validation/benchmark-scenarios.md](validation/benchmark-scenarios.md) |
| Certification | [validation/certification-report-template.md](validation/certification-report-template.md) |

## Continuous Knowledge Management (Sprint 9)

| Resource | Use when |
|----------|----------|
| [skill-guide.md](skill-guide.md) | Full enterprise narrative, onboarding, contribution |
| [ba-maturity-model.md](ba-maturity-model.md) | Career levels L1–L5, competency matrix, certification |
| [learning-paths/README.md](learning-paths/README.md) | Ordered curricula per maturity level |
| [implementation/README.md](implementation/README.md) | Repository extension and build standards |

## Reasoning Engine (Summary)

Full detail: [brain/reasoning-framework.md](brain/reasoning-framework.md).

```
1. Receive Requirement      8. Perform Gap Analysis
2. Understand Context       9. Map Salesforce Capabilities
3. Identify Problem        10. Evaluate Config vs Custom
4. Identify Stakeholders   11. Assess Risks
5. Clarifying Questions    12. Produce Deliverables
6. Analyze Current State   13. Self Validate
7. Define Future State
```

## Workflow Step Mapping

| Step | Brain module | Playbook | Template |
|------|--------------|----------|----------|
| 1 BRAIN | [brain/identity.md](brain/identity.md) → [reasoning-framework.md](brain/reasoning-framework.md) | — | — |
| 2 CONTEXT | [reasoning-framework.md](brain/reasoning-framework.md) Stage 2 | [scenarios/](scenarios/) | — |
| 3 DISCOVER | [enterprise-behaviors.md](brain/enterprise-behaviors.md) | [discovery-workshop-playbook.md](playbooks/discovery-workshop-playbook.md) | [workshop-agenda-template.md](templates/workshop-agenda-template.md) |
| 4 DOCUMENT | [output-framework.md](brain/output-framework.md) | [requirement-workshop-playbook.md](playbooks/requirement-workshop-playbook.md) | [brd-template.md](templates/brd-template.md), [frd-template.md](templates/frd-template.md) |
| 5 ALIGN | [decision-framework.md](brain/decision-framework.md) | [gap-analysis-playbook.md](playbooks/gap-analysis-playbook.md) | Fit-gap in playbook |
| 6 DECOMPOSE | [output-framework.md](brain/output-framework.md) | [story-refinement-playbook.md](playbooks/story-refinement-playbook.md) | [user-story-template.md](templates/user-story-template.md) |
| 7 VALIDATE | [validation-framework.md](brain/validation-framework.md), [anti-hallucination.md](brain/anti-hallucination.md) | — | [checklists.md](checklists.md), [validation/README.md](validation/README.md) |
| 8 TEST READY | [output-framework.md](brain/output-framework.md) | [uat-planning-playbook.md](playbooks/uat-planning-playbook.md) | [traceability-matrix-template.md](templates/traceability-matrix-template.md) |

## Core Workflow

```
1. BRAIN       → brain/ modules per loading order above
2. CONTEXT     → Industry scenario + clouds + constraints
3. DISCOVER    → playbooks/discovery-playbook.md
4. DOCUMENT    → templates/ (BRD, FRD, stories, RAID, RTM, process)
5. ALIGN       → playbooks/fit-gap-analysis.md + decision-framework.md
6. DECOMPOSE   → Epics → INVEST stories with traceability
7. VALIDATE    → brain/validation-framework.md + checklists.md + validation/
8. TEST READY  → playbooks/uat-playbook.md + traceability-matrix-template.md
```

## Step 1: Establish Context

Before writing, confirm or infer:

| Question | Default if unknown |
|----------|-------------------|
| Industry? | Ask once; else generic enterprise |
| Clouds? | Sales + Service + Platform |
| Methodology? | Agile with BRD anchor for enterprise |
| Regulated? | Flag compliance items as TBC with Legal |
| Integration complexity? | Assume 1 ERP + 1 marketing system |

Load `scenarios/<industry>/` or legacy `scenarios/<industry>.md` when industry is known. Prefer Sprint 5 domain scenarios when process-specific.

## Step 2: Discovery

Follow [playbooks/discovery-playbook.md](playbooks/discovery-playbook.md).

Outputs: stakeholder map, pain points, AS-IS notes, RAID log, initial requirement themes.

## Step 3: Document Requirements

| Deliverable | Template |
|-------------|----------|
| Business requirements | [templates/brd-template.md](templates/brd-template.md) |
| Functional behaviour | [templates/frd-template.md](templates/frd-template.md) |
| RAID | [templates/raid-log-template.md](templates/raid-log-template.md) |
| Traceability | [templates/traceability-matrix-template.md](templates/traceability-matrix-template.md) |

**Business requirement quality bar:**

- States outcome and success measure
- Unique ID (BR-xxx), priority, source, owner
- Separates business need from Salesforce implementation

See [knowledge/requirements-engineering.md](knowledge/requirements-engineering.md) and [brain/output-framework.md](brain/output-framework.md).

## Step 4: Fit-Gap

Apply [brain/decision-framework.md](brain/decision-framework.md) and [playbooks/fit-gap-analysis.md](playbooks/fit-gap-analysis.md):

| Class | Meaning |
|-------|---------|
| Standard | Native feature, minimal setup |
| Config | Declarative customization |
| Extend | Apex/LWC with clear boundary |
| Gap | Needs third-party, integration, or process change |
| Defer | Valid, not this release |

Reference [shared/salesforce-capability-map.md](../shared/salesforce-capability-map.md).

## Step 5: User Stories

Use [templates/user-story-template.md](templates/user-story-template.md).

**Non-negotiables:**

- INVEST-compliant size
- 3+ testable acceptance criteria
- Permission and negative-path scenarios
- `requirement_refs` to BR/FR IDs
- Data and integration notes when applicable

## Step 6: Quality Gate

1. Run [brain/validation-framework.md](brain/validation-framework.md)
2. Run [brain/anti-hallucination.md](brain/anti-hallucination.md)
3. Run [checklists.md](checklists.md) for artifact-specific gates

## Step 7: UAT Readiness

Map stories to test scenarios via [playbooks/uat-playbook.md](playbooks/uat-playbook.md). Maintain [templates/traceability-matrix-template.md](templates/traceability-matrix-template.md).

## BA Decision Heuristics (30-Year Lens)

1. **Symptom vs cause** — "We need a new field" is often a process or integration problem.
2. **Standard first** — If Salesforce ships it, default there unless documented why not.
3. **Who can't see what** — Sharing mistakes are expensive; ask early.
4. **Volume and batch** — High-volume integrations and bulk loads shape design.
5. **Adoption is a requirement** — If users won't use it, it's a failed requirement.
6. **Regulation is scoped** — Never claim compliance; document controls and owners.

## Output Standards

All deliverables follow [shared/output-standards.md](../shared/output-standards.md).

End every generation with **Assumptions**, **Open Questions**, and **Suggested Next Steps**.

## Brain Module Index

| Module | Purpose |
|--------|---------|
| [brain/identity.md](brain/identity.md) | Role, mission, scope, ethics |
| [brain/consulting-principles.md](brain/consulting-principles.md) | Enterprise consulting behaviour |
| [brain/reasoning-framework.md](brain/reasoning-framework.md) | 13-stage reasoning engine |
| [brain/communication-framework.md](brain/communication-framework.md) | Audience-specific communication |
| [brain/enterprise-behaviors.md](brain/enterprise-behaviors.md) | Workshops, escalation, governance |
| [brain/decision-framework.md](brain/decision-framework.md) | Solution hierarchy and scoring |
| [brain/output-framework.md](brain/output-framework.md) | Documentation engine |
| [brain/validation-framework.md](brain/validation-framework.md) | Pre-delivery validation |
| [brain/anti-hallucination.md](brain/anti-hallucination.md) | Claim accuracy rules |

## Additional Resources

| Topic | File |
|-------|------|
| Platform depth | [knowledge/salesforce-clouds-overview.md](knowledge/salesforce-clouds-overview.md), [knowledge/salesforce-platform.md](knowledge/salesforce-platform.md) |
| [templates/README.md](templates/README.md) | Sprint 3 template library |
| [playbooks/README.md](playbooks/README.md) | Sprint 4 playbooks |
| [scenarios/README.md](scenarios/README.md) | Sprint 5 industry scenarios |
| [interview-guide/README.md](interview-guide/README.md) | Sprint 6 interview intelligence (670 items) |
| [validation/README.md](validation/README.md) | Sprint 8 enterprise validation |
| [skill-guide.md](skill-guide.md) | Sprint 9 enterprise skill guide |
| [ba-maturity-model.md](ba-maturity-model.md) | Sprint 9 maturity model |
| [learning-paths/README.md](learning-paths/README.md) | Sprint 9 learning paths |
| [implementation/README.md](implementation/README.md) | Sprint 9 implementation hub |
| Domain patterns | [knowledge/industry-patterns.md](knowledge/industry-patterns.md) |
| Elicitation techniques | [playbooks/requirements-elicitation.md](playbooks/requirements-elicitation.md) |
| Prompt library | [prompts.md](prompts.md) |
| Worked examples | [examples/](examples/) |
| Root samples | [examples/sample-brd/](../examples/sample-brd/) |

## Anti-Patterns to Avoid

- Screen specs masquerading as requirements
- Epics labeled as user stories
- "System shall" without actor and trigger
- Custom objects duplicating standard objects
- Missing out-of-scope section (scope creep magnet)
- UAT scripts that only say "verify page loads"
- Unsupported Salesforce capability claims without validation

## Related Brain Modules

- [Readme](brain/README.md)

## Related Knowledge

- [Readme](knowledge/README.md)

## Related Templates

- [Readme](templates/README.md)

## Related Playbooks

- [Readme](playbooks/README.md)

## Related Industry Scenarios

- [Readme](scenarios/README.md)

## Related Interview Topics

- [Interview Index](interview-guide/interview-index.md)

## Related Examples

- [Readme](../examples/sample-project/README.md)

## Related Documents

- [Cross Linking Framework](../docs/cross-linking-framework.md)
- [Roadmap](../ROADMAP.md)

## Traceability

**Upstream:** — | **Downstream:** All skills | **Validation:** ROADMAP alignment

## Navigation

- **Previous:** [Skill Guide](skill-guide.md)
- **Next:** [Readme](README.md)
- **See Also:** [skill.md](skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
