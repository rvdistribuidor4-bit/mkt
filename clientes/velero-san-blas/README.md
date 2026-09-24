# Velero San Blas — Panamá

Cliente de turismo náutico. Velero con base en las islas de San Blas (Guna Yala),
Panamá. El dueño ofrece tres servicios: **alojamiento a bordo** (tipo Airbnb),
**paseos de día** y **charters privados**, más actividades (snorkel, pesca,
visita a comunidad guna).

## Estado

| Pieza | Estado |
|---|---|
| Landing bilingüe EN/ES | 🟡 Armada, faltan datos reales |
| Fotos | 🔴 Placeholders — ver `DATOS-PENDIENTES.md` |
| Dominio y hosting | 🔴 Sin definir |
| Instagram | ⚪ No iniciado |

## Estructura

```
velero-san-blas/
├── web/
│   ├── index.html       ← landing EN (mercado principal)
│   ├── es/index.html    ← landing ES
│   ├── css/styles.css   ← hoja única, compartida
│   ├── js/main.js       ← menú, galería, formulario
│   └── img/             ← 15 placeholders + favicon
├── contenido/           ← plan de Instagram y blog (pendiente)
├── marca/               ← paleta y logo (pendiente)
└── DATOS-PENDIENTES.md  ← ⭐ lo que hay que pedirle al dueño
```

## Decisiones tomadas

**Bilingüe desde el arranque.** El turismo de San Blas es mayormente de EEUU,
Canadá y Europa, pero también hay mercado panameño y latino. Las dos versiones
se enlazan con `hreflang`, así Google sirve la correcta según el país.

**Una sola landing por idioma, no un sitio multipágina.** Convierte mejor y se
publica antes. Si más adelante hace falta SEO de cola larga, se abren páginas
separadas por servicio.

**Tres canales de reserva conviviendo:**
- **WhatsApp** — el que más convierte y no paga comisión. Botón flotante siempre visible.
- **Formulario** — arma un mensaje de WhatsApp con fechas y cantidad de personas ya cargadas. Sin backend. Opcionalmente envía por email vía Formspree.
- **Airbnb** — el anuncio existente, que aporta las reseñas y la confianza.

**"Cómo llegar" tiene sección propia.** Es la duda número uno de todo turista de
San Blas (4x4 desde Ciudad de Panamá, puerto de Cartí, tasas gunas). Quien la
responde bien se queda con la reserva.

## Paleta

| Rol | HEX |
|---|---|
| Azul profundo (fondos oscuros) | `#062B3E` |
| Azul medio | `#0B3D56` |
| Turquesa caribe (acento, CTA) | `#18A9A5` |
| Turquesa oscuro (hover) | `#0F8580` |
| Arena (fondos alternos) | `#F3E9DA` |
| Texto sobre claro | `#10222C` |

## Reglas de contenido

- **Solo fotos reales del barco.** Nada de bancos de imágenes ni IA para mostrar
  el velero, camarotes o comidas: el huésped llega y compara.
- **Reseñas textuales**, nunca inventadas.
- **Precios claros** y qué no está incluido, para evitar reclamos en el muelle.
- Las fotos de comunidades gunas, solo con permiso de las personas retratadas.

## Probar en local

```bash
cd web && python3 -m http.server 8099
# http://localhost:8099/index.html  (EN)
# http://localhost:8099/es/index.html  (ES)
```

## Verificado

Probado en Chromium a 1280px y 390px: sin errores de consola, sin scroll
horizontal en móvil, menú y selector de idioma funcionando, y el formulario
captura correctamente nombre, servicio, fechas y cantidad de personas.
