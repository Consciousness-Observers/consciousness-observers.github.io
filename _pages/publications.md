---
layout: page
title: publications
permalink: /publications/
nav: true
nav_order: 5
---

CO-LAB itself does not produce publications — this page lists the individual peer-reviewed work of our members, published through their respective laboratories. CO-LAB is a platform for discussion and collaboration; publication credit follows standard academic norms and is determined by each member's home institution and research group.

{% if site.data.publications %}
  {% bibliography %}
{% else %}
  <p><em>No publications listed yet.</em></p>
{% endif %}
