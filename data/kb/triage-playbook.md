# Support triage playbook (sample)

Seed article for future `triage_ticket` routing. Not used in Phase 0.

## Queues

| Queue | When to use |
|-------|-------------|
| `billing` | Invoices, refunds, plan changes |
| `technical` | Outages, API errors, integration bugs |
| `account` | Login, SSO, user access |
| `unassigned` | Unclear or multi-topic tickets |

## Priority hints

- **critical** — full outage or data loss
- **high** — major feature broken for many users
- **normal** — single-user or workaround available
- **low** — questions, docs, cosmetic issues

## Example

Subject: "Cannot login after SSO change" → queue `account`, priority `high`.
