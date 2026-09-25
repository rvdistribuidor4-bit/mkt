# Thyra — Velero en San Blas, Panamá

Velero de 42 pies con base en las islas de San Blas (Guna Yala), Panamá.
Tres servicios: **alojamiento a bordo** (tipo Airbnb), **paseos de día** y
**charters privados**, más actividades (snorkel, pesca, visita a comunidad guna).

## Estado

| Pieza | Estado |
|---|---|
| Landing bilingüe EN/ES | 🟢 Demo terminada |
| Fotos del barco | 🟢 Reales (10) |
| Fotos de entorno | 🟡 Solo `pesca.jpg` sigue siendo generada |
| Videos | 🟢 4 clips reales, con carga diferida |
| Precios | 🟡 Propuesta con auditoría de mercado, a validar |
| Reseñas | 🟡 De ejemplo |
| Cobro en USD | 🔴 Falta abrir cuenta |
| Dominio y hosting | 🔴 Sin definir |
| Instagram | 🟡 Carrusel + reel en video listos (`contenido/ig/`) |

## Estructura

```
velero-thyra/
├── web/
│   ├── index.html       ← landing EN
│   ├── es/index.html    ← landing ES
│   ├── css/styles.css   ← sistema visual completo
│   ├── js/main.js       ← menú, scroll, animaciones, galería, reels, formulario
│   ├── img/             ← 12 fotos reales + 1 de referencia + posters
│   └── vid/             ← 4 clips verticales (2,9 MB, carga diferida)
├── ESTRATEGIA.md        ← ⭐ análisis: por qué la web está armada así
├── PRECIOS-Y-COBRO.md   ← ⭐ auditoría de mercado, precios, cancelación y cobro
├── PLAN-CAPTACION.md    ← ⭐ cómo llegar a una reserva por semana, canal por canal
├── DATOS-PENDIENTES.md  ← ⭐ qué falta para publicar
└── contenido/
    └── ig/              ← carrusel (4 placas), reel en video, textos y las fuentes para regenerarlos
```

## En una línea

La competencia de San Blas vende itinerarios; esta web vende **un día de tu
vida** — y apalanca la única ventaja que Thyra tiene y no se puede copiar:
**cinco pasajeros, no cincuenta**. El análisis completo está en `ESTRATEGIA.md`.

## Paleta

| Rol | HEX |
|---|---|
| Azul abismo | `#04212E` |
| Azul profundo | `#0A3D4D` |
| Turquesa laguna (CTA) | `#3FC1B0` |
| Latón (detalles) | `#C08A4E` |
| Arena | `#F2E7D5` |
| Papel | `#FBF8F3` |

Tipografía: **Fraunces** (titulares) + **Inter** (texto), vía Google Fonts.

## Probar en local

```bash
cd web && python3 -m http.server 8100
# http://localhost:8100/index.html     (EN)
# http://localhost:8100/es/index.html  (ES)
```

## Verificado

Chromium a 1440px y 390px: sin 404, sin errores de consola, sin scroll
horizontal en móvil. Header sólido al bajar, animaciones de entrada,
lightbox, CTA fijo en móvil y selector de idioma, todos operativos.
Las 10 imágenes pesan 2 MB en total (23 MB originales, optimizadas al 8%).
