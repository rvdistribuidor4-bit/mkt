# Orden DEFINITIVA para el Claude que administra el VPS de ARA Solutions
**Dominio:** studio.arasolutions.com.ar · **Reverse proxy:** Caddy DENTRO de Docker (`ara-health-staging-reverse-proxy-1`) · A record ya apunta al VPS.

> Diagnóstico confirmado en el VPS: Caddy corre en Docker (no systemd), su Caddyfile
> NO tiene bloque `studio`, y no hay ninguna app "studio" desplegada. Los stacks viven
> en `/opt/ara/staging/`. Hay que DESPLEGAR el sitio estático y agregar el vhost.
> Todo additive + reload en caliente. NO recrear ni reiniciar el reverse proxy ni los
> stacks existentes (Health, TV, Distribution).

---

## 📋 Bloque para pegar en el chat del VPS

```
CONTEXTO (ya diagnosticado por vos): Caddy corre en Docker
(contenedor ara-health-staging-reverse-proxy-1), no como servicio.
El Caddyfile no tiene bloque para studio. El DNS de
studio.arasolutions.com.ar ya apunta al VPS (179.43.112.190).
Falta DESPLEGAR la landing de ARA Studio (sitio estático NUEVO)
y agregar su vhost. NO es la misma app que health/tv/distribution.

OBJETIVO: publicar studio.arasolutions.com.ar con HTTPS, SIN
recrear ni reiniciar los servicios existentes y SIN downtime.
Solo additive + reload en caliente.

ARCHIVOS: repo público https://github.com/rvdistribuidor4-bit/mkt
carpeta agencia-ara-studio/web/ (index.html, ara-icon.png,
reel-cafe.jpg, reel-boutique.jpg). HTML/CSS/JS puro, sin backend.

PLAN (adaptalo a lo que veas; vos conocés el layout real):
1) Cloná el repo en el host:
   git clone --depth 1 https://github.com/rvdistribuidor4-bit/mkt /opt/ara/studio/mkt
   (a futuro se actualiza con: git -C /opt/ara/studio/mkt pull)
2) Levantá un contenedor estático liviano llamado ara-studio
   (caddy:2-alpine o nginx:alpine) que sirva la carpeta
   /opt/ara/studio/mkt/agencia-ara-studio/web montada read-only,
   SIN publicar puertos al host (solo interno), CONECTADO a la
   misma red Docker del reverse proxy (confirmala con
   docker inspect ara-health-staging-reverse-proxy-1).
3) En el Caddyfile montado en el reverse proxy, agregá SOLO este
   bloque nuevo, sin tocar los demás:

   studio.arasolutions.com.ar {
       reverse_proxy ara-studio:80
   }

4) Mostrame el diff del Caddyfile ANTES de recargar. Recargá EN
   CALIENTE, sin recrear el contenedor del reverse proxy:
   docker exec ara-health-staging-reverse-proxy-1 caddy reload \
     --config <ruta-del-Caddyfile-dentro-del-contenedor> --adapter caddyfile
5) Caddy va a emitir el certificado Let's Encrypt solo (DNS ok,
   puertos 80/443 abiertos). Esperá ~1 minuto.
6) VERIFICÁ obligatoriamente:
   - https://studio.arasolutions.com.ar carga con cert válido.
   - health, tv, app y distribution siguen respondiendo igual.
   - docker ps: ara-studio Up y los demás SIN reiniciarse.

REGLAS: additive only. NO recrear ni reiniciar el reverse proxy ni
los stacks existentes. reload, NO restart. Si algo obligara a
recrear el reverse proxy, PARÁ y avisá antes de hacerlo.
```

---

## Cómo actualizamos a futuro
- Yo edito `agencia-ara-studio/web/index.html` en el repo → push a `main`.
- En el VPS: `git pull` en la carpeta del sitio (o le decís al Claude del VPS "actualizá el sitio de ARA Studio").
- El `git pull` trae los cambios de la rama **main**.

## WhatsApp de ARA Studio ✅
- Número: **+54 9 351 773-4177** → `wa.me/5493517734177`. Ya está en toda la web. El VPS lo toma con `git pull`.

*Última actualización: 2026-09-26.*
