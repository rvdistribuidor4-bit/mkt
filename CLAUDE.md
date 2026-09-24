# Reglas de trabajo — repo MKT

Instrucciones para cualquier sesión que trabaje en este repositorio.

---

## 💰 Generación de imágenes, video y voz: CONSULTAR ANTES

**Regla firme: antes de generar cualquier imagen, video o audio pago, decir qué
herramienta se piensa usar y cuánto sale, y esperar confirmación.**

No generar "para probar". No generar varias variantes sin avisar. El costo lo
paga el usuario y la decisión de gastar es suya.

### Precios relevados (septiembre 2026)

**Imágenes — el AI Gateway de Vercel es de 2 a 8 veces más barato que ElevenLabs
para el mismo modelo.** Verificar siempre contra
`https://ai-gateway.vercel.sh/v1/models`, que trae los precios en vivo.

| Modelo | Vía ElevenLabs | Vía Gateway Vercel |
|---|---|---|
| Seedream 5 Pro | US$0,298 | **US$0,035** |
| Gemini 3.1 Flash Image | US$0,148 | **US$0,067** |
| **Flux 1.1 Pro** (`bfl/flux-pro-1.1`) | — | **US$0,04** |
| Flux 1.1 Ultra | — | US$0,06 |
| Flux Kontext Pro (editar imagen) | — | US$0,04 |
| Recraft 4.1 Flash | — | US$0,007 |
| Muse Image 1.0 | — | US$0,01 |

**Por defecto, para imágenes: usar Flux por el gateway de Vercel.** Es lo que el
usuario tiene contratado y es de las opciones más económicas con buena calidad.

**Ir a ElevenLabs solo cuando aporta algo que el gateway no tiene**, y avisando:
- Escalado de imagen (`topaz-image-upscale`, ~US$0,18)
- Voz / TTS (~US$0,03 por 6 s con `eleven_multilingual_v2`)
- Video generativo (caro: Veo 3.1 Fast ~US$2,65 por 8 s)
- Transcripción y edición sobre un flujo ya armado

### Antes de gastar, preguntarse

1. ¿Hace falta generar, o ya hay material real del cliente?
2. ¿El gateway de Vercel lo hace más barato?
3. ¿Cuántas variantes hacen falta de verdad? (`generations_count=1` salvo que se
   pidan opciones)
4. ¿El usuario lo aprobó?

Casi todos los modelos de imagen aceptan `estimate_only` para cotizar sin gastar.

---

## 📸 Material de los clientes

**Todo lo que muestra el producto real del cliente tiene que ser material real
del cliente.** Nada de imágenes generadas ni de banco para mostrar un barco, un
consultorio o un plato que el cliente va a entregar. Si el visitante reserva
viendo algo que no existe, son reseñas destruidas y publicidad engañosa.

Las imágenes generadas sí sirven para: ilustraciones educativas (lo que no se
puede fotografiar), entorno genérico, mapas, íconos y placas.

Cuando se use material de referencia, **marcarlo en la pieza** y listarlo en el
`DATOS-PENDIENTES.md` del cliente.

**Personas identificables**: no van a una web pública sin consentimiento
por escrito. Ante la duda, recortar o descartar.

---

## 🔌 Herramientas conectadas

| Servicio | Para qué | Nota |
|---|---|---|
| **AI Gateway de Vercel** | Texto e **imágenes** | Sin API key: el proxy inyecta credenciales. Free tier bloquea algunos modelos premium |
| **ElevenLabs** | Voz, video, upscale, edición | Caro para imágenes; conviene solo por lo que el gateway no cubre |
| **Windsor.ai** | Instagram, Facebook, GA4, Search Console | Admite **varias cuentas por conector**: no hay que desconectar una para agregar otra |
| **GitHub** | Repo `rvdistribuidor4-bit/mkt` | Rama de trabajo: `claude/admiring-wozniak-ej55eh` |

---

## 🧱 Cómo se arman los sitios

HTML estático, CSS propio, JS sin dependencias. Sin build, sin frameworks.
Cargan rápido con mala conexión y se publican en Vercel o Netlify apuntando a
la carpeta `web/`.

**Verificar siempre en Chromium real antes de entregar**: sin errores de
consola, sin 404, sin scroll horizontal en móvil (390 px) y con las imágenes
lazy disparadas.

```bash
# El Chromium del contenedor está en:
/opt/pw-browsers/chromium-1194/chrome-linux/chrome   # usar --no-sandbox
```

⚠️ Ese Chromium **no trae códecs H.264**, así que los MP4 no se reproducen en
las pruebas. La lógica de video se valida con un WebM temporal.

---

## 🗂 Estructura

```
clientes/<cliente>/
├── web/          ← sitio estático
├── contenido/    ← planes de IG y blog
├── marca/        ← paleta, logo, línea visual
├── README.md     ← estado y decisiones
└── DATOS-PENDIENTES.md  ← qué falta pedirle al cliente
```

Cada cliente nuevo va como carpeta dentro de `clientes/` y se suma a la tabla
del `README.md` de la raíz.
