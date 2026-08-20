# Email Setup Contract

The publication is intentionally static and provider-neutral.

## Current target: Kit

Kit's current free Newsletter Plan supports up to 10,000 subscribers and includes unlimited sends, forms, a newsletter feed, and a welcome sequence.

1. Create the Kit Newsletter account.
2. Create a Form for The AI Builder Dispatch.
3. Use an inline display form.
4. Enable confirmation/double opt-in unless there is a strong reason to use auto-confirmation.
5. Create a one-email welcome sequence.
6. Add a tag such as `website` to subscribers who join from GitHub Pages.
7. Copy the form action URL or embed details.
8. Put the action URL in `_config.yml` under `email.form_action`.
9. Set `email.enabled: true`.
10. Push the commit and test with a fresh email address.

## Subscriber source of truth

GitHub Pages does not store subscriber data. The selected email provider does.

## Test checklist

- Submit a fresh address from `/subscribe/`.
- Confirm the address in the provider dashboard.
- Confirm the confirmation email arrives.
- Confirm the welcome email arrives.
- Confirm the subscriber receives the `website` tag.
- Publish a test issue.
- Confirm the broadcast reaches the test address.
- Click unsubscribe and confirm suppression.
- Verify RSS still works independently.
