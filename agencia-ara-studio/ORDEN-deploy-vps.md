# Orden DEFINITIVA para el Claude que administra el VPS de ARA Solutions
**Dominio:** studio.arasolutions.com.ar · **Web server:** Caddy (NO nginx) · A record ya cargado.

> Versión segura: el VPS corre Caddy con Health, TV, Master y Distribution. NO se instala
> nginx (pelearía por 80/443). Se agrega un vhost estático, con diff + validación + OK
> antes de recargar, y reload (no restart).

---

## 📋 Bloque para pegar en el chat del VPS

```
Necesito desplegar un sitio web estático nuevo: la landing de
ARA Studio. Es HTML/CSS puro, sin backend ni base de datos.

IMPORTANTE — NO instales nginx. El VPS usa Caddy y ahí corren
Health, TV, Master y Distribution. nginx pelearía por los puertos
80/443 y puede tirar abajo los 4 servicios. Servilo con Caddy,
que ya maneja HTTPS automático (sin certbot).

DOMINIO: studio.arasolutions.com.ar
(El registro A ya está cargado apuntando al VPS.)

ARCHIVOS (repo público):
- Repo: https://github.com/rvdistribuidor4-bit/mkt
- Carpeta: agencia-ara-studio/web/ (index.html + ara-icon.png)

QUÉ NECESITO:
1) Clonar el repo en el VPS como carpeta versionable, para poder
   actualizar después con git pull. Elegí la ruta según cómo está
   organizado /opt/ara y decime cuál usaste.
2) Agregar un vhost estático en el Caddyfile para
   studio.arasolutions.com.ar. HTTPS automático. Sin tocar ningún
   vhost existente.
3) ANTES de recargar Caddy: mostrame el diff del Caddyfile y
   validá la config con caddy validate. Esperá mi OK.
4) Recargá (reload, NO restart) para no cortar los servicios
   que están arriba.
5) Después del reload, verificá obligatoriamente que health, tv,
   app y distribution siguen respondiendo, y que
   studio.arasolutions.com.ar carga con certificado válido y
   redirige HTTP→HTTPS.
6) README corto con el comando de actualización (git pull).

Las fuentes vienen de Google Fonts, el server no necesita nada
extra. Mostrame el diff del Caddyfile y esperá mi OK antes de
recargar.
```

---

## Cómo actualizamos a futuro
- Yo edito `agencia-ara-studio/web/index.html` en el repo → push a `main`.
- En el VPS: `git pull` en la carpeta del sitio (o le decís al Claude del VPS "actualizá el sitio de ARA Studio").
- El `git pull` trae los cambios de la rama **main**.

## Pendiente menor (lo actualizo yo)
- La web tiene un placeholder de WhatsApp (`000000000`). Cuando me pases tu número de ARA Studio, lo cambio en el repo y el VPS lo toma con `git pull`.

*Última actualización: 2026-09-25.*
