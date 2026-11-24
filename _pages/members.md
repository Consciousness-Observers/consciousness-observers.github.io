---
layout: page
title: members
permalink: /members/
nav: true
nav_order: 2
---

Everyone here participates as an equal. A few volunteers handle logistics and website maintenance, but there are no roles, no ranks, and no hierarchy.

Because we are a decentralised group, the order of members below is **shuffled on every page load** — nobody is listed first, and position carries no meaning.

{% include member_card.liquid %}

<script>
  // 每次打开都重新排序：去中心化组织，顺序本身不该传递任何信息。
  (function () {
    function shuffle() {
      var wrap = document.querySelector('.team-members');
      if (!wrap) return;
      var cards = Array.prototype.slice.call(wrap.children);
      for (var i = cards.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = cards[i]; cards[i] = cards[j]; cards[j] = tmp;
      }
      for (var k = 0; k < cards.length; k++) wrap.appendChild(cards[k]);
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', shuffle);
    } else {
      shuffle();
    }
  })();
</script>

*Interested in joining? Visit the [Join](/join/) page.*
