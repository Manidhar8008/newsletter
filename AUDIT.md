# Publication Audit

## Keep

- `_posts/` for published editorial content
- `founder-story/` for the Founder Story index
- `author.md`, `about.md`, `contact.md`, `privacy.md` for identity and trust
- `EMAIL_SETUP.md` until live email is connected
- `STYLE_GUIDE.md` as the editorial source of truth
- GitHub Pages workflow, assets, and Jekyll configuration

## Removed during cleanup

- Duplicate `founder-story.md` route; `founder-story/index.md` is the canonical Founder Story section.
- One-time `DEPLOYMENT-CHECK.md`; deployment state belongs in GitHub Actions, not the publication.

## Principle

Every page must either publish, help a reader discover, establish trust, or operate the publication. Temporary debugging artifacts do not belong in the public repository.
