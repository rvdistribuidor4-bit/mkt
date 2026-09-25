# Cómo se publica la web de Lazarte

## El problema que resuelve

El sitio lo sirve **Hostinger** y hasta ahora se subía **a mano**. Resultado:
la web viva quedó atrás del repo. Al 25/09/2026 faltaban publicar el teléfono
fijo, el schema con las dos sedes, el formulario que abre WhatsApp con los datos
cargados y el sello de marca del hero. Todo hecho, nadie viéndolo.

## Cómo queda

`.github/workflows/deploy-lazarte.yml`: **cada push a `main` que toque
`clientes/centro-ojos-lazarte/web/` publica solo.**

Antes de subir corre una validación: si algún HTML quedó sin cerrar o algún
JSON-LD no parsea, **el deploy falla y no publica**. Es la red que evita mandar
a producción un archivo roto.

Solo sube lo que cambió, y **no borra** lo que ya estaba en el servidor y no
viene del repo (`dangerous-clean-slate: false`).

## Los tres secretos

Van en GitHub → Settings → Secrets and variables → Actions. **No van al repo.**

| Secreto | De dónde sale |
|---|---|
| `HOSTINGER_FTP_HOST` | hPanel → Archivos → Cuentas FTP → *Dirección/Host* |
| `HOSTINGER_FTP_USER` | ídem, *Nombre de usuario FTP* |
| `HOSTINGER_FTP_PASSWORD` | ídem. Si no se conoce, se cambia desde ahí |

## Publicar a mano

GitHub → pestaña **Actions** → *Publicar web de Lazarte* → **Run workflow**.

## Verificar que salió

```bash
curl -s https://www.centrodeojoslazarte.com/ | grep -c "423-3716"
```

Si devuelve 0, la web viva sigue atrasada.

## Si Hostinger no usa `public_html`

Es la carpeta habitual, pero algunos planes usan otra. Se ve en hPanel →
Administrador de archivos, y se corrige en `server-dir` del workflow.
