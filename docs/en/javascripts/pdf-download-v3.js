// "Download PDF" header button (v3: text label + streaming progress).
// Manual pages (…/Manuals/…/X.html, excluding index stubs) get a labelled
// button that fetches the pre-generated PDF twin with a live percentage,
// then saves it. Styles are inlined so no stylesheet change is required.
(function () {
  var LABEL = "Download PDF";
  var DONE_LABEL = "Downloaded ✓";

  var ICON_SVG =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" ' +
    'style="width:1.15rem;height:1.15rem;fill:currentColor;">' +
    '<path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>';

  var SPINNER_SVG =
    '<svg viewBox="0 0 24 24" aria-hidden="true" ' +
    'style="width:1.15rem;height:1.15rem;animation:ih-pdf-spin 1s linear infinite;">' +
    '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2.5" ' +
    'stroke-dasharray="42" stroke-dashoffset="14" stroke-linecap="round"/></svg>';

  var LABEL_STYLE = "font-size:.65rem;margin-left:.15rem;white-space:nowrap;";

  function isManualPage() {
    return /\/Manuals\//.test(decodeURIComponent(location.pathname)) &&
      /\.html$/.test(location.pathname) &&
      !/\/index\.html$/i.test(location.pathname); // index stubs have no PDF
  }

  function ensureSpinKeyframes() {
    if (document.getElementById("ih-pdf-spin-style")) return;
    var st = document.createElement("style");
    st.id = "ih-pdf-spin-style";
    st.textContent = "@keyframes ih-pdf-spin{to{transform:rotate(360deg)}}";
    document.head.appendChild(st);
  }

  function setContent(a, iconHtml, text) {
    a.innerHTML = iconHtml + '<span style="' + LABEL_STYLE + '">' + text + "</span>";
  }

  var downloading = false;

  function onClick(e) {
    // Older browsers without streaming fetch: let the plain <a download> work.
    if (!window.fetch || !window.ReadableStream || !window.URL ||
        typeof URL.createObjectURL !== "function") {
      return;
    }
    e.preventDefault();
    if (downloading) return;
    downloading = true;

    var a = e.currentTarget;
    var url = a.getAttribute("href");
    ensureSpinKeyframes();
    setContent(a, SPINNER_SVG, "0%");

    fetch(url).then(function (resp) {
      if (!resp.ok) throw new Error("http " + resp.status);
      var total = parseInt(resp.headers.get("Content-Length") || "0", 10);
      var reader = resp.body.getReader();
      var chunks = [];
      var received = 0;
      function pump() {
        return reader.read().then(function (r) {
          if (r.done) return;
          chunks.push(r.value);
          received += r.value.length;
          setContent(a, SPINNER_SVG, total
            ? Math.min(99, Math.round(received / total * 100)) + "%"
            : (received / 1048576).toFixed(1) + "MB");
          return pump();
        });
      }
      return pump().then(function () {
        return new Blob(chunks, { type: "application/pdf" });
      });
    }).then(function (blob) {
      var objUrl = URL.createObjectURL(blob);
      var tmp = document.createElement("a");
      tmp.href = objUrl;
      tmp.download = decodeURIComponent(url.split("/").pop());
      document.body.appendChild(tmp);
      tmp.click();
      tmp.remove();
      setTimeout(function () { URL.revokeObjectURL(objUrl); }, 10000);
      setContent(a, ICON_SVG, DONE_LABEL);
      setTimeout(function () {
        setContent(a, ICON_SVG, LABEL);
        downloading = false;
      }, 2500);
    }).catch(function () {
      // Fall back to a plain navigation download — always works.
      setContent(a, ICON_SVG, LABEL);
      downloading = false;
      window.location.href = url;
    });
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
    a.title = LABEL;
    a.setAttribute("aria-label", LABEL);
    a.href = location.pathname.replace(/\.html$/, ".pdf");
    // Empty download attr => browser names the file after the URL's last
    // segment, i.e. the source filename (e.g. ER805用户手册_V1.0.pdf)
    a.setAttribute("download", "");
    a.style.cssText = "width:auto;padding:0 .5rem;display:inline-flex;align-items:center;";
    setContent(a, ICON_SVG, LABEL);
    a.addEventListener("click", onClick);

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
