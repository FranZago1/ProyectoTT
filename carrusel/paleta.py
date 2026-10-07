"""Paleta del carrusel: k-means (numpy) sobre los píxeles de contenido de las slides originales.

El fondo se reporta aparte (color dominante); el texto, como el cluster más oscuro.
Salida: trabajo/<slug>/paleta.json y memoria/paletas.json (versionado, lo usa memoria/ESTILO.md).
"""

from __future__ import annotations

import json

import numpy as np
from PIL import Image

from .comun import Rutas, leer_plan, log, rgb_a_hex


def kmeans(x: np.ndarray, k: int, semilla: int = 0, iteraciones: int = 40) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(semilla)
    # inicialización k-means++
    centros = [x[rng.integers(len(x))]]
    for _ in range(1, k):
        d = np.min(((x[:, None, :] - np.array(centros)[None]) ** 2).sum(-1), axis=1)
        centros.append(x[rng.choice(len(x), p=d / d.sum())])
    c = np.array(centros, dtype=np.float64)
    for _ in range(iteraciones):
        etq = np.argmin(((x[:, None, :] - c[None]) ** 2).sum(-1), axis=1)
        nuevo = np.array([x[etq == i].mean(axis=0) if (etq == i).any() else c[i] for i in range(k)])
        if np.allclose(nuevo, c, atol=0.5):
            break
        c = nuevo
    return c, np.bincount(etq, minlength=k)


def paleta(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    plan = leer_plan(rutas)
    cfg = config["paleta"]
    rng = np.random.default_rng(0)
    contenido, fondos = [], []
    for s in plan["slides"]:
        img = np.array(Image.open(rutas.slides / f"{s['n']:02d}.png").convert("RGB")).reshape(-1, 3).astype(float)
        fondo = np.median(img, axis=0)
        fondos.append(fondo)
        dif = np.abs(img - fondo).max(axis=1)
        pix = img[dif > 40]  # sin antialiasing claro
        if len(pix):
            contenido.append(pix[rng.choice(len(pix), min(len(pix), cfg["muestras"] // 7), replace=False)])
    x = np.vstack(contenido)
    centros, cuenta = kmeans(x, cfg["k"])
    orden = np.argsort(-cuenta)
    colores = [{"hex": rgb_a_hex(centros[i]), "proporcion": round(float(cuenta[i] / cuenta.sum()), 3)}
               for i in orden]
    # acentos: solo píxeles saturados (verde/rojo/naranja de los gráficos)
    mx, mn = x.max(axis=1), x.min(axis=1)
    sat = (mx - mn) / np.maximum(mx, 1)
    sx = x[(sat > 0.35) & (mx > 60)]
    acentos = []
    if len(sx) > 200:
        ca, na = kmeans(sx, min(cfg["k_acentos"], len(sx) // 50))
        acentos = [{"hex": rgb_a_hex(ca[i]), "proporcion": round(float(na[i] / na.sum()), 3)}
                   for i in np.argsort(-na) if na[i] / na.sum() >= 0.03]
    lum = centros @ np.array([0.299, 0.587, 0.114])
    resultado = {"fondo": rgb_a_hex(np.median(fondos, axis=0)), "texto": rgb_a_hex(centros[np.argmin(lum)]),
                 "contenido": colores, "acentos": acentos}
    (rutas.trabajo / "paleta.json").write_text(json.dumps(resultado, indent=2), encoding="utf-8")
    ruta_mem = rutas.memoria / "paletas.json"
    todas = json.loads(ruta_mem.read_text(encoding="utf-8")) if ruta_mem.exists() else {}
    todas[slug] = resultado
    ruta_mem.parent.mkdir(parents=True, exist_ok=True)
    ruta_mem.write_text(json.dumps(todas, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"[paleta] {slug}: fondo {resultado['fondo']}, texto {resultado['texto']}, "
        + ", ".join(f"{c['hex']} ({c['proporcion']:.0%})" for c in colores)
        + " | acentos: " + ", ".join(f"{c['hex']} ({c['proporcion']:.0%})" for c in acentos))
