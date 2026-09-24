#!/usr/bin/env python3
"""Renderiza reel.html a las capas PNG transparentes que usa armar_reel.py."""
import pathlib, time
from playwright.sync_api import sync_playwright

AQUI = pathlib.Path(__file__).parent.resolve()
CAPAS = AQUI / "reel-capas"; CAPAS.mkdir(exist_ok=True)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

with sync_playwright() as p:
    nav = p.chromium.launch(executable_path=CHROME,
                            args=["--no-sandbox", "--ignore-certificate-errors", "--disable-dev-shm-usage"])
    pag = nav.new_page(viewport={"width": 1080, "height": 1920})
    pag.goto((AQUI / "reel.html").as_uri(), wait_until="networkidle")
    pag.wait_for_function("document.fonts.ready.then(()=>true)", timeout=15000)
    cargadas = {f.split(":")[0] for f in pag.evaluate(
        "Array.from(document.fonts).filter(f=>f.status=='loaded').map(f=>f.family)")}
    assert {"Fraunces", "Inter"} <= cargadas, f"faltan fuentes: {cargadas}"
    time.sleep(1.2)
    for i, capa in enumerate(pag.query_selector_all(".ov"), 1):
        d = CAPAS / f"ov{i}.png"
        capa.screenshot(path=str(d), omit_background=True)
        print(f"  {d.name}  {d.stat().st_size // 1024} KB")
    nav.close()
