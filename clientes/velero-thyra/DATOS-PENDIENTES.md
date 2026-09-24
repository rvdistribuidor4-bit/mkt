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

Puesto en la demo como un 42 pies típico. Confirmar con el dueño:

- [x] Eslora: 42 pies *(dato real)*
- [ ] Camarotes: la demo dice 3 dobles
- [ ] Pasajeros: la demo dice 6 máximo
- [ ] Baños: la demo dice 2 + ducha
- [ ] Marca, modelo y año del velero
- [ ] Nombre del capitán y una línea sobre él
- [ ] ¿Hay tripulación además del capitán?

## 4. Fotos reales — **lo más importante**

Las 10 imágenes de `web/img/` son **generadas, de referencia**. Sirven para que
el dueño vea la web funcionando; **no para publicar**. Si un huésped reserva
viendo un barco que no es el Thyra, son reseñas destruidas y reclamo por
publicidad engañosa.

Reemplazar respetando el nombre de archivo:

| Archivo | Qué foto va | Mínimo |
|---|---|---|
| `hero.jpg` | **La más importante.** Thyra fondeado junto a una isla, drone, hora dorada | 1920×1080 |
| `cabina.jpg` | Camarote doble hecho, con luz natural | 1200×800 |
| `cubierta.jpg` | Bañera y cubierta con el mar de fondo | 1200×800 |
| `navegando.jpg` | Thyra a vela, desde otra embarcación o drone | 1400×900 |
| `snorkel.jpg` | Bajo el agua: coral, peces | 1200×800 |
| `comida.jpg` | Un almuerzo real servido a bordo | 1200×800 |
| `isla.jpg` | Isla desierta de San Blas, aérea si se puede | 1400×900 |
| `atardecer.jpg` | Thyra fondeado al anochecer con luces | 1400×900 |
| `pesca.jpg` | Caña, captura del día | 1200×800 |
| `molas.jpg` | Molas compradas en la comunidad | 1200×800 |

> Si el dueño no tiene foto aérea, **vale la pena pagar un drone una tarde**. El
> hero es la imagen que decide si alguien sigue leyendo.

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
los dos HTML. Es el aviso de que las fotos y precios son de referencia.

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
