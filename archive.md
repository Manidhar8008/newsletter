---
layout: default
title: Archive
description: "The complete archive of The AI Builder Dispatch."
permalink: /archive/
---

<article class="issue simple-page">
  <div class="eyebrow">THE ARCHIVE</div>
  <h1>Everything I have published.</h1>
  <p class="lead">Founder stories, system builds, experiments, field notes, and the questions that keep changing the work.</p>

  <div class="topic-list" style="margin:32px 0 20px">
    <a href="{{ '/search/' | relative_url }}?q=founder"><span class="check-box">□</span> Founder</a>
    <a href="{{ '/search/' | relative_url }}?q=systems"><span class="check-box">□</span> Systems</a>
    <a href="{{ '/search/' | relative_url }}?q=build"><span class="check-box">□</span> Build</a>
    <a href="{{ '/search/' | relative_url }}?q=AI"><span class="check-box">□</span> AI</a>
  </div>

  <section class="archive-preview">
  {% for issue in site.posts %}
    <article class="archive-row">
      <div class="issue-date">{{ issue.date | date: "%d %b %Y" }}<br>{{ issue.read_time | default: '—' }}{% if issue.read_time %} min{% endif %}</div>
      <div>
        <div class="eyebrow">{{ issue.section | default: 'DISPATCH' }}</div>
        <h3><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h3>
        <p>{{ issue.description | default: issue.excerpt | strip_html | truncate: 180 }}</p>
      </div>
    </article>
  {% endfor %}
  </section>
</article>
