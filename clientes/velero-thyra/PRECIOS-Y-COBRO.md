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

### Recomendación operativa

**Esquema de dos pasos, que es el que ya usa la industria:**

1. **Seña 30% por transferencia internacional en USD (Wise).** Es lo que usan la mayoría de los charters del Caribe, y con razón: Wise da datos de cuenta locales en dólares, el cliente transfiere como si fuera doméstico, el tipo de cambio es el real y la comisión es mínima comparada con el 5,4% de PayPal. Se deja PayPal como alternativa para el cliente que solo quiere poner la tarjeta.
2. **Saldo 70% en efectivo USD al subir a bordo.** En Guna Yala el dólar en efectivo es la moneda real, el capitán lo necesita igual para tasas y compras, y no paga comisión nadie.

La seña cubre el no-show; el grueso no paga comisiones. Ya está redactado así en la FAQ de la web, en los dos idiomas.

### La pregunta de fondo no es el medio de cobro, es quién factura

Conviene separar dos cosas que se mezclan:

**1. Dónde se genera la renta.** El barco está en Panamá, el capitán vive en Panamá, el servicio se presta íntegramente en aguas panameñas. **Es renta de fuente panameña.** Si la factura una estructura panameña, tributa en Panamá, que es donde la actividad efectivamente ocurre. Eso es lo ordinario en el negocio náutico, no una maniobra.

**2. Quién la cobra.** Si el titular de la cuenta es Fabio como persona física residente fiscal en Argentina, entra a jugar que **Argentina grava la renta mundial de sus residentes** — y ahí el medio de cobro es irrelevante, porque lo que define la obligación es la residencia del titular, no por dónde pasó el dinero.

O sea: la diferencia entre las dos situaciones no la hace usar Wise en lugar de PayPal. La hace **de quién es la estructura que factura**.

### ⚠️ Dos datos que cambian el cálculo

- **Desde febrero de 2026 Argentina adhiere al estándar CRS 2.0.** Wise, PayPal y Payoneer **reportan automáticamente** saldos y movimientos a las autoridades fiscales argentinas. Cualquier esquema que dependa de que "no hay control" está construido sobre una premisa que este año dejó de ser cierta.
- **Panamá tiene sistema territorial**, pero eso no significa que no grave: no grava la renta de fuente extranjera, y esta operación es de fuente **panameña**. Hay que ver qué régimen aplica a un charter turístico y qué registros pide la autoridad marítima.

### Lo que hay que preguntarle al contador

No "cómo cobro sin que se vea", sino:

1. **¿Qué estructura corresponde en Panamá** para un charter que opera íntegramente ahí? ¿Sociedad panameña, registro como operador turístico, qué pide la autoridad marítima?
2. **¿Cuál es la situación de residencia fiscal de Fabio?** Es lo que determina si la renta panameña le impacta en Argentina.
3. **¿Cómo se documentan los cobros en efectivo a bordo** para que la contabilidad cierre?

Tiene que ser un contador con experiencia en servicios al exterior y, si se puede, que conozca Panamá. **Esto excede lo que yo puedo recomendar**: puedo dejar el circuito de cobro andando y los textos escritos, pero la estructura la define un profesional que se haga responsable de lo que firma.

### Pasos concretos para arrancar

- [ ] **Definir quién factura** (punto 1 de arriba). Todo lo demás depende de esto.
- [ ] Abrir **Wise Business** a nombre de quien corresponda una vez resuelto lo anterior.
- [ ] Abrir **PayPal** como alternativa de tarjeta.
- [ ] Armar el circuito: quién manda los datos de transferencia, quién confirma la seña, dónde se anota la reserva.
- [ ] Definir **cómo se registran los cobros en efectivo** a bordo.

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
