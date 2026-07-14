// "Download PDF" header button.
// Manual pages (…/Manuals/…/X.html) link straight to the pre-generated PDF
// twin (X.pdf, produced at deploy time by scripts/generate_manual_pdfs.py).
// All other pages get no button.
(function () {
  function isManualPage() {
    return /\/Manuals\//.test(decodeURIComponent(location.pathname)) &&
      /\.html$/.test(location.pathname) &&
      !/\/index\.html$/i.test(location.pathname); // index stubs have no PDF
  }

  function cleanupButtons() {
    var old = document.querySelectorAll(".pdf-download, .pdf-download-header");
    old.forEach(function (el) {
      if (el && el.parentNode) el.parentNode.removeChild(el);
    });
  }

  function ensureHeaderButton() {
    if (!isManualPage()) return;
    var headerInner = document.querySelector(".md-header__inner");
    if (!headerInner) return;
    if (headerInner.querySelector(".pdf-download-header")) return;

    var target = headerInner.querySelector('label[for="__search"]') || headerInner.lastElementChild;

    var a = document.createElement("a");
    a.className = "md-header__button md-icon pdf-download-header";
    a.title = "下载 PDF";
    a.setAttribute("aria-label", "下载 PDF");
    a.href = location.pathname.replace(/\.html$/, ".pdf");
    // Empty download attr => browser names the file after the URL's last
    // segment, i.e. the source filename (e.g. ER805用户手册_V1.0.pdf)
    a.setAttribute("download", "");
    a.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/>' +
      "</svg>";

    if (target && target.parentNode) {
      target.parentNode.insertBefore(a, target);
    } else {
      headerInner.appendChild(a);
    }
  }

  function boot() {
    cleanupButtons();
    ensureHeaderButton();

    // Material for MkDocs (with navigation.instant) exposes document$ observable.
    var doc$ = window.document$;
    if (doc$ && typeof doc$.subscribe === "function") {
      doc$.subscribe(function () {
        requestAnimationFrame(function () {
          cleanupButtons();
          ensureHeaderButton();
        });
      });
      return;
    }

    // Fallback for older setups
    document.addEventListener("navigation:complete", function () {
      cleanupButtons();
      ensureHeaderButton();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
