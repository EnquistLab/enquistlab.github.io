$(document).ready(function () {
  // add toggle functionality to abstract, award and bibtex buttons
  $("a.abstract").click(function () {
    $(this).parent().parent().find(".abstract.hidden").toggleClass("open");
    $(this).parent().parent().find(".award.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.award").click(function () {
    $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".award.hidden").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.bibtex").click(function () {
    $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".award.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden").toggleClass("open");
  });
  $("a").removeClass("waves-effect waves-light");

  // bootstrap-toc
  if ($("#toc-sidebar").length) {
    // remove related publications years from the TOC
    $(".publications h2").each(function () {
      $(this).attr("data-toc-skip", "");
    });
    var navSelector = "#toc-sidebar";
    var $myNav = $(navSelector);
    Toc.init($myNav);
    $("body").scrollspy({
      target: navSelector,
      offset: 100,
    });
  }

  // add css to jupyter notebooks
  const cssLink = document.createElement("link");
  cssLink.href = "../css/jupyter.css";
  cssLink.rel = "stylesheet";
  cssLink.type = "text/css";

  let jupyterTheme = determineComputedTheme();

  $(".jupyter-notebook-iframe-container iframe").each(function () {
    $(this).contents().find("head").append(cssLink);

    if (jupyterTheme == "dark") {
      $(this).bind("load", function () {
        $(this).contents().find("body").attr({
          "data-jp-theme-light": "false",
          "data-jp-theme-name": "JupyterLab Dark",
        });
      });
    }
  });

  // trigger popovers
  $('[data-toggle="popover"]').popover({
    trigger: "hover",
  });

  // ── Photo watermark (lower-right, subtle) ───────────────────────────────
  // CSS already covers .photo-gallery a::after and figure::after.
  // This handles any remaining substantial images (e.g. inline markdown images).
  document.querySelectorAll('img').forEach(function (img) {
    // Skip tiny icons, SVGs, logos, and emoji
    var src = img.getAttribute('src') || '';
    if (img.width < 80 || src.match(/\.(svg)$/i) || src.match(/icon|logo|favicon|emoji/i)) return;
    // Skip images already covered by CSS watermark containers
    if (img.closest('.photo-gallery, figure')) return;
    var parent = img.parentElement;
    if (!parent || parent.querySelector('.bje-watermark')) return;
    // Make parent a positioning context if needed
    if (window.getComputedStyle(parent).position === 'static') {
      parent.style.position = 'relative';
    }
    var mark = document.createElement('span');
    mark.className = 'bje-watermark';
    mark.textContent = '\u00a9 Brian J. Enquist';
    mark.style.cssText = [
      'position:absolute', 'bottom:6px', 'right:8px',
      'font-size:0.58rem', 'font-weight:500',
      "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif",
      'letter-spacing:0.03em', 'color:rgba(255,255,255,0.88)',
      'background:rgba(0,0,0,0.30)', 'padding:1px 5px', 'border-radius:3px',
      'pointer-events:none', 'z-index:20', 'line-height:1.5'
    ].join(';');
    parent.appendChild(mark);
  });
  // ────────────────────────────────────────────────────────────────────────
});
