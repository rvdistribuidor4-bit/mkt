# Thyra · Precios, cancelación y cobro

Análisis para decidir con el dueño. Los precios ya están cargados en la web como
propuesta; cambiarlos es un buscar-y-reemplazar.

---

## 1. Auditoría de mercado (San Blas, 2026)

Precios públicos de la competencia, relevados en septiembre de 2026:

| Producto | Mercado | Fuente |
|---|---|---|
| Charter compartido, todo incluido | **US$200–350** pp/noche | itravelbyboat, bluesailing |
| Charter privado, velero económico | desde **US$500**/noche barco entero | catamaranadventures |
| Catamarán privado | **US$900–2.600**/noche (2 pax) | ampatours |
| **Day tour en lancha** (el volumen real) | **US$114–148** pp | sanblastourspty, ampatours |
| Day tour en velero | **US$265** pp | Expedia |
| Traslado 4x4 desde Ciudad de Panamá | US$35–150 pp | varios |
| Tasa de ingreso a Guna Yala | **US$22** pp | varios |

## 2. La jugada: no competir donde están todos

El instinto sería pelear en el mercado de charters de varios días. **Es un error**:
ahí está lleno de catamaranes de 45 pies con aire acondicionado, y el Thyra es un
clásico de madera de 42 pies con 5 plazas. En esa comparación pierde por ficha
técnica, aunque gane por alma.

**Donde hay volumen real es en el day tour.** Cientos de personas por día salen de
Ciudad de Panamá al amanecer, se meten en una lancha con veinte desconocidos, la
lancha golpea contra el oleaje 40 minutos, y pagan **US$114–148**.

A esa misma persona le ofrecemos, **por el mismo precio**, un velero con capitán,
cinco pasajeros máximo, sombra, almuerzo a bordo y navegación a vela.

> **El día completo no es un producto más: es la puerta de entrada.** Es lo que da
> el flujo que el dueño pide, y es el que llena el barco entre charters largos.

## 3. Precios propuestos

Capacidad real: **5 pasajeros + capitán**.

| Experiencia | Precio | Barco lleno | Contra el mercado |
|---|---|---|---|
| **Día completo (12 h)** | US$120 pp | US$600/día | Precio de lancha, producto de velero. **Menos de la mitad** que el day tour en velero de la competencia (US$265) |
| **Noche a bordo** | US$150 pp/noche, mín. 2 | US$750/noche | **25% por debajo** del piso de mercado (US$200) |
| **Barco entero** | US$750/día, hasta 5 | — | Contra los US$500 del velero económico y los US$900+ del catamarán |

**Por qué estos números y no otros**

- **US$120** es deliberadamente igual al day tour en lancha. La decisión del turista deja de ser de precio y pasa a ser de producto — y ahí ganamos siempre.
- **US$150** la noche mantiene margen y sigue siendo la opción más barata del archipiélago para dormir a bordo.
- El barco entero a **US$750** cierra el arbitraje: 5 personas sueltas pagan US$750 la noche, así que el privado no puede costar menos.

**Piso para que salga**: 3 pasajeros en el día completo (US$360). Con menos, conviene ofrecer fecha alternativa antes que salir a pérdida.

**Lo que NO está incluido** y hay que decirlo desde el principio: traslado 4x4 (~US$40 pp) y tasa de Guna Yala (US$22 pp). Que el cliente sume mentalmente US$180 y no se sienta engañado en el muelle.

## 4. Política de cancelación (propuesta, ya cargada en la web)

**Seña del 30% para reservar.**

| Aviso | Qué pasa |
|---|---|
| Más de 30 días | La seña se transfiere a cualquier fecha dentro de 12 meses, sin cargo |
| 15 a 30 días | Se retiene la mitad de la seña; la otra mitad queda como crédito |
| Menos de 15 días | Se retiene la seña, pero la reserva se puede ceder a otra persona sin costo |

**Si cancela el barco, el pasajero no pierde nada.** Clima o seguridad, decisión
del capitán siempre: nueva fecha o devolución del 100%, seña incluida.

> Esa última cláusula no es generosidad, es seguridad operativa: **ningún capitán
> debe sentir presión económica para salir con mal tiempo.** Y comercialmente es
> un argumento de venta: el que reserva a ciegas desde otro continente necesita
> saber que el clima no le cuesta la plata.

## 5. Cobrar en dólares desde Argentina

**Situación:** barco en Panamá, dueño argentino, clientes internacionales.

### Lo que no sirve

- **Stripe**: no opera ni en Panamá ni en Argentina. Solo con una LLC en EEUU o una sociedad en el Reino Unido. Descartado por ahora.
- **Mercado Pago**: pesos argentinos. No aplica.

### Lo que sí sirve

| Opción | Para qué | Costo aprox. | Fricción para el turista |
|---|---|---|---|
| **PayPal** | Seña con tarjeta | ~5,4% + cambio | Baja: lo conoce todo el mundo |
| **Payoneer** (Request a Payment) | Seña con tarjeta o transferencia | ~3% tarjeta, 0,5% cambio | Media |
| **Wise Business** | Transferencia en USD | Comisión baja, cambio real | Media-alta: hay que transferir |
| **Efectivo USD al abordar** | El saldo | 0% | Ninguna: es lo normal en San Blas |
| **Airbnb** | Reservas que ya llegan por ahí | ~15% | Ninguna, pero es la más cara |

### Recomendación

**Esquema de dos pasos, que es el que ya usa la industria:**

1. **Seña 30% por link de pago** (PayPal para empezar por volumen de reconocimiento; Payoneer si el volumen crece, porque es la mitad de caro).
2. **Saldo 70% en efectivo USD al subir a bordo.** En Guna Yala el dólar en efectivo es la moneda real, el capitán lo necesita para tasas y compras, y evita comisiones.

Ese esquema cubre el riesgo de no-show con la seña y minimiza comisiones sobre el grueso.

### Pasos concretos

- [ ] Definir **quién factura**: ¿el dueño como persona en Argentina, o hay sociedad en Panamá? Cambia todo lo demás.
- [ ] Abrir **PayPal Business** con el correo del negocio y verificar cuenta bancaria.
- [ ] Abrir **Payoneer** en paralelo y comparar con dos cobros reales.
- [ ] Cargar el link de pago en la web (el formulario y la FAQ ya anuncian "link de pago seguro").
- [ ] Definir el circuito: quién manda el link, quién confirma, dónde se anota la reserva.

### ⚠️ Antes de mover un peso

Desde **febrero de 2026 Argentina adhiere al estándar CRS 2.0**: PayPal, Wise y
Payoneer reportan saldos y movimientos a las autoridades fiscales argentinas. No
es un problema, pero **sí cambia cómo conviene estructurarlo**.

**Esto lo tiene que ver un contador con experiencia en servicios al exterior, no
nosotros.** Yo puedo dejar el circuito armado y los links funcionando; la decisión
de dónde factura y cómo lo declara es del dueño y su contador.

---

## Fuentes

- [San Blas Catamaran Charter Cost 2026 — itravelbyboat](https://www.itravelbyboat.com/post/how-much-does-a-san-blas-catamaran-charter-cost-in-2026)
- [San Blas Cost 2026: $148 Day Trip to Multi-Day Sailing — ampatours](https://www.ampatours.com/how-much-does-san-blas-cost/)
- [Budget Friendly Shared Charter — bluesailing](https://bluesailing.net/en_us/destinos/budget-friendly-shared-charters/)
- [San Blas Tour Prices 2026 | From $114 per Person](https://sanblastourspty.com/en/precios)
- [San Blas day tour on sailboat, all inclusive — Expedia](https://www.expedia.com/zh/things-to-do/san-blas-day-tour-on-sailboat-island-hopping-all-inclusive.a5138395.activity-details)
- [Stripe global availability](https://stripe.com/global)
- [Payoneer: cómo recibir pagos en Argentina (2026) — Wise](https://wise.com/ar/blog/payoneer-recibir-pagos)
- [Deel, Payoneer y Wise: cobrar del exterior en regla 2026 — Conta Online](https://www.contaonline.com.ar/blog/deel-payoneer-wise-cobrar-exterior-argentina-2026/)
