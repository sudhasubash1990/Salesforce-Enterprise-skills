---
title: Security Test Assessment Playbook
module: Salesforce Quality Engineering
category: QE Specialized Skill Playbook
document_type: Playbook
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, security-testing, playbook]
---

# Security Test Assessment Playbook

## Purpose

Structured workflow for assessing security testing scope. Produces an assessment — chains to [PTA](../../permission-testing-agent/SKILL.md) for detailed test scenarios.

## Assessment Steps

### Step 1 — Identify Security-Relevant Changes
- New/modified objects, fields, record types
- Profile or permission set changes
- Sharing rule additions or OWD changes
- Experience Cloud configuration
- Connected app or Named Credential changes

### Step 2 — Map Personas to Access Requirements
- List all personas affected by changes
- Document expected CRUD per persona per object
- Document expected FLS per persona per sensitive field
- Identify segregation of duties requirements

### Step 3 — Assess Sharing Model Impact
- Current OWD settings for affected objects
- Role hierarchy relevance
- Sharing rules (criteria-based, owner-based)
- Restriction rules and scoping rules
- Territory model impact (if applicable)

### Step 4 — Assess Special Access Contexts
- Experience Cloud (partner/customer/guest)
- API-only access (integrations, connected apps)
- Shield encryption impact on queries
- Mobile access differences

### Step 5 — Document Assessment and Chain
- Produce Security Assessment section in SST report
- Identify risks and open questions
- **Chain to PTA** for detailed test scenario generation

## Output

Security Assessment section (section 6 of 18-section SST report) with chain recommendation to PTA.

## Related

- [PTA SKILL.md](../../permission-testing-agent/SKILL.md)
- [Security Testing Knowledge](../knowledge/security-testing.md)
