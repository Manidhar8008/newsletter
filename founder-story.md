---
layout: default
title: Founder Story
permalink: /founder-story/
---

<div class="masthead-meta">
  <span>THE FOUNDER STORY</span>
  <span>FIRST EDITION</span>
  <span>PERSONAL ARCHIVE</span>
</div>

<section class="hero">
  <p class="kicker">A NEW SERIES</p>
  <h1>The Founder Story</h1>
  <p class="hero-copy">The person behind the systems. The decisions behind the products. The long trail from doing the work to designing the machine that can do the work.</p>
</section>

<section class="latest-list">
{% assign founder_posts = site.categories.founder %}
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
  <p class="section-label">THE RULE</p>
  <p>This series will stay close to the facts: what happened, what was learned, what was built, and what changed next.</p>
</section>
