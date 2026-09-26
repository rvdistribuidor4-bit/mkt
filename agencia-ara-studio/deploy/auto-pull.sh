#!/bin/sh
# Auto-deploy del sitio de ARA Studio en el VPS (lo corre cron).
# Si hay commits nuevos en main: git pull y, segun el modo, refresca ara-studio.
#
# Uso:  auto-pull.sh [none|restart|rebuild]
#   none    -> el contenedor sirve la carpeta MONTADA (con el pull alcanza). DEFAULT.
#   restart -> hay un archivo montado suelto: docker restart ara-studio
#   rebuild -> imagen con COPY: docker compose ... up -d --build --no-deps ara-studio
#
# Variables:
#   ARA_STUDIO_REPO     ruta del clon (default /opt/ara/studio/mkt)
#   ARA_STUDIO_COMPOSE  ruta del docker-compose.yml (solo para modo rebuild)

REPO="${ARA_STUDIO_REPO:-/opt/ara/studio/mkt}"
MODE="${1:-none}"
COMPOSE="${ARA_STUDIO_COMPOSE:-}"

cd "$REPO" || { echo "$(date -Is) ERROR: no existe $REPO"; exit 1; }
git config --global --add safe.directory "$REPO" 2>/dev/null || true

before="$(git rev-parse HEAD 2>/dev/null || echo none)"
if ! git pull --quiet --ff-only origin main; then
  echo "$(date -Is) ERROR en git pull (credenciales / permisos / red)"; exit 1
fi
after="$(git rev-parse HEAD 2>/dev/null || echo none)"

[ "$before" = "$after" ] && exit 0   # sin cambios: nada que hacer

case "$MODE" in
  restart)
    docker restart ara-studio || echo "$(date -Is) WARN: restart fallo" ;;
  rebuild)
    if [ -n "$COMPOSE" ]; then
      docker compose -f "$COMPOSE" up -d --build --no-deps ara-studio || echo "$(date -Is) WARN: rebuild fallo"
    else
      docker compose up -d --build --no-deps ara-studio || echo "$(date -Is) WARN: rebuild (sin ARA_STUDIO_COMPOSE) fallo"
    fi ;;
  none) : ;;
esac

echo "$(date -Is) ara-studio deploy OK: ${before} -> ${after} (mode=${MODE})"
