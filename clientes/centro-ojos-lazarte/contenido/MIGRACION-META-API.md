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
| Cuenta de Instagram tipo Empresa | ✅ `17841414497159496` |
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

### 1. Crear la app

1. Entrar a **developers.facebook.com** → *Mis aplicaciones* → *Crear*.
2. Tipo: **Empresa** (Business).
3. Asociarla a la cuenta comercial del Centro de Ojos Lazarte.
4. Agregar el producto **Instagram** → *Instagram Graph API*.

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

**La opción buena, que no vence nunca:** en *Meta Business Suite → Configuración
del negocio → Usuarios → Usuarios del sistema*, crear un usuario del sistema,
darle acceso a la página y a la app, y generar su token con los mismos permisos.
Ese no caduca y evita tener que renovar cada dos meses. Si se puede, hacer esta.

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
- [ ] Crear la app de Meta y sacar el token *(lo hace el cliente)*
- [ ] Cargar `META_IG_TOKEN` en el entorno
- [ ] Reescribir la rutina para que publique por Graph API
- [ ] Reactivar la rutina
- [ ] Sumar Search Console (y GA4, cuando el tag esté verificado)
