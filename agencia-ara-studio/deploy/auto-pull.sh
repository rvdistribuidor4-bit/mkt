#!/bin/sh
# Auto-deploy del sitio de ARA Studio en el VPS.
# Lo corre cron cada 1-2 min: si hay commits nuevos en main, hace git pull
# y (segun como sirva el contenedor) refresca ara-studio.
#
# Uso:  auto-pull.sh [none|restart|rebuild]
#   none    -> el contenedor sirve la carpeta MONTADA (con el pull ya alcanza). DEFAULT.
#   restart -> el contenedor copio los archivos: docker restart ara-studio
#   rebuild -> imagen con COPY en Dockerfile: docker compose up -d --build ara-studio
#
# Ajusta REPO si tu clon esta en otra ruta (confirmar con: docker inspect ara-studio).

set -e
REPO="${ARA_STUDIO_REPO:-/opt/ara/studio/mkt}"
MODE="${1:-none}"

cd "$REPO" || exit 0
before="$(git rev-parse HEAD 2>/dev/null || echo none)"
git pull --quiet --ff-only origin main || exit 0
after="$(git rev-parse HEAD 2>/dev/null || echo none)"

# sin cambios: no hacemos nada
[ "$before" = "$after" ] && exit 0

case "$MODE" in
  restart) docker restart ara-studio >/dev/null 2>&1 || true ;;
  rebuild) docker compose up -d --build ara-studio >/dev/null 2>&1 || true ;;
  none)    : ;;  # volumen montado: el pull ya publico los cambios
esac

echo "$(date -Is) ara-studio deploy: ${before} -> ${after} (mode=${MODE})"
