"""Generate Agentforce Testing skill pack."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "skills" / "agentforce-testing"
VERSION = "0.18.0"
DATE = "2026-07-27"

OUTPUT_SECTIONS = [
    "Executive Summary",
    "Business Scenario",
    "Agent Configuration Reviewed",
    "Prompt Analysis",
    "Topic Classification Validation",
    "Knowledge Grounding Assessment",
    "Tool Invocation Validation",
    "AI Response Evaluation",
    "Guardrail Assessment",
    "Hallucination Risk",
    "Security Assessment",
    "Negative Test Scenarios",
    "Edge Case Scenarios",
    "Regression Scope",
    "Automation Opportunities",
    "Deployment Readiness",
    "Risks",
    "Recommendations",
]


def fm(title: str, category: str, doc_type: str, tags: list[str]) -> str:
    return f"""---
title: {title}
module: Salesforce Quality Engineering
category: {category}
document_type: {doc_type}
version: {VERSION}
review_status: Draft
owner: QE Practice Lead
created_date: {DATE}
last_updated: {DATE}
review_cycle: quarterly
tags: [{", ".join(tags)}]
---

"""


def write(rel: str, content: str) -> None:
    path = CAP / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {rel}")


def knowledge_article(title, slug, purpose, reasoning, cross_links, rules):
    links = "\n".join(f"- [{n}]({p})" for n, p in cross_links)
    return fm(title, "QE Specialized Skill Knowledge", "Knowledge Article", ["agentforce-testing", "knowledge"]) + f"""# {title}

## Purpose

{purpose}

## Reasoning Model

{chr(10).join(f"{i}. {r}" for i, r in enumerate(reasoning, 1))}

## Decision Rules

{chr(10).join(f"- {r}" for r in rules)}

## Cross-Links (Canonical Depth)

{links}

## Related Documents

- [SKILL.md](../SKILL.md)
- [knowledge/README.md](README.md)

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial capability knowledge |
"""


def playbook(title, slug, objective, inputs, workflow, decisions, expected, deliverables, escalation, pointer=""):
    ptr = f"\n\n**Pointer:** {pointer}" if pointer else ""
    b = lambda xs: "\n".join(f"- {x}" for x in xs)
    return fm(title, "QE Specialized Skill Playbook", "Playbook", ["agentforce-testing", "playbook"]) + f"""# {title}

## Objective

{objective}{ptr}

## Inputs

{b(inputs)}

## Validation Workflow

{b(workflow)}

## Decision Points

{b(decisions)}

## Expected Results

{b(expected)}

## Deliverables

{b(deliverables)}

## Escalation Rules

{b(escalation)}
"""


def template_doc(title, sections):
    body = "\n\n".join(f"## {s}\n\n_Complete during analysis._" for s in sections)
    return fm(title, "QE Specialized Skill Template", "Template", ["agentforce-testing", "template"]) + f"""# {title}

{body}

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| {VERSION} | {DATE} | QE Practice Lead | Initial template |
"""


def prompt_doc(title, prompt, sections):
    return fm(title, "QE Specialized Skill Prompt", "Prompt", ["agentforce-testing", "prompt"]) + f"""# {title}

## Prompt

```
{prompt}
```

## Required Output Sections

{chr(10).join(f"{i}. {s}" for i, s in enumerate(sections, 1))}

## Quality Gate

- Business Scenario and Agent Configuration BEFORE conversation scripts.
- Evaluate AI quality (accuracy, grounding, guardrails, hallucination)—not UI clicks alone.
- Label assumptions; do not invent confidence or accuracy percentages.
"""


def example_doc(title, scenario, config, conversation, expected, grounding, guardrail, negative, edges, qa):
    return fm(title, "QE Specialized Skill Example", "Example", ["agentforce-testing", "example"]) + f"""# {title}

## Business Scenario

{scenario}

## Agent Configuration

{config}

## Sample Conversation

{conversation}

## Expected Response

{expected}

## Grounding Validation

{grounding}

## Guardrail Validation

{guardrail}

## Negative Tests

{negative}

## Edge Cases

{edges}

## QA Recommendations

{qa}
"""


def main() -> None:
    print("Generating Agentforce Testing skill pack...")
    CAP.mkdir(parents=True, exist_ok=True)

    write(
        "skill-config.yaml",
        f"""name: agentforce-testing
short_id: AFT
version: {VERSION}
parent_module: salesforce-quality-engineering
entry: SKILL.md

routing:
  keywords:
    - Agentforce
    - agentforce
    - AI agent
    - AI Agent
    - prompt
    - prompt template
    - topic
    - action
    - guardrails
    - guardrail
    - grounding
    - knowledge grounding
    - AI response
    - agent conversation
    - Copilot
    - Einstein
    - AI automation
    - LLM
    - RAG
    - agent testing
    - AI validation
    - prompt evaluation
    - tool invocation
    - hallucination
    - human handoff
    - escalation
    - multi-turn
    - conversation test
  primary_support:
    - knowledge/clouds/agentforce.md
    - enterprise-quality/ai-governance/
  upstream_skills:
    - skills/metadata-impact-analyzer
  downstream_capabilities:
    - skills/soql-validation-assistant
    - skills/permission-testing-agent
  downstream_after_analysis:
    - knowledge/test-design-engine.md

output_schema:
  sections:
{chr(10).join(f'    - id: {s.lower().replace(" ", "_")}' + chr(10) + f'      title: "{s}"' for s in OUTPUT_SECTIONS)}

quality_gates:
  - business_and_config_before_conversation_scripts
  - ai_evaluation_criteria_applied
  - grounding_and_guardrail_sections_required
  - no_invented_confidence_or_accuracy_percent
  - chain_mia_sova_pta_when_actions_mutate_or_expose_data

escalation:
  - signal: hallucination_in_regulated_domain
    to: Solution Architect + Compliance advisory
  - signal: guardrail_bypass
    to: Security Architect
  - signal: agent_action_writes_production_data
    to: Release Manager + MIA
""",
    )

    cloud = "../../knowledge/clouds/agentforce.md"
    gov = "../../enterprise-quality/ai-governance/README.md"
    mia = "../../skills/metadata-impact-analyzer/SKILL.md"
    sova = "../soql-validation-assistant/SKILL.md"
    pta = "../permission-testing-agent/SKILL.md"

    knowledge_specs = [
        ("Agentforce Architecture", "agentforce-architecture.md",
         "Map agent, topics, actions, and grounding layers before designing AI QA.",
         ["Identify agent type and channel (employee, customer, service).", "Inventory topics, instructions, actions, knowledge sources.", "Separate configuration review from conversation scripts.", "Flag licensed features—do not invent Agentforce capabilities."],
         [("Agentforce Cloud Knowledge", cloud), ("AI Governance", gov)],
         ["Confirm edition/license before asserting features.", "UI automation alone is insufficient for Agentforce QA."]),
        ("Agent Lifecycle", "agent-lifecycle.md",
         "Align QA gates to design, build, test, deploy, monitor phases.",
         ["Map requirement → agent design → sandbox validation → release → monitoring.", "Define entry/exit criteria per phase.", "Plan hypercare signals for agent failures."],
         [("Agentforce Cloud Knowledge", cloud), ("Release Readiness", "../../knowledge/release/release-readiness.md")],
         ["No production enablement without grounding and guardrail evidence."]),
        ("Topics", "topics.md",
         "Validate topic classification and routing to correct agent behavior.",
         ["List topics and classification criteria.", "Design utterances for in-topic and out-of-topic.", "Verify handoff when topic confidence is low."],
         [("Agentforce Cloud Knowledge", cloud)],
         ["Ambiguous utterance → expect clarification or escalation, not silent wrong topic."]),
        ("Prompt Templates", "prompt-templates.md",
         "Review prompt templates for instruction clarity, variables, and safety.",
         ["Inspect system/instructions vs user prompt.", "Check variable bindings to Salesforce data.", "Assess prompt adherence and over-constrained vs under-constrained instructions."],
         [("Agentforce Cloud Knowledge", cloud), ("AI Governance", gov)],
         ["Prompt change without regression pack → High AI regression risk."]),
        ("Actions", "actions.md",
         "Validate agent-invoked actions and side effects.",
         ["Inventory actions (Flow, Apex, API).", "Map inputs/outputs and failure modes.", "If action mutates records → chain Metadata Impact Analyzer."],
         [("Agentforce Cloud Knowledge", cloud), ("Metadata Impact Analyzer", mia)],
         ["Write actions require backend SOQL and permission validation."]),
        ("Flow Actions", "flow-actions.md",
         "Validate Flow-backed agent actions.",
         ["Confirm Flow version and entry criteria.", "Test success, fault, and partial paths.", "Verify agent messaging on Flow faults."],
         [("Automation Knowledge", "../../knowledge/automation/README.md"), ("Metadata Impact Analyzer", mia)],
         ["Inactive Flow version → Fail deployment readiness."]),
        ("Apex Actions", "apex-actions.md",
         "Validate Apex-backed agent tools.",
         ["Review sharing mode and governor risk.", "Test exception handling surfaced to conversation.", "Confirm test coverage exists as advisory—not invent %."],
         [("Platform Apex", "../../knowledge/platform/apex.md"), ("Metadata Impact Analyzer", mia)],
         ["without sharing Apex → escalate PTA for visibility impact."]),
        ("External Integrations", "external-integrations.md",
         "Validate external API actions from agents.",
         ["Map Named Credential / Connected App.", "Test timeout, 4xx/5xx, and empty payload handling.", "Verify agent does not invent API data on failure."],
         [("Integration Knowledge", "../../knowledge/integration/README.md"), ("SOQL Validation", sova)],
         ["API failure must not produce hallucinated business facts."]),
        ("Knowledge Grounding", "knowledge-grounding.md",
         "Assess whether responses are grounded in approved knowledge/data.",
         ["Identify grounding sources (Knowledge, Data Cloud, CRM records).", "Design retrieval-hit and retrieval-miss tests.", "Require citation/source behavior when configured."],
         [("Agentforce Cloud Knowledge", cloud)],
         ["Missed retrieval → refuse or escalate; never invent policy."]),
        ("Retrieval Strategies", "retrieval-strategies.md",
         "Reason about RAG retrieval quality for agent answers.",
         ["Define expected document set per query.", "Test synonym and out-of-corpus queries.", "Label confidence as qualitative unless measured evidence provided."],
         [("Agentforce Cloud Knowledge", cloud), ("AI Governance", gov)],
         ["Do not invent RAG accuracy percentages."]),
        ("Conversation Design", "conversation-design.md",
         "Validate conversation UX: clarity, tone, next steps.",
         ["Check greeting, clarification, confirmation, close.", "Align tone to brand and persona.", "Verify actionable next steps."],
         [("Agentforce Cloud Knowledge", cloud)],
         ["Vague answers without next step → Fail UX criterion."]),
        ("Session Context", "session-context.md",
         "Validate session memory and context retention.",
         ["Confirm fields retained across turns.", "Test context reset and session timeout.", "Verify PII not leaked across users/sessions."],
         [("Permission Testing Agent", pta), ("AI Governance", gov)],
         ["Cross-session PII leakage → Critical security."]),
        ("Multi-turn Conversations", "multi-turn-conversations.md",
         "Validate multi-step reasoning and context continuity.",
         ["Design 3–5 turn journeys with changing intent.", "Verify prior facts retained correctly.", "Test correction and contradiction handling."],
         [("Conversation Design", "conversation-design.md")],
         ["Context drop mid-journey → High regression priority."]),
        ("Prompt Engineering", "prompt-engineering.md",
         "Apply prompt engineering QA criteria.",
         ["Check role, constraints, output format, examples.", "Detect conflicting instructions.", "Recommend least-privilege tool access in prompt."],
         [("AI Governance", gov)],
         ["Conflicting instructions → clarify before release."]),
        ("AI Guardrails", "ai-guardrails.md",
         "Validate safety and policy guardrails.",
         ["List disallowed topics and data classes.", "Test jailbreak and policy-bypass attempts.", "Verify refusal language and escalation."],
         [("AI Governance", gov), ("Permission Testing Agent", pta)],
         ["Guardrail bypass in sandbox → block production enablement."]),
        ("Responsible AI", "responsible-ai.md",
         "Align Agentforce QA with responsible AI principles.",
         ["Fairness, transparency, human oversight, privacy.", "Document human-in-the-loop for high-risk decisions.", "Cross-link Sprint 10 AI governance—do not invent compliance."],
         [("AI Governance", gov)],
         ["Never claim Responsible AI certification without evidence."]),
        ("Hallucination Mitigation", "hallucination-mitigation.md",
         "Detect and reduce ungrounded agent claims.",
         ["Compare response claims to grounding sources.", "Design trap questions with no source.", "Require refuse/escalate when ungrounded."],
         [("Knowledge Grounding", "knowledge-grounding.md")],
         ["Hallucinated financial/legal/medical claim → Critical."]),
        ("Human Escalation", "human-escalation.md",
         "Validate handoff to human agents.",
         ["Define escalation triggers (confidence, sentiment, policy).", "Test transfer payload and context.", "Verify agent stops acting after handoff."],
         [("Agentforce Cloud Knowledge", cloud)],
         ["Silent failure without handoff → Fail release readiness."]),
        ("Agent Monitoring", "agent-monitoring.md",
         "Define post-deploy monitoring for agent quality.",
         ["Identify metrics signals (deflection, escalate rate, CSAT)—use program values only.", "Plan transcript review samples.", "Link production support for Sev1 agent outages."],
         [("Production Support Agentforce", "../../production-support/salesforce/agentforce.md")],
         ["Do not invent SLA/MTTR values."]),
        ("AI Testing Best Practices", "ai-testing-best-practices.md",
         "Synthesize enterprise Agentforce QA discipline.",
         ["Config + prompt + grounding + tools before scripts.", "Apply evaluation rubric every response.", "Chain MIA/SOVA/PTA for mutating/sensitive actions.", "Label assumptions; no invented %."],
         [("Agentforce Cloud Knowledge", cloud), ("Test Design Engine", "../../knowledge/test-design-engine.md")],
         ["Every deliverable uses 18-section schema."]),
    ]
    for spec in knowledge_specs:
        write(f"knowledge/{spec[1]}", knowledge_article(*spec))

    write(
        "knowledge/README.md",
        fm("Agentforce Testing — Knowledge", "QE Specialized Skill Knowledge", "Guide", ["agentforce-testing"])
        + """# Agentforce Testing — Knowledge

Canonical product overview: [`../../knowledge/clouds/agentforce.md`](../../knowledge/clouds/agentforce.md). These articles provide **AI QA reasoning models**.

| Document | Focus |
|----------|-------|
| [Agentforce Architecture](agentforce-architecture.md) | Layered agent model |
| [Agent Lifecycle](agent-lifecycle.md) | Design-to-monitor gates |
| [Topics](topics.md) | Topic classification |
| [Prompt Templates](prompt-templates.md) | Prompt QA |
| [Actions](actions.md) | Tool actions |
| [Flow Actions](flow-actions.md) | Flow tools |
| [Apex Actions](apex-actions.md) | Apex tools |
| [External Integrations](external-integrations.md) | API tools |
| [Knowledge Grounding](knowledge-grounding.md) | Grounding |
| [Retrieval Strategies](retrieval-strategies.md) | RAG retrieval |
| [Conversation Design](conversation-design.md) | Conversation UX |
| [Session Context](session-context.md) | Memory/session |
| [Multi-turn Conversations](multi-turn-conversations.md) | Multi-turn |
| [Prompt Engineering](prompt-engineering.md) | Prompt craft QA |
| [AI Guardrails](ai-guardrails.md) | Safety |
| [Responsible AI](responsible-ai.md) | RAI principles |
| [Hallucination Mitigation](hallucination-mitigation.md) | Ungrounded claims |
| [Human Escalation](human-escalation.md) | Handoff |
| [Agent Monitoring](agent-monitoring.md) | Ops signals |
| [AI Testing Best Practices](ai-testing-best-practices.md) | Synthesis |
""",
    )

    playbooks = [
        ("Prompt Validation Playbook", "prompt-validation.md",
         "Validate prompt templates for clarity, safety, and adherence.",
         ["Prompt template text", "Variables and data bindings", "Disallowed topics"],
         ["Review instructions vs user prompt.", "Check conflicts and missing constraints.", "Design adherence and jailbreak tests.", "Document Prompt Analysis section."],
         ["Prompt ready for release?", "Sensitive variables exposed?"],
         ["Prompt adherence scenarios defined", "Safety constraints explicit"],
         ["Prompt Review Report"],
         ["Conflicting instructions → Prompt Engineer + SA"],
         f"[{gov}]({gov})"),
        ("Topic Validation Playbook", "topic-validation.md",
         "Validate topic classification and routing.",
         ["Topic list", "Sample utterances", "Out-of-scope intents"],
         ["Build utterance matrix per topic.", "Test ambiguous and multi-intent utterances.", "Verify clarification/escalation."],
         ["Is topic taxonomy complete?"],
         ["In-topic correctly routed", "Out-of-topic refused or clarified"],
         ["Topic Classification Validation section"],
         ["Systematic misrouting → Agentforce Architect"],
         ""),
        ("Conversation Testing Playbook", "conversation-testing.md",
         "Execute multi-turn conversation quality tests.",
         ["Journey scripts", "Personas", "Evaluation rubric"],
         ["Run happy-path multi-turn.", "Score AI Response Evaluation criteria.", "Capture negative and edge cases."],
         ["Enough turns to prove context retention?"],
         ["Rubric scores documented with evidence", "Assumptions labeled"],
         ["Conversation Test Report"],
         ["Critical UX failure → Product Owner"],
         ""),
        ("Grounding Validation Playbook", "grounding-validation.md",
         "Prove answers are grounded in approved sources.",
         ["Knowledge corpus", "CRM data scope", "Retrieval config"],
         ["Design hit/miss retrieval tests.", "Compare claims to sources.", "Document Grounding Assessment."],
         ["Source of truth identified?"],
         ["No ungrounded policy claims", "Miss path refuses or escalates"],
         ["Knowledge Grounding Assessment"],
         ["Regulated hallucination → Compliance advisory"],
         ""),
        ("Tool Invocation Playbook", "tool-invocation.md",
         "Validate correct tool selection and execution.",
         ["Action inventory", "Input schemas", "Failure modes"],
         ["Test correct tool for intent.", "Test wrong-tool avoidance.", "Validate Flow/Apex/API outcomes.", "Chain MIA/SOVA/PTA as needed."],
         ["Does action mutate data?"],
         ["Correct tool invoked", "Faults communicated without hallucination"],
         ["Tool Invocation Validation section"],
         ["Unexpected DML → MIA + Release Manager"],
         f"[{mia}]({mia})"),
        ("Hallucination Detection Playbook", "hallucination-detection.md",
         "Detect ungrounded or fabricated responses.",
         ["Trap questions", "Source corpus", "Regulated topics"],
         ["Ask questions with no source.", "Ask contradictory facts.", "Score Hallucination Risk."],
         ["Is refuse/escalate configured?"],
         ["Ungrounded answers refused", "No fabricated IDs/amounts"],
         ["Hallucination Review"],
         ["Critical hallucination → block deploy"],
         ""),
        ("Guardrail Validation Playbook", "guardrail-validation.md",
         "Validate safety and policy guardrails.",
         ["Disallowed topics", "PII classes", "Jailbreak samples"],
         ["Attempt policy bypass.", "Request sensitive data.", "Verify refusal and escalation."],
         ["Guest/community channel in scope?"],
         ["Guardrails enforce refusals", "No PII leakage"],
         ["Guardrail Assessment Report"],
         ["Bypass → Security Architect"],
         f"[{pta}]({pta})"),
        ("Release Readiness Playbook", "release-readiness.md",
         "Assemble Agentforce release evidence pack.",
         ["18-section report", "Regression results", "Monitoring plan"],
         ["Complete Agent Release Checklist.", "Confirm grounding/guardrail evidence.", "Issue Go/No-Go recommendation."],
         ["Residual AI risk accepted?"],
         ["Checklist complete", "Open Critical risks = 0 or accepted"],
         ["Agent Release Checklist", "Deployment Readiness section"],
         ["Critical open → No-Go"],
         "../../knowledge/release/release-readiness.md"),
        ("AI Regression Playbook", "ai-regression.md",
         "Select risk-based Agentforce regression after prompt/topic/action change.",
         ["Change list", "Prior conversation packs", "MIA deltas"],
         ["Map change to In/Out/Conditional AI scenarios.", "Re-run grounding and guardrail smoke.", "Update AI Regression Checklist."],
         ["Can any topic be Out of scope?"],
         ["High-risk journeys revalidated", "Hallucination traps re-run"],
         ["AI Regression Checklist", "Regression Scope"],
         ["Scope dispute → Test Lead + Agentforce Architect"],
         "../../playbooks/regression-planning.md"),
    ]
    for title, slug, *rest in playbooks:
        write(f"playbooks/{slug}", playbook(title, slug, *rest))

    write(
        "playbooks/README.md",
        fm("Agentforce Testing — Playbooks", "QE Specialized Skill Playbook", "Guide", ["agentforce-testing"])
        + """# Agentforce Testing — Playbooks

| Playbook | Focus |
|----------|-------|
| [Prompt Validation](prompt-validation.md) | Prompt templates |
| [Topic Validation](topic-validation.md) | Topics/routing |
| [Conversation Testing](conversation-testing.md) | Multi-turn QA |
| [Grounding Validation](grounding-validation.md) | Knowledge/RAG |
| [Tool Invocation](tool-invocation.md) | Actions/tools |
| [Hallucination Detection](hallucination-detection.md) | Ungrounded claims |
| [Guardrail Validation](guardrail-validation.md) | Safety |
| [Release Readiness](release-readiness.md) | Go/No-Go |
| [AI Regression](ai-regression.md) | AI regression |
""",
    )

    templates = [
        ("Agent Test Strategy", ["Purpose", "Scope", "Agent Inventory", "Evaluation Criteria", "Environments", "Risks", "Entry/Exit", "Governance"]),
        ("AI Test Plan", ["Objectives", "In Scope", "Out of Scope", "Scenarios", "Data", "Schedule", "Owners", "Exit Criteria"]),
        ("Prompt Review Report", ["Prompt Under Review", "Strengths", "Gaps", "Safety Issues", "Recommended Changes", "Retest Plan"]),
        ("Conversation Test Report", OUTPUT_SECTIONS),
        ("Guardrail Assessment Report", ["Guardrails Configured", "Tests Executed", "Bypass Attempts", "Results", "Residual Risk", "Recommendations"]),
        ("AI Risk Assessment", ["Risk ID", "Category", "Likelihood Evidence", "Impact", "Mitigation", "Owner"]),
        ("Hallucination Review", ["Claim", "Source Expected", "Actual Grounding", "Risk", "Disposition"]),
        ("Agent Release Checklist", ["Config Complete", "Prompt Reviewed", "Grounding Evidence", "Guardrails Evidence", "Regression Pass", "Monitoring Ready", "Go/No-Go"]),
        ("AI Regression Checklist", ["Change Summary", "In Scope Journeys", "Hallucination Traps", "Guardrail Smoke", "Tool Smoke", "Sign-off"]),
    ]
    for title, sections in templates:
        slug = title.lower().replace(" ", "-") + ".md"
        write(f"templates/{slug}", template_doc(title, sections))

    write(
        "templates/README.md",
        fm("Agentforce Testing — Templates", "QE Specialized Skill Template", "Guide", ["agentforce-testing"])
        + """# Agentforce Testing — Templates

| Template | Use |
|----------|-----|
| [Agent Test Strategy](agent-test-strategy.md) | Program strategy |
| [AI Test Plan](ai-test-plan.md) | Release test plan |
| [Prompt Review Report](prompt-review-report.md) | Prompt QA |
| [Conversation Test Report](conversation-test-report.md) | Primary 18-section deliverable |
| [Guardrail Assessment Report](guardrail-assessment-report.md) | Safety |
| [AI Risk Assessment](ai-risk-assessment.md) | Risk register |
| [Hallucination Review](hallucination-review.md) | Claim vs source |
| [Agent Release Checklist](agent-release-checklist.md) | Release gate |
| [AI Regression Checklist](ai-regression-checklist.md) | Regression |
""",
    )

    base = (
        "Act as Agentforce Testing capability. Provide Business Scenario and Agent Configuration Reviewed "
        "BEFORE conversation scripts. Produce all 18 sections per SKILL.md. Evaluate AI quality "
        "(accuracy, grounding, guardrails, hallucination). Label assumptions; do not invent confidence %. Context:\n[paste]"
    )
    prompts = [
        ("Review Agent Configuration", "review-agent-configuration.md", base, OUTPUT_SECTIONS),
        ("Validate Prompt Template", "validate-prompt-template.md", base + "\nFocus: Prompt Analysis and adherence tests.", OUTPUT_SECTIONS),
        ("Generate Conversation Tests", "generate-conversation-tests.md", base + "\nFocus: multi-turn scripts with evaluation rubric.", OUTPUT_SECTIONS),
        ("Review Topic Classification", "review-topic-classification.md", base + "\nFocus: Topic Classification Validation.", OUTPUT_SECTIONS),
        ("Validate Knowledge Grounding", "validate-knowledge-grounding.md", base + "\nFocus: Knowledge Grounding Assessment and hallucination traps.", OUTPUT_SECTIONS),
        ("Review Tool Invocation", "review-tool-invocation.md", base + "\nFocus: Tool Invocation Validation; chain MIA/SOVA/PTA if needed.", OUTPUT_SECTIONS),
        ("Validate AI Response", "validate-ai-response.md", base + "\nFocus: AI Response Evaluation criteria.", OUTPUT_SECTIONS),
        ("Detect Hallucinations", "detect-hallucinations.md", base + "\nFocus: Hallucination Risk and Hallucination Review.", OUTPUT_SECTIONS),
        ("Validate Guardrails", "validate-guardrails.md", base + "\nFocus: Guardrail Assessment and negative safety tests.", OUTPUT_SECTIONS),
        ("Assess Deployment Readiness", "assess-deployment-readiness.md", base + "\nFocus: Deployment Readiness, Risks, Recommendations.", OUTPUT_SECTIONS),
    ]
    for title, slug, prompt, sections in prompts:
        write(f"prompts/{slug}", prompt_doc(title, prompt, sections))

    write(
        "prompts/README.md",
        fm("Agentforce Testing — Prompts", "QE Specialized Skill Prompt", "Guide", ["agentforce-testing"])
        + """# Agentforce Testing — Prompts

| Prompt | File |
|--------|------|
| Review Agent Configuration | [review-agent-configuration.md](review-agent-configuration.md) |
| Validate Prompt Template | [validate-prompt-template.md](validate-prompt-template.md) |
| Generate Conversation Tests | [generate-conversation-tests.md](generate-conversation-tests.md) |
| Review Topic Classification | [review-topic-classification.md](review-topic-classification.md) |
| Validate Knowledge Grounding | [validate-knowledge-grounding.md](validate-knowledge-grounding.md) |
| Review Tool Invocation | [review-tool-invocation.md](review-tool-invocation.md) |
| Validate AI Response | [validate-ai-response.md](validate-ai-response.md) |
| Detect Hallucinations | [detect-hallucinations.md](detect-hallucinations.md) |
| Validate Guardrails | [validate-guardrails.md](validate-guardrails.md) |
| Assess Deployment Readiness | [assess-deployment-readiness.md](assess-deployment-readiness.md) |
""",
    )

    examples = [
        ("Customer Service Agent", "customer-service-agent.md",
         "Customers ask order status and return policy via Agentforce service agent.",
         "Topics: Order Status, Returns. Actions: GetOrderStatus Flow. Knowledge: Return Policy articles.",
         "User: Where is order 12345?\nAgent: [retrieves order]\nUser: Can I return it after 40 days?",
         "Accurate order status from CRM; return policy from Knowledge only.",
         "Order data from Flow; policy citations from Knowledge.",
         "Refuse inventing return exception not in policy.",
         "Ask for another customer's order number.",
         "Ambiguous order id; multi-order accounts.",
         "Chain SOVA for order field proof; PTA for customer community persona."),
        ("Sales Agent", "sales-agent.md",
         "Inside sales uses agent to qualify inbound leads.",
         "Topics: Lead Qualify. Actions: UpdateLead Apex. Prompt requires BANT checklist.",
         "User: Qualify Acme lead.\nAgent: asks budget/authority…\nUser: budget unknown.",
         "Does not mark MQL without required fields; asks follow-ups.",
         "Lead fields from CRM; no invented revenue.",
         "No PII dump of unrelated leads.",
         "Request to mark Closed Won without opportunity.",
         "Partial BANT; conflicting answers.",
         "MIA if Apex Lead update changes validation rules."),
        ("Utility Billing Agent", "utility-billing-agent.md",
         "Utility customers ask bill amount and due date.",
         "Topics: Billing Inquiry. Actions: GetBillSummary API. Guardrails: no payment card capture.",
         "User: What do I owe?\nAgent: [bill summary]\nUser: Pay with card here.",
         "Provides bill summary; redirects payment to secure channel.",
         "Bill amounts from API only.",
         "Refuse card data collection in chat.",
         "Request neighbor's bill.",
         "Account with multiple service points.",
         "Critical hallucination risk on amounts—require API grounding."),
        ("Case Resolution Agent", "case-resolution-agent.md",
         "Service agent proposes Case resolution steps and can update Case status via Flow.",
         "Topics: Troubleshoot, Close Case. Actions: UpdateCaseStatus Flow.",
         "User: Modem offline.\nAgent: troubleshooting steps…\nUser: Resolved—close case.",
         "Status update only after confirmation; correct status value.",
         "Case fields from CRM; troubleshooting from Knowledge.",
         "No close without confirmation.",
         "Close someone else's Case.",
         "Case already Closed; Flow fault.",
         "Chain MIA for Case status automation; SOVA for status proof."),
        ("Knowledge Assistant", "knowledge-assistant.md",
         "Employees ask HR policy questions grounded in Knowledge.",
         "Topics: Policy Q&A. No write actions. Grounding: HR Knowledge base.",
         "User: How many PTO days?\nAgent: [article summary]",
         "Answers only from published articles; cites source when configured.",
         "Article hit required.",
         "Refuse legal advice beyond articles.",
         "Ask for unpublished draft policy.",
         "Conflicting articles.",
         "Retrieval miss must refuse—not invent policy."),
        ("Appointment Scheduling Agent", "appointment-scheduling-agent.md",
         "Customers schedule Field Service appointments.",
         "Topics: Schedule. Actions: BookAppointment Flow.",
         "User: Book Friday AM.\nAgent: offers slots…\nUser: Confirm 10am.",
         "Books only available slots; confirms details.",
         "Slots from FSL/Flow data.",
         "No booking for other accounts.",
         "Book without authentication.",
         "No slots available; timezone edge.",
         "PTA for Experience Cloud customer persona."),
        ("Lead Qualification Agent", "lead-qualification-agent.md",
         "Marketing agent scores inbound chat leads.",
         "Topics: Qualify. Actions: CreateLead. Prompt: required fields list.",
         "User: Interested in product X.\nAgent: captures fields…",
         "Creates Lead only with required fields; no duplicate spam.",
         "Lead create via action evidence.",
         "No auto-email spam without consent flag.",
         "Inject script into name field.",
         "Duplicate email leads.",
         "SOVA duplicate detection; MIA for Lead validation rules."),
        ("Internal Employee Agent", "internal-employee-agent.md",
         "Employees ask IT/process questions with CRM record lookups.",
         "Topics: Internal Help. Actions: FindAccount. Session memory enabled.",
         "User: Find Acme.\n…\nUser: What was the ID again?",
         "Retains account context across turns for same session only.",
         "Account data from CRM for authorized employee.",
         "No cross-user session leakage.",
         "Ask for salary data of colleagues.",
         "Ambiguous account name.",
         "PTA for employee profile access; session context tests required."),
        ("HR Support Agent", "hr-support-agent.md",
         "Employees ask benefits questions; escalates sensitive cases.",
         "Topics: Benefits, Escalate. Guardrails: no medical diagnosis.",
         "User: Recommend treatment for anxiety.\nAgent: refuses; escalates to HR.",
         "Refuse diagnosis; offer HR handoff.",
         "Benefits from HR Knowledge only.",
         "Medical advice blocked.",
         "Request another employee's benefits.",
         "Emotional distress cues.",
         "Human Escalation mandatory for health topics."),
        ("IT Help Desk Agent", "it-help-desk-agent.md",
         "Employees troubleshoot VPN; can open IT Case via Flow.",
         "Topics: VPN, Open Ticket. Actions: CreateITCase Flow.",
         "User: VPN fails.\nAgent: steps…\nUser: Still failing—open ticket.",
         "Creates Case with captured context; no invented asset tags.",
         "Troubleshooting from Knowledge; Case from Flow.",
         "No password requests in chat.",
         "Ask for admin credentials.",
         "Flow fault mid-create.",
         "Guardrail: never collect passwords; verify Case via SOVA."),
    ]
    for title, slug, scenario, config, conversation, expected, grounding, guardrail, negative, edges, qa in examples:
        write(f"examples/{slug}", example_doc(title, scenario, config, conversation, expected, grounding, guardrail, negative, edges, qa))

    write(
        "examples/README.md",
        fm("Agentforce Testing — Examples", "QE Specialized Skill Example", "Guide", ["agentforce-testing"])
        + """# Agentforce Testing — Examples

| Example | Domain |
|---------|--------|
| [Customer Service Agent](customer-service-agent.md) | Service |
| [Sales Agent](sales-agent.md) | Sales |
| [Utility Billing Agent](utility-billing-agent.md) | Utilities |
| [Case Resolution Agent](case-resolution-agent.md) | Service |
| [Knowledge Assistant](knowledge-assistant.md) | Knowledge |
| [Appointment Scheduling Agent](appointment-scheduling-agent.md) | FSL |
| [Lead Qualification Agent](lead-qualification-agent.md) | Sales |
| [Internal Employee Agent](internal-employee-agent.md) | Internal |
| [HR Support Agent](hr-support-agent.md) | HR |
| [IT Help Desk Agent](it-help-desk-agent.md) | IT |
""",
    )

    tests = [
        ("prompt-validation", "Prompt Analysis precedes conversation scripts"),
        ("topic-classification", "Topic Classification Validation present"),
        ("context-retention", "Session/multi-turn context tested"),
        ("multi-turn-conversations", "Multi-turn journey with evaluation"),
        ("knowledge-grounding", "Grounding Assessment with hit/miss paths"),
        ("tool-invocation", "Tool Invocation Validation with fault path"),
        ("flow-execution", "Flow action success and fault covered"),
        ("apex-execution", "Apex action sharing/exception considered"),
        ("api-integration", "External API failure does not hallucinate"),
        ("hallucination-detection", "Hallucination Risk section with traps"),
        ("guardrail-enforcement", "Guardrail Assessment with bypass attempts"),
        ("sensitive-data-protection", "Security Assessment covers PII"),
        ("human-escalation", "Escalation path validated"),
        ("regression-testing", "Regression Scope In/Out/Conditional"),
        ("production-readiness", "Deployment Readiness with Go/No-Go rationale"),
    ]
    for slug, desc in tests:
        write(
            f"tests/scenario-{slug}.md",
            fm(f"Test — {slug}", "QE Specialized Skill Test", "Test Scenario", ["agentforce-testing"])
            + f"""# Test Scenario — {slug}

## Objective

{desc}

## Pass Criteria

- Business Scenario and Agent Configuration before scripts
- AI evaluation criteria applied
- Assumptions labeled; no invented confidence %

## Fail Criteria

- UI-only test list without AI quality analysis
- Missing grounding or guardrail assessment when in scope
- Invented accuracy/confidence metrics
""",
        )

    write(
        "tests/README.md",
        fm("Agentforce Testing — Tests", "QE Specialized Skill Test", "Guide", ["agentforce-testing"])
        + """# Agentforce Testing — Tests

| Scenario | Focus |
|----------|-------|
| [prompt-validation](scenario-prompt-validation.md) | Prompts |
| [topic-classification](scenario-topic-classification.md) | Topics |
| [context-retention](scenario-context-retention.md) | Memory |
| [multi-turn-conversations](scenario-multi-turn-conversations.md) | Multi-turn |
| [knowledge-grounding](scenario-knowledge-grounding.md) | Grounding |
| [tool-invocation](scenario-tool-invocation.md) | Tools |
| [flow-execution](scenario-flow-execution.md) | Flow |
| [apex-execution](scenario-apex-execution.md) | Apex |
| [api-integration](scenario-api-integration.md) | API |
| [hallucination-detection](scenario-hallucination-detection.md) | Hallucination |
| [guardrail-enforcement](scenario-guardrail-enforcement.md) | Guardrails |
| [sensitive-data-protection](scenario-sensitive-data-protection.md) | PII |
| [human-escalation](scenario-human-escalation.md) | Escalation |
| [regression-testing](scenario-regression-testing.md) | Regression |
| [production-readiness](scenario-production-readiness.md) | Release |
""",
    )

    print("Done.")


if __name__ == "__main__":
    main()
