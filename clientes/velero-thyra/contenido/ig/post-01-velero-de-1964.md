# Pieza demo · Carrusel «Un velero de 1964»

**Formato:** carrusel de 4 placas, 1080 × 1350 px
**Archivos:** `thyra-carrusel-1.jpg` … `thyra-carrusel-4.jpg`
**Fuente editable:** `placas.html` (se re-renderiza y no cuesta nada, ver abajo)
**Costo de producción:** US$0 — HTML renderizado, fotos reales del barco

---

## Por qué este ángulo

Todos los charters de San Blas publican la misma foto: agua turquesa y una
hamaca. Compiten por ver quién tiene el mar más azul, y el mar es el mismo para
todos.

El Thyra tiene algo que ninguno puede copiar: **es un barco de 1964, de casco de
madera, todavía navegando.** Eso frena el scroll porque es raro, es verdadero y
se puede verificar.

Y además resuelve la objeción real del pasajero que duda —*¿me voy a marear?*—
sin nombrarla: **trece toneladas no se zarandean.**

---

## Las cuatro placas

| # | Qué hace | Texto principal |
|---|---|---|
| 1 | Frena el scroll | *Este velero tiene 62 años y sigue cruzando el Caribe* |
| 2 | Da la prueba | 1964 · Madera · 13 t → *Por eso no se zarandea* |
| 3 | Genera deseo | *Caoba y bronce* |
| 4 | Cierra | *5 pasajeros. No 50* · US$120 · WhatsApp |

---

## Texto del posteo (español)

> Sueca, 1964. Madera polaca. Trece toneladas.
>
> El Thyra se construyó para cruzar océanos, y sesenta y dos años después sigue
> haciéndolo: hoy fondea en San Blas, entre las islas de Guna Yala.
>
> Pesa casi el doble que un velero moderno de su tamaño. Eso, que en un catálogo
> suena a dato aburrido, arriba se siente de una sola manera: el barco no se
> zarandea. Si nunca dormiste en un velero, este es el velero para hacerlo.
>
> Abajo es todo caoba y bronce. Barcos así ya no se construyen; los que siguen a
> flote son los que alguien cuidó.
>
> Salen cinco pasajeros, no cincuenta. Leandro cocina a bordo — cocinó en
> restaurantes de Miami, Brasil y España antes de llegar a las islas.
>
> Día completo, 12 horas · US$120 por persona
> Escribinos por WhatsApp, el link está en la bio 🧭

**Hashtags** (mezcla de alcance y de intención de compra, que son los que
convierten):

```
#SanBlas #GunaYala #SanBlasPanama #Panama #VisitPanama #velero #sailing
#classicyacht #woodenboat #sailingpanama #caribbean #islasdesanblas
#quehacerenpanama #viajarapanama #sailboatlife #boatlife
```

## English version

> Built in Sweden in 1964, out of Polish timber. Thirteen tonnes.
>
> Thyra was made to cross oceans — and sixty-two years later she still does. She
> now anchors in San Blas, among the Guna Yala islands.
>
> She weighs nearly twice what a modern boat her size does. On paper that reads
> like trivia; on board it means one thing — she doesn't roll. If you've never
> slept on a sailboat, this is the one to do it on.
>
> Below deck it's all mahogany and bronze. They don't build them like this
> anymore, and the ones still afloat are the ones somebody looked after.
>
> Five guests, not fifty. Leandro cooks on board — he cooked in Miami, Brazil
> and Spain before he got to the islands.
>
> Full day, 12 hours · US$120 per person
> WhatsApp us, link in bio 🧭

---

## Textos alternativos (accesibilidad, se cargan al subir)

1. El velero Thyra fondeado al atardecer, con luces encendidas bajo el toldo.
2. Placa de datos: 1964, casco de madera, 13 toneladas.
3. Interior del Thyra: literas, maderas oscuras y molas gunas en las paredes.
4. El Thyra visto desde el aire sobre agua turquesa, con la lancha y una tabla
   de paddle al costado.

---

## Cómo publicarlo

- **Orden de las placas:** tal cual están numeradas. La 1 es la portada del
  feed, así que es la que decide si alguien entra.
- **Link en la bio:** poner la web del Thyra o el link directo de WhatsApp. Sin
  eso, la placa 4 promete algo que no está.
- **Historias:** subir la placa 1 y la 4 con sticker de enlace el mismo día.
- **Reutilizable:** este mismo carrusel sirve de anclado en el perfil. Es el que
  explica *qué es* el Thyra, y eso no caduca.

## Cómo volver a generarlo

```bash
cd clientes/velero-thyra/contenido/ig
python3 render_placas.py     # lee placas.html y escribe los 4 JPG
```

Cambiar un texto es editar `placas.html` y volver a correrlo. Sin costo, sin
herramientas de pago, y siempre con las fotos reales del barco.

---

## Pendiente para la próxima pieza

- **Una foto de Leandro** al timón o cocinando. La historia del capitán es el
  mejor reel que tiene este cliente y hoy no hay material para armarlo.
- **Un plato servido a bordo.** Se menciona en el texto y no se puede mostrar.
