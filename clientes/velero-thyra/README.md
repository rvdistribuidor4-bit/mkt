# Thyra — Velero en San Blas, Panamá

Velero de 42 pies con base en las islas de San Blas (Guna Yala), Panamá.
Tres servicios: **alojamiento a bordo** (tipo Airbnb), **paseos de día** y
**charters privados**, más actividades (snorkel, pesca, visita a comunidad guna).

## Estado

| Pieza | Estado |
|---|---|
| Landing bilingüe EN/ES | 🟢 Demo terminada |
| Fotos del barco | 🟢 Reales (5) |
| Fotos de entorno | 🟡 De referencia — snorkel, isla, comida, pesca |
| Precios y reseñas | 🟡 De ejemplo |
| Dominio y hosting | 🔴 Sin definir |
| Instagram | ⚪ No iniciado |

## Estructura

```
velero-thyra/
├── web/
│   ├── index.html       ← landing EN
│   ├── es/index.html    ← landing ES
│   ├── css/styles.css   ← sistema visual completo
│   ├── js/main.js       ← menú, scroll, animaciones, galería, formulario
│   └── img/             ← 10 imágenes de referencia + favicon
├── ESTRATEGIA.md        ← ⭐ análisis: por qué la web está armada así
├── DATOS-PENDIENTES.md  ← ⭐ qué falta para publicar
└── contenido/ · marca/  ← plan IG y blog (pendiente)
```

## En una línea

La competencia de San Blas vende itinerarios; esta web vende **un día de tu
vida** — y apalanca la única ventaja que Thyra tiene y no se puede copiar:
**seis pasajeros, no sesenta**. El análisis completo está en `ESTRATEGIA.md`.

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
