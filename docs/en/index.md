---
title: Documentation
hide:
  - navigation
  - toc
---

<div class="pm-home">
  <h1 class="pm-home__title">Documentation</h1>
  <p class="pm-home__subtitle">Product manuals and guides (MkDocs + Material)</p>

  <div class="pm-home__search">
    <div class="pm-home-search" role="search" aria-label="Search all docs">
      <span class="pm-home-search__icon" aria-hidden="true">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <path fill="currentColor" d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.57 4.23l.27.27h.8l5 5-1.5 1.5-5-5v-.8l-.27-.27A6.48 6.48 0 0 1 9.5 16 6.5 6.5 0 1 1 9.5 3m0 2A4.5 4.5 0 1 0 14 9.5 4.5 4.5 0 0 0 9.5 5Z"/>
        </svg>
      </span>
      <input class="pm-home-search__input" id="pm-home-search-input" type="search" placeholder="Search all docs" autocomplete="off" />
      <span class="pm-home-search__hint">Ctrl K</span>
    </div>
  </div>

  <div class="pm-home-search__results" id="pm-home-search-results" aria-live="polite" style="display:none"></div>

  <nav class="pm-home__tabs" aria-label="Categories">
    <button class="pm-home__tab pm-home__tab--active" type="button" data-tab="enrouter">EnRouter</button>
  </nav>

  <section class="pm-home__section" id="enrouter" data-tab-panel="enrouter">
    <h2 class="pm-home__h2">EnRouter</h2>
    <div class="pm-home__grid">
      <a class="pm-card" href="EnRouter/index.html">
        <div class="pm-card__img pm-card__img--green">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3h-2V6H6v3H4V6m0 5h16a2 2 0 0 1 2 2v3h-2v-3H4v3H2v-3a2 2 0 0 1 2-2m2 6h12v2H6v-2Z"/></svg>
        </div>
        <div class="pm-card__body">
          <div class="pm-card__title">EnRouter</div>
          <div class="pm-card__desc">Product documentation entry</div>
        </div>
      </a>

      <a class="pm-card" href="EnRouter/IR302/index.html">
        <div class="pm-card__img pm-card__img--purple">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M12 3 2 9l10 6 10-6-10-6m0 10L2 7v10l10 6 10-6V7l-10 6Z"/></svg>
        </div>
        <div class="pm-card__body">
          <div class="pm-card__title">IR302</div>
          <div class="pm-card__desc">IR302 documentation overview</div>
        </div>
      </a>

      <a class="pm-card" href="EnRouter/IR302/quickstart.html">
        <div class="pm-card__img pm-card__img--blue">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6m4 18H6V4h7v5h5v11z"/></svg>
        </div>
        <div class="pm-card__body">
          <div class="pm-card__title">Quickstart</div>
          <div class="pm-card__desc">Install, power-on, login, and basic setup</div>
        </div>
      </a>

      <a class="pm-card" href="EnRouter/IR302/faq.html">
        <div class="pm-card__img pm-card__img--orange">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-10 10 10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m1 17h-2v-2h2v2m2.07-7.75-.9.92A3.49 3.49 0 0 0 13 15h-2v-.5c0-1 .4-2 1.07-2.68l1.24-1.26a1.5 1.5 0 1 0-2.56-1.06H8.75a3.25 3.25 0 1 1 6.32 1.75Z"/></svg>
        </div>
        <div class="pm-card__body">
          <div class="pm-card__title">FAQ</div>
          <div class="pm-card__desc">Troubleshooting and common questions</div>
        </div>
      </a>
    </div>
  </section>
</div>

<style>
  .pm-home {
    max-width: 64rem;
    margin: 0 auto;
    padding: 1.25rem 1rem 2rem;
  }
  .pm-home__title {
    text-align: center;
    font-size: clamp(2rem, 4vw, 3rem);
    margin: 0.75rem 0 0.25rem;
    letter-spacing: -0.02em;
  }
  .pm-home__subtitle {
    text-align: center;
    margin: 0 0 1.25rem;
    color: var(--md-default-fg-color--light);
  }
  .pm-home__search {
    display: flex;
    justify-content: center;
    margin: 1rem 0 1.25rem;
  }
  .pm-home-search {
    width: min(56rem, 92vw);
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.65rem 1rem;
    border-radius: 999px;
    border: 2px solid color-mix(in srgb, var(--md-primary-fg-color) 65%, var(--md-default-bg-color));
    background: color-mix(in srgb, var(--md-primary-fg-color) 8%, var(--md-default-bg-color));
    color: var(--md-default-fg-color);
    box-shadow: 0 6px 18px rgba(0,0,0,.08);
    transition: box-shadow 120ms ease, border-color 120ms ease, transform 120ms ease, background 120ms ease;
  }
  .pm-home-search:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 26px rgba(0,0,0,.12);
  }
  .pm-home-search:focus-within {
    border-color: var(--md-primary-fg-color);
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--md-primary-fg-color) 25%, transparent), 0 10px 26px rgba(0,0,0,.12);
    background: var(--md-default-bg-color);
    transform: translateY(-1px);
  }
  .pm-home-search__icon svg {
    width: 1.3rem;
    height: 1.3rem;
    color: var(--md-default-fg-color--light);
  }
  .pm-home-search__input {
    flex: 1;
    border: none;
    outline: none;
    background: transparent;
    color: var(--md-default-fg-color);
    font-size: 1.05rem;
    line-height: 1.6;
  }
  .pm-home-search__input::placeholder {
    color: var(--md-default-fg-color--light);
  }
  .pm-home__searchhint {
    padding: 0.15rem 0.5rem;
    border-radius: 0.5rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    background: var(--md-default-bg-color);
    color: var(--md-default-fg-color--light);
    font-size: 0.8rem;
    line-height: 1.4;
  }
  .pm-home-search__results {
    width: min(56rem, 92vw);
    margin: 0 auto 1.25rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.8rem;
    background: var(--md-default-bg-color);
    overflow: hidden;
    box-shadow: 0 14px 34px rgba(0,0,0,.10);
  }
  .pm-home-search__meta {
    padding: 0.7rem 1rem;
    color: var(--md-default-fg-color--light);
    border-bottom: 1px solid var(--md-default-fg-color--lightest);
    font-size: 0.9rem;
  }
  .pm-home-search__item {
    display: flex;
    gap: 0.75rem;
    padding: 0.9rem 1rem;
    text-decoration: none;
    color: var(--md-default-fg-color);
    border-top: 1px solid var(--md-default-fg-color--lightest);
  }
  .pm-home-search__item:first-of-type { border-top: none; }
  .pm-home-search__item:hover {
    background: color-mix(in srgb, var(--md-primary-fg-color) 8%, transparent);
  }
  .pm-home-search__itemicon svg {
    width: 1.3rem;
    height: 1.3rem;
    color: var(--md-default-fg-color--light);
    margin-top: 0.2rem;
  }
  .pm-home-search__itemtitle {
    font-weight: 800;
    margin-bottom: 0.25rem;
    font-size: 1.05rem;
  }
  .pm-home-search__itemdesc {
    color: var(--md-default-fg-color--light);
    line-height: 1.45;
  }
  .pm-home-search__hit {
    color: var(--md-primary-fg-color);
    font-weight: 800;
  }
  .pm-home__tabs {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    margin: 0.25rem 0 1.25rem;
  }
  .pm-home__tab {
    appearance: none;
    display: inline-flex;
    align-items: center;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    text-decoration: none;
    color: var(--md-default-fg-color--light);
    border: 1px solid var(--md-default-fg-color--lightest);
    background: var(--md-default-bg-color);
    font-weight: 600;
    cursor: pointer;
  }
  .pm-home__tab:hover {
    border-color: color-mix(in srgb, var(--md-primary-fg-color) 45%, var(--md-default-fg-color--lightest));
    color: var(--md-primary-fg-color);
  }
  .pm-home__tab--active {
    border-color: color-mix(in srgb, var(--md-primary-fg-color) 55%, var(--md-default-fg-color--lightest));
    color: var(--md-primary-fg-color);
    background: color-mix(in srgb, var(--md-primary-fg-color) 8%, var(--md-default-bg-color));
  }
  .pm-home__section {
    margin: 1.5rem 0 0.75rem;
  }
  .pm-home__h2 {
    margin: 0.25rem 0 0.75rem;
    font-size: 1.35rem;
  }
  .pm-home__grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
  @media (max-width: 60rem) {
    .pm-home__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  }
  @media (max-width: 38rem) {
    .pm-home__grid { grid-template-columns: 1fr; }
  }
  .pm-card {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    border-radius: 0.9rem;
    background: var(--md-default-bg-color);
    border: 1px solid var(--md-default-fg-color--lightest);
    text-decoration: none;
    color: var(--md-default-fg-color);
    transition: transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
  }
  .pm-card:hover {
    transform: translateY(-2px);
    border-color: color-mix(in srgb, var(--md-primary-fg-color) 35%, var(--md-default-fg-color--lightest));
    box-shadow: 0 12px 28px rgba(0,0,0,.10);
  }
  .pm-card__img {
    width: 4.25rem;
    height: 4.25rem;
    border-radius: 0.9rem;
    display: grid;
    place-items: center;
    flex-shrink: 0;
    color: white;
  }
  .pm-card__img svg {
    width: 2.1rem;
    height: 2.1rem;
  }
  .pm-card__img--green { background: linear-gradient(135deg, #16a34a, #22c55e); }
  .pm-card__img--blue { background: linear-gradient(135deg, #2563eb, #60a5fa); }
  .pm-card__img--purple { background: linear-gradient(135deg, #7c3aed, #a78bfa); }
  .pm-card__img--orange { background: linear-gradient(135deg, #f59e0b, #fbbf24); }
  .pm-card__title {
    font-weight: 800;
    margin: 0.05rem 0 0.25rem;
    letter-spacing: -0.01em;
  }
  .pm-card__desc {
    color: var(--md-default-fg-color--light);
    font-size: 0.95rem;
    line-height: 1.35;
  }
</style>

<script>
  (function () {
    var INDEX_URL = "search/search_index.json";
    var state = { index: null, ready: false };

    function norm(s) {
      return (s || "").toString().trim().toLowerCase();
    }

    function escapeHtml(text) {
      return (text || "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }

    function highlight(text, needle) {
      var safe = escapeHtml(text);
      if (!needle) return safe;
      var re = new RegExp(needle.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "ig");
      return safe.replace(re, function (m) {
        return '<span class="pm-home-search__hit">' + m + "</span>";
      });
    }

    function pickSnippet(text, needle) {
      var raw = (text || "").replace(/\s+/g, " ").trim();
      if (!raw) return "";
      if (!needle) return raw.slice(0, 90);
      var idx = raw.toLowerCase().indexOf(needle);
      if (idx < 0) return raw.slice(0, 90);
      var start = Math.max(0, idx - 28);
      var end = Math.min(raw.length, idx + needle.length + 60);
      var prefix = start > 0 ? "…" : "";
      var suffix = end < raw.length ? "…" : "";
      return prefix + raw.slice(start, end) + suffix;
    }

    function ensureIndex() {
      if (state.ready) return Promise.resolve(state.index);
      return fetch(INDEX_URL, { credentials: "same-origin" })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          state.index = data || {};
          state.ready = true;
          return state.index;
        })
        .catch(function () {
          state.ready = true;
          state.index = { docs: [] };
          return state.index;
        });
    }

    function searchDocs(q) {
      var needle = norm(q);
      if (!needle) return [];
      var docs = (state.index && state.index.docs) ? state.index.docs : [];
      var res = [];
      for (var i = 0; i < docs.length; i++) {
        var d = docs[i] || {};
        var title = (d.title || d.location || "").toString();
        var text = (d.text || "").toString();
        var hay = norm(title + " " + text);
        var pos = hay.indexOf(needle);
        if (pos >= 0) {
          res.push({ title: title, location: d.location || "", text: text, score: pos });
        }
      }
      res.sort(function (a, b) { return a.score - b.score; });
      return res.slice(0, 8);
    }

    function renderResults(container, query, items) {
      container.innerHTML = "";
      if (!query.trim()) {
        container.style.display = "none";
        return;
      }
      var header = document.createElement("div");
      header.className = "pm-home-search__meta";
      if (!items.length) {
        header.textContent = "No matching results found";
      } else {
        header.textContent = items.length + " results";
      }
      container.appendChild(header);

      if (items.length) {
        for (var i = 0; i < items.length; i++) {
          var it = items[i];
          var a = document.createElement("a");
          a.className = "pm-home-search__item";
          a.href = it.location || "#";
          a.innerHTML =
            '<span class="pm-home-search__itemicon" aria-hidden="true">' +
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6m4 18H6V4h7v5h5v11z"/></svg>' +
            "</span>" +
            '<div class="pm-home-search__itembody">' +
            '<div class="pm-home-search__itemtitle">' + highlight(it.title || it.location, norm(query)) + "</div>" +
            '<div class="pm-home-search__itemdesc">' + highlight(pickSnippet(it.text, norm(query)), norm(query)) + "</div>" +
            "</div>";
          container.appendChild(a);
        }
      }
      container.style.display = "";
    }

    function bootTabs() {
      var tabs = Array.prototype.slice.call(document.querySelectorAll(".pm-home__tab[data-tab]"));
      var panels = Array.prototype.slice.call(document.querySelectorAll("[data-tab-panel]"));
      if (!tabs.length || !panels.length) return;

      function setActive(key) {
        tabs.forEach(function (t) {
          var on = t.getAttribute("data-tab") === key;
          if (on) t.classList.add("pm-home__tab--active");
          else t.classList.remove("pm-home__tab--active");
        });
        panels.forEach(function (p) {
          p.hidden = p.getAttribute("data-tab-panel") !== key;
        });
      }

      var initial = (location.hash || "").replace("#", "");
      var valid = tabs.some(function (t) { return t.getAttribute("data-tab") === initial; });
      setActive(valid ? initial : tabs[0].getAttribute("data-tab"));

      tabs.forEach(function (t) {
        if (t.dataset.boundTab === "true") return;
        t.dataset.boundTab = "true";
        t.addEventListener("click", function () {
          var key = t.getAttribute("data-tab");
          if (!key) return;
          setActive(key);
          history.replaceState(null, "", "#" + key);
        });
      });
    }

    function bootSearch() {
      var input = document.getElementById("pm-home-search-input");
      var results = document.getElementById("pm-home-search-results");
      if (!input || !results || input.dataset.bound === "true") return;
      input.dataset.bound = "true";

      ensureIndex();

      input.addEventListener("input", function () {
        ensureIndex().then(function () {
          var items = searchDocs(input.value);
          renderResults(results, input.value, items);
        });
      });

      input.addEventListener("keydown", function (e) {
        if ((e.ctrlKey || e.metaKey) && (e.key === "k" || e.key === "K")) {
          e.preventDefault();
          input.focus();
          input.select();
        }
        if (e.key === "Escape") {
          input.value = "";
          results.style.display = "none";
          input.blur();
        }
      });

      document.addEventListener("click", function (e) {
        if (!results.contains(e.target) && e.target !== input) {
          results.style.display = "none";
        }
      });
    }

    function boot() {
      bootTabs();
      bootSearch();
    }

    document.addEventListener("DOMContentLoaded", boot);
    document.addEventListener("navigation:complete", boot);
    var doc$ = window.document$;
    if (doc$ && typeof doc$.subscribe === "function") {
      doc$.subscribe(function () { requestAnimationFrame(boot); });
    }
  })();
</script>

