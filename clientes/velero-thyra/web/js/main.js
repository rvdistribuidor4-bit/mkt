/* THYRA — JS sin dependencias.
   Menu movil · header al hacer scroll · animaciones de entrada ·
   lightbox de galeria · formulario de reserva.

   FORMULARIO: por defecto arma un mensaje de WhatsApp con todos los datos
   cargados (sin backend, sin costo). Para recibir por email, poner el
   endpoint de Formspree en data-endpoint del <form>. */
(function () {
  'use strict';

  var hdr = document.querySelector('.hdr');

  // --- header solido al bajar ---
  if (hdr) {
    var onScroll = function () {
      hdr.classList.toggle('stuck', window.scrollY > 40);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // --- menu movil ---
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

  // --- animaciones de entrada ---
  var rises = document.querySelectorAll('.rise');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: .12 });
    rises.forEach(function (el) { io.observe(el); });
  } else {
    rises.forEach(function (el) { el.classList.add('in'); });
  }

  // --- lightbox ---
  var lb = document.querySelector('.lb');
  if (lb) {
    var lbImg = lb.querySelector('img');
    document.querySelectorAll('.gal img').forEach(function (img) {
      img.addEventListener('click', function () {
        lbImg.src = img.currentSrc || img.src;
        lbImg.alt = img.alt;
        lb.classList.add('on');
        document.body.style.overflow = 'hidden';
      });
    });
    var close = function () { lb.classList.remove('on'); document.body.style.overflow = ''; };
    lb.addEventListener('click', close);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  }

  // --- reels ---
  // El <video> ya esta en el HTML con poster; solo se le asigna el src cuando
  // entra en pantalla, asi la portada no paga los megas de entrada.
  // Dentro de un iframe (y en iOS) el navegador puede bloquear el autoplay aun
  // con el video en silencio: en ese caso NO se deja el poster congelado y
  // mudo, se muestra un boton de play y cualquier toque sobre la tarjeta lo
  // arranca, que es un gesto del usuario y siempre esta permitido.
  var reels = document.querySelectorAll('.reel');
  if (reels.length) {

    var arrancar = function (fig) {
      var v = fig.querySelector('video');
      if (!v) return;
      if (!v.src) v.src = fig.dataset.src;          // descarga diferida
      var p = v.play();
      if (p && p.then) {
        p.then(function () { fig.classList.remove('blocked'); })
         .catch(function () { fig.classList.add('blocked'); });  // muestra el boton
      }
    };

    if ('IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) arrancar(e.target);
          else {
            var v = e.target.querySelector('video');
            if (v && !v.paused) v.pause();
          }
        });
      }, { threshold: .3 });
      reels.forEach(function (r) { obs.observe(r); });
    } else {
      reels.forEach(arrancar);
    }

    reels.forEach(function (fig) {
      var v = fig.querySelector('video');
      if (!v) return;
      v.addEventListener('playing', function () {
        fig.classList.add('playing');
        fig.classList.remove('blocked');
      });

      // tocar la tarjeta: arranca si esta frenado, y si ya corre alterna el sonido
      fig.addEventListener('click', function () {
        if (v.paused) { arrancar(fig); return; }
        sonido(fig, v);
      });
    });

    function sonido(fig, v) {
      var encender = v.muted;
      document.querySelectorAll('.reel').forEach(function (o) {
        var ov = o.querySelector('video');
        if (ov) { ov.muted = true; }
        o.classList.remove('loud');
      });
      v.muted = !encender;
      fig.classList.toggle('loud', encender);
      if (encender && v.paused) v.play().catch(function () {});
    }

    document.querySelectorAll('.reel .snd').forEach(function (btn) {
      btn.addEventListener('click', function (ev) {
        ev.stopPropagation();
        var fig = btn.closest('.reel');
        var v = fig.querySelector('video');
        if (!v) return;
        if (v.paused) arrancar(fig);
        sonido(fig, v);
      });
    });

    document.querySelectorAll('.reel .playbtn').forEach(function (btn) {
      btn.addEventListener('click', function (ev) {
        ev.stopPropagation();
        arrancar(btn.closest('.reel'));
      });
    });
  }

  // --- formulario ---
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
          // si el email falla, la consulta no se pierde: se abre WhatsApp
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
    var lines = [form.dataset.msgIntro || 'Hola, quiero consultar por una reserva.', ''];
    [['nombre', 'lName'], ['servicio', 'lService'], ['desde', 'lFrom'],
     ['hasta', 'lTo'], ['personas', 'lGuests'], ['mensaje', 'lMsg']]
      .forEach(function (p) {
        var v = d.get(p[0]);
        if (v) lines.push((form.dataset[p[1]] || p[0]) + ': ' + v);
      });
    return 'https://wa.me/' + (form.dataset.phone || '') + '?text=' + encodeURIComponent(lines.join('\n'));
  }
})();
