#!/usr/bin/env python3
"""Genera un voucher personalizado de Refly, en JPG y PDF.

    python3 generar_voucher.py --para "Sofía" --de "Mamá y Papá"
    python3 generar_voucher.py --para "Juan Pérez" --de "Los chicos del trabajo" \
                               --codigo RFLY-2026-0042

El JPG es para mandar por WhatsApp; el PDF, para imprimir (A5 apaisado).
Si no se pasa codigo, se genera uno. La vigencia es de 12 meses desde hoy.
"""
import argparse, datetime, pathlib, random, string, time
from playwright.sync_api import sync_playwright

AQUI = pathlib.Path(__file__).parent.resolve()
SALIDA = AQUI / "emitidos"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto",
         "septiembre","octubre","noviembre","diciembre"]


def codigo_nuevo():
    az = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"RFLY-{datetime.date.today():%Y}-{az}"


def en_castellano(f):
    return f"{f.day} de {MESES[f.month - 1]} de {f.year}"


def emitir(para, de, codigo, vence):
    SALIDA.mkdir(exist_ok=True)
    base = SALIDA / f"voucher-{codigo}"
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME,
            args=["--no-sandbox", "--ignore-certificate-errors", "--disable-dev-shm-usage"])
        pag = nav.new_page(viewport={"width": 1600, "height": 1000}, device_scale_factor=2)
        pag.goto((AQUI / "voucher.html").as_uri(), wait_until="networkidle")
        pag.wait_for_function("document.fonts.ready.then(()=>true)", timeout=15000)
        pag.evaluate("""([para, de, codigo, vence]) => {
            document.getElementById('para').textContent = para;
            document.getElementById('de').textContent = de;
            document.getElementById('codigo').textContent = codigo;
            document.getElementById('vence').textContent = vence;
        }""", [para, de, codigo, vence])
        time.sleep(0.6)
        pag.query_selector(".v").screenshot(path=f"{base}.jpg", type="jpeg", quality=94)
        pag.pdf(path=f"{base}.pdf", width="210mm", height="148mm",
                print_background=True, margin={"top": "0", "bottom": "0",
                                               "left": "0", "right": "0"})
        nav.close()
    return base


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--para", required=True, help="nombre de quien va a volar")
    ap.add_argument("--de", required=True, help="quien regala")
    ap.add_argument("--codigo", default=None)
    ap.add_argument("--meses", type=int, default=12, help="vigencia (default 12)")
    a = ap.parse_args()

    codigo = a.codigo or codigo_nuevo()
    hoy = datetime.date.today()
    # 12 meses exactos; si el dia no existe en el mes destino, cae al ultimo
    mes = hoy.month - 1 + a.meses
    anio, mes = hoy.year + mes // 12, mes % 12 + 1
    dia = min(hoy.day, [31, 29 if anio % 4 == 0 and (anio % 100 or anio % 400 == 0)
                        else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][mes - 1])
    vence = datetime.date(anio, mes, dia)

    base = emitir(a.para, a.de, codigo, en_castellano(vence))
    print(f"  {base.name}.jpg  (WhatsApp)")
    print(f"  {base.name}.pdf  (imprimir, A5 apaisado)")
    print(f"  código {codigo} · vence el {en_castellano(vence)}")
