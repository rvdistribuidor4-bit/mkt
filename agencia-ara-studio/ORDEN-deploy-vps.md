# Orden para el Claude que administra el VPS de ARA Solutions
*(Copiá y pegá el bloque de abajo en ese chat. Antes, completá lo que está entre [ ].)*

---

## 📋 Bloque para pegar

```
Necesito desplegar un sitio web estático nuevo en este VPS: la landing de ARA Studio
(nuestra unidad de marketing). Es HTML/CSS puro, sin backend ni base de datos.

ARCHIVOS (ya están en GitHub, repo público):
- Repo: https://github.com/rvdistribuidor4-bit/mkt
- Carpeta: agencia-ara-studio/web/  (index.html + ara-icon.png)
- Raw index: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/agencia-ara-studio/web/index.html
- Raw icono: https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/agencia-ara-studio/web/ara-icon.png

QUÉ NECESITO QUE HAGAS:
1. Clonar/descargar esos 2 archivos al VPS (mantené la estructura: index.html y ara-icon.png en la misma carpeta).
2. Servirlo con nginx como sitio estático en el dominio/subdominio: [ARA_STUDIO_DOMINIO]
   (ej.: studio.[DOMINIO-ARA-SOLUTIONS]  ó  el dominio propio arastudio.com.ar si ya lo tengo).
3. Configurar HTTPS con Let's Encrypt/certbot (SSL válido) y forzar HTTP→HTTPS.
4. Confirmarme la IP del servidor y qué registro DNS tengo que crear (A / CNAME) para apuntar el dominio.
5. Dejarlo como carpeta versionable para poder actualizarlo después con un git pull (yo lo actualizo desde el mismo repo).

DATOS:
- Es 100% estático (nginx sirviendo index.html). No necesita Node, PHP ni DB.
- Fuentes tipográficas: se cargan desde Google Fonts (Sora + Manrope) — el server no necesita nada extra.
- Si querés, dejá un pequeño script/README para actualizarlo (git pull en la carpeta del sitio).

Cuando esté arriba, pasame la URL final y la IP + el registro DNS a cargar.
```

---

## ✅ Notas para vos (Ricardo) — antes de mandar la orden
1. **Definí el dominio/subdominio** y reemplazá `[ARA_STUDIO_DOMINIO]`:
   - **Opción rápida (recomendada):** un **subdominio** del dominio que ya usa ARA Solutions (ej. `studio.arasolutions.xxx`). No hay que comprar nada, sale hoy.
   - **Opción marca propia:** un dominio nuevo `arastudio.com` / `arastudio.com.ar` (hay que verificar disponibilidad y comprarlo).
2. **Pendiente menor:** en la web hay un **placeholder de WhatsApp** (`000000000`). Cuando me pases tu número de ARA Studio, lo actualizo en el repo y el VPS lo toma con un `git pull`.
3. El sitio ya quedó **versionado en el repo** (`agencia-ara-studio/web/`), así que futuras mejoras las hago yo ahí y el VPS solo actualiza.

## Cómo actualizamos a futuro (sin fricción)
- Yo edito `agencia-ara-studio/web/index.html` en el repo → push.
- El VPS hace `git pull` (o vos le decís al Claude del VPS "actualizá el sitio de ARA Studio") → cambios online.

*Última actualización: 2026-09-25.*
