#!/usr/bin/env python3
"""Arma el reel del Thyra: fotos con movimiento + clips reales + capas de texto.

    python3 render_reel_capas.py   # primero las capas PNG
    python3 armar_reel.py          # despues el video

Salida: thyra-reel.mp4 — 1080x1920, 30 fps, ~32 s, sin audio (la musica se pone
desde la libreria de Instagram: la que se incrusta en el archivo la silencian
por derechos y ademas no suma alcance).

Dos reglas de legibilidad, que son las que mandan sobre la duracion:

1. Cada texto entra despues de que termino la transicion y se va antes de que
   empiece la siguiente. Nunca hay dos textos encimados: durante el crossfade
   la pantalla no tiene letras.
2. El tramo dura lo que tarda en leerse el texto, con aire. De ahi que los
   tramos con mas palabras sean mas largos.

Nota de calidad: los clips llegaron por WhatsApp a 464x832 y 576x1024, asi que
en los tramos de video se nota. Cuando Leandro mande los originales por Drive,
se cambian las rutas y se vuelve a correr este script.
"""
import pathlib, subprocess, tempfile, imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
AQUI = pathlib.Path(__file__).parent.resolve()
IMG = AQUI.parent.parent / "web" / "img"
VID = AQUI.parent.parent / "web" / "vid"
CAPAS = AQUI / "reel-capas"
SALIDA = AQUI / "thyra-reel.mp4"
W, H, FPS, TRANS = 1080, 1920, 30, 0.4
ENTRA, SALE = 0.35, 0.45          # cuanto tarda el texto en aparecer y en irse

# capas: (archivo, segundo en que entra). Si es None, el texto se va solo antes
# de la transicion; en la placa las filas se quedan hasta el final.
GUION = [
    dict(tipo="foto",  fuente=IMG / "real-atardecer.jpg",       dur=5.2, zoom="in",
         capas=[("ov1.png", 0.35)]),
    dict(tipo="video", fuente=VID / "thyra-casco.mp4",          dur=4.4, desde=0.5,
         capas=[("ov2.png", 0.35)]),
    dict(tipo="placa",                                          dur=7.6, quedan=True,
         capas=[("ov3.png", 0.20), ("ov4.png", 0.60), ("ov5.png", 1.90),
                ("ov6.png", 3.20), ("ov7.png", 4.70)]),
    dict(tipo="foto",  fuente=IMG / "real-salon.jpg",           dur=5.4, zoom="out",
         capas=[("ov8.png", 0.35)]),
    dict(tipo="video", fuente=VID / "thyra-archipielago.mp4",   dur=4.4, desde=2.5,
         capas=[("ov9.png", 0.35)]),
    dict(tipo="foto",  fuente=IMG / "real-aerea-hq.jpg",        dur=6.6, zoom="in",
         capas=[("ov10.png", 0.35)]),
]
# al entrar y salir de la placa oscura, un negro corto le da respiro al ojo
CORTES = ["fade", "fadeblack", "fadeblack", "fade", "fade"]


def correr(args):
    r = subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *args],
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"ffmpeg fallo:\n{' '.join(map(str, args))}\n{r.stderr}")


def tramo(i, t, tmp):
    """Construye un tramo suelto de 1080x1920 a 30 fps."""
    destino = tmp / f"t{i}.mp4"
    dur, nframes = t["dur"], round(t["dur"] * FPS)
    entradas, cadena = [], []

    if t["tipo"] == "video":
        entradas += ["-ss", str(t["desde"]), "-t", str(dur), "-i", str(t["fuente"])]
        cadena.append(
            f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={W*2}:{H*2},scale={W}:{H}:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,"
            f"fps={FPS},setsar=1,format=yuv420p[base]")
    elif t["tipo"] == "placa":
        entradas += ["-f", "lavfi", "-t", str(dur),
                     "-i", f"color=c=0x04212E:s={W}x{H}:r={FPS}"]
        cadena.append("[0:v]format=yuv420p[base]")
    else:
        entradas += ["-loop", "1", "-framerate", str(FPS), "-i", str(t["fuente"])]
        # el zoompan salta de a un pixel: se trabaja al doble y se baja
        z = ("min(1+0.00040*on,1.11)" if t["zoom"] == "in"
             else "max(1.11-0.00040*on,1.0)")
        cadena.append(
            f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase:flags=lanczos,"
            f"crop={W*2}:{H*2},"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={nframes}:s={W}x{H}:fps={FPS},unsharp=5:5:0.5:5:5:0.0,"
            f"setsar=1,format=yuv420p[base]")

    prev = "base"
    for n, (archivo, entra) in enumerate(t["capas"], start=1):
        entradas += ["-loop", "1", "-framerate", str(FPS), "-i", str(CAPAS / archivo)]
        f = [f"fade=t=in:st={entra}:d={ENTRA}:alpha=1"]
        if not t.get("quedan"):          # se va antes de que empiece la transicion
            f.append(f"fade=t=out:st={dur - TRANS - SALE:.2f}:d={SALE}:alpha=1")
        cadena.append(f"[{n}:v]format=rgba,{','.join(f)}[c{n}]")
        cadena.append(f"[{prev}][c{n}]overlay=0:0:format=auto[o{n}]")
        prev = f"o{n}"
    cadena.append(f"[{prev}]null[out]")

    correr([*entradas, "-filter_complex", ";".join(cadena), "-map", "[out]",
            "-frames:v", str(nframes), "-c:v", "libx264", "-preset", "slow",
            "-crf", "16", "-pix_fmt", "yuv420p", str(destino)])
    return destino


with tempfile.TemporaryDirectory() as td:
    tmp = pathlib.Path(td)
    print("tramos:")
    tramos = []
    for i, t in enumerate(GUION):
        tramos.append(tramo(i, t, tmp))
        nombre = t["fuente"].name if t["tipo"] != "placa" else "placa de datos"
        print(f"  {i+1}. {t['tipo']:5} {nombre:26} {t['dur']:.1f}s"
              f"   lectura ~{t['dur'] - ENTRA - SALE - TRANS:.1f}s")

    entradas, cadena, prev, largo = [], [], "0:v", GUION[0]["dur"]
    for i in range(1, len(GUION)):
        etq = "v" + str(i)
        cadena.append(f"[{prev}][{i}:v]xfade=transition={CORTES[i-1]}:"
                      f"duration={TRANS}:offset={largo - TRANS:.3f}[{etq}]")
        prev, largo = etq, largo + GUION[i]["dur"] - TRANS
    for t in tramos:
        entradas += ["-i", str(t)]

    correr([*entradas, "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-filter_complex", ";".join(cadena),
            "-map", f"[{prev}]", "-map", f"{len(tramos)}:a", "-shortest",
            "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "20",
            "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", str(FPS * 2),
            "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(SALIDA)])

print(f"\n{SALIDA.name}  {largo:.1f}s  {SALIDA.stat().st_size // 1024} KB")
