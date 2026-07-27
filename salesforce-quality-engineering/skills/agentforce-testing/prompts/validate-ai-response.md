---
title: Validate AI Response
module: Salesforce Quality Engineering
category: QE Specialized Skill Prompt
document_type: Prompt
version: 0.18.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [agentforce-testing, prompt]
---

# Validate AI Response

## Prompt

```
Act as Agentforce Testing capability. Provide Business Scenario and Agent Configuration Reviewed BEFORE conversation scripts. Produce all 18 sections per SKILL.md. Evaluate AI quality (accuracy, grounding, guardrails, hallucination). Label assumptions; do not invent confidence %. Context:
[paste]
Focus: AI Response Evaluation criteria.
```

## Required Output Sections

1. Executive Summary
2. Business Scenario
3. Agent Configuration Reviewed
4. Prompt Analysis
5. Topic Classification Validation
6. Knowledge Grounding Assessment
7. Tool Invocation Validation
8. AI Response Evaluation
9. Guardrail Assessment
10. Hallucination Risk
11. Security Assessment
12. Negative Test Scenarios
13. Edge Case Scenarios
14. Regression Scope
15. Automation Opportunities
16. Deployment Readiness
17. Risks
18. Recommendations

## Quality Gate

- Business Scenario and Agent Configuration BEFORE conversation scripts.
- Evaluate AI quality (accuracy, grounding, guardrails, hallucination)—not UI clicks alone.
- Label assumptions; do not invent confidence or accuracy percentages.
