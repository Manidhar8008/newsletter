# The AI Builder Dispatch

A GitHub Pages newsletter and permanent web archive.

## Publish an issue

Create a Markdown file in `_posts/` using:

`YYYY-MM-DD-title.md`

Add Jekyll front matter:

```yaml
---
layout: post
title: "Issue title"
description: "Short description"
date: 2026-08-20
---
```

Commit and push. GitHub Pages builds the site automatically.

## Architecture

- Markdown: content source
- Jekyll: static-site generator
- GitHub Pages: hosting
- RSS: syndication
- Email: intentionally decoupled for later provider experiments
