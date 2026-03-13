// Add a dedicated sidebar search that lists matching nav items
(function () {
  function getSidebar() {
    return document.querySelector(".md-sidebar--primary");
  }

  function getNav(sidebar) {
    return (
      sidebar.querySelector(".md-nav--primary") ||
      sidebar.querySelector(".md-nav")
    );
  }

  function ensureSidebarSearch() {
    var sidebar = getSidebar();
    if (!sidebar) return null;

    var existing = sidebar.querySelector(".md-nav-search");
    if (existing) return existing;

    var container = document.createElement("div");
    container.className = "md-nav-search";

    var input = document.createElement("input");
    input.type = "search";
    input.className = "md-nav-search__input";
    input.placeholder = "搜索目录";
    input.setAttribute("aria-label", "搜索目录");

    container.appendChild(input);

    var inner =
      sidebar.querySelector(".md-sidebar__scrollwrap") ||
      sidebar.querySelector(".md-sidebar__inner") ||
      sidebar;
    var nav = getNav(sidebar);
    var title =
      sidebar.querySelector(".md-nav--primary > .md-nav__title") ||
      sidebar.querySelector(".md-sidebar__title") ||
      sidebar.querySelector(".md-nav__title");

    if (title && title.parentNode === inner) {
      if (title.nextSibling) {
        inner.insertBefore(container, title.nextSibling);
      } else {
        inner.appendChild(container);
      }
    } else if (nav && nav.parentNode === inner) {
      inner.insertBefore(container, nav);
    } else {
      inner.insertBefore(container, inner.firstChild);
    }

    return container;
  }

  function ensureResults(container) {
    var results = container.querySelector(".md-nav-search__results");
    if (results) return results;
    results = document.createElement("div");
    results.className = "md-nav-search__results";
    container.appendChild(results);
    return results;
  }

  function collectLinks() {
    var sidebar = getSidebar();
    if (!sidebar) return [];
    var nav = getNav(sidebar);
    if (!nav) return [];
    return Array.prototype.slice.call(nav.querySelectorAll("a.md-nav__link"));
  }

  function showHint(container, text) {
    var results = ensureResults(container);
    results.innerHTML = "";
    var header = document.createElement("div");
    header.className = "md-nav-search__count";
    header.textContent = text;
    results.appendChild(header);
    results.style.display = "";
  }

  function updateResults(container, query) {
    var results = ensureResults(container);
    var needle = query.trim().toLowerCase();

    results.innerHTML = "";
    if (!needle) {
      showHint(container, "键入以开始搜索");
      return;
    }

    var links = collectLinks();
    var matches = links
      .map(function (link) {
        return {
          text: (link.textContent || "").trim(),
          href: link.getAttribute("href") || "",
        };
      })
      .filter(function (item) {
        return item.text.toLowerCase().indexOf(needle) !== -1;
      })
      .slice(0, 20);

    if (!matches.length) {
      showHint(container, "没有找到符合条件的结果");
      return;
    }

    var header = document.createElement("div");
    header.className = "md-nav-search__count";
    header.textContent = matches.length + " 个符合条件的结果";
    results.appendChild(header);

    function escapeHtml(text) {
      return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }

    function highlight(text) {
      var safe = escapeHtml(text);
      var re = new RegExp(needle.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "ig");
      return safe.replace(re, function (m) {
        return '<mark class="md-nav-search__hit">' + m + "</mark>";
      });
    }

    var docIcon = '<svg class="md-nav-search__link-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6m4 18H6V4h7v5h5v11z"/></svg>';

    matches.forEach(function (item) {
      var row = document.createElement("a");
      row.className = "md-nav-search__link";
      row.href = item.href;
      row.innerHTML = docIcon + '<span>' + highlight(item.text) + '</span>';
      row.addEventListener("click", function () {
        var results = container.querySelector(".md-nav-search__results");
        if (results) results.style.display = "none";
        closePopup(container);
      });
      results.appendChild(row);
    });

    results.style.display = "";
  }

  function bind() {
    var container = ensureSidebarSearch();
    if (!container) return;
    var input = container.querySelector("input");
    if (!input || input.dataset.bound === "true") return;
    input.dataset.bound = "true";

    input.addEventListener("mousedown", function (e) {
      e.stopPropagation();
    });

    input.addEventListener("click", function (e) {
      e.stopPropagation();
    });

    input.addEventListener("input", function () {
      updateResults(container, input.value);
    });

    input.addEventListener("focus", function () {
      container.classList.add("md-nav-search--focused");
      openPopup(container, { autofocus: true });
      if (!input.value.trim()) {
        showHint(container, "键入以开始搜索");
      }
    });

    input.addEventListener("blur", function () {
      // Delay to allow click on results
      setTimeout(function () {
        if (!container.contains(document.activeElement)) {
          container.classList.remove("md-nav-search--focused");
        }
      }, 150);
    });

    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        closePopup(container);
        input.blur();
      }
    });

    // Close only when clicking the backdrop (see openPopup)
  }

  function openPopup(container) {
    var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
    if (container.classList.contains("md-nav-search--popup")) return;

    var rect = container.getBoundingClientRect();
    container.dataset.origStyle = container.getAttribute("style") || "";
    container.dataset.origParent = "";
    container.dataset.origNext = "";

    var parent = container.parentNode;
    var next = container.nextSibling;
    if (parent) {
      container.dataset.origParent = "1";
      container._origParent = parent;
      container._origNext = next;
    }

    var backdrop = document.createElement("div");
    backdrop.className = "md-nav-search__backdrop";
    backdrop.addEventListener("click", function () {
      var results = container.querySelector(".md-nav-search__results");
      if (results) results.style.display = "none";
      closePopup(container);
      var input = container.querySelector("input");
      if (input) input.blur();
    });
    document.body.appendChild(backdrop);

    // Move to body to avoid sidebar stacking context
    document.body.appendChild(container);

    container.style.position = "fixed";
    container.style.left = rect.left + "px";
    container.style.top = rect.top + "px";
    container.style.width = "min(28rem, 90vw)";
    container.style.zIndex = "1001";

    container.classList.add("md-nav-search--popup");

    if (options.autofocus !== false) {
      var input = container.querySelector("input");
      if (input) {
        requestAnimationFrame(function () {
          input.focus();
          input.select();
          setTimeout(function () {
            input.focus();
            input.select();
          }, 30);
        });
      }
    }
  }

  function closePopup(container) {
    if (!container.classList.contains("md-nav-search--popup")) return;

    var backdrop = document.querySelector(".md-nav-search__backdrop");
    if (backdrop && backdrop.parentNode) backdrop.parentNode.removeChild(backdrop);

    var orig = container.dataset.origStyle || "";
    if (container._origParent) {
      if (container._origNext && container._origNext.parentNode === container._origParent) {
        container._origParent.insertBefore(container, container._origNext);
      } else {
        container._origParent.appendChild(container);
      }
      container._origParent = null;
      container._origNext = null;
    }

    if (orig) {
      container.setAttribute("style", orig);
    } else {
      container.removeAttribute("style");
    }
    container.classList.remove("md-nav-search--popup");
  }

  function boot() {
    ensureSidebarSearch();
    bind();
  }

  document.addEventListener("DOMContentLoaded", boot);
  document.addEventListener("navigation:complete", boot);

  var doc$ = window.document$;
  if (doc$ && typeof doc$.subscribe === "function") {
    doc$.subscribe(function () {
      requestAnimationFrame(boot);
    });
  }
})();
