// Bridge script for embedding MkDocs inside a parent site (e.g. WordPress iframe)
// - Posts current URL (path/query/hash) to parent so it can sync address bar if needed
// - Posts height to parent so iframe can auto-resize
(function () {
  function getDocHeight() {
    var body = document.body;
    var html = document.documentElement;
    if (!body || !html) return 0;
    return Math.max(
      body.scrollHeight,
      body.offsetHeight,
      html.clientHeight,
      html.scrollHeight,
      html.offsetHeight
    );
  }

  function post(type, payload) {
    try {
      window.parent && window.parent.postMessage({ source: "mkdocs", type: type, payload: payload }, "*");
    } catch (e) {
      // ignore
    }
  }

  function postUrl() {
    post("url", {
      path: location.pathname + location.search + location.hash,
    });
  }

  function postHeight() {
    post("height", {
      height: getDocHeight(),
    });
  }

  function boot() {
    // Initial
    postUrl();
    postHeight();

    // Update on resize/hash changes
    window.addEventListener("resize", postHeight);
    window.addEventListener("hashchange", function () {
      postUrl();
      postHeight();
    });

    // Material for MkDocs instant navigation hook
    var doc$ = window.document$;
    if (doc$ && typeof doc$.subscribe === "function") {
      doc$.subscribe(function () {
        requestAnimationFrame(function () {
          postUrl();
          postHeight();
        });
      });
    } else {
      // Fallback: observe DOM changes (best-effort)
      try {
        var mo = new MutationObserver(function () {
          postHeight();
        });
        mo.observe(document.documentElement, { childList: true, subtree: true });
      } catch (e) {
        // ignore
      }
    }
  }

  if (window.self === window.top) return; // not embedded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

