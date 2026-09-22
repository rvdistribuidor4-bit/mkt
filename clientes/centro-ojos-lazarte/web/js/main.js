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

  // Formulario de contacto -> abre WhatsApp con los datos cargados
  var form = document.getElementById('contactForm');
  if (form) {
    var WA_NUMBER = '5493516371007';
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      function val(id) {
        var el = document.getElementById(id);
        return el && el.value ? el.value.trim() : '';
      }
      var nombre = val('nombre');
      var telefono = val('telefono');
      if (!nombre || !telefono) {
        alert('Por favor completá al menos tu nombre y teléfono.');
        return;
      }
      var lines = [
        'Hola, quiero solicitar un turno en Centro de Ojos Lazarte.',
        '',
        'Nombre: ' + nombre,
        'Teléfono: ' + telefono
      ];
      var email = val('email');
      if (email) lines.push('Email: ' + email);
      var motivo = val('motivo');
      if (motivo) lines.push('Motivo: ' + motivo);
      var fecha = val('fecha');
      if (fecha) lines.push('Día preferido: ' + fecha);
      var sede = val('sede');
      if (sede) lines.push('Sede: ' + sede);
      var mensaje = val('mensaje');
      if (mensaje) lines.push('Mensaje: ' + mensaje);

      var url = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(lines.join('\n'));

      // Feedback visual
      var btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.textContent = 'Abriendo WhatsApp…';
        btn.disabled = true;
        setTimeout(function () {
          btn.textContent = 'Enviar solicitud de turno';
          btn.disabled = false;
        }, 4000);
      }
      window.open(url, '_blank');
    });
  }
});
