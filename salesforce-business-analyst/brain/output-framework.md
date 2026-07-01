---
title: Output Framework
module: Salesforce Business Analyst
category: Brain
document_type: Framework
version: 0.2.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/output-framework.md, salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/validation-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/business-analysis.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/brain/README.md]
keywords: [output framework]
tags: [salesforce, business-analyst, brain, documentation]
type: brain-module
---

# Output Framework

## Purpose

Documentation engine for Sprint 1 Milestone 1.9. Defines which artifact to produce, which template to use, required metadata, quality checks, and cross-references for each enterprise deliverable type.

## Artifact Selection Matrix

| User need | Artifact | Template | Playbook |
|-----------|----------|----------|----------|
| Business needs, scope, objectives | BRD | [brd-template.md](../templates/brd-template.md) | [discovery-playbook.md](../playbooks/discovery-playbook.md) |
| Detailed system behaviour | FRD | [frd-template.md](../templates/frd-template.md) | [requirements-elicitation.md](../playbooks/requirements-elicitation.md) |
| Agile backlog items | User stories | [user-story-template.md](../templates/user-story-template.md) | — |
| Standard vs custom decisions | Fit-gap analysis | Matrix in [fit-gap-analysis.md](../playbooks/fit-gap-analysis.md) | [fit-gap-analysis.md](../playbooks/fit-gap-analysis.md) |
| AS-IS / TO-BE visualization | Process map | [process-map.md](../templates/process-map.md) | [discovery-playbook.md](../playbooks/discovery-playbook.md) |
| Elicitation session output | Workshop notes | [workshop-agenda.md](../templates/workshop-agenda.md) | [discovery-playbook.md](../playbooks/discovery-playbook.md) |
| Risks, assumptions, issues, dependencies | RAID log | [raid-log-template.md](../templates/raid-log-template.md) | [discovery-playbook.md](../playbooks/discovery-playbook.md) |
| Req → story → test linkage | RTM | [traceability-matrix-template.md](../templates/traceability-matrix-template.md) | [uat-playbook.md](../playbooks/uat-playbook.md) |
| UAT execution | Test scenarios | UAT structure in [uat-playbook.md](../playbooks/uat-playbook.md) | [uat-playbook.md](../playbooks/uat-playbook.md) |
| Discovery close-out | Executive summary / readout | BRD §1 or [discovery-readout-outline.md](../examples/discovery-readout-outline.md) | [discovery-workshop-playbook.md](../playbooks/discovery-workshop-playbook.md) |
| Stakeholder influence | Stakeholder matrix | [stakeholder-matrix-template.md](../templates/stakeholder-matrix-template.md) | [requirements-elicitation.md](../playbooks/requirements-elicitation.md) |
| Process accountability | RACI | [raci-template.md](../templates/raci-template.md) | [discovery-workshop-playbook.md](../playbooks/discovery-workshop-playbook.md) |

Full template index: [../templates/README.md](../templates/README.md). RTM alias: [rtm-template.md](../templates/rtm-template.md).

## Metadata Requirements

Every generated artifact must include YAML frontmatter per [../../docs/metadata-schema.md](../../docs/metadata-schema.md):

```yaml
---
title: string
type: brd | frs | user-story | fit-gap | workshop-notes | process-map | traceability | raid | test-scenario
version: semver
status: draft | review | approved | deprecated
last_updated: YYYY-MM-DD
---
```

Optional: `project`, `author`, `tags`, `clouds`, `industry`, `parent_id`, `reviewers`.

## ID Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Business requirement | BR-xxx | BR-001 |
| Functional requirement | FR-xxx | FR-014 |
| User story | US-xxx | US-042 |
| Test scenario | TS-xxx | TS-008 |
| Epic | EP-xxx | EP-005 |
| Decision | D-xxx | D-02 |
| Risk / Assumption / Issue / Dependency | R- / A- / I- / DEP- | R-003 |

See [../../shared/taxonomy.md](../../shared/taxonomy.md).

## Quality Checks per Artifact

| Artifact | Minimum quality bar |
|----------|---------------------|
| BRD | Outcome per BR; unique IDs; in/out scope; assumptions |
| FRD | Testable behaviour; actor + trigger; links to BR |
| User story | INVEST; 3+ AC; requirement_refs |
| Fit-gap | Classification + recommendation + owner per row |
| RTM | No orphan stories or requirements |
| RAID | Owner and date on material items |
| Workshop notes | Decisions vs open questions separated |
| UAT scenario | Business scenario; not "page loads" only |

Detailed gates: [../checklists.md](../checklists.md), [validation-framework.md](validation-framework.md).

## Cross-Reference Rules

1. User stories **must** include `requirement_refs` to BR/FR IDs
2. RTM rows link BR → FR → US → TS
3. Fit-gap rows reference BR/FR IDs
4. RAID assumptions link to requirements they affect
5. FRD sections reference BR IDs; do not duplicate business rationale

## Review Checklist (Author)

Before marking `status: review`:

- [ ] Frontmatter complete
- [ ] Terminology matches [../../shared/glossary.md](../../shared/glossary.md)
- [ ] Output standards applied: [../../shared/output-standards.md](../../shared/output-standards.md)
- [ ] No PII or real client identifiers
- [ ] Assumptions, open questions, next steps included
- [ ] [anti-hallucination.md](anti-hallucination.md) pass

## Version History in Artifacts

Document control table or changelog section for material BRD/FRD revisions:

| Version | Date | Author | Summary |
|---------|------|--------|---------|

## Generation Workflow

```
1. Classify request → Artifact Selection Matrix
2. Load brain/reasoning-framework.md stages 1–11
3. Load template
4. Apply output-standards.md
5. Run validation-framework.md + checklists.md
6. Append assumptions, open questions, next steps
```


## Related Knowledge Documents

- [../../shared/document-types.md](../../shared/document-types.md)
- [../../shared/output-standards.md](../../shared/output-standards.md)
- [../../shared/reusable-components.md](../../shared/reusable-components.md)




## Related Interview Questions

- [../interview-guide.md](../interview-guide.md)

## Related Brain Modules

- [Output Framework](output-framework.md)
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

- **Previous:** [Identity](identity.md)
- **Next:** [Reasoning Framework](reasoning-framework.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
