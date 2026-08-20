---
layout: default
title: Subscribe
description: "Get The AI Builder Dispatch by email."
permalink: /subscribe/
---

<article class="issue simple-page">
  <div class="eyebrow">SUBSCRIBE</div>
  <h1>Stay close to the work.</h1>
  <p class="lead">Get the next dispatch when it is published: founder stories, system builds, experiments, failures, and the next question.</p>

  <form class="inline-subscribe large-subscribe" action="{{ '/subscribe/' | relative_url }}" method="get">
    <label class="sr-only" for="subscribe-email">Email address</label>
    <input id="subscribe-email" name="email" type="email" placeholder="your@email.com" autocomplete="email" required>
    <button type="submit" aria-label="Continue to subscription">→</button>
  </form>

  <section class="subscribe-explainer">
    <div class="eyebrow">WHAT ARRIVES</div>
    <h2>One useful dispatch.</h2>
    <p>A founder story. A system build. An experiment. A field note. The unfinished thinking that normally disappears before a polished launch.</p>

    <div class="eyebrow">WHAT HAPPENS NEXT</div>
    <h2>The archive stays the source of truth.</h2>
    <p>Email is a distribution layer, not the publication itself. We will connect and test providers without changing the website, RSS feed, or archive.</p>
  </section>

  <p class="subscribe-note">The email provider will be connected in the next infrastructure pass. Your address is not stored by this static page.</p>
</article>
