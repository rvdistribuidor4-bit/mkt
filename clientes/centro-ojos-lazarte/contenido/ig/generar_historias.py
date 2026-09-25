#!/usr/bin/env python3
"""Arma las historias 9:16. Piezas propias, no la placa del feed encogida.

    python3 generar_historias.py

Una historia se ve dos segundos, en vertical y a pantalla completa. Su trabajo
NO es repetir el posteo: es plantear la duda que el posteo responde, y mandar
al feed o a WhatsApp. Por eso cada una lleva UNA sola linea, distinta a la del
feed, y ninguna muestra la placa.
"""
import pathlib, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = pathlib.Path(__file__).parent.resolve()
SALIDA = AQUI / "historias"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
FOTOS = "../../fotos-drive"

# (nombre, overline, linea grande, remate, foto de fondo o None)
# La linea grande NUNCA repite el titular del feed: lo antecede.
HISTORIAS = [
    ("sol", "Consejo visual", "¿Tus anteojos de sol filtran UV de verdad?",
     "No todos lo hacen. Los oscuros sin filtro son peores que no usar nada.", None),
    ("clinica", "Antes de venir", "¿Nunca viniste a una consulta oftalmológica?",
     "Te mostramos dónde vas a estar.", f"{FOTOS}/sala-espera.jpg"),
    ("dr-lazarte", "Dirección médica", "35 años atendiendo en Córdoba.",
     "Dr. Armando Lazarte.", f"{FOTOS}/consultorio.jpg"),
    ("ojo-rojo", "Síntomas", "El ojo rojo casi siempre se pasa solo.",
     "Casi siempre.", None),
    ("trayectoria", "Cirugía de cataratas", "200 por mes.",
     "No es una cifra de folleto.", f"{FOTOS}/equipos-diagnostico.jpg"),
    ("control-anual", "Control", "¿Cuándo fue tu último control de la vista?",
     "Si tardás en contestar, ya pasó demasiado.", None),
    ("no-automedicarse", "Consejo visual", "Las gotas del cajón no sirven para todo.",
     "Cada ojo es distinto.", None),
    ("obras-sociales", "Coberturas", "PAMI, OSDE, APROSS, Swiss Medical, Galeno.",
     "Y bastantes más. Consultanos por la tuya.", f"{FOTOS}/admision.jpg"),
    ("dolor-ojo", "Síntomas", "¿Te duele el ojo o te duele la cabeza?",
     "No siempre es fácil distinguirlo.", f"{FOTOS}/consultorio-lampara.jpg"),
    ("dia-madre", "Día de la Madre", "A todas las que cuidan de los suyos.",
     "Que no falte quien cuide de ustedes.", None),
    ("cambios-vision", "Consejo visual", "Si tu visión cambia de golpe, no esperes.",
     "Los cambios repentinos merecen atención.", f"{FOTOS}/equipos-diagnostico.jpg"),
    ("vision-control", "Turnos", "Ver bien también es calidad de vida.",
     "Escribinos y coordinamos tu turno.", f"{FOTOS}/pasillo.jpg"),
]

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#222}
.h{width:1080px;height:1920px;position:relative;overflow:hidden;background:#0C264B;
   font-family:Inter,sans-serif;color:#FBFCFD;margin-bottom:40px}
.h img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.velo{position:absolute;inset:0;background:linear-gradient(180deg,
      rgba(12,38,75,.80) 0%,rgba(12,38,75,.62) 38%,rgba(12,38,75,.94) 100%)}
.plano{position:absolute;inset:0;background:
      radial-gradient(120% 80% at 80% 12%,#123A64 0%,#0C264B 55%,#08192F 100%)}
/* 300px arriba y 420 abajo: lo que tapan la barra de perfil y la de respuesta */
.in{position:absolute;inset:0;padding:300px 92px 420px;display:flex;
    flex-direction:column;z-index:3}
.over{font-size:28px;letter-spacing:.24em;text-transform:uppercase;font-weight:600;
      color:#74938E;padding-top:22px;border-top:3px solid #3D8B7A;align-self:flex-start;
      text-shadow:0 2px 16px rgba(12,38,75,.95)}
h1{font-size:86px;line-height:1.14;font-weight:700;margin-top:auto;letter-spacing:-.015em;
   text-shadow:0 3px 34px rgba(12,38,75,.8)}
.remate{font-size:38px;line-height:1.45;color:#C7D6D2;margin-top:32px;max-width:20ch;
        text-shadow:0 2px 20px rgba(12,38,75,.85)}
.pie{margin-top:auto;border-top:2px solid rgba(116,147,142,.4);padding-top:26px}
.cta{font-size:34px;font-weight:700}
.cta span{color:#3D8B7A}
.firma{font-size:21px;letter-spacing:.2em;color:#74938E;font-weight:600;margin-top:12px}
"""

def bloque(n, over, linea, remate, foto):
    fondo = f'<img src="{foto}"><div class="velo"></div>' if foto else '<div class="plano"></div>'
    return f"""<div class="h" data-nombre="{n}">{fondo}<div class="in">
  <div class="over">{over}</div>
  <h1>{linea}</h1>
  <div class="remate">{remate}</div>
  <div class="pie">
    <div class="cta">Turnos por WhatsApp <span>→</span> link en la bio</div>
    <div class="firma">CENTRO DE OJOS LAZARTE</div>
  </div></div></div>"""

if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    html = SALIDA / "_historias.html"
    html.write_text(
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>'
        + "\n".join(bloque(*x) for x in HISTORIAS) + '</body></html>')

    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME,
            args=["--no-sandbox", "--ignore-certificate-errors", "--disable-dev-shm-usage"])
        pag = nav.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
        pag.goto(html.as_uri(), wait_until="networkidle")
        pag.wait_for_function("document.fonts.ready.then(()=>true)", timeout=15000)
        assert "Inter" in {f.split(":")[0] for f in pag.evaluate(
            "Array.from(document.fonts).filter(f=>f.status=='loaded').map(f=>f.family)")}
        time.sleep(1.2)
        for el in pag.query_selector_all(".h"):
            d = SALIDA / f"historia-{el.get_attribute('data-nombre')}.jpg"
            el.screenshot(path=str(d), type="jpeg", quality=95)
            Image.open(d).resize((1080, 1920), Image.LANCZOS).save(
                d, "JPEG", quality=90, optimize=True, progressive=True)
            print(f"  {d.name}  {d.stat().st_size//1024} KB")
        nav.close()
