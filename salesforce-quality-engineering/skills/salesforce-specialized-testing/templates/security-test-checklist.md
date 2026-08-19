---
title: Security Test Checklist Template
module: Salesforce Quality Engineering
category: QE Specialized Skill Template
document_type: Template
version: 0.25.0
review_status: Draft
owner: QE Practice Lead
created_date: 2026-08-19
last_updated: 2026-08-19
review_cycle: quarterly
tags: [salesforce-specialized-testing, security-checklist]
---

# Security Test Checklist

## CRUD / FLS

- [ ] Object-level access verified per persona
- [ ] Field-level security verified for sensitive fields
- [ ] Read vs Edit permissions validated
- [ ] "View All" / "Modify All" justified where granted

## Sharing Model

- [ ] OWD settings reviewed for affected objects
- [ ] Role hierarchy access validated
- [ ] Sharing rules (criteria/owner-based) tested
- [ ] Restriction rules validated (if applicable)
- [ ] Scoping rules validated (if applicable)

## Profiles and Permission Sets

- [ ] Profile assignments reviewed
- [ ] Permission set grants follow least privilege
- [ ] PSG composition verified
- [ ] No excessive system permissions without justification

## Record Visibility

- [ ] Record ownership access confirmed
- [ ] Manual sharing behavior validated
- [ ] Queue membership access tested
- [ ] Territory access validated (if applicable)

## Experience Cloud

- [ ] Guest user profile has minimal access
- [ ] Partner/customer portal access boundaries tested
- [ ] Sharing sets configured correctly
- [ ] Public pages expose no sensitive data

## API Security

- [ ] Connected app scopes are minimal
- [ ] OAuth flow tested (token acquisition, refresh, revocation)
- [ ] Named Credentials use per-user or named principal appropriately
- [ ] API-only profiles have no UI access

## Chain

After completing this checklist assessment, **chain to [PTA](../../permission-testing-agent/SKILL.md)** for detailed security test scenario generation.
