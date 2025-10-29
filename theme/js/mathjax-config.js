MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]},
  svg: {fontCache: 'global'},
  loader: {load: ['ui/lazy']},
  options: {
    enableMenu: false
  }
};

(function () {
  var script = document.createElement('script');
  script.src = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-chtml.min.js';
  script.async = true;
  script.crossOrigin = "anonymous";
  script.referrerPolicy = "no-referrer";
  script.integrity = "sha512-93xLZnNMlYI6xaQPf/cSdXoBZ23DThX7VehiGJJXB76HTTalQKPC5CIHuFX8dlQ5yzt6baBQRJ4sDXhzpojRJA==";
  document.head.appendChild(script);
})();