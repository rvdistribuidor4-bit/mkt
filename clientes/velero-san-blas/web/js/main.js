/* Velero San Blas — JS minimo, sin dependencias.
   Cubre: menu movil, lightbox de galeria y envio del formulario de reserva.

   FORMULARIO: por defecto arma un mensaje de WhatsApp con todos los datos
   cargados (funciona sin backend ni costo). Si se quiere recibir por email,
   cargar el endpoint de Formspree en data-endpoint del <form> y el script
   envia por email en lugar de abrir WhatsApp. */
(function () {
  'use strict';

  // --- menu movil ---
  var hdr = document.querySelector('.hdr');
  var tog = document.querySelector('.mtog');
  if (tog && hdr) {
    tog.addEventListener('click', function () {
      var open = hdr.classList.toggle('open');
      tog.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    hdr.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () { hdr.classList.remove('open'); });
    });
  }

  // --- lightbox de galeria ---
  var lb = document.querySelector('.lb');
  if (lb) {
    var lbImg = lb.querySelector('img');
    document.querySelectorAll('.gal img').forEach(function (img) {
      img.addEventListener('click', function () {
        lbImg.src = img.currentSrc || img.src;
        lbImg.alt = img.alt;
        lb.classList.add('on');
      });
    });
    lb.addEventListener('click', function () { lb.classList.remove('on'); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') lb.classList.remove('on');
    });
  }

  // --- formulario de reserva ---
  var form = document.querySelector('.form');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = new FormData(form);
    var endpoint = form.dataset.endpoint;

    if (endpoint) {
      var btn = form.querySelector('button[type=submit]');
      var label = btn.textContent;
      btn.disabled = true;
      btn.textContent = form.dataset.sending || 'Enviando...';
      fetch(endpoint, { method: 'POST', body: d, headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('http ' + r.status);
          form.reset();
          btn.textContent = form.dataset.sent || '¡Enviado!';
        })
        .catch(function () {
          // si el email falla, no se pierde la consulta: se abre WhatsApp
          window.open(waLink(d), '_blank', 'noopener');
          btn.textContent = label;
        })
        .finally(function () {
          setTimeout(function () { btn.disabled = false; btn.textContent = label; }, 4000);
        });
      return;
    }

    window.open(waLink(d), '_blank', 'noopener');
  });

  function waLink(d) {
    var phone = form.dataset.phone || '';
    var L = {
      intro: form.dataset.msgIntro || 'Hola, quiero consultar por una reserva.',
      name: form.dataset.lName || 'Nombre',
      service: form.dataset.lService || 'Servicio',
      from: form.dataset.lFrom || 'Desde',
      to: form.dataset.lTo || 'Hasta',
      guests: form.dataset.lGuests || 'Personas',
      msg: form.dataset.lMsg || 'Mensaje'
    };
    var lines = [L.intro, ''];
    function add(label, val) { if (val) lines.push(label + ': ' + val); }
    add(L.name, d.get('nombre'));
    add(L.service, d.get('servicio'));
    add(L.from, d.get('desde'));
    add(L.to, d.get('hasta'));
    add(L.guests, d.get('personas'));
    add(L.msg, d.get('mensaje'));
    return 'https://wa.me/' + phone + '?text=' + encodeURIComponent(lines.join('\n'));
  }
})();
