#!/bin/sh
# Instalador de auto-deploy de ARA Studio. Correr UNA sola vez en el VPS.
# Detecta como sirve el contenedor ara-studio e instala un cron cada 2 min.
# Pensado para correrse desde la consola VNC (no hace falta tipear simbolos raros).

REPO="${ARA_STUDIO_REPO:-/opt/ara/studio/mkt}"
SCRIPT="$REPO/agencia-ara-studio/deploy/auto-pull.sh"
LOG="/var/log/ara-studio-deploy.log"

echo "=================================================="
echo " ARA Studio - instalador de auto-deploy"
echo " Repo: $REPO"
echo "=================================================="

if [ ! -d "$REPO/.git" ]; then
  echo "ERROR: $REPO no es un repo git."
  echo "Si tu clon esta en otra ruta, corre:  ARA_STUDIO_REPO=/otra/ruta sh $0"
  exit 1
fi

git config --global --add safe.directory "$REPO" 2>/dev/null || true
chmod +x "$SCRIPT" 2>/dev/null || true

# --- detectar modo segun los mounts del contenedor ---
MODE="none"
EXTRA=""
if command -v docker >/dev/null 2>&1; then
  MOUNTS="$(docker inspect ara-studio --format '{{range .Mounts}}{{.Source}}->{{.Destination}} {{end}}' 2>/dev/null)"
  echo "Mounts del contenedor: ${MOUNTS:-<ninguno>}"
  if printf '%s' "$MOUNTS" | grep -q "agencia-ara-studio/web"; then
    MODE="none"       # carpeta montada: el pull ya publica
  elif printf '%s' "$MOUNTS" | grep -q "index.html"; then
    MODE="restart"    # archivo suelto montado
  else
    MODE="rebuild"    # imagen con COPY
    CF="$(docker inspect ara-studio --format '{{index .Config.Labels "com.docker.compose.project.config_files"}}' 2>/dev/null)"
    echo "Compose file detectado: ${CF:-<no detectado>}"
    [ -n "$CF" ] && EXTRA="ARA_STUDIO_COMPOSE=$CF "
  fi
else
  echo "AVISO: docker no encontrado; asumo modo none."
fi
echo "==> Modo elegido: $MODE"

echo ""
echo "== Prueba manual (si algo falla, se ve aca) =="
ARA_STUDIO_REPO="$REPO" ${EXTRA:+env $EXTRA} sh "$SCRIPT" "$MODE"
echo "(si no imprimio 'deploy OK' es porque no habia commits nuevos; es normal)"

echo ""
echo "== Instalando cron cada 2 minutos =="
LINE="*/2 * * * * ARA_STUDIO_REPO=$REPO ${EXTRA}$SCRIPT $MODE >> $LOG 2>&1"
( crontab -l 2>/dev/null | grep -v 'auto-pull.sh'; echo "$LINE" ) | crontab -
echo "Cron instalado:"
crontab -l | grep 'auto-pull.sh'

echo ""
echo "LISTO. Log de deploys: $LOG"
echo "Para verificar: hace un cambio, espera 2 min y corre:  tail -n 20 $LOG"
