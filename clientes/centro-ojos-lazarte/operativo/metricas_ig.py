#!/usr/bin/env python3
"""Metricas de Instagram por la API de Meta. Reemplaza el informe de Windsor.

    python3 metricas_ig.py            # ultimos 10 posts + cuenta
    python3 metricas_ig.py --n 20

Lee META_IG_TOKEN del entorno. Nunca lo imprime.
"""
import argparse, json, os, re, sys, urllib.error, urllib.parse, urllib.request

API = "https://graph.facebook.com/v21.0"
IG_USER_ID = os.environ.get("META_IG_USER_ID", "17841414497159496")
METRICAS = "reach,views,total_interactions,saved,shares"


def pedir(ruta, **params):
    # Si no hay token explicito, lo inyecta el proxy del entorno (ver publicar_ig.py)
    t = os.environ.get("META_IG_TOKEN")
    if t:
        params["access_token"] = t
    try:
        with urllib.request.urlopen(f"{API}/{ruta}?{urllib.parse.urlencode(params)}",
                                    timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Meta respondio {e.code}: "
                 + re.sub(r"access_token=[^&\"\s]+", "access_token=<oculto>",
                          e.read().decode(errors='replace')))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=10)
    n = ap.parse_args().n

    c = pedir(IG_USER_ID, fields="username,followers_count,follows_count,media_count")
    print(f"@{c['username']}  ·  {c['followers_count']} seguidores  ·  "
          f"{c['media_count']} publicaciones  ·  sigue a {c['follows_count']}\n")

    posts = pedir(f"{IG_USER_ID}/media", limit=n,
                  fields="id,timestamp,media_type,permalink,like_count,comments_count")["data"]
    print(f"{'fecha':12} {'tipo':16} {'alcance':>8} {'vistas':>7} {'inter':>6} "
          f"{'guard':>6} {'comp':>5} {'likes':>6}")
    print("-" * 74)
    for p in posts:
        ins = {x["name"]: x["values"][0]["value"]
               for x in pedir(f"{p['id']}/insights", metric=METRICAS).get("data", [])}
        print(f"{p['timestamp'][:10]:12} {p['media_type']:16} "
              f"{ins.get('reach','-'):>8} {ins.get('views','-'):>7} "
              f"{ins.get('total_interactions','-'):>6} {ins.get('saved','-'):>6} "
              f"{ins.get('shares','-'):>5} {p.get('like_count','-'):>6}")
