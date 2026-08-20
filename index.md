---
layout: default
title: The AI Builder Dispatch
description: "A founder's field paper on building AI systems, products, and a life around the work."
---

<section class="front-page-intro">
  <div>
    <p class="kicker">THE AI BUILDER DISPATCH · ISSUE 001</p>
    <h1>A field paper from the work.</h1>
  </div>
  <p class="intro-copy">I build systems, break them, rebuild them, and write down what changes. This is the record: the questions before the build, the systems underneath it, and the next question that appears after.</p>
</section>

{% assign lead = site.posts | first %}
{% if lead %}
<section class="lead-story">
  <div class="lead-meta">{{ lead.date | date: "%d %B %Y" }} · {{ lead.section | default: 'DISPATCH' }}</div>
  <h2><a href="{{ lead.url | relative_url }}">{{ lead.title }}</a></h2>
  <p>{{ lead.description | default: lead.excerpt | strip_html | truncate: 360 }}</p>
  <a class="read-link" href="{{ lead.url | relative_url }}">Read the dispatch →</a>
</section>
{% endif %}

<section class="story-grid">
{% for issue in site.posts limit:4 offset:1 %}
  <article class="story-card">
    <p class="section-label">{{ issue.section | default: 'DISPATCH' }}</p>
    <h3><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h3>
    <p class="story-meta">{{ issue.date | date: "%d %b %Y" }}{% if issue.read_time %} · {{ issue.read_time }} min{% endif %}</p>
    <p>{{ issue.description | default: issue.excerpt | strip_html | truncate: 190 }}</p>
  </article>
{% endfor %}
</section>

<section class="founder-strip">
  <div>
    <p class="section-label">THE FOUNDER</p>
    <h2>Manidhar Pati</h2>
    <p>Solopreneur and builder in Warangal, India. I am documenting the systems, experiments, constraints, and decisions behind the work.</p>
  </div>
  <a class="read-link" href="{{ '/founder-story/' | relative_url }}">Read the Founder Story →</a>
</section>

<section class="subscribe-strip">
  <div>
    <p class="section-label">THE NEXT EDITION</p>
    <h2>Get the next dispatch.</h2>
    <p>The website is live now. Email delivery is the next layer; the publication is being kept independent of the email provider.</p>
  </div>
  <a class="subscribe-button" href="{{ '/subscribe/' | relative_url }}">Subscribe →</a>
</section>

<div class="section-rule"><span>RECENT</span></div>

<section class="archive-preview">
{% for issue in site.posts limit:10 %}
  <article class="archive-row">
    <div class="issue-date">{{ issue.date | date: "%d %b %Y" }}</div>
    <div>
      <p class="section-label">{{ issue.section | default: 'DISPATCH' }}</p>
      <h3><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h3>
    </div>
  </article>
{% endfor %}
</section>

<div class="archive-link-row">
  <a class="read-link" href="{{ '/archive/' | relative_url }}">Open the complete archive →</a>
</div>
