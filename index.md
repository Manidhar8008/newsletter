---
layout: default
title: The AI Builder Dispatch
description: "A founder's field paper on building AI systems, products, and a life around the work."
---

{% assign lead = site.posts | first %}

<section class="dispatch-hero">
  <div class="hero-kicker">THE AI BUILDER DISPATCH</div>
  <h1>THE OS<br>FOR CREATORS</h1>
  <p class="hero-copy">Questions before the build. Systems underneath it. Experiments that change the next move.</p>

  {% if lead %}
  <a class="primary-cta" href="{{ lead.url | relative_url }}">
    <span>Read {{ lead.title }}</span>
    <span aria-hidden="true">→</span>
  </a>
  {% endif %}
</section>

<div class="dotted-rule" aria-hidden="true"></div>

<section class="topic-strip" aria-label="Topics">
  <div class="topic-list">
    <a href="{{ '/archive/#local-models' | relative_url }}"><span class="check-box" aria-hidden="true">□</span> Local Models</a>
    <a href="{{ '/archive/#memory' | relative_url }}"><span class="check-box" aria-hidden="true">□</span> Memory Systems</a>
    <a href="{{ '/archive/#workflows' | relative_url }}"><span class="check-box" aria-hidden="true">□</span> Solo Workflows</a>
    <a href="{{ '/archive/#agents' | relative_url }}"><span class="check-box" aria-hidden="true">□</span> AI Systems</a>
  </div>
</section>

<section class="lead-panel">
  {% if lead %}
    <div class="eyebrow">{{ lead.section | default: 'DISPATCH' }} · {{ lead.date | date: "%d %B %Y" }}</div>
    <h2><a href="{{ lead.url | relative_url }}">{{ lead.title }}</a></h2>
    <p>{{ lead.description | default: lead.excerpt | strip_html | truncate: 300 }}</p>
    <a class="text-link" href="{{ lead.url | relative_url }}">Read the issue →</a>
  {% else %}
    <div class="eyebrow">FIRST EDITION</div>
    <h2>The work starts here.</h2>
    <p>The publication is being built from the questions, systems, failures, and experiments behind the work.</p>
  {% endif %}
</section>

<section class="story-grid compact-grid">
{% for issue in site.posts limit:4 offset:1 %}
  <article class="story-card" {% if issue.section == 'FOUNDER STORY' %}id="founder"{% endif %}>
    <div class="eyebrow">{{ issue.section | default: 'DISPATCH' }}</div>
    <h3><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h3>
    <p class="story-meta">{{ issue.date | date: "%d %b %Y" }}{% if issue.read_time %} · {{ issue.read_time }} min{% endif %}</p>
    <p>{{ issue.description | default: issue.excerpt | strip_html | truncate: 165 }}</p>
  </article>
{% endfor %}
</section>

<section class="persona-panel">
  <div>
    <div class="eyebrow">THE FOUNDER</div>
    <h2>Manidhar Pati</h2>
    <p>Solopreneur and builder in Warangal, India. I document what I build, what breaks, what changes, and the question that follows.</p>
  </div>
  <div class="persona-links">
    <a href="{{ '/founder-story/' | relative_url }}" class="text-link">Founder story →</a>
    <a href="https://github.com/Manidhar8008" class="text-link">GitHub →</a>
    <a href="{{ '/about/' | relative_url }}" class="text-link">About →</a>
  </div>
</section>

<section class="subscribe-panel">
  <div>
    <div class="eyebrow">THE NEXT DISPATCH</div>
    <h2>Stay close to the work.</h2>
    <p>One useful dispatch from the actual work. No generic AI news dump.</p>
  </div>
  <form class="inline-subscribe" action="{{ '/subscribe/' | relative_url }}" method="get">
    <label class="sr-only" for="home-email">Email address</label>
    <input id="home-email" name="email" type="email" placeholder="your@email.com" autocomplete="email" required>
    <button type="submit" aria-label="Continue to subscription">→</button>
  </form>
</section>

<div class="section-rule"><span>RECENT</span></div>

<section class="archive-preview">
{% for issue in site.posts limit:8 %}
  <article class="archive-row">
    <div class="issue-date">{{ issue.date | date: "%d %b %Y" }}</div>
    <div>
      <div class="eyebrow">{{ issue.section | default: 'DISPATCH' }}</div>
      <h3><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h3>
    </div>
  </article>
{% endfor %}
</section>

<div class="archive-link-row">
  <a class="text-link" href="{{ '/archive/' | relative_url }}">View the full archive →</a>
</div>
