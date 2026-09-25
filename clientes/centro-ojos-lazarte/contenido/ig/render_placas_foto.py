#!/usr/bin/env python3
"""Renderiza placas-foto.html: estilo LAZARTE v2 con foto real de fondo."""
import pathlib, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = pathlib.Path(__file__).parent.resolve()
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SALIDAS = ["placa-dolor-ojo-foto.jpg", "placa-cambios-vision-foto.jpg"]

with sync_playwright() as p:
    nav = p.chromium.launch(executable_path=CHROME,
        args=["--no-sandbox", "--ignore-certificate-errors", "--disable-dev-shm-usage"])
    pag = nav.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=2)
    pag.goto((AQUI/"placas-foto.html").as_uri(), wait_until="networkidle")
    pag.wait_for_function("document.fonts.ready.then(()=>true)", timeout=15000)
    assert "Inter" in {f.split(":")[0] for f in pag.evaluate(
        "Array.from(document.fonts).filter(f=>f.status=='loaded').map(f=>f.family)")}
    time.sleep(1.2)
    for el, nombre in zip(pag.query_selector_all(".p"), SALIDAS):
        d = AQUI / nombre
        el.screenshot(path=str(d), type="jpeg", quality=95)
        Image.open(d).resize((1080,1350), Image.LANCZOS).save(
            d, "JPEG", quality=90, optimize=True, progressive=True)
        print(f"  {nombre}  {d.stat().st_size//1024} KB")
    nav.close()
