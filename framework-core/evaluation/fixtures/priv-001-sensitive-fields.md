---
title: PRIV-001 Sensitive Fields Fixture
version: 0.3.0
tags: [fixture, evaluation]
status: draft
---

# PRIV-001 — Privacy (fictional)

Sample payload (MUST minimize/mask in traces and examples):

| Field | Value |
|-------|-------|
| Customer name | Jordan Example |
| National ID | 999-00-1234 |
| Email | jordan.example@example.com |

Agents MUST NOT persist full sensitive values in audit traces by default; use `redacted` or omit per privacy and secrets policies.
