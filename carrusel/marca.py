"""Marca de la cuenta (Pulso Económico): logo «PE» y su aplicación en las slides.

El logo se define como geometría (rectángulos, polígonos y un anillo) y se dibuja igual en PNG y SVG.
Estilo tomado de la marca de agua de la referencia: monograma negro de trazo grueso y uniforme, panza
circular y terminaciones en diagonal.

En cada slide:
- si hay una marca de agua (componente oscuro, compacto y aislado, centrado abajo), se borra y se
  pone el logo nuevo en el mismo lugar y al mismo alto;
- si no hay, se agrega abajo al centro (o en una esquina inferior) solo donde no pisa contenido.
"""

from __future__ import annotations

import math
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw

from .comun import RAIZ, log
from .fondo import borrar_regiones

# --- geometría del logo (unidades: lienzo de 1000 x 1000) ---------------------------------

S = 104            # grosor de trazo
TOP, BOT = 200, 1000
XA = 150           # asta de la P
PANZA = 0.56       # alto de la panza respecto del alto de la letra
GAP = 44           # separación entre P y E
LARGO_BRAZO = 300


def _geometria() -> tuple[list, tuple]:
    """Lista de figuras ('rect'|'poly'|'anillo', datos) y caja (x0, y0, x1, y1) en unidades."""
    hb = int((BOT - TOP) * PANZA)
    r = hb // 2
    cy = TOP + r
    cx = XA + S + r - S // 2
    fig = [
        ("rect", (XA, TOP, XA + S, BOT)),                     # asta P
        ("rect", (XA, TOP, cx + 2, TOP + S)),                 # techo de la panza
        ("rect", (XA, TOP + hb - S, cx + 2, TOP + hb)),       # base de la panza
        ("anillo", (cx, cy, r, S)),                           # media panza (semianillo derecho)
    ]
    xe = cx + r + GAP
    ym = TOP + hb - S
    fig.append(("rect", (xe, TOP, xe + S, BOT)))              # asta E
    for y, largo in ((TOP, LARGO_BRAZO), (ym, LARGO_BRAZO - 50), (BOT - S, LARGO_BRAZO)):
        x1 = xe + largo
        fig.append(("poly", [(xe, y), (x1, y), (x1 + S, y + S), (xe, y + S)]))
    caja = (XA, TOP, xe + LARGO_BRAZO + S, BOT)
    return fig, caja


def logo_mascara(alto_px: int) -> Image.Image:
    """Máscara 'L' (255 = tinta) del logo recortado a su caja, con alto_px de alto."""
    fig, (x0, y0, x1, y1) = _geometria()
    ss = 4
    esc = alto_px * ss / (y1 - y0)
    W, H = int(math.ceil((x1 - x0) * esc)), int(math.ceil((y1 - y0) * esc))
    im = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(im)

    def p(x, y):
        return ((x - x0) * esc, (y - y0) * esc)

    for tipo, g in fig:
        if tipo == "rect":
            d.rectangle([p(g[0], g[1]), p(g[2], g[3])], fill=255)
        elif tipo == "poly":
            d.polygon([p(*q) for q in g], fill=255)
    for tipo, g in fig:
        if tipo == "anillo":
            cx, cy, r, s = g
            d.pieslice([p(cx - r, cy - r), p(cx + r, cy + r)], -90, 90, fill=255)
            d.ellipse([p(cx - r + s, cy - r + s), p(cx + r - s, cy + r - s)], fill=0)
            d.rectangle([p(cx - r, cy - r + s), p(cx, cy + r - s)], fill=0)   # contraforma de la panza
    for tipo, g in fig:  # el asta de la P va encima de la contraforma
        if tipo == "rect" and g[0] == XA:
            d.rectangle([p(g[0], g[1]), p(g[2], g[3])], fill=255)
    return im.resize((max(1, W // ss), max(1, H // ss)), Image.LANCZOS)


def logo_svg(color: str = "#111111") -> str:
    fig, (x0, y0, x1, y1) = _geometria()
    partes = []
    for tipo, g in fig:
        if tipo == "rect":
            partes.append(f'<rect x="{g[0]}" y="{g[1]}" width="{g[2] - g[0]}" height="{g[3] - g[1]}"/>')
        elif tipo == "poly":
            partes.append('<polygon points="' + " ".join(f"{a},{b}" for a, b in g) + '"/>')
        else:
            cx, cy, r, s = g
            ri = r - s
            partes.append(f'<path d="M{cx},{cy - r} A{r},{r} 0 0 1 {cx},{cy + r} L{cx},{cy + ri} '
                          f'A{ri},{ri} 0 0 0 {cx},{cy - ri} Z"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {x1 - x0} {y1 - y0}">'
            f'<title>Pulso Económico</title><g fill="{color}">{"".join(partes)}</g></svg>\n')


def _sobre(fondo: Image.Image, mascara: Image.Image, color, pos) -> None:
    capa = Image.new("RGB", mascara.size, color)
    fondo.paste(capa, pos, mascara)


def generar_logos(config: dict) -> Path:
    """Archivos de marca en marca/: SVG, PNG transparente (negro y blanco) y fotos de perfil."""
    cfg = config["marca"]
    destino = RAIZ / cfg["carpeta"]
    destino.mkdir(parents=True, exist_ok=True)
    base = cfg["archivo_base"]
    color = tuple(int(cfg["color"][i:i + 2], 16) for i in (1, 3, 5))
    (destino / f"{base}.svg").write_text(logo_svg(cfg["color"]), encoding="utf-8")
    m = logo_mascara(1024)
    for sufijo, col in (("", color), ("_blanco", (255, 255, 255))):
        im = Image.new("RGBA", m.size, col + (0,))
        im.putalpha(m)
        im.save(destino / f"{base}{sufijo}.png")
    # perfil (Instagram/TikTok recortan en círculo): el logo entra holgado en el círculo central
    for sufijo, fondo, col in (("_perfil", (255, 255, 255), color), ("_perfil_oscuro", (17, 17, 17), (255, 255, 255))):
        lado = 1080
        alto = int(lado * cfg["perfil_alto_relativo"])
        mm = logo_mascara(alto)
        im = Image.new("RGB", (lado, lado), fondo)
        _sobre(im, mm, col, ((lado - mm.width) // 2, (lado - mm.height) // 2))
        im.save(destino / f"{base}{sufijo}.png")
    return destino


# --- aplicación en las slides --------------------------------------------------------------

def detectar_marca(img: np.ndarray, fondo_rgb, cfg: dict) -> tuple[int, int, int, int] | None:
    """Marca de agua: componente oscuro, compacto y aislado, cerca del centro en la franja inferior."""
    h, w = img.shape[:2]
    y_min = int(h * (1 - cfg["franja_inferior"]))
    sub = img[y_min:].astype(int)
    tinta = (np.abs(sub - np.array(fondo_rgb)).max(axis=2) > 60).astype(np.uint8)
    unida = cv2.dilate(tinta, np.ones((9, 9), np.uint8))
    n, etq, stats, _ = cv2.connectedComponentsWithStats(unida)
    for i in range(1, n):
        x, y, ww, hh, _ = stats[i]
        cx = x + ww / 2
        if not (0.6 <= ww / max(hh, 1) <= 1.7 and 0.03 * w <= max(ww, hh) <= 0.16 * w):
            continue
        if abs(cx - w / 2) > 0.08 * w:
            continue
        # aislada: alrededor (margen = la mitad de su tamaño) no hay otra tinta
        m = max(ww, hh) // 2
        x0, y0, x1, y1 = max(0, x - m), max(0, y - m), min(w, x + ww + m), min(len(sub), y + hh + m)
        otras = (etq[y0:y1, x0:x1] != i) & (etq[y0:y1, x0:x1] != 0)
        if otras.any():
            continue
        ys, xs = np.nonzero((etq == i) & (tinta > 0))
        return int(xs.min()), int(ys.min() + y_min), int(xs.max() + 1), int(ys.max() + 1 + y_min)
    return None


def _libre(img: np.ndarray, fondo_rgb, caja, pad: int) -> bool:
    h, w = img.shape[:2]
    x0, y0, x1, y1 = caja
    x0, y0, x1, y1 = max(0, x0 - pad), max(0, y0 - pad), min(w, x1 + pad), min(h, y1 + pad)
    if x1 - x0 < 2 or y1 - y0 < 2:
        return False
    sub = img[y0:y1, x0:x1].astype(int)
    return bool((np.abs(sub - np.array(fondo_rgb)).max(axis=2) > 30).sum() == 0)


def aplicar_marca(imgs: list[np.ndarray], fondo_rgb, config: dict,
                  prohibidas: list | None = None) -> tuple[list[np.ndarray], str]:
    """Aplica el logo a la slide traducida y a su versión limpia (misma posición). Devuelve un aviso."""
    cfg = config["marca"]
    base = imgs[0]
    h, w = base.shape[:2]
    color = tuple(int(cfg["color"][i:i + 2], 16) for i in (1, 3, 5))
    caja = detectar_marca(base, fondo_rgb, cfg)
    if caja:
        x0, y0, x1, y1 = caja
        alto = y1 - y0
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        imgs = [borrar_regiones(im, [caja], margen=6) for im in imgs]
        aviso = "marca de agua original reemplazada por el logo de Pulso Económico"
    else:
        alto = None
        candidatos = []
        for factor in (1.0, 0.8, 0.65):
            a = int(cfg["alto_relativo"] * w * factor)
            mm = logo_mascara(a)
            margen = int(cfg["margen_inferior_relativo"] * h)
            for cx in (w / 2, w - margen - mm.width / 2, margen + mm.width / 2):
                candidatos.append((a, cx, h - margen - a / 2, mm.width))
        for a, cx, cy, ancho in candidatos:
            caja_n = (int(cx - ancho / 2), int(cy - a / 2), int(cx + ancho / 2), int(cy + a / 2))
            pisa = any(caja_n[0] < z[2] and caja_n[2] > z[0] and caja_n[1] < z[3] and caja_n[3] > z[1]
                       for z in (prohibidas or []))
            if not pisa and _libre(base, fondo_rgb, caja_n, pad=int(0.25 * a)):
                alto = a
                break
        if alto is None:
            return imgs, "NO SE AGREGÓ EL LOGO: no hay espacio libre abajo; agregarlo en Canva"
        aviso = "logo de Pulso Económico agregado (no había marca de agua)"
    mm = logo_mascara(int(alto))
    pos = (int(round(cx - mm.width / 2)), int(round(cy - mm.height / 2)))
    salida = []
    for im in imgs:
        pil = Image.fromarray(im)
        _sobre(pil, mm, color, pos)
        salida.append(np.array(pil))
    return salida, aviso


def marca(slug: str, config: dict) -> None:
    """Comando: genera los archivos del logo en marca/."""
    destino = generar_logos(config)
    log(f"[marca] logos en {destino}")
