---
layout: page
title:
permalink: /
---

<div class="row align-items-center mt-4 mb-4">
  <div class="col-md-8">
    <h1 style="font-weight: 700; color: var(--global-theme-color);">Consciousness Observers</h1>
    <p style="font-size: 1.1rem; color: var(--global-text-color-light); margin-bottom: 1.2rem;">
      CO-LAB · Linking Across Boundaries
    </p>
    <p style="font-size: 1rem; line-height: 1.7;">
      A student-led team working on consciousness across physics, psychology, neuroscience,
      biomedical engineering and philosophy.
    </p>
  </div>
  <div class="col-md-4 text-center">
    <img class="only-light" src="{{ '/assets/img/CO_Logo_round.png' | relative_url }}"
         alt="CO-LAB logo" width="700" height="703"
         style="margin: 0 auto; max-width: 200px; height: auto;" loading="eager">
    <img class="only-dark" src="{{ '/assets/img/CO_Logo_round_light.png' | relative_url }}"
         alt="CO-LAB logo" width="700" height="703"
         style="margin: 0 auto; max-width: 200px; height: auto;" loading="eager">
  </div>
</div>

<div class="home-prose">
  <p>
    We are a handful of students who want to understand consciousness. Between us we cover most
    of the disciplines the question touches, and most of the programmes the university has built
    for it. The name says the rest: <em>Consciousness Observers — Linking Across Boundaries</em>.
  </p>

  <p>
    We work decentralised: every member takes part in decisions and in the chores, and there are
    no ranks. We read original papers together, argue about them, and turn what survives into
    something others can use — a workshop, a reading record, this site.
  </p>

  <p>
    CO-LAB became a resident team of the <strong>Future Learning Center, Zhejiang University</strong>
    in 2026. We have a room there, plus the centre's spaces, 3D printers and student network. The
    room matters: it holds the reading list, the open questions and half-finished workshop material
    between sessions. We remain an independent, cross-school student group — not attached to one
    department, not run by faculty.
  </p>
</div>

<div class="photo-grid">
  <figure class="photo-slot"><div class="photo-empty">Photo to come</div><figcaption>Our room in the Future Learning Center</figcaption></figure>
  <figure class="photo-slot"><div class="photo-empty">Photo to come</div><figcaption>Desks and the reading wall</figcaption></figure>
  <figure class="photo-slot"><div class="photo-empty">Photo to come</div><figcaption>The team at work</figcaption></figure>
</div>

<div class="home-prose">
  <p>
    We run a reading group — one concept per session, the original papers behind it, five evenings
    a term, the records kept as an
    <a href="https://consciousness-observers.github.io/concepts-and-approaches/">open book</a>.
    We run a full-day workshop that goes from evolutionary origins to a 3D-printed brain. Members
    also present their own work across disciplines, and what is worth keeping is written up in
    public.
  </p>
</div>

<div class="home-contact">
  <p>
    Write to <a href="mailto:consciousness.observers@outlook.com">consciousness.observers@outlook.com</a>
    — to collaborate, sit in on a session, or argue. What we are reading and running goes on our
    official account.
  </p>
  {% include wechat.html %}
</div>

<style>
  .home-prose p {
    font-size: 1.02rem;
    line-height: 1.8;
    margin-bottom: 1.15rem;
  }
  .home-prose p:last-child { margin-bottom: 0; }

  .photo-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
  }
  .photo-slot { margin: 0; }
  .photo-empty {
    display: flex; align-items: center; justify-content: center;
    aspect-ratio: 4 / 3;
    border: 1px dashed var(--global-divider-color);
    border-radius: 8px;
    background: var(--global-card-bg-color);
    color: var(--global-text-color-light);
    font-size: .82rem;
  }
  .photo-slot figcaption {
    margin-top: .45rem;
    font-size: .8rem;
    color: var(--global-text-color-light);
  }

  .home-contact {
    margin-top: 2.4rem;
    padding-top: 1.4rem;
    border-top: 1px solid var(--global-divider-color);
  }
  .home-contact p {
    font-size: 1.02rem;
    line-height: 1.8;
  }
</style>
