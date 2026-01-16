// Inject a "Download PDF" button that triggers browser print (Save as PDF)
(function () {
  function cleanupOldButtons() {
    // Remove older in-content button if it exists (from previous versions)
    var old = document.querySelectorAll(".pdf-download");
    if (!old || !old.length) return;
    old.forEach(function (el) {
      if (el && el.parentNode) el.parentNode.removeChild(el);
    });
  }

  function ensureHeaderButton() {
    var headerInner = document.querySelector(".md-header__inner");
    if (!headerInner) return;

    // Avoid duplicates (instant navigation)
    if (headerInner.querySelector(".pdf-download-header")) return;

    var target = headerInner.querySelector('label[for="__search"]') || headerInner.lastElementChild;

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "md-header__button md-icon pdf-download-header";
    btn.title = "下载 PDF（打印/另存为 PDF）";
    btn.setAttribute("aria-label", "下载 PDF（打印/另存为 PDF）");
    btn.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M5 20h14v-2H5v2zm7-18 5.5 5.5-1.42 1.42L13 5.84V16h-2V5.84L7.92 8.92 6.5 7.5 12 2z"/>' +
      "</svg>";
    btn.addEventListener("click", function () {
      window.print();
    });

    if (target && target.parentNode) {
      target.parentNode.insertBefore(btn, target);
    } else {
      headerInner.appendChild(btn);
    }
  }

  function boot() {
    // Initial render
    cleanupOldButtons();
    ensureHeaderButton();

    // Material for MkDocs (with navigation.instant) exposes document$ observable.
    // This is the most reliable hook after each page render.
    var doc$ = window.document$;
    if (doc$ && typeof doc$.subscribe === "function") {
      doc$.subscribe(function () {
        // allow DOM to settle
        requestAnimationFrame(function () {
          cleanupOldButtons();
          ensureHeaderButton();
        });
      });
      return;
    }

    // Fallback for older setups
    document.addEventListener("navigation:complete", function () {
      cleanupOldButtons();
      ensureHeaderButton();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

