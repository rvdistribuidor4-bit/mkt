#!/usr/bin/env python3
"""Renderiza placas.html a los JPG del carrusel de Instagram.

    python3 render_placas.py

Se dibuja al doble de tamano y se baja a 1080x1350: el texto sale mas nitido
que renderizando directo al tamano final. Costo cero, sin herramientas pagas.
"""
import pathlib, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = pathlib.Path(__file__).parent.resolve()
FUENTE = AQUI / "placas.html"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ANCHO, ALTO = 1080, 1350

with sync_playwright() as p:
    nav = p.chromium.launch(executable_path=CHROME, args=[
        "--no-sandbox", "--ignore-certificate-errors", "--disable-dev-shm-usage"])
    pag = nav.new_page(viewport={"width": ANCHO, "height": ALTO}, device_scale_factor=2)
    errores = []
    pag.on("console", lambda m: errores.append(m.text) if m.type == "error" else None)
    pag.goto(FUENTE.as_uri(), wait_until="networkidle")
    pag.wait_for_function("document.fonts.ready.then(()=>true)", timeout=15000)
    cargadas = {f.split(":")[0] for f in pag.evaluate(
        "Array.from(document.fonts).filter(f=>f.status=='loaded').map(f=>f.family)")}
    assert {"Fraunces", "Inter"} <= cargadas, f"faltan fuentes: {cargadas}"
    time.sleep(1.5)

    for i, placa in enumerate(pag.query_selector_all(".p"), 1):
        destino = AQUI / f"thyra-carrusel-{i}.jpg"
        placa.screenshot(path=str(destino), type="jpeg", quality=95)
        img = Image.open(destino).resize((ANCHO, ALTO), Image.LANCZOS)
        img.save(destino, "JPEG", quality=90, optimize=True, progressive=True)
        print(f"  {destino.name}  {img.size[0]}x{img.size[1]}  {destino.stat().st_size // 1024} KB")

    if errores:
        print("errores de consola:", errores)
    nav.close()
