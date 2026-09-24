# Datos pendientes — Velero San Blas

Todo lo que hay que pedirle al dueño antes de publicar. El sitio ya está armado
y funcionando; sin estos datos no se puede poner online.

## 1. Reemplazos de texto (buscar y reemplazar en los 2 HTML)

| Buscar | Reemplazar por | Dónde aparece |
|---|---|---|
| `«Nombre del velero»` | Nombre real del barco | title, header, hero, footer, JSON-LD |
| `507XXXXXXXX` | WhatsApp con código de país, **sin + ni espacios** (ej. `50761234567`) | links de WhatsApp, botón flotante, `data-phone` del form |
| `https://tudominio.com` | Dominio real | canonical, hreflang, Open Graph, JSON-LD |
| `AIRBNB-URL` | Link al anuncio de Airbnb | botón "Ver anuncio", footer |
| `US$ XXX` | Precios reales de cada servicio | 3 tarjetas de servicio |
| `US$ XX` | Tasa de ingreso a Guna Yala | sección "No incluido" |

Comando para verificar que no quedó ninguno:

```bash
grep -rn "«Nombre del velero»\|507XXXXXXXX\|tudominio.com\|AIRBNB-URL\|US\$ XX" web/
```

## 2. Datos del barco (ficha técnica)

- [ ] Eslora (pies)
- [ ] Cantidad de camarotes
- [ ] Capacidad máxima de pasajeros
- [ ] Cantidad de baños
- [ ] Tipo y año del barco
- [ ] Nombre del capitán y una línea sobre él
- [ ] Calificación promedio y cantidad de reseñas (para el hero)

## 3. Fotos reales — **obligatorias, sin excepción**

Los 15 archivos en `web/img/` son placeholders que dicen qué foto va en cada lugar.
Hay que reemplazarlos **respetando el nombre del archivo**.

| Archivo | Qué foto va | Tamaño mínimo |
|---|---|---|
| `hero-velero.jpg` | El velero fondeado frente a una isla, hora dorada | 1920×1080 |
| `cabina.jpg` | Camarote doble hecho, con luz natural | 800×600 |
| `day-charter.jpg` | Pasajeros navegando, velas arriba | 800×600 |
| `charter-privado.jpg` | Grupo disfrutando el barco completo | 800×600 |
| `comida-abordo.jpg` | Plato servido en cubierta | 900×700 |
| `gal-1.jpg` | El velero al atardecer (horizontal, va ancha) | 1400×700 |
| `gal-2.jpg` … `gal-6.jpg` | Agua turquesa, snorkel, cubierta, interior, proa | 800×800 |
| `velero-ficha.jpg` | El barco navegando con vela desplegada | 900×700 |
| `act-snorkel.jpg` | Bajo el agua: coral, peces | 800×600 |
| `act-pesca.jpg` | Caña, captura del día | 800×600 |
| `act-guna.jpg` | Visita a la comunidad, molas | 800×600 |

> **Regla firme:** solo fotos reales de **este** barco. Nada de bancos de imágenes
> ni de IA para mostrar el velero, los camarotes o las comidas. Si el huésped
> llega y el barco no es el de la foto, son reseñas destruidas y reclamos por
> publicidad engañosa. La IA sí sirve para el mapa ilustrado de cómo llegar,
> íconos y piezas de Instagram.

**Foto de la comunidad guna:** solo con permiso de las personas retratadas.

## 4. Reseñas

Copiar textual 3 reseñas reales de Airbnb o Google, con nombre, país y fecha.
**Nunca inventarlas** — Airbnb las muestra públicamente y se verifica en dos clics.

## 5. Textos que solo puede dar el dueño

- [ ] Descripción del barco (2–3 frases, sección "El velero")
- [ ] **Formas de pago** aceptadas (FAQ) — esta pregunta sin responder hace perder reservas
- [ ] **Política de cancelación**, incluido el caso de mal tiempo (FAQ)
- [ ] Qué incluye/no incluye, si difiere de lo que está cargado

## 6. Opcional: recibir las consultas por email

Hoy el formulario arma un mensaje de WhatsApp con todos los datos cargados
(funciona sin backend y sin costo). Para recibir además por email:

1. Crear un formulario gratuito en [formspree.io](https://formspree.io)
2. Agregar el endpoint al `<form>` en los dos HTML:

```html
<form class="form" data-endpoint="https://formspree.io/f/XXXXXXX" ...>
```

Si el email falla, el script abre WhatsApp igual: la consulta no se pierde.

## 7. Publicación

El sitio es estático: se sube a Vercel, Netlify o Cloudflare Pages
apuntando a la carpeta `web/`. Sin build, sin servidor, sin costo de hosting.
