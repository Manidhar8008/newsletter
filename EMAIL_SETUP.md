# Email Setup and Distribution Contract

**Last repository audit:** 2026-10-13

The publication is a static Jekyll archive hosted on GitHub Pages. Email distribution is deliberately separate from the web archive.

## Current repository state

- `email.provider` is set to `kit`.
- `email.enabled` is `false`.
- `email.form_action` and `email.form_url` are empty.
- GitHub Pages does not store subscriber form submissions.
- The separate `Startup-borardcasting-system/distribution/newsletter.py` helper is still a dry-run/placeholder and does not perform a real send.
- No live distribution cron or provider credentials were verified.

Do **not** enable the subscription form by changing only `email.enabled`. A valid provider form action or a server-side subscription endpoint must exist first.

## Option A — start without paying

Kit's official Free plan documentation currently lists up to 10,000 subscribers, unlimited forms and email broadcasts, and API access. Its current help page lists visual automations, sequences, and RSS campaigns as paid-plan features. Check the current provider terms before making a decision:

- [Kit Free plan](https://help.kit.com/en/articles/16627071-the-kit-free-plan)
- [Kit pricing](https://kit.com/pricing)

For a manual-broadcast launch, create a Kit account and a form, enable confirmation/double opt-in, then paste the actual form action or embed details into configuration. Do not expect the free plan to provide every automated welcome/RSS workflow.

## Option B — custom scheduled distribution

If the requirement is “a visitor opts in on this website, then a background job sends each new issue to eligible subscribers,” the minimum production path is:

1. A server-side endpoint to receive opt-ins. A static Jekyll page cannot securely persist submissions by itself.
2. Double opt-in and consent timestamps.
3. A database/provider as the subscriber source of truth; do not store the list in Git.
4. A publication trigger or scheduled worker.
5. A persistent delivery ledger with a unique key per issue/subscriber.
6. A provider API adapter with retries, provider webhooks, suppression, and unsubscribe support.
7. Deployment secrets for API credentials.
8. A dry-run, an authorized test inbox, and duplicate/unsubscribe tests before broad delivery.

A cron workflow coordinates work; it should not be the only copy of subscriber data and must not imply success when the provider is disconnected.

## Test checklist

Use the full [Distribution Automation Test Plan](DISTRIBUTION_AUTOMATION_TEST_PLAN.md) before enabling delivery.

- [ ] Submit a valid address and confirm it remains pending until verified.
- [ ] Confirm the address and ensure it becomes eligible.
- [ ] Submit the same address again with different letter case; ensure deduplication.
- [ ] Publish a test issue and render its email payload.
- [ ] Run the same job twice; ensure the second run sends no duplicate.
- [ ] Unsubscribe the test address and ensure future batches exclude it.
- [ ] Remove provider credentials; verify the job fails closed with zero sends.
- [ ] Confirm RSS and the public archive continue to work independently.

## Privacy and safety

Only send to people who explicitly opted in. Do not scrape, infer, or import addresses from unrelated mailboxes. Keep subscriber data and API keys out of public files and Git history. Every email must offer a working unsubscribe mechanism.

**Current status: not connected; no real email sending is enabled.**
