// Show a per-page "Edit this page" link under the main H1.
// We reuse the existing Material edit button URL so it always points to the exact source file.
(function () {
  function getLabels() {
    var lang = (document.documentElement.getAttribute("lang") || "").toLowerCase();
    if (lang.startsWith("zh")) {
      return { view: "查看源码" };
    }
    return { view: "View source" };
  }

  function findEditUrl() {
    // Material renders edit/view buttons as ".md-content__button" anchors.
    var candidates = document.querySelectorAll("a.md-content__button");
    if (!candidates || !candidates.length) return "";
    for (var i = 0; i < candidates.length; i++) {
      var href = candidates[i].getAttribute("href") || "";
      if (!href) continue;
      // Prefer GitHub edit link
      if (href.indexOf("/edit/") !== -1 || href.indexOf("/blob/") !== -1) return href;
    }
    return candidates[0].getAttribute("href") || "";
  }

  function toBlobUrl(url) {
    // https://github.com/<org>/<repo>/edit/<branch>/<path>
    // -> https://github.com/<org>/<repo>/blob/<branch>/<path>
    if (!url) return "";
    if (url.indexOf("/edit/") !== -1) return url.replace("/edit/", "/blob/");
    return url;
  }

  function toGiteeUrl(url) {
    // GitHub -> Gitee mirror (same owner/repo/path)
    if (!url) return "";
    return url
      .replace(/^https?:\/\/github\.com\//i, "https://gitee.com/")
      .replace(/^https?:\/\/www\.github\.com\//i, "https://gitee.com/");
  }

  function inject() {
    var main =
      document.querySelector('[data-md-component="content"] .md-content__inner') ||
      document.querySelector(".md-content__inner");
    if (!main) return;
    // Remove previous injection (instant navigation / re-render)
    var old = main.querySelector(".pm-edit-under-title");
    if (old && old.parentNode) old.parentNode.removeChild(old);

    var h1 = main.querySelector(".md-typeset h1") || main.querySelector("h1");
    if (!h1) return;

    var url = findEditUrl();
    if (!url) return;
    var blobUrl = toGiteeUrl(toBlobUrl(url));
    var labels = getLabels();

    var wrap = document.createElement("div");
    wrap.className = "pm-edit-under-title";
    wrap.innerHTML =
      '<a class="pm-edit-under-title__link" href="' +
      blobUrl +
      '" target="_blank" rel="noopener noreferrer">' +
      labels.view +
      "</a>";
    h1.insertAdjacentElement("afterend", wrap);
  }

  document.addEventListener("DOMContentLoaded", inject);
  document.addEventListener("navigation:complete", inject);
  var doc$ = window.document$;
  if (doc$ && typeof doc$.subscribe === "function") {
    doc$.subscribe(function () {
      requestAnimationFrame(inject);
    });
  }

  // Best-effort immediate run (in case DOMContentLoaded already fired)
  inject();
})();

