# Datos pendientes — Thyra

La web **es una demo de presentación**. Esto es lo que hace falta para
convertirla en el sitio real y publicable.

## 1. Reemplazos de texto (los dos HTML)

| Buscar | Reemplazar por |
|---|---|
| `507XXXXXXXX` | WhatsApp con código de país, **sin + ni espacios** (ej. `50761234567`) |
| `https://tudominio.com` | Dominio real |
| `AIRBNB-URL` | Link al anuncio de Airbnb |

Verificar que no quedó ninguno:

```bash
grep -rn "507XXXXXXXX\|tudominio.com\|AIRBNB-URL" web/
```

## 2. Precios — hoy son de ejemplo

Los de la demo están puestos según valores de mercado de San Blas, **no son los
del dueño**:

| Experiencia | En la demo | Real |
|---|---|---|
| Noche a bordo | US$165 pp/noche | ☐ |
| Paseo de día | US$135 pp/día | ☐ |
| Charter privado | US$980 /día barco entero | ☐ |
| Tasa de Guna Yala | (no especificada) | ☐ |

Aparecen en: hero, barra fija de móvil, tres tarjetas de experiencias.

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

**Regla que ya se cumple: todo lo que muestra el Thyra es una foto real del
Thyra.** Ninguna imagen generada muestra el barco.

### Ya incorporadas (reales)

| Archivo | Qué es | Dónde se usa |
|---|---|---|
| `real-aerea-hq.jpg` | Aérea del Thyra fondeado sobre el arrecife | Hero + galería |
| `real-banera.jpg` | Bañera con toldo, timón de madera | Paseo de día + galería |
| `real-camarote-proa.jpg` | Camarote de proa con claraboya | Noche a bordo |
| `real-camarote-molas.jpg` | Cucheta con molas en el revestimiento | Sección El velero |
| `real-salon.jpg` | Salón completo | Charter privado |

> ⚠️ **La aérea llegó a 591 px y se escaló 2× a 1182 px.** El escalado respetó
> el encuadre y no inventó nada, pero **conviene pedir el original en alta
> resolución**: es la imagen que decide si alguien sigue leyendo.

### Todavía de referencia (generadas, no muestran el barco)

| Archivo | Qué reemplazar por |
|---|---|
| `snorkel.jpg` | Snorkel real en San Blas: coral, peces |
| `isla.jpg` | Una isla del archipiélago donde fondea el Thyra |
| `comida.jpg` | Un almuerzo real servido a bordo |
| `pesca.jpg` | La caña, o la captura del día |
| `molas.jpg` | Molas compradas en la comunidad |

### Fotos que faltan y suman mucho

- [ ] **Thyra navegando a vela**, desde otra embarcación o drone
- [ ] **Thyra fondeado al atardecer**, con luces encendidas
- [ ] La cocina / galley
- [ ] El capitán a bordo

**Foto de comunidad guna:** solo con permiso de las personas retratadas.

## 5. Reseñas

Tres reales de Airbnb o Google, textuales, con nombre, país y mes.
Las de la demo dicen "reseña de ejemplo" a propósito: **nunca inventarlas.**

## 6. Textos que solo puede dar el dueño

- [ ] **Formas de pago** (FAQ) — sin esto se pierden reservas
- [ ] **Política de cancelación**, incluido mal tiempo (FAQ)
- [ ] Confirmar qué incluye y qué no
- [ ] Mínimo de noches (la demo dice 2)
- [ ] Temporada: ¿opera todo el año?

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
