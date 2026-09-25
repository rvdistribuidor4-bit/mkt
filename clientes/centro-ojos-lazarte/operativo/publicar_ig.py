#!/usr/bin/env python3
"""Publica en Instagram por la API de Meta. Reemplaza a Windsor, sin costo.

    python3 publicar_ig.py --verificar   # prueba el token, no publica nada
    python3 publicar_ig.py --proximo     # publica el primer post PENDIENTE
    python3 publicar_ig.py --proximo --ensayo   # muestra que haria, sin publicar

Lee el token de la variable de entorno META_IG_TOKEN. Nunca lo imprime.

La cola de publicacion es `contenido/plan-mes.md`: el script toma el primer
bloque con `estado: PENDIENTE`, publica, agrega el comentario de WhatsApp y
marca el bloque como PUBLICADO con la fecha y el media_id.
"""
import argparse, datetime, json, os, pathlib, re, sys, urllib.parse, urllib.request

API = "https://graph.facebook.com/v21.0"
IG_USER_ID = os.environ.get("META_IG_USER_ID", "17841414497159496")
PLAN = pathlib.Path(__file__).parent.parent / "contenido" / "plan-mes.md"
COMENTARIO = ("📲 Sacá tu turno por WhatsApp: https://wa.me/5493516371007"
              " · 📍 Deán Funes 614 · 9 de Julio 778, Córdoba")


def token():
    t = os.environ.get("META_IG_TOKEN")
    if not t:
        sys.exit("Falta META_IG_TOKEN en el entorno. Ver contenido/MIGRACION-META-API.md")
    return t


def llamar(metodo, ruta, **params):
    params["access_token"] = token()
    url = f"{API}/{ruta}"
    datos = urllib.parse.urlencode(params).encode()
    pedido = (urllib.request.Request(url, data=datos, method="POST") if metodo == "POST"
              else urllib.request.Request(f"{url}?{datos.decode()}"))
    try:
        with urllib.request.urlopen(pedido, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detalle = e.read().decode(errors="replace")
        # el token viaja en la query: no dejarlo en el log
        detalle = re.sub(r"access_token=[^&\"\s]+", "access_token=<oculto>", detalle)
        sys.exit(f"Meta respondio {e.code}: {detalle}")


def verificar():
    yo = llamar("GET", IG_USER_ID, fields="username,followers_count,media_count")
    print(f"✅ token OK — @{yo['username']}  ·  {yo['followers_count']} seguidores"
          f"  ·  {yo['media_count']} publicaciones")


# ---------- la cola vive en plan-mes.md ----------

# Ojo con re.S aca: hace que "." cruce saltos de linea y entonces el titulo se
# come los bloques siguientes (probado: tomaba el post 1 con la imagen del 2).
# El caption, que si es multilinea, usa [\s\S] en vez de activar re.S.
BLOQUE = re.compile(
    r"^### (?P<n>\d+) · (?P<titulo>.+)$\n"
    r"^\*\*estado: (?P<estado>[^*\n]+)\*\*$\n"
    r"^IMG: (?P<img>\S+)$\n"
    r"^CAPTION:$\n```\n(?P<caption>[\s\S]*?)\n```",
    re.M)


def proximo():
    texto = PLAN.read_text()
    for m in BLOQUE.finditer(texto):
        if m.group("estado").strip() == "PENDIENTE":
            return texto, m
    return texto, None


def marcar(texto, m, media_id):
    hoy = datetime.date.today().isoformat()
    nuevo = f"**estado: PUBLICADO ({hoy} · media_id {media_id})**"
    viejo = f"**estado: {m.group('estado').strip()}**"
    inicio = m.start()
    PLAN.write_text(texto[:inicio] + texto[inicio:].replace(viejo, nuevo, 1))


def publicar(m, ensayo):
    img, caption = m.group("img"), m.group("caption")
    print(f"→ {m.group('n')} · {m.group('titulo')}\n   imagen: {img}")
    if ensayo:
        print("   (ensayo: no se publica nada)")
        return None
    cont = llamar("POST", f"{IG_USER_ID}/media", image_url=img, caption=caption)
    pub = llamar("POST", f"{IG_USER_ID}/media_publish", creation_id=cont["id"])
    media_id = pub["id"]
    print(f"   publicado · media_id {media_id}")
    llamar("POST", f"{media_id}/comments", message=COMENTARIO)
    print("   comentario de WhatsApp agregado")
    return media_id


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    ap.add_argument("--proximo", action="store_true")
    ap.add_argument("--ensayo", action="store_true")
    a = ap.parse_args()

    if a.verificar:
        verificar()
    elif a.proximo:
        texto, m = proximo()
        if not m:
            print("No quedan posts PENDIENTE. El plan del mes esta completo.")
            sys.exit(0)
        media_id = publicar(m, a.ensayo)
        if media_id:
            marcar(texto, m, media_id)
            print("   plan-mes.md actualizado")
    else:
        ap.print_help()
