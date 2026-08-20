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

  {% if site.email.enabled and site.email.form_action %}
  <form class="inline-subscribe large-subscribe" action="{{ site.email.form_action }}" method="post">
    <label class="sr-only" for="subscribe-email">Email address</label>
    <input id="subscribe-email" name="email" type="email" placeholder="your@email.com" autocomplete="email" required>
    <input type="hidden" name="tag" value="website">
    <button type="submit" aria-label="Subscribe">→</button>
  </form>
  {% else %}
  <div class="subscribe-note">The website is ready, but the external email service is not connected yet. The two addresses you tested previously were not stored by GitHub Pages.</div>
  <a class="primary-cta" href="#provider-setup"><span>Finish email setup</span><span aria-hidden="true">→</span></a>
  {% endif %}

  <section class="subscribe-explainer">
    <div class="eyebrow">WHAT ARRIVES</div>
    <h2>One useful dispatch.</h2>
    <p>A founder story. A system build. An experiment. A field note. The unfinished thinking that normally disappears before a polished launch.</p>

    <div class="eyebrow">WHAT HAPPENS NEXT</div>
    <h2>The archive stays the source of truth.</h2>
    <p>Email is distribution. The website, RSS feed, and archive remain permanent and independent from the email provider.</p>
  </section>

  <section id="provider-setup" class="subscribe-explainer">
    <div class="eyebrow">EMAIL INFRASTRUCTURE</div>
    <h2>Kit is the first provider target.</h2>
    <p>We are using Kit as the first email service target because its current free Newsletter Plan supports up to 10,000 subscribers and includes unlimited sends, forms, a newsletter feed, and a welcome sequence.</p>
    <ol>
      <li>Create the free Kit Newsletter account.</li>
      <li>Create an inline Form for The AI Builder Dispatch.</li>
      <li>Enable the confirmation email and a one-email welcome sequence.</li>
      <li>Give me the Form embed/action details so I can wire this static site to it.</li>
    </ol>
    <p>Kit supports JavaScript and HTML form embeds, so GitHub Pages can remain the public publication while Kit handles subscriber storage and email delivery.</p>
  </section>

  <p class="subscribe-note">No subscriber address is stored by this GitHub Pages site itself. Once Kit is connected, Kit becomes the subscriber system of record.</p>
</article>
