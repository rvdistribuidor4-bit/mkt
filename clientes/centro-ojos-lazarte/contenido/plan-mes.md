# Plan de contenido IG — Centro de Ojos Lazarte

> ⏸️ **PAUSADO — Windsor pasó a plan pago (25/09/2026).** La rutina automática
> está desactivada. Los 10 posts pendientes se cargan a mano en Meta Business
> Suite siguiendo `PUBLICAR-A-MANO.md`, y las placas que antes salían de Canva
> ya están descargadas en `ig/`. Para volver al modo automático, sin costo:
> `MIGRACION-META-API.md`.

**Modo autónomo.** Cadencia Lun/Mié/Vie 10:00 ART. La rutina corre
`operativo/publicar_ig.py --proximo`, que toma el **primer bloque con
`estado: PENDIENTE`**, lo publica por la API de Meta, agrega el comentario de
WhatsApp y marca el bloque como PUBLICADO con su `media_id`.

**Formato de cada bloque** — el script lo parsea, así que respetarlo:

```
### N · Título
**estado: PENDIENTE**
IMG: <url pública de la imagen>
CAPTION:
```‌(bloque de código con el texto tal cual va)```‌
```

⚠️ **`IMG` tiene que ser una URL pública.** Meta no acepta que le subas un
archivo. Por eso las placas viven en el repo y se sirven desde
`raw.githubusercontent.com`, **y la rama `main` tiene que tenerlas**.

Cuenta de Instagram: `17841414497159496`. Token: `META_IG_TOKEN` en el entorno.
**Cumplimiento:** sin promesas de resultado ni superlativos; disclaimer en temas
médicos.

---

### 1 · Hábitos frente a las pantallas (carrusel)
**estado: PUBLICADO (2026-09-23 · media_id 18078993317356407 · comentario WA OK)**
SPEC: `export-design DAHUk0p5o8k jpg` → carrusel `create_carousel_post` image_urls =

[ `https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/2026-09-22-portada-habitos.jpg`, urls[10], urls[13], urls[14], urls[12], urls[11], urls[16] ].
CAPTION:
```
Muchas horas frente a la pantalla le pasan factura a tu vista 👀

5 hábitos simples para cuidarla:
1️⃣ Regla 20-20-20: cada 20 min, mirá 20 segundos algo a 6 metros
2️⃣ Cuidá la distancia a la pantalla
3️⃣ Descansá la mirada con pausas
4️⃣ Trabajá con buena luz
5️⃣ No te frotes los ojos

Pequeños cambios, gran diferencia para tu salud visual.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #pantallas #cuidadodelavista #centrodeojoslazarte
```

### 2 · Consejo: cuidá tus ojos del sol (placa)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-sol.jpg
CAPTION:
```
El sol también afecta tus ojos ☀️👓

Usá anteojos de sol adecuados cuando corresponda: cuidan tus ojos de la radiación, no son solo estética.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #cuidadodelavista #centrodeojoslazarte
```

### 12 · Así es la clínica (carrusel institucional)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-clinica-1-portada.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-clinica-2-admision.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-clinica-3-espera.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-clinica-4-consultorio.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-clinica-5-equipos.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-clinica-6-cierre.jpg
CAPTION:
```
¿Nunca viniste? Mirá dónde vas a estar 👁️

Sabemos que ir al oftalmólogo por primera vez da un poco de cosa: no sabés cómo es el lugar, ni con qué te vas a encontrar. Así que te lo mostramos.

Admisión, sala de espera, consultorios y el equipamiento para estudios de alta complejidad — todo en el mismo lugar donde te atendés.

Dos sedes en el centro de Córdoba:
📍 Deán Funes 614 (centro integral)
📍 9 de Julio 778 (consultorios externos)

Atendemos PAMI, obras sociales y particulares.
Más de 35 años cuidando la vista de los cordobeses.

📲 Turnos y consultas por WhatsApp — link en la bio

#oftalmología #córdoba #saludvisual #centrodeojoslazarte #cirugíadecataratas
```

### 3 · Dr. Armando Lazarte (institucional)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-dr-lazarte.jpg
CAPTION:
```
Detrás de cada consulta hay un equipo que te acompaña 💙

La dirección médica está a cargo del Dr. Armando Lazarte, con más de 35 años de trayectoria dedicados a la oftalmología y la cirugía de cataratas en Córdoba. Trato cercano, escucha y acompañamiento en cada paso.

📍 Deán Funes 614 · 9 de Julio 778 — Córdoba

#oftalmología #cirugíadecataratas #córdoba #centrodeojoslazarte
```

### 4 · Síntoma: ¿tenés el ojo rojo? (placa)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-ojo-rojo.jpg
CAPTION:
```
¿Tenés el ojo rojo? 👁️

Puede ser algo pasajero… o una señal de que algo necesita atención. Si persiste, o aparece con dolor o cambios en la visión, consultá.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #centrodeojoslazarte
```

### 13 · Trayectoria en números (carrusel)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-tray-1-portada.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-tray-2-numeros.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-tray-3-quirofano.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-tray-4-referencia.jpg, https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-tray-5-cierre.jpg
CAPTION:
```
200 cirugías de cataratas por mes 👁️

No es una cifra de folleto. Es lo que hacemos, todos los meses, desde hace más de tres décadas.

Desde 1990:
▸ 15.000+ cirugías realizadas
▸ 3.000+ pacientes por año
▸ 40+ personas en el equipo
▸ Quirófano propio e internación ambulatoria

Consulta, estudios y cirugía en la misma institución. No derivamos a otro lado.

Somos centro de referencia para todo el norte de Córdoba: recibimos pacientes derivados de otros centros, obras sociales y médicos de familia.

Dirección médica: Dr. Armando Lazarte.

📲 Turnos y consultas por WhatsApp — link en la bio
📍 Deán Funes 614 · 9 de Julio 778 — Córdoba

#cirugíadecataratas #oftalmología #córdoba #centrodeojoslazarte
```

### 5 · Control oftalmológico anual (placa)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-control-anual.jpg
CAPTION:
```
Ver bien no siempre significa que esté todo bien 👀

Muchas enfermedades de los ojos no dan síntomas al principio. Un control al año ayuda a detectarlas a tiempo. Si hace más de un año que no controlás tu vista, este es un buen momento.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #controloftalmológico #centrodeojoslazarte
```

### 6 · Consejo: no te automediques (placa)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-no-automedicarse.jpg
CAPTION:
```
¿Molestia en los ojos? No uses gotas por tu cuenta 🚫💧

Cada ojo es diferente y no todas las gotas sirven para lo mismo. Ante una molestia que persiste, consultá antes de automedicarte.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #centrodeojoslazarte
```

### 7 · Obras sociales (placa CTA)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-obras-sociales.jpg
CAPTION:
```
Trabajamos con tu obra social 💙

PAMI, OSDE, APROSS, Swiss Medical, Galeno y muchas más. Consultanos por tu cobertura y coordiná tu turno.

📍 Deán Funes 614 · 9 de Julio 778 — Córdoba

#obrasociales #oftalmología #córdoba #centrodeojoslazarte
```

### 8 · Síntoma: ¿te duele el ojo? (placa)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-dolor-ojo-foto.jpg
CAPTION:
```
¿Te duele el ojo? 👁️

El dolor ocular no debería ignorarse, sobre todo si es intenso o aparece junto con cambios en la visión. Ante la duda, consultá.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #centrodeojoslazarte
```

### 11 · Día de la Madre (placa especial)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-dia-madre.jpg
CAPTION:
```
Este domingo es el Día de la Madre 💛

A todas las mamás que cuidan a los suyos cada día: gracias. Que no falte quien cuide de ustedes… ni de su visión. ¡Feliz día!

📍 Centro de Ojos Lazarte — Córdoba

#diadelamadre #córdoba #centrodeojoslazarte
```

---

## Historias (requieren material del usuario)
Cuando haya fotos/videos reales (día de cirugía, testimonios, equipo), se arman
historias específicas. El publicador **no** genera historias solo: las pide al usuario.
### 9 · Consejo: no ignores los cambios repentinos (placa)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-cambios-vision-foto.jpg
CAPTION:
```
Si tu visión cambia de golpe, no lo dejes pasar ⚠️👀

Los cambios repentinos en la visión merecen atención. Consultá con un profesional cuanto antes.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #centrodeojoslazarte
```

### 10 · Tu visión merece un control (placa CTA)
**estado: PENDIENTE**
IMG: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/clientes/centro-ojos-lazarte/contenido/ig/placa-vision-control.jpg
CAPTION:
```
Tu visión merece un control 💙

Ver bien también es cuidar tu calidad de vida. Si hace tiempo que no controlás tu vista, escribinos y coordinamos tu turno.

📍 Centro de Ojos Lazarte — Córdoba
ℹ️ Información general, no reemplaza una consulta.

#saludvisual #oftalmología #córdoba #centrodeojoslazarte
```

