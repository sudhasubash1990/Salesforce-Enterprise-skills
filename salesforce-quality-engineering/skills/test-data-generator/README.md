---
title: Test Data Generator — README
module: Salesforce Quality Engineering
category: QE Specialized Skill
document_type: Guide
version: 0.20.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-07-27
last_updated: 2026-07-27
review_cycle: quarterly
tags: [test-data-generator]
---

# Test Data Generator (TDG)

## Purpose

Enterprise **Test Data Management** capability for Salesforce QE. Designs and generates realistic, relationship-aware, validation-compliant, **synthetic** test data — not random fake rows and never real PII.

Canonical data encyclopedia remains in [`../../knowledge/data/`](../../knowledge/data/README.md). This pack holds **TDM generation reasoning models**.

## Capabilities

- Business-scenario-driven data requirements  
- Object and relationship inventory before payloads  
- Positive, negative, boundary, duplicate, ownership, and sharing datasets  
- Validation-rule-aware generation (unless negative testing requested)  
- Volume strategy (single → bulk → LDV) with cleanup  
- Format templates: CSV, JSON, Data Loader, Bulk API, CLI, Apex factory  
- Security: synthetic default, masking guidance, PTA chain for personas  
- SOQL stubs for post-generation proof (SOVA)  

## Supported Data Types

Standard CRM · Custom Objects · Junction · Person Account · Lead/Opportunity/Case · Product/Price Book · Asset/Contract/Order/Quote · Campaign · Knowledge · Industry-shaped objects · Custom Metadata (seed, where applicable)

## Folder Structure

```
skills/test-data-generator/
├── SKILL.md
├── README.md
├── skill-config.yaml
├── knowledge/       ← 16 reasoning articles
├── playbooks/       ← 8 playbooks
├── templates/       ← 8 templates
├── prompts/         ← 10 prompts
├── examples/        ← 12 examples
└── tests/           ← 11 scenarios
```

## Inputs

| Input | Required |
|-------|----------|
| Business scenario / test phase | Yes |
| Data requirements (positive/negative/personas) | Yes |
| Objects and relationships | Yes |
| Record types / VR / picklists (known) | Recommended |
| Volume target | Recommended |
| Environment (SIT/UAT/sandbox) | Recommended |
| MIA impact (new fields/VR) | When metadata changed |

## Outputs

14-section TDM report — see [SKILL.md](SKILL.md). Primary template: [templates/data-generation-report.md](templates/data-generation-report.md).

## Sample Prompt

```
Load skills/test-data-generator/SKILL.md.
Business Scenario: UAT seed for B2B sales pipeline with two personas.
Objects: Account, Contact, Opportunity (with products).
Produce all 14 sections including Relationship Diagram, synthetic sample data,
SOQL stubs, and Cleanup Strategy. No real PII.
```

See [prompts/README.md](prompts/README.md).

## Example Scenarios

See [examples/README.md](examples/README.md) — CRM, Service, Utilities, Retail, Quote-to-Cash, Experience Cloud, Agentforce, and more.

## Best Practices

- Business scenario + objects/relationships **before** payloads  
- Synthetic by default; mask if using partial clones  
- Respect validation rules for positive data  
- Always plan cleanup for bulk/LDV  
- Chain SOVA for proof; PTA for sharing personas  
- Label assumptions for org-specific automation  

## Data Governance

- Never use production customer data in generated packs  
- Classify sensitive fields; prefer synthetic substitutes  
- Document ownership of seed packs and refresh cadence  
- Align with program GDPR/HIPAA/PCI policies — do not invent attestations  

## Common Pitfalls

- Orphan child records without parents  
- Ignoring required fields / record types  
- Bulk load without External IDs or cleanup  
- Sharing tests without correct OwnerId / roles  
- Duplicating Sprint 4A encyclopedia content  

## Limitations

- No live org import execution  
- Org-specific VR/Flow behavior must be confirmed  
- Planned siblings (Production RCA) — cross-link only; OmniStudio → [OmniStudio QA](../omnistudio-qa/SKILL.md); migration dry-run → [Data Migration QA](../data-migration-qa/SKILL.md)

## Future Enhancements

- Deeper OmniStudio JSON payload packs with [OmniStudio QA](../omnistudio-qa/SKILL.md)
- Migration-ready dataset packs with [Data Migration QA](../data-migration-qa/SKILL.md)
- Baseline regression dataset registry  

## Related Documents

- [SKILL.md](SKILL.md)  
- [skill-config.yaml](skill-config.yaml)  
- [Parent skill.md](../../skill.md)  
- [Sprint 4A Data Knowledge](../../knowledge/data/README.md)  
- [Sprint 5 Test Data Strategy](../../templates/test-data-strategy.md)  

## Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| 0.20.0 | 2026-07-27 | QE Practice Lead | Initial Test Data Generator capability |
