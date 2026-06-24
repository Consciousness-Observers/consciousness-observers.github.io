---
layout: page
title: publications
permalink: /publications/
nav: true
nav_order: 5
---

Peer-reviewed work by CO-LAB members, published through their home institutions.

{% if site.data.publications %}
  {% bibliography %}
{% else %}
  <p><em>No publications listed yet.</em></p>
{% endif %}
