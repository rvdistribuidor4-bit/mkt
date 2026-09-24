#!/usr/bin/env python3
"""Arma el reel del Thyra: fotos con movimiento + clips reales + capas de texto.

    python3 render_reel_capas.py   # primero las capas PNG
    python3 armar_reel.py          # despues el video

Salida: thyra-reel.mp4 — 1080x1920, 30 fps, ~20 s, sin audio (la musica se
pone desde la libreria de Instagram: la que se incrusta en el archivo la
silencian por derechos y ademas no suma alcance).

Nota de calidad: los clips llegaron por WhatsApp a 464x832 y 576x1024, asi que
en los tramos de video se nota. Cuando Leandro mande los originales por Drive,
se reemplazan las rutas y se vuelve a correr este script.
"""
import pathlib, subprocess, tempfile, imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
AQUI = pathlib.Path(__file__).parent.resolve()
IMG = AQUI.parent.parent / "web" / "img"
VID = AQUI.parent.parent / "web" / "vid"
CAPAS = AQUI / "reel-capas"
SALIDA = AQUI / "thyra-reel.mp4"
W, H, FPS, TRANS = 1080, 1920, 30, 0.5

# (tipo, fuente, duracion, capa de texto, arranque del clip, zoom)
GUION = [
    ("foto",  IMG / "real-atardecer.jpg",  4.0, "ov1.png", None, "in"),
    ("video", VID / "thyra-casco.mp4",     3.4, "ov2.png", 0.5,  None),
    ("placa", CAPAS / "ov3.png",           3.6, None,      None, None),
    ("foto",  IMG / "real-salon.jpg",      3.4, "ov4.png", None, "out"),
    ("video", VID / "thyra-archipielago.mp4", 3.4, "ov5.png", 2.5, None),
    ("foto",  IMG / "real-aerea-hq.jpg",   4.8, "ov6.png", None, "in"),
]
# la transicion cambia segun lo que une: al entrar y salir de la placa oscura
# conviene un negro corto, que da respiro. El resto encadena.
CORTES = ["fade", "fadeblack", "fadeblack", "fade", "fade"]


def correr(args):
    r = subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *args],
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"ffmpeg fallo:\n{' '.join(map(str,args))}\n{r.stderr}")


def tramo(i, tipo, fuente, dur, capa, desde, zoom, tmp):
    """Construye un tramo suelto de 1080x1920 a 30 fps."""
    destino = tmp / f"t{i}.mp4"
    nframes = round(dur * FPS)
    entradas, cadena = [], []

    if tipo == "video":
        entradas += ["-ss", str(desde), "-t", str(dur), "-i", str(fuente)]
        cadena.append(
            f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={W*2}:{H*2},scale={W}:{H}:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,"
            f"fps={FPS},setsar=1,format=yuv420p[base]")
    else:
        entradas += ["-loop", "1", "-framerate", str(FPS), "-i", str(fuente)]
        if zoom:
            # el zoompan salta de a un pixel: se trabaja al doble y se baja
            z = ("min(1+0.00042*on,1.11)" if zoom == "in"
                 else "max(1.11-0.00042*on,1.0)")
            cadena.append(
                f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase:flags=lanczos,"
                f"crop={W*2}:{H*2},"
                f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
                f"d={nframes}:s={W}x{H}:fps={FPS},unsharp=5:5:0.5:5:5:0.0,"
                f"setsar=1,format=yuv420p[base]")
        else:  # placa de datos: quieta, que el texto no se ablande
            cadena.append(
                f"[0:v]scale={W}:{H},fps={FPS},setsar=1,format=yuv420p[base]")

    if capa:
        entradas += ["-loop", "1", "-framerate", str(FPS), "-i", str(CAPAS / capa)]
        cadena.append("[1:v]format=rgba,fade=t=in:st=0.25:d=0.55:alpha=1[capa]")
        cadena.append("[base][capa]overlay=0:0:format=auto[out]")
    else:
        cadena.append("[base]null[out]")

    correr([*entradas, "-filter_complex", ";".join(cadena), "-map", "[out]",
            "-frames:v", str(nframes), "-c:v", "libx264", "-preset", "slow",
            "-crf", "16", "-pix_fmt", "yuv420p", str(destino)])
    return destino


with tempfile.TemporaryDirectory() as td:
    tmp = pathlib.Path(td)
    print("tramos:")
    tramos = []
    for i, (tipo, fuente, dur, capa, desde, zoom) in enumerate(GUION):
        tramos.append(tramo(i, tipo, fuente, dur, capa, desde, zoom, tmp))
        print(f"  {i+1}. {tipo:5} {fuente.name:26} {dur:.1f}s")

    # encadenado con transiciones
    entradas, cadena, prev, largo = [], [], "0:v", GUION[0][2]
    for i in range(1, len(GUION)):
        largo_nuevo = largo + GUION[i][2] - TRANS
        etq = "v" + str(i)
        cadena.append(f"[{prev}][{i}:v]xfade=transition={CORTES[i-1]}:"
                      f"duration={TRANS}:offset={largo - TRANS:.3f}[{etq}]")
        prev, largo = etq, largo_nuevo
    for t in tramos:
        entradas += ["-i", str(t)]

    correr([*entradas, "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-filter_complex", ";".join(cadena),
            "-map", f"[{prev}]", "-map", f"{len(tramos)}:a", "-shortest",
            "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "20",
            "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", str(FPS * 2),
            "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(SALIDA)])

print(f"\n{SALIDA.name}  {largo:.1f}s  {SALIDA.stat().st_size // 1024} KB")
