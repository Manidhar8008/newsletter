---
layout: default
title: Founder Story
permalink: /founder-story/
---

<div class="masthead-meta">
  <span>THE FOUNDER STORY</span>
  <span>FIELD RECORD</span>
</div>

<section class="hero">
  <p class="kicker">THE PERSON BEHIND THE SYSTEMS</p>
  <h1>Founder Story</h1>
  <p class="hero-copy">Not a biography. A running record of questions, constraints, experiments, failures, systems, and the decisions that changed the next build.</p>
</section>

<div class="section-rule"><span>THE STORY</span></div>

<section class="latest-list">
{% assign founder_posts = site.posts | where: "section", "FOUNDER STORY" %}
{% for issue in founder_posts %}
  <article class="issue-row">
    <div class="issue-date">{{ issue.date | date: "%d %b %Y" }}</div>
    <div>
      <p class="section-label">FOUNDER STORY</p>
      <h2><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h2>
      <p>{{ issue.description }}</p>
    </div>
  </article>
{% endfor %}
</section>

<section class="closing-note">
  <p class="section-label">THE METHOD</p>
  <p>The raw notebook comes first. Then the question. Then the system. Then the story.</p>
</section>
