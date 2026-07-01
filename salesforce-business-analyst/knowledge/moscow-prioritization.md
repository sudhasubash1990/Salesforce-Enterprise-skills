---
title: MoSCoW Prioritization
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: foundational
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/requirement-gathering.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [moscow prioritization]
tags: [moscow, prioritization, scope]
review-cycle: quarterly
salesforce-cloud: Platform
---

# MoSCoW Prioritization

## Overview

Must, Should, Could, Won't classification for Salesforce release scope.

## Purpose

Enterprise-standard prioritization for BRD and workshop outputs.

## Why It Matters

Without Won't, scope creep is inevitable. Without Must discipline, releases slip.

## Business Context

MoSCoW negotiates trade-offs when capacity is fixed.

## Salesforce Context

Apply per requirement and per capability theme; align to release trains R1/R2/R3.

## Core Concepts

| Priority | Meaning | Release implication |
|----------|---------|---------------------|
| **Must** | Release blocker; no workaround | Required for go-live |
| **Should** | Important; workaround exists | Strong candidate; may defer with sponsor approval |
| **Could** | Desirable if capacity | Pull if slack |
| **Won't** | Explicitly out of this release | Prevents creep |

**Enterprise rule:** Every Must needs documented business justification and sponsor awareness.

## Key Terminology

See [../../shared/taxonomy.md](../../shared/taxonomy.md#priority-taxonomy-moscow).

## Frameworks and Models

Workshop prioritization segment in discovery playbook.

## Enterprise Best Practices

- Cap Must list to realistic capacity
- Won't list reviewed in steering
- Re-MoSCoW at change requests

## Common Mistakes

- 80% Must
- Empty Won't section

## Anti-Patterns

- Renaming Won't to Could to avoid difficult conversation

## Decision Guidelines

If Must exceeds capacity, facilitate sponsor trade-off session—do not silently demote.

## Real-World Examples

CPQ evaluation Won't R1; dealer portal cases Must R3 in Apex Manufacturing sample.

## Industry Considerations

Regulated Must items may be legal mandates—validate with Compliance, not BA alone.

## AI Guidance

Apply MoSCoW in BRD tables. Challenge all-Must lists respectfully.

## Review Checklist

- [ ] Each Must justified
- [ ] Won't section populated
- [ ] Release hints aligned

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Output Framework](../brain/output-framework.md)

## Related Knowledge

- [Readme](README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](../playbooks/README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Requirement Gathering](../interview-guide/requirement-gathering.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Kano Model](kano-model.md)
- **Next:** [Prioritization Techniques](prioritization-techniques.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
