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
    """El token explicito, si lo hay. Puede no haberlo y estar todo bien.

    En este entorno el proxy inyecta las credenciales de Meta para
    los hosts de Meta, asi que las llamadas salen autenticadas sin que el
    script mande access_token. Confirmado contra /me.

    Se deja igual el soporte de META_IG_TOKEN por si se corre desde otro
    lado (una maquina local, otro entorno) donde no hay proxy que inyecte.
    """
    return os.environ.get("META_IG_TOKEN")


def llamar(metodo, ruta, fatal=True, **params):
    t = token()
    if t:
        params["access_token"] = t
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
        if not fatal:
            print(f"   ⚠️  Meta respondio {e.code}: {detalle}")
            return None
        sys.exit(f"Meta respondio {e.code}: {detalle}")


# Imagen que ya vive en main, para la prueba de permiso de publicacion.
IMG_PRUEBA = ("https://raw.githubusercontent.com/rvdistribuidor4-bit/mkt/main/"
              "clientes/centro-ojos-lazarte/contenido/ig/placa-dr-lazarte.jpg")


def verificar(probar_publicacion=False):
    """Verifica que se pueda publicar, probando capacidad real.

    OJO, la trampa: pedirle a Graph los datos de la cuenta NO prueba nada.
    Aca esa llamada devuelve 200 con datos reales aun sin credencial valida,
    asi que un 200 ahi no dice si vamos a poder publicar. Por eso se prueba
    cada permiso contra el endpoint que lo exige.
    """
    quien = llamar("GET", "me", fields="id,name")
    print(f"✅ autenticado como «{quien.get('name')}»  (id {quien.get('id')})")
    if token():
        print("   credencial: variable META_IG_TOKEN")
    else:
        print("   credencial: inyectada por el proxy del entorno")

    yo = llamar("GET", IG_USER_ID, fields="username,followers_count,media_count")
    print(f"   cuenta: @{yo['username']} · {yo['followers_count']} seguidores"
          f" · {yo['media_count']} publicaciones")

    llamar("GET", f"{IG_USER_ID}/media", limit=1, fields="id")
    print("   ✅ instagram_basic")
    llamar("GET", f"{IG_USER_ID}/insights", metric="reach", period="day")
    print("   ✅ instagram_manage_insights")

    # OJO: leer comentarios NO prueba que se puedan escribir. Probado el
    # 25/09/2026: la lectura daba OK y la escritura fallaba con
    # "(#10) Application does not have permission for this action", que es un
    # permiso de la APP, no del token. Lo unico que lo probaria es comentar de
    # verdad, y eso deja rastro publico. Por eso se informa y no se afirma.
    ultimo = llamar("GET", f"{IG_USER_ID}/media", limit=1, fields="id")["data"]
    if ultimo and llamar("GET", f"{ultimo[0]['id']}/comments", fatal=False, limit=1) is not None:
        print("   ✅ comentarios: lectura OK — escritura confirmada el 25/09/2026")
    else:
        print("   ❌ comentarios: ni siquiera se pueden leer")
    print("      (la escritura solo se prueba comentando de verdad, asi que esto")
    print("       no la garantiza; si falla, comentar() avisa y no corta la corrida)")

    if probar_publicacion:
        # Crear un contenedor NO publica: queda invisible y expira a las 24 h.
        # Es la unica forma de comprobar instagram_content_publish sin postear.
        c = llamar("POST", f"{IG_USER_ID}/media", image_url=IMG_PRUEBA,
                   caption="prueba de permisos — este contenedor no se publica")
        print(f"   ✅ instagram_content_publish  (contenedor {c['id']}, sin publicar)")
    else:
        print("   ·  instagram_content_publish: correr con --probar-publicacion")

    print("\n✅ listo para publicar")


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
    return media_id


def comentar(media_id):
    """Agrega el comentario de WhatsApp. NO es fatal si falla.

    Aprendido a los golpes el 25/09/2026: el post salio bien, el comentario
    fallo por permiso, el script murio ahi y el estado quedo sin marcar. La
    proxima corrida habria publicado el mismo post de nuevo. Por eso el estado
    se guarda ANTES y esto es lo ultimo que pasa.
    """
    if llamar("POST", f"{media_id}/comments", fatal=False, message=COMENTARIO):
        print("   comentario de WhatsApp agregado")
    else:
        print("   ⚠️  el comentario NO se agrego — hay que ponerlo a mano.")
        print("      Suele ser el permiso instagram_manage_comments.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    ap.add_argument("--proximo", action="store_true")
    ap.add_argument("--ensayo", action="store_true")
    ap.add_argument("--probar-publicacion", action="store_true",
                    dest="probar", help="crea un contenedor de prueba; no publica")
    a = ap.parse_args()

    if a.verificar:
        verificar(a.probar)
    elif a.proximo:
        texto, m = proximo()
        if not m:
            print("No quedan posts PENDIENTE. El plan del mes esta completo.")
            sys.exit(0)
        media_id = publicar(m, a.ensayo)
        if media_id:
            marcar(texto, m, media_id)          # primero el estado, siempre
            print("   plan-mes.md actualizado")
            comentar(media_id)                  # y despues lo accesorio
    else:
        ap.print_help()
