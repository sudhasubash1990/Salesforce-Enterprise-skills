---
title: AI in Business Analysis
module: Salesforce Business Analyst
category: Knowledge
document_type: Knowledge Article
version: 0.3.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
difficulty: intermediate
industry: all
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/output-framework.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/interview-index.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/knowledge/README.md]
keywords: [ai in business analysis]
tags: [ai, responsible-ai, agents, prompt-engineering]
review-cycle: quarterly
salesforce-cloud: Platform
---

# AI in Business Analysis

## Overview

Responsible use of AI for requirements analysis, workshops, and documentation on Salesforce programs.

## Purpose

Guide human and agent practitioners on AI-assisted BA with mandatory human accountability.

## Why It Matters

Unreviewed AI output causes hallucinated requirements, compliance risk, and client trust failure.

## Business Context

AI accelerates drafting; humans approve, facilitate, and own decisions.

## Salesforce Context

Agents load skill.md, brain modules, and knowledge base—must validate before client delivery.

## Core Concepts

| Use case | AI role | Human role |
|----------|---------|------------|
| Requirement analysis | Draft, gap detect | Validate with stakeholders |
| Workshops | Prep questions, synthesize notes | Facilitate, decide |
| Documentation | Generate from templates | Review, approve sign-off |
| Fit-gap | Suggest standard options | Architect confirm |
| Traceability | Draft RTM | PO/BA maintain |

**Responsible AI principles:**

- Label assumptions and TBC items
- No invented compliance claims
- Human review before external sharing
- Prompt patterns in [../prompts.md](../prompts.md)

## Key Terminology

| Term | Definition |
|------|------------|
| Human-in-the-loop | Mandatory review before production use |
| Agent | AI guided by repository skills |

## Frameworks and Models

- [../brain/anti-hallucination.md](../brain/anti-hallucination.md)
- [../brain/validation-framework.md](../brain/validation-framework.md)
- [../../.cursor/rules/instructions.mdc](../../.cursor/rules/instructions.mdc)

## Enterprise Best Practices

- Use templates for structure
- Peer review AI-generated BRD sections
- Log AI-assisted drafts as draft status until approved
- Anonymize all examples

## Common Mistakes

- Pasting AI output to client without review
- Trusting feature claims without documentation check

## Anti-Patterns

- AI as substitute for discovery
- Skipping validation framework for speed

## Decision Guidelines

Regulated or high-risk requirements: extra human review; AI draft only.

## Real-World Examples

Agent drafts user stories from BRD excerpt; BA refines AC and runs checklists before sprint.

## Industry Considerations

Client policies on AI usage—document in RAID if restricted.

## AI Guidance

This article governs you. Always run validation and anti-hallucination before responding.

## Review Checklist

- [ ] Validation framework pass
- [ ] Assumptions section present
- [ ] No unsupported Salesforce claims

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

- [Interview Index](../interview-guide/interview-index.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Brain modules | **Downstream:** Templates, playbooks, deliverables | **Validation:** checklists.md

## Navigation

- **Previous:** [Acceptance Criteria](acceptance-criteria.md)
- **Next:** [Assumptions Management](assumptions-management.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
