---
title: Requirements Elicitation
module: Salesforce Business Analyst
category: Playbook
document_type: Consulting Methodology
version: 1.1.0
review_status: Approved
owner: BA Practice Lead
created_date: 2026-07-02
last_updated: 2026-07-02
review_cycle: quarterly
related_brain_modules: [salesforce-business-analyst/brain/reasoning-framework.md, salesforce-business-analyst/brain/enterprise-behaviors.md]
related_knowledge: [salesforce-business-analyst/knowledge/README.md]
related_templates: [salesforce-business-analyst/templates/README.md]
related_playbooks: [salesforce-business-analyst/playbooks/README.md]
related_scenarios: [salesforce-business-analyst/scenarios/README.md]
related_interview_topics: [salesforce-business-analyst/interview-guide/advanced/scenario-questions.md]
related_examples: [examples/sample-project/README.md]
related_documents: [salesforce-business-analyst/skill.md, salesforce-business-analyst/playbooks/README.md]
keywords: [requirements elicitation]
tags: [requirements-elicitation]
---

# Requirements Elicitation Playbook

Advanced elicitation beyond standard workshops.

## Preparation

- Review existing artifacts (SOW, prior BRDs, org charts)
- Prepare persona-based question sets
- Confirm recording / note-taking permissions
- Book 60–90 min per SME role; avoid groupthink in first round

## Question Framework (SPIN Adapted)

| Type | Purpose | Example |
|------|---------|---------|
| Situation | Context | "How do leads arrive today?" |
| Problem | Pain | "Where do duplicates cause rework?" |
| Implication | Impact | "What happens when sync fails overnight?" |
| Need-payoff | Value | "If reps saw X at login, what would change?" |

## Role-Based Question Banks

### Sales Rep

- Walk through last won deal—systems touched?
- What do you do in spreadsheets that isn't in CRM?
- Mobile constraints in field?

### Service Agent

- Open a complex case—what info is missing?
- Escalation triggers?
- Knowledge findability?

### Manager

- Forecast and pipeline confidence?
- Approval bottlenecks?
- Reporting gaps?

### IT / Integration

- System of record per entity?
- API limits, batch windows?
- Identity and SSO model?

## Techniques

### Prototyping Validation

Show Salesforce demo or wireframe: "Does this support step 3 of your process?"

### Contradiction Surfacing

When two SMEs disagree, document both views; schedule decision session.

### Observation

Shadow 2-hour live work session—note workarounds (they become requirements).

## Documenting Elicitation Output

Same day:

1. Themes → draft BR IDs
2. Quotes → workshop appendix (anonymized if needed)
3. New assumptions → RAID
4. Open questions → numbered list with owners

## Elicitation Anti-Patterns

| Anti-pattern | Fix |
|--------------|-----|
| Leading questions | "How do you handle X?" not "You want automation for X, right?" |
| Solution jumping | Capture need; fit-gap later |
| Single SME truth | Triangulate with 2+ sources |
| Missing silent stakeholders | Ask "who will resist this change?" |

## Related Brain Modules

- [Reasoning Framework](../brain/reasoning-framework.md)
- [Enterprise Behaviors](../brain/enterprise-behaviors.md)

## Related Knowledge

- [Readme](../knowledge/README.md)

## Related Templates

- [Readme](../templates/README.md)

## Related Playbooks

- [Readme](README.md)

## Related Industry Scenarios

- [Readme](../scenarios/README.md)

## Related Interview Topics

- [Scenario Questions](../interview-guide/advanced/scenario-questions.md)

## Related Examples

- [Readme](../../examples/sample-project/README.md)

## Related Documents

- [Skill](../skill.md)
- [Readme](README.md)

## Traceability

**Upstream:** Knowledge, templates | **Downstream:** Scenarios, workshop outputs | **Validation:** checklists.md

## Navigation

- **Previous:** [Requirement Workshop Playbook](requirement-workshop-playbook.md)
- **Next:** [Solution Recommendation Playbook](solution-recommendation-playbook.md)
- **See Also:** [skill.md](../skill.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 1.1.0 | 2026-07-02 | BA Practice Lead | Sprint 7 cross-linking and metadata enrichment |
