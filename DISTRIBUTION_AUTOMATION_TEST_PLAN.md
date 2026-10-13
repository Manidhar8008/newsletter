# Newsletter Distribution Automation — Computer-Only Test Plan

**Status:** BLOCKED / NOT CONFIGURED  
**Audit date:** 2026-10-13  
**Scope:** The AI Builder Dispatch on GitHub Pages, plus the newsletter distribution helper in `Manidhar8008/Startup-borardcasting-system`.

## 1. Verified baseline

- The newsletter is a static Jekyll site hosted on GitHub Pages.
- `_config.yml` currently sets `email.enabled: false`, with empty `email.form_action` and `email.form_url`.
- `subscribe.md` intentionally shows the disconnected-provider state while the form is disabled.
- GitHub Pages does not persist form submissions or maintain a subscriber database.
- `distribution/newsletter.py` formats an issue and returns `dry_run` by default. Its non-dry-run branch currently returns `queued` as a placeholder; it does not send email.
- A dedicated newsletter workflow was not found by the code search, and the expected `.github/workflows/newsletter.yml` path does not exist.
- No subscriber addresses, provider credentials, or live deliveries were accessed or changed during this audit.

**Conclusion:** The public archive works independently, but the end-to-end subscription-to-delivery path is not live. Do not enable the form or claim that a cron sender is running until the tests below pass.

## 2. Target architecture

1. **Consent UI:** the public form posts to an authenticated server endpoint, not to GitHub Pages itself. Collect only the email address and explicit consent required for the publication.
2. **Confirmation:** new addresses enter `pending_confirmation`. Send a confirmation link; do not include unconfirmed addresses in broadcasts.
3. **Source of truth:** store subscriber state in a database or the chosen email provider. Never commit subscriber addresses, confirmation tokens, unsubscribe tokens, or provider secrets into this repository.
4. **Publication trigger:** a new issue commit creates a delivery batch for that issue. A scheduled worker can reconcile pending work, but a cron job is not the database and is not the email provider.
5. **Eligibility filter:** only `confirmed + active` subscribers are eligible. Unsubscribed, bounced, complained, pending, or suppressed addresses must be excluded.
6. **Idempotency:** use a unique delivery key such as `(issue_id, subscriber_id)`. Running the job twice must not send the same issue twice.
7. **Delivery adapter:** send via a configured provider API. Missing credentials must fail closed; the system must not return a false `sent` or `queued` status.
8. **Audit and recovery:** store provider message ID, attempt count, timestamps, and result. Retry transient errors with backoff; suppress permanent failures. Provide a working one-click unsubscribe route.
9. **Human control:** dry-run first. Require a deliberate production enablement after test results are reviewed.

## 3. Computer-only trace

### Fixture input

- Issue: `issue-003`
- Subscribers:
  - `confirmed.active@example.test` — confirmed and active
  - `pending@example.test` — awaiting confirmation
  - `unsubscribed@example.test` — previously opted out
  - `bounce@example.test` — suppressed after a permanent bounce
  - `CONFIRMED.ACTIVE@example.test` — duplicate of the first address after normalization

All fixture addresses use the reserved `.test` domain. They are not real recipients.

### Expected trace

1. Validate the issue metadata and canonical URL. If missing, stop before creating a batch.
2. Normalize addresses for comparison and remove duplicates.
3. Select only confirmed, active, non-suppressed subscribers.
4. Create one delivery record for the eligible normalized address.
5. In dry-run mode, render the payload and record `dry_run`; send zero network requests.
6. Run the same issue a second time. The unique delivery key must prevent another delivery record or send.
7. Mark one fixture as unsubscribed and re-run eligibility. It must be excluded before provider submission.
8. Remove the provider API key. The job must fail with `provider_unconfigured` and zero sends.
9. Simulate a transient provider error. The job may retry with backoff, but it must not create a second successful delivery.
10. Simulate a permanent rejection or complaint. Suppress that address from future batches.
11. Confirm the archive and RSS feed remain available even if the email provider is down.

**Expected live email count for this plan: 0.**

## 4. Acceptance matrix

| Test | Expected result |
|---|---|
| Malformed email | Rejected; no subscriber record |
| Valid address, no confirmation | Pending; excluded from issue deliveries |
| Successful confirmation | Active and eligible |
| Duplicate signup with different letter case | One normalized subscriber |
| Unsubscribe | Suppressed immediately from future deliveries |
| Issue published once | One idempotent delivery per eligible subscriber |
| Scheduler runs twice | No duplicate send |
| Provider credential absent | Explicit failure; zero network sends |
| Temporary provider failure | Bounded retry with backoff |
| Permanent bounce or complaint | Address suppressed |
| RSS/archive when mailer is down | Still available |
| Dry-run mode | Payloads and counts only; zero sends |

## 5. Go-live gates

- [ ] Choose and configure the subscriber system of record.
- [ ] Implement a server-side opt-in endpoint and double opt-in.
- [ ] Implement persistent delivery records and idempotency.
- [ ] Implement real provider send and webhook handling.
- [ ] Implement unsubscribe and suppression.
- [ ] Run unit tests and a dry-run against fixture data.
- [ ] Complete one controlled test delivery to an explicitly authorized test inbox.
- [ ] Verify unsubscribe and duplicate-job behavior.
- [ ] Confirm secret values are stored as deployment secrets, not files.
- [ ] Only then enable public subscription and automated delivery.

## 6. Cost decision

Do not buy a paid email plan before validating the actual requirement. As checked on 2026-10-13, Kit's official Free plan page lists up to 10,000 subscribers, unlimited forms and broadcasts, and API access at no cost; it lists visual automations, sequences, and RSS campaigns among features requiring a paid plan. That can support a low-cost manual-broadcast path, but do not assume it provides a free native cron/RSS automation.

- Kit Free details: https://help.kit.com/en/articles/16627071-the-kit-free-plan
- Kit pricing: https://kit.com/pricing

If a true custom cron sender is the requirement, the missing work is a server endpoint, persistent subscriber state, delivery idempotency, an email provider API, and deployment secrets. Compare that build cost with provider pricing before purchasing. GitHub Pages alone cannot implement those backend responsibilities.

## 7. Current execution result

**Repository audit:** completed  
**Live provider verification:** not run (not configured)  
**Real email delivery:** not run; zero sends  
**Scheduled job:** not verified / not configured  
**Production readiness:** blocked until the go-live gates pass
