#!/usr/bin/env python3
"""Renderiza un HTML de placas a JPG de 1080x1350, listos para Instagram.

    python3 render_placas_foto.py placas-foto.html
    python3 render_placas_foto.py carrusel-clinica.html

Cada bloque .p del HTML lleva data-nombre, que define el archivo de salida.
Se dibuja al doble y se baja: el texto sale mas nitido que a tamano final.
"""
import pathlib, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = pathlib.Path(__file__).parent.resolve()
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ANCHO, ALTO = 1080, 1350
fuente = AQUI / (sys.argv[1] if len(sys.argv) > 1 else "placas-foto.html")

with sync_playwright() as p:
    nav = p.chromium.launch(executable_path=CHROME,
        args=["--no-sandbox", "--ignore-certificate-errors", "--disable-dev-shm-usage"])
    pag = nav.new_page(viewport={"width": ANCHO, "height": ALTO}, device_scale_factor=2)
    pag.goto(fuente.as_uri(), wait_until="networkidle")
    pag.wait_for_function("document.fonts.ready.then(()=>true)", timeout=15000)
    assert "Inter" in {f.split(":")[0] for f in pag.evaluate(
        "Array.from(document.fonts).filter(f=>f.status=='loaded').map(f=>f.family)")}, "no cargo Inter"
    time.sleep(1.2)
    for el in pag.query_selector_all(".p"):
        nombre = el.get_attribute("data-nombre")
        assert nombre, "falta data-nombre en un bloque .p"
        d = AQUI / f"placa-{nombre}.jpg"
        el.screenshot(path=str(d), type="jpeg", quality=95)
        Image.open(d).resize((ANCHO, ALTO), Image.LANCZOS).save(
            d, "JPEG", quality=90, optimize=True, progressive=True)
        print(f"  {d.name}  {d.stat().st_size//1024} KB")
    nav.close()
