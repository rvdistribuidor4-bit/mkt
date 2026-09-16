document.addEventListener('DOMContentLoaded', function () {
  // Mobile menu toggle
  var toggle = document.querySelector('.mtog');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', nav.classList.contains('open'));
    });
    // Mobile: toggle dropdown on click
    nav.querySelectorAll('li').forEach(function (li) {
      var link = li.querySelector('a');
      var dd = li.querySelector('.dropdown');
      if (dd && link) {
        link.addEventListener('click', function (e) {
          if (window.innerWidth <= 768) {
            e.preventDefault();
            li.classList.toggle('mob-open');
          }
        });
      }
    });
    // Close nav when a dropdown link is clicked (mobile)
    nav.querySelectorAll('.dropdown a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
    // Close nav when a non-dropdown link is clicked
    nav.querySelectorAll(':scope > li > a').forEach(function (a) {
      if (!a.nextElementSibling || !a.nextElementSibling.classList.contains('dropdown')) {
        a.addEventListener('click', function () {
          nav.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        });
      }
    });
  }
});
