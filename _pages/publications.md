---
layout: page
title: publications
permalink: /publications/
nav: true
nav_order: 5
---

This page collects peer-reviewed work published by CO-LAB members through their home institutions. CO-LAB itself does not produce publications — credit follows standard academic authorship norms.

{% if site.data.publications %}
  {% bibliography %}
{% else %}
  <p><em>No publications listed yet.</em></p>
{% endif %}
