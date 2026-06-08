/**
 * toc-h1.js
 * 将页面中的 h1 标题也纳入右侧 TOC（MkDocs Material 默认只显示 h2-h6）
 */
(function () {
  "use strict";

  function rebuildToc() {
    // 获取文章内容区域和 TOC 容器
    const article = document.querySelector("article.md-content__inner");
    const tocNav = document.querySelector(".md-sidebar--secondary .md-nav--secondary");
    
    if (!article || !tocNav) return;

    // 获取所有标题（h1-h4）
    const headings = article.querySelectorAll("h1, h2, h3, h4");
    if (headings.length === 0) return;

    // 构建新的 TOC 结构
    const tocList = document.createElement("ul");
    tocList.className = "md-nav__list";

    let currentH1 = null;
    let currentH1List = null;
    let currentH2 = null;
    let currentH2List = null;
    let currentH3 = null;
    let currentH3List = null;

    headings.forEach((heading) => {
      const id = heading.id;
      if (!id) return;

      const text = heading.textContent.replace(/¶$/, "").trim();
      const level = parseInt(heading.tagName.charAt(1));

      const li = document.createElement("li");
      li.className = "md-nav__item";

      const a = document.createElement("a");
      a.className = "md-nav__link";
      a.href = "#" + id;
      a.textContent = text;

      li.appendChild(a);

      if (level === 1) {
        // h1 - 顶级
        tocList.appendChild(li);
        currentH1 = li;
        currentH1List = null;
        currentH2 = null;
        currentH2List = null;
        currentH3 = null;
        currentH3List = null;
      } else if (level === 2) {
        // h2
        if (currentH1) {
          if (!currentH1List) {
            currentH1List = document.createElement("ul");
            currentH1List.className = "md-nav__list";
            const nav = document.createElement("nav");
            nav.className = "md-nav";
            nav.appendChild(currentH1List);
            currentH1.appendChild(nav);
          }
          currentH1List.appendChild(li);
        } else {
          tocList.appendChild(li);
        }
        currentH2 = li;
        currentH2List = null;
        currentH3 = null;
        currentH3List = null;
      } else if (level === 3) {
        // h3 - 必须嵌套在 h2 或 h1 下
        if (currentH2) {
          // h3 嵌套在 h2 下
          if (!currentH2List) {
            currentH2List = document.createElement("ul");
            currentH2List.className = "md-nav__list";
            const nav = document.createElement("nav");
            nav.className = "md-nav";
            nav.appendChild(currentH2List);
            currentH2.appendChild(nav);
          }
          currentH2List.appendChild(li);
        } else if (currentH1) {
          // h3 嵌套在 h1 下（当没有 h2 时）
          if (!currentH1List) {
            currentH1List = document.createElement("ul");
            currentH1List.className = "md-nav__list";
            const nav = document.createElement("nav");
            nav.className = "md-nav";
            nav.appendChild(currentH1List);
            currentH1.appendChild(nav);
          }
          currentH1List.appendChild(li);
        } else {
          tocList.appendChild(li);
        }
        currentH3 = li;
        currentH3List = null;
      } else if (level === 4) {
        // h4 - 必须嵌套在 h3、h2 或 h1 下
        if (currentH3) {
          // h4 嵌套在 h3 下
          if (!currentH3List) {
            currentH3List = document.createElement("ul");
            currentH3List.className = "md-nav__list";
            const nav = document.createElement("nav");
            nav.className = "md-nav";
            nav.appendChild(currentH3List);
            currentH3.appendChild(nav);
          }
          currentH3List.appendChild(li);
        } else if (currentH2) {
          // h4 嵌套在 h2 下（当没有 h3 时）
          if (!currentH2List) {
            currentH2List = document.createElement("ul");
            currentH2List.className = "md-nav__list";
            const nav = document.createElement("nav");
            nav.className = "md-nav";
            nav.appendChild(currentH2List);
            currentH2.appendChild(nav);
          }
          currentH2List.appendChild(li);
        } else if (currentH1) {
          // h4 嵌套在 h1 下（当没有 h2 和 h3 时）
          if (!currentH1List) {
            currentH1List = document.createElement("ul");
            currentH1List.className = "md-nav__list";
            const nav = document.createElement("nav");
            nav.className = "md-nav";
            nav.appendChild(currentH1List);
            currentH1.appendChild(nav);
          }
          currentH1List.appendChild(li);
        } else {
          tocList.appendChild(li);
        }
      }
    });

    // 替换原有 TOC
    const oldList = tocNav.querySelector("ul.md-nav__list");
    if (oldList && tocList.children.length > 0) {
      oldList.parentNode.replaceChild(tocList, oldList);
    } else if (!oldList && tocList.children.length > 0) {
      tocNav.appendChild(tocList);
    }
  }

  // 页面加载完成后执行
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", rebuildToc);
  } else {
    rebuildToc();
  }

  // 支持 MkDocs Material 的 instant loading
  if (typeof document$ !== "undefined") {
    document$.subscribe(rebuildToc);
  }
})();
