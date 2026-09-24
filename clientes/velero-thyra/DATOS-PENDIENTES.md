# Datos pendientes — Thyra

La web **es una demo de presentación**. Esto es lo que hace falta para
convertirla en el sitio real y publicable.

## 1. Reemplazos de texto (los dos HTML)

| Buscar | Reemplazar por |
|---|---|
| `https://tudominio.com` | Dominio real |
| `AIRBNB-URL` | Link al anuncio de Airbnb |

**Contactos ya cargados:**

| Quién | WhatsApp | Uso |
|---|---|---|
| **Fabio** (dueño) | +54 9 3548 63-5569 | ✅ Número público de la web: botón flotante, CTAs y formulario |
| **Leo** (capitán) | +507 6921-3447 | Interno / post-reserva. Aparece nombrado en la web, sin número |

> **Por qué Fabio y no Leo en la web.** El turista escribe de madrugada desde
> Europa o EEUU. Si ese mensaje cae en un teléfono fondeado en San Blas sin
> señal, la respuesta llega dos días tarde y la reserva se perdió. Fabio tiene
> señal estable. Leo aparece **por nombre** en la sección del velero, que es lo
> que humaniza, y su número se pasa una vez confirmada la reserva.
> Si el dueño prefiere al revés, es cambiar una variable.

Verificar que no quedó ninguno:

```bash
grep -rn "507XXXXXXXX\|tudominio.com\|AIRBNB-URL" web/
```

## 2. Precios — propuesta con auditoría de mercado

Ver **`PRECIOS-Y-COBRO.md`**: relevamiento de la competencia, los tres precios
propuestos y por qué. Resumen:

| Experiencia | Propuesto | Barco lleno (5) |
|---|---|---|
| Día completo (12 h) | US$120 pp | US$600 |
| Noche a bordo | US$150 pp/noche | US$750 |
| Barco entero | US$750/día | — |

- [ ] **Que el dueño valide los tres precios y el piso de 3 pasajeros para salir**
- [ ] Confirmar la tasa de Guna Yala vigente (relevada: US$22 pp)
- [ ] Confirmar el costo del traslado 4x4 que cobra su proveedor

## 3. Ficha del barco — confirmar

⚠️ **Las fotos contradicen parte de lo que supuse.** El salón tiene camas a los
lados, así que la distribución **no** son tres camarotes cerrados con puerta.
Por eso la web ya no afirma "3 dobles" ni "cada camarote tiene puerta": dice
"3 camarotes" y la FAQ invita a consultar qué cuchetas toca según el grupo.
Hay que cerrar esto con el dueño antes de publicar.

- [x] Eslora: 42 pies *(dato del dueño)*
- [ ] **Distribución real**: ¿cuántos camarotes cerrados y cuántas plazas en el salón?
- [ ] Pasajeros máximo: la demo dice 6
- [ ] Baños: la demo dice 2 + ducha
- [ ] Marca, modelo y **año** — es un clásico de madera, y el año suma valor
- [ ] Nombre del capitán y una línea sobre él
- [ ] ¿Hay tripulación además del capitán?

## 4. Fotos

**Regla que se cumple: todo lo que muestra el Thyra es una foto real del Thyra.**
10 fotos reales, 2 de referencia, y ninguna de las dos muestra el barco.

### Reales, ya incorporadas

| Archivo | Qué es | Dónde se usa |
|---|---|---|
| `real-aerea-hq.jpg` | Aérea sobre el arrecife | Hero |
| `real-navegando.jpg` | El Thyra a vela | Paseo de día |
| `real-atardecer.jpg` | Fondeado al anochecer, con luces | Charter privado |
| `real-camarote-proa.jpg` | Camarote de proa con claraboya | Noche a bordo |
| `real-camarote-molas.jpg` | Cucheta con molas | Sección El velero |
| `real-sunset.jpg` | Silueta contra el atardecer naranja | Galería (destacada) |
| `real-banera.jpg` | Bañera con toldo y timón | Galería |
| `real-salon.jpg` | Salón completo | Galería |
| `real-fondeadero.jpg` | El fondeadero desde cubierta | Galería |
| `real-proa-guna.jpg` | Bandera de Guna Yala en la proa | Comunidad guna |

### Todavía de referencia

| Archivo | Reemplazar por |
|---|---|
| `pesca.jpg` | La caña, o la captura del día — **es la última imagen generada que queda** |

El snorkel ya es real: salió de un fotograma del video del drone.

### Faltan y suman

- [ ] Un almuerzo real servido a bordo
- [ ] La cocina / galley
- [ ] El capitán a bordo

## 4bis. Lo que las fotos revelaron

**Corregido en la web:**

- **El casco es blanco, de fibra.** Yo había escrito "no es un charter de plástico blanco", lo cual era falso. Ahora el copy dice lo que efectivamente pasa: por fuera es un cuarenta y dos pies blanco y prolijo, y abajo es todo teca barnizada y bronce. El contraste funciona mejor que la afirmación equivocada.

**A confirmar con el dueño:**

- [ ] **Marca y modelo.** La vela mayor lleva el logo de Beneteau y el número **331**. Puede ser el modelo, el número de vela, o una vela de segunda mano de otro barco (es común). Confirmar antes de publicarlo en la ficha.
- [ ] **Bandera argentina a bordo.** ¿El capitán es argentino? Si lo es, **es un gancho enorme para el mercado hispano**: un argentino en San Blas vende distinto a un charter anónimo. Vale una línea en la sección del velero.
- [ ] **Dos fotos sin confirmar.** La silueta del atardecer y la del fondeadero podrían no ser el Thyra (en la del fondeadero el cojín rojo en primer plano sugiere que está tomada *desde* el Thyra, y el velero que se ve es otro). Sus textos alternativos son neutros a propósito: no afirman que el barco sea el Thyra. Si lo son, se ajustan en un minuto.

## 4ter. Videos

Cuatro clips verticales, en la sección **Ver / Watch**. Se descargan recién
cuando entran en pantalla (2,9 MB en total, que la portada no paga de entrada),
se reproducen en loop sin sonido y tienen botón para activar el audio.

| Clip | Qué muestra | Peso |
|---|---|---|
| `thyra-drone.mp4` | Isla, arrecife y snorkel desde el aire | 805 KB |
| `thyra-casco.mp4` | El Thyra desde el agua, de proa a popa | 632 KB |
| `thyra-archipielago.mp4` | Aéreas del archipiélago con veleros fondeados | 525 KB |
| `thyra-rio.mp4` | Cayuco río arriba, selva y cascada | 909 KB |

### ⚠️ Consentimiento de las personas filmadas

- **Descarté un tramo** del primer video donde aparece **una mujer claramente
  identificable en primer plano**, durante varios segundos. No va a una web
  pública sin su permiso por escrito. Si lo da, el material está y es bueno.
- En el clip del río **se ve gente caminando y en el cayuco**, mayormente de
  espaldas. Riesgo bajo, pero conviene pedir el OK igual.
- Los demás clips no tienen personas identificables.

### Nota técnica

El Chromium de este contenedor no trae códecs H.264, así que **no pude
reproducir los MP4 acá**. Validé la lógica completa (carga diferida, loop,
pausa al salir de pantalla, botón de sonido) con un archivo WebM: funciona.
Los MP4 son H.264 estándar y reproducen en cualquier navegador real. Probé
generar WebM para servir además, pero con este material pesaban **más** que
los MP4, así que no compensa.

## 5. Reseñas

Tres reales de Airbnb o Google, textuales, con nombre, país y mes.
Las de la demo dicen "reseña de ejemplo" a propósito: **nunca inventarlas.**

## 6. Textos que solo puede dar el dueño

- [x] ~~Formas de pago~~ → propuesta cargada: seña 30% por link, saldo en efectivo USD. **Falta abrir la cuenta** (ver `PRECIOS-Y-COBRO.md`)
- [x] ~~Política de cancelación~~ → propuesta cargada en la FAQ. **Falta que el dueño la apruebe**
- [ ] Confirmar qué incluye y qué no
- [ ] Mínimo de noches (la demo dice 2)
- [ ] Temporada: ¿opera todo el año?
- [ ] ¿El día completo sale desde Cartí o desde dónde? El horario 7–19 asume salida de puerto

## 7. Sacar la marca de demo

Cuando todo lo anterior esté cargado, borrar el bloque `demo-note` del footer en
los dos HTML. Hoy aclara que las fotos del barco son reales pero que arrecife,
isla y comida siguen siendo de referencia, y que precios y reseñas son de ejemplo.

## 8. Publicación

Sitio estático: se sube a Vercel, Netlify o Cloudflare Pages apuntando a `web/`.
Sin build, sin servidor. Conviene dominio propio y el sitio enlazado desde el
perfil de Instagram y el anuncio de Airbnb.

## 9. Opcional: consultas por email

El formulario ya arma el mensaje de WhatsApp con todos los datos. Para recibir
además por email, crear un formulario en [formspree.io](https://formspree.io) y
agregarlo a los dos HTML:

```html
<form class="form" data-endpoint="https://formspree.io/f/XXXXXXX" ...>
```

Si el email falla, abre WhatsApp igual: la consulta no se pierde.
