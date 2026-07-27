---
title: Agentforce Testing — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.18.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [agentforce-testing]
---

# Agentforce Testing

## Purpose

Enterprise **AI Quality Engineering** capability for Salesforce Agentforce. Validates prompt quality, topic routing, grounding, tool invocation, guardrails, hallucination risk, and conversation correctness — not a traditional UI automation framework.

## Capabilities

- Agent configuration and prompt review  
- Topic classification and multi-turn conversation testing  
- Knowledge grounding and retrieval assessment  
- Tool/Flow/Apex/API invocation validation  
- Guardrail and hallucination detection  
- Security/PII assessment with PTA chain  
- Regression and release readiness for AI agents  

## Supported Agentforce Components

Agents · Topics · Instructions · Prompt Templates · Actions (Flow, Apex, External) · Knowledge Grounding · Session Context · Escalation · Guardrails · Monitoring (advisory)

## Folder Structure

```
skills/agentforce-testing/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 20 reasoning articles
├── playbooks/       ← 9 playbooks
├── templates/       ← 9 templates
├── prompts/         ← 10 prompts
├── examples/        ← 10 examples
└── tests/           ← 15 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Business scenario / persona | Yes |
| Agent configuration (topics, prompts, actions) | Yes |
| Knowledge/grounding sources | Recommended |
| Guardrail policy | Recommended |
| MIA impact report | When actions mutate metadata/data |

## Outputs

18-section AI QA report — see [SKILL.md](SKILL.md). Primary template: [templates/conversation-test-report.md](templates/conversation-test-report.md).

## Sample Prompt

```
Load skills/agentforce-testing/SKILL.md.
Business Scenario: Customers ask bill amount via Utility Billing Agent.
Agent config: GetBillSummary API action; Knowledge for payment policy; no card capture.
Produce all 18 sections including grounding, guardrails, and hallucination traps.
```

## Example Scenarios

See [examples/README.md](examples/README.md) — Service, Sales, Utilities, Knowledge, FSL, HR, IT, and more.

## AI Testing Best Practices

- Config + prompt + grounding + tools **before** conversation scripts  
- Score responses with the evaluation rubric every time  
- Chain MIA / SOVA / PTA for mutating or sensitive actions  
- Label assumptions; never invent confidence or accuracy %  

## Known Limitations

- No live org/LLM execution in the skill pack  
- Feature availability depends on license — confirm before asserting  
- Compliance attestations require human Legal/Compliance  

## Future Enhancements

- Deeper Agentforce Studio metadata fixtures  
- Production transcript sampling playbooks  
- Industry golden conversation packs  

## Related Documents

- [SKILL.md](SKILL.md)
- [../README.md](../README.md)
- [../../knowledge/clouds/agentforce.md](../../knowledge/clouds/agentforce.md)
- [../../enterprise-quality/ai-governance/README.md](../../enterprise-quality/ai-governance/README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.18.0 | 2026-07-27 | QE Practice Lead | Initial release |
