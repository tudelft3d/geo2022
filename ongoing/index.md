---
layout: page
title: Current theses
color: white
logo: fa-book
permalink: /ongoing/
---

Everyone currently graduating, ordered by process step. The tags show
where each student is in the
[graduation process]({{ "/rules/" | prepend: site.baseurl }}):
<span class="tag is-light">Preparation</span> →
<span class="tag is-phase-kickoff">Kick-off</span> →
<span class="tag is-phase-midterm">Midterm</span> →
<span class="tag is-phase-greenlight">Green light</span> → finalisation.
Looking for finished theses? Browse the
[thesis archive]({{ "/theses/" | prepend: site.baseurl }}).

{% include thesis_current.html %}

<p class="is-size-7 has-text-grey">
  Last updated: {{ site.data.theses_updated.current | date_to_long_string }}.
</p>
