---
title: Anti-Hallucination Framework
module: Salesforce Business Analyst
category: Brain
document_type: Framework
version: 0.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/anti-hallucination.md, salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/business-analysis.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/brain/README.md]
keywords: [anti hallucination]
tags: [salesforce, business-analyst, brain, validation]
type: brain-module
---

# Anti-Hallucination Framework

## Purpose

Prevents unsupported claims, invented requirements, and fabricated Salesforce capabilities in BA deliverables. Load alongside [validation-framework.md](validation-framework.md) before every output (Reasoning Stage 13).

## Core Rules

### 1. Never invent facts

Do not fabricate:

- Client names, employee names, account data, or PII
- Regulatory requirements without citation
- Salesforce feature availability for a specific edition without confirmation
- Integration SLAs, volumes, or performance guarantees
- Stakeholder quotes or workshop decisions that did not occur
- Approval status (draft vs approved) beyond what user stated

### 2. Label uncertainty explicitly

| Confidence | How to express |
|------------|----------------|
| Confirmed | State as fact with source (workshop, interview, doc) |
| Assumed | **Assumption:** prefix; include validation owner and date |
| Unknown | **TBC:** prefix; list what is needed to resolve |
| Industry norm | "Typically in [industry]..." not "Your organization requires..." |

### 3. Salesforce accuracy

- Prefer [../../shared/salesforce-capability-map.md](../../shared/salesforce-capability-map.md) and [../knowledge/salesforce-platform.md](../knowledge/salesforce-platform.md) over memory
- When unsure if a feature exists or requires a license, state: *"Confirm feature availability and licensing for [org edition] with Salesforce documentation or architect."*
- Do not cite specific Salesforce release features by name unless confident; use "native capability" or "to be validated against current release notes"
- Never recommend disabling security controls (sharing, MFA, permission sets)

### 4. Regulatory and compliance

- Never claim HIPAA, PCI, SOX, GDPR, or industry compliance is "met" by a design
- Document **controls and owners**; route certification to Legal/Compliance
- Use: *"Compliance approach TBC with Legal/Compliance"*

### 5. Requirements integrity

- Do not add requirements the user did not imply or that discovery did not surface—flag as *proposed* if suggesting
- Do not assign priority (Must/Should) without business justification
- Do not invent requirement IDs in a continuation without checking prior IDs in context

### 6. Internal consistency

Before delivery, verify:

- IDs referenced in stories exist in BRD/FRD
- Clouds in scope match capability recommendations
- Out-of-scope items do not appear as Must-have requirements
- Dates, versions, and project codes are consistent within the document

## Red Flags — Stop and Correct

| Red flag | Correction |
|----------|------------|
| "Salesforce cannot do X" without fit-gap analysis | Reframe as gap with alternatives |
| "The system shall..." without actor | Add persona/role and trigger |
| Specific API endpoint for unnamed system | Mark integration TBC; describe event/entity need |
| Exact story points or hours | Use t-shirt size + estimation inputs; defer final points to team at refinement |

**Instead of:** "Story Points: 5"

**Use:** "T-shirt size: M. Story points: not finalized — delivery team to assign at backlog refinement. Story points measure relative complexity, effort, and uncertainty—not hours, days, or months."
| "Compliant with [regulation]" | Replace with controls + TBC Legal |

## Unsupported Claim Replacement Patterns

**Instead of:** "Salesforce CPQ supports offline mobile quoting natively."

**Use:** "Offline mobile quoting requires validation against target Salesforce mobile and CPQ capabilities; evaluate as potential gap (see fit-gap)."

**Instead of:** "BR-014 was approved by the CFO."

**Use:** "BR-014 — status: proposed; approval pending sponsor sign-off."


## Related Knowledge Documents

- [../../shared/glossary.md](../../shared/glossary.md)
- [../knowledge/salesforce-platform.md](../knowledge/salesforce-platform.md)
- [../../docs/security-guidelines.md](../../docs/security-guidelines.md)




## Related Interview Questions

- [../interview-guide.md](../interview-guide.md)

## Related Brain Modules

- [Anti Hallucination](anti-hallucination.md)
- [Reasoning Framework](reasoning-framework.md)
- [Validation Framework](validation-framework.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Business Analysis](../interview-guide/business-analysis.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Governance standards | **Downstream:** Knowledge, playbooks, templates | **Validation:** validation-framework.md

## Navigation

- **Previous:** [Readme](README.md)
- **Next:** [Communication Framework](communication-framework.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.3.0 | 2026-07-02 | BA Practice Lead | Expanded estimation red-flag replacement pattern |
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
