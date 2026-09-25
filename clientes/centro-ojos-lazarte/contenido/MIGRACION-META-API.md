# Salir de Windsor — publicar y medir con la API de Meta (gratis)

Windsor pasó a plan pago. **No hace falta pagarlo**: era un intermediario. Todo
lo que hacía —publicar en Instagram y leer métricas— lo da Meta directo y sin
costo, porque Windsor llamaba por dentro exactamente a esta misma API.

**Verificado en este contenedor:** `graph.facebook.com` responde (devuelve el
error de Meta pidiendo token, no un bloqueo de red). El reemplazo es viable.

**Límite de publicación de Meta:** 100 posts cada 24 horas. Publicamos 3 por
semana.

---

## Lo que ya está y no hay que tocar

| Requisito | Estado |
|---|---|
| Cuenta de Instagram tipo Empresa | ✅ `17841414497159496` (confirmado: ya devolvía insights) |
| App de Meta | ✅ creada (ver abajo, hay dos) |
| Página de Facebook vinculada | ✅ «Centro de ojo Lazarte» `1164144553456561` |
| Imágenes en una URL pública | ✅ ya se sirven desde GitHub (`raw.githubusercontent.com`) |

⚠️ Las 6 placas nuevas (`placa-sol`, `placa-ojo-rojo`, `placa-no-automedicarse`,
`placa-dolor-ojo`, `placa-cambios-vision`, `placa-vision-control`) están en la
rama de trabajo. Para la ruta por API hay que **mergearlas a `main`**, porque la
URL pública que lee Meta apunta a `main`. Para la carga manual no hace falta:
ahí los archivos se suben desde la computadora.

Ese tercer punto suele ser el que más traba, porque Meta no acepta que le subas
un archivo: necesita una URL pública. Nosotros ya la teníamos.

---

## Lo que hay que hacer una sola vez

Esto lo tiene que hacer **alguien con el Facebook del cliente**, porque pide su
login. Son unos 40 minutos.

### 1. La app — ✅ YA ESTÁ

Hay **dos apps creadas**, las dos bajo el negocio «Centro de ojo Lazarte»:

| App | ID | Modo |
|---|---|---|
| Centro de ojos Lazarte | `1357320925736401` | En desarrollo |
| centro de ojos lazarte v1 | `1579592890194197` | En desarrollo |

**Usar una sola.** Abrir las dos y quedarse con la que ya tenga **Instagram**
en *Productos*. Si ninguna lo tiene, usar `Centro de ojos Lazarte`
(`1357320925736401`) y agregarle el producto **Instagram → Instagram Graph
API**. A la otra conviene borrarla o dejarla de lado, para no confundirse
después con cuál token es cuál.

> ### ⚠️ «Modo: En desarrollo» NO es un problema
>
> Es la duda que frena a todo el mundo acá, así que: **no hace falta pasar la
> app a producción ni pedir App Review.** La revisión de Meta es para apps que
> manejan cuentas de terceros. Cuando el token lo genera alguien que tiene rol
> en la app (administrador, desarrollador o tester) y los activos son propios
> —la página y la cuenta de Instagram del cliente—, los permisos se otorgan
> igual, con la app en desarrollo. Lo mismo vale para el token de usuario del
> sistema.
>
> Traducido: **se puede publicar hoy, sin esperar aprobación de nadie.**

### 2. Sacar el token

La forma corta es desde el **Explorador de la API Graph**
(developers.facebook.com/tools/explorer), eligiendo la app y pidiendo estos
permisos:

```
instagram_basic
instagram_content_publish
instagram_manage_insights
pages_show_list
pages_read_engagement
```

Ese token dura una hora. Para convertirlo en uno de **60 días**:

```
GET https://graph.facebook.com/v21.0/oauth/access_token
    ?grant_type=fb_exchange_token
    &client_id=<APP_ID>
    &client_secret=<APP_SECRET>
    &fb_exchange_token=<TOKEN_CORTO>
```

**La opción buena, que no vence nunca — hacer esta.** En
**business.facebook.com/settings** → *Usuarios* → **Usuarios del sistema**:

1. *Agregar* → nombre: `publicador-ig` → rol **Administrador del sistema**.
2. *Agregar activos* → **Apps** → la app elegida → **Control total**.
3. *Agregar activos* → **Cuentas de Instagram** → `@centrodeojoslazarte` → **Control total**.
4. *Agregar activos* → **Páginas** → `Centro de ojo Lazarte` → **Control total**.
5. **Generar token nuevo** → elegir la app → tildar los cinco permisos de arriba.

Ese token **no caduca**. Se muestra **una sola vez**: copiarlo en ese momento.
Si se pierde, no se recupera — se genera otro y listo.

### 3. Guardarlo donde corresponde

⚠️ **El token es una credencial: no va al repositorio.** Ni en un archivo, ni en
un commit, ni pegado en el chat.

Va en la configuración del entorno de esta sesión (el menú del entorno en la
barra de título → *Edit*): en **API credentials** si aparece esa sección, y si
no, como variable de entorno. Los nombres que voy a leer son:

```
META_IG_TOKEN      el token de larga duración
META_IG_USER_ID    17841414497159496
```

Una sesión nueva lo toma automáticamente.

---

## Lo que hago yo después

Con el token cargado, reemplazo las llamadas a Windsor en la rutina y todo
vuelve a funcionar igual que antes, sin que toques nada.

**Publicar una placa** son dos llamadas:

```bash
# 1 · crear el contenedor
POST https://graph.facebook.com/v21.0/<IG_USER_ID>/media
     ?image_url=<URL>&caption=<TEXTO>&access_token=<TOKEN>
# devuelve  { "id": "<CREATION_ID>" }

# 2 · publicarlo
POST https://graph.facebook.com/v21.0/<IG_USER_ID>/media_publish
     ?creation_id=<CREATION_ID>&access_token=<TOKEN>
# devuelve  { "id": "<MEDIA_ID>" }
```

**Carrusel:** cada imagen se sube con `is_carousel_item=true`, después un
contenedor con `media_type=CAROUSEL` y `children=<ids>`, y se publica igual.

**El comentario de WhatsApp**, que en el planificador manual no se puede
programar, acá sí:

```bash
POST https://graph.facebook.com/v21.0/<MEDIA_ID>/comments
     ?message=<TEXTO>&access_token=<TOKEN>
```

**Las métricas** salen del mismo token, así que la auditoría mensual vuelve sola:

```bash
GET /<IG_USER_ID>/media?fields=id,caption,media_type,permalink,timestamp,like_count,comments_count
GET /<MEDIA_ID>/insights?metric=reach,views,total_interactions,saved,shares
GET /<IG_USER_ID>?fields=followers_count,media_count
```

---

## El prompt nuevo de la rutina

Cuando el token esté cargado y las placas en `main`, la rutina
`trig_01C9DQ6kPasmAsXBwrcdfRSN` se reactiva con este prompt, que es mucho más
corto que el anterior porque toda la lógica se fue al script:

```
[Publicador autónomo LAZARTE — el usuario autorizó publicar sin consultar.
NO preguntes; ejecutá.]

1) cd clientes/centro-ojos-lazarte/operativo
2) python3 publicar_ig.py --verificar
   Si falla: avisá con el error de Meta tal cual y NO sigas. No reintentes en
   loop: la próxima corrida Lun/Mié/Vie retoma.
3) python3 publicar_ig.py --proximo
   El script publica el primer bloque PENDIENTE de contenido/plan-mes.md,
   agrega el comentario de WhatsApp y marca el bloque con su media_id.
4) Si dice que no quedan posts PENDIENTE: avisá que el plan del mes se
   completó y ofrecé armar el próximo. NO publiques nada.
5) Agregá la fila correspondiente en marca/linea-visual.md (Publicaciones
   realizadas). Commit + push a main.
6) Avisá al usuario en 1-2 líneas qué se publicó.

Nunca imprimas META_IG_TOKEN. Cumplimiento médico: los CAPTION ya traen el
disclaimer donde corresponde; no agregues promesas de resultado.
```

Lo que se gana respecto del anterior: el comentario de WhatsApp vuelve a ser
automático, Canva sale de la cadena y, si algo falla, falla en un script que se
puede correr a mano con `--ensayo` para ver qué iba a hacer.

---

## Las otras dos fuentes, también gratis

No son urgentes; se suman cuando el Instagram ya esté andando.

- **Search Console** — API gratuita. Necesita una cuenta de servicio de Google
  Cloud agregada como usuario en la propiedad. Es la fuente que hoy muestra los
  112 clics mensuales, o sea la más valiosa que tiene el cliente.
- **GA4** — API gratuita, misma cuenta de servicio.
  ⚠️ **Antes de conectarla hay que resolver otra cosa:** GA4 no registra ni una
  sesión en 30 días mientras Search Console ve 112 clics. Conectar la API no
  sirve de nada hasta que se verifique que el tag está instalado en el sitio que
  está online.

---

## Estado

- [x] Confirmado que Windsor está en plan Trial vencido
- [x] Confirmado que `graph.facebook.com` es alcanzable desde el contenedor
- [x] Rutina automática **desactivada** para que no duplique con la carga manual
- [x] Puente manual listo → `PUBLICAR-A-MANO.md`
- [x] ~~Crear la app de Meta~~ → hay dos, bajo el negocio «Centro de ojo Lazarte»
- [ ] Elegir una de las dos y agregarle el producto Instagram
- [x] ~~Generar el token de usuario del sistema~~ → el cliente ya lo tiene
- [x] Scripts escritos y probados en seco → `operativo/publicar_ig.py`, `operativo/metricas_ig.py`
- [x] `plan-mes.md` pasado a un formato que el script parsea (línea `IMG:`)
- [ ] 🔴 **Cargar `META_IG_TOKEN` en el entorno** (no en el repo, no en el chat).
      Una sesión nueva lo toma; la actual no lo ve
- [ ] 🔴 **Mergear las 6 placas nuevas a `main`** — la URL que lee Meta apunta ahí
- [ ] Correr `publicar_ig.py --verificar` y después `--proximo --ensayo`
- [ ] Reactivar la rutina apuntando al script
- [ ] Sumar Search Console (y GA4, cuando el tag esté verificado)
