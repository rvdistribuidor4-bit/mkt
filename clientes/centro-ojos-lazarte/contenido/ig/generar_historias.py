#!/usr/bin/env python3
"""Arma la historia 9:16 de cada placa del feed.

    python3 generar_historias.py

La historia NO es una pieza nueva: es la placa del día montada en 1080x1920
para empujar tráfico al posteo. Es el uso que mejor rinde y el único que la
API permite, porque los stickers de link y las encuestas no se pueden poner
por API (y el sticker de link además pide 10 mil seguidores).
"""
import pathlib, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = pathlib.Path(__file__).parent.resolve()
SALIDA = AQUI / "historias"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# placa del feed -> historia. Solo las que estan en la cola.
PLACAS = ["placa-sol", "placa-clinica-1-portada", "placa-dr-lazarte",
          "placa-ojo-rojo", "placa-tray-1-portada", "placa-control-anual",
          "placa-no-automedicarse", "placa-obras-sociales",
          "placa-dolor-ojo-foto", "placa-dia-madre",
          "placa-cambios-vision-foto", "placa-vision-control"]

PLANTILLA = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#222}}
.h{{width:1080px;height:1920px;position:relative;overflow:hidden;background:#0C264B;
   font-family:Inter,sans-serif;color:#FBFCFD;display:flex;flex-direction:column;
   align-items:center;padding:150px 60px 170px;margin-bottom:40px}}
.marca{{font-size:24px;letter-spacing:.26em;font-weight:700;color:#74938E}}
.placa{{margin-top:auto;margin-bottom:auto;width:900px;border-radius:28px;overflow:hidden;
       box-shadow:0 40px 90px rgba(0,0,0,.45)}}
.placa img{{width:100%;display:block}}
.cta{{font-size:46px;font-weight:700;line-height:1.25;text-align:center}}
.cta span{{color:#3D8B7A}}
.sub{{font-size:30px;color:#C7D6D2;margin-top:20px;text-align:center;line-height:1.45}}
</style></head><body>
{bloques}
</body></html>"""

BLOQUE = """<div class="h" data-nombre="{n}">
  <div class="marca">CENTRO DE OJOS LAZARTE</div>
  <div class="placa"><img src="../{n}.jpg"></div>
  <div class="cta">Nuevo en el feed <span>↑</span></div>
  <div class="sub">Turnos por WhatsApp · link en la bio</div>
</div>"""

if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    faltan = [n for n in PLACAS if not (AQUI / f"{n}.jpg").exists()]
    assert not faltan, f"faltan placas: {faltan}"
    html = AQUI / "historias" / "_historias.html"
    html.write_text(PLANTILLA.format(bloques="\n".join(BLOQUE.format(n=n) for n in PLACAS)))

    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME,
            args=["--no-sandbox", "--ignore-certificate-errors", "--disable-dev-shm-usage"])
        pag = nav.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
        pag.goto(html.as_uri(), wait_until="networkidle")
        pag.wait_for_function("document.fonts.ready.then(()=>true)", timeout=15000)
        time.sleep(1.0)
        for el in pag.query_selector_all(".h"):
            d = SALIDA / f"historia-{el.get_attribute('data-nombre')}.jpg"
            el.screenshot(path=str(d), type="jpeg", quality=95)
            Image.open(d).resize((1080, 1920), Image.LANCZOS).save(
                d, "JPEG", quality=90, optimize=True, progressive=True)
            print(f"  {d.name}  {d.stat().st_size//1024} KB")
        nav.close()
