# The AI Builder Dispatch

[![Production deployment](https://github.com/Manidhar8008/newsletter/actions/workflows/deploy.yml/badge.svg)](https://github.com/Manidhar8008/newsletter/actions/workflows/deploy.yml)
[![Pull request checks](https://github.com/Manidhar8008/newsletter/actions/workflows/pr-check.yml/badge.svg)](https://github.com/Manidhar8008/newsletter/actions/workflows/pr-check.yml)

**Live site:** https://manidhar8008.github.io/newsletter/

A GitHub Pages newsletter and permanent web archive.

## Publish an issue

Create a Markdown file in `_posts/` using `YYYY-MM-DD-title.md` and valid Jekyll front matter:

```yaml
---
layout: post
title: "Issue title"
description: "Short description"
date: 2026-10-13
---
```

Push to `main`. The production workflow builds and audits the site, then deploys the generated artifact. A scheduled rebuild runs each morning so date-scheduled posts can become public without a new content commit. Pull requests run build and validation checks without deploying.

Use workflow dispatch with **Draft Mode** to build Jekyll drafts for validation; draft builds do not deploy to the public site.

## Quality and security gates

- Ruby version declared in `.ruby-version`
- Bundler/Jekyll cache and 10-minute build timeout
- Pinned runner image: `ubuntu-24.04`
- Jekyll doctor, strict front matter, build profile, and stack traces
- Ruby gem vulnerability audit and Dependabot updates
- Generated HTML title/description checks
- Internal-link, image-alt, duplicate-title/permalink, filename, and RSS XML checks
- Minimal per-job permissions and a 5-minute deployment timeout
- Build summary includes commit, runtime versions, build time, and output size

## Architecture

- Markdown: content source
- Jekyll: static-site generator
- GitHub Pages: hosting
- RSS: syndication
- Email: separate integration; subscriber collection and email delivery are not enabled until a provider/backend is configured

## Distribution readiness

See [Email Setup](EMAIL_SETUP.md) and the [Distribution Automation Test Plan](DISTRIBUTION_AUTOMATION_TEST_PLAN.md). The website archive can publish independently of email distribution. Never enable the public form until an actual subscriber endpoint or provider form action is configured.
