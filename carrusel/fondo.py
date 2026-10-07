"""Reconstrucción de fondo: muestreo de color por fila para respetar degradados."""

from __future__ import annotations

import cv2
import numpy as np


def color_fondo_global(img: np.ndarray) -> np.ndarray:
    """Color de fondo dominante (mediana de los bordes)."""
    h, w = img.shape[:2]
    b = max(4, w // 60)
    bordes = np.concatenate([
        img[:, :b].reshape(-1, 3), img[:, -b:].reshape(-1, 3),
        img[:b, :].reshape(-1, 3), img[-b:, :].reshape(-1, 3),
    ])
    return np.median(bordes, axis=0)


def perfil_fondo_filas(img: np.ndarray, excluir: np.ndarray | None = None,
                       ancho_muestra: int | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Color de fondo por fila a izquierda y derecha (mediana de una franja de borde).

    excluir: máscara bool (h, w) de píxeles a ignorar (texto, gráficos).
    Devuelve (izq, der), cada uno (h, 3) float.
    """
    h, w = img.shape[:2]
    a = ancho_muestra or max(8, w // 14)
    izq = np.zeros((h, 3), np.float32)
    der = np.zeros((h, 3), np.float32)
    glob = color_fondo_global(img).astype(np.float32)
    for y in range(h):
        for franja, destino, sl in ((img[y, :a], izq, slice(0, a)), (img[y, w - a:], der, slice(w - a, w))):
            if excluir is not None:
                ok = ~excluir[y, sl]
                franja = franja[ok]
            if len(franja) >= 3:
                destino[y] = np.median(franja, axis=0)
            else:
                destino[y] = np.nan
    for arr in (izq, der):
        for c in range(3):
            col = arr[:, c]
            malos = np.isnan(col)
            if malos.all():
                col[:] = glob[c]
            elif malos.any():
                idx = np.arange(h)
                col[malos] = np.interp(idx[malos], idx[~malos], col[~malos])
    # suavizado vertical para evitar bandas
    k = max(3, (h // 90) | 1)
    izq = cv2.GaussianBlur(izq.reshape(h, 1, 3), (1, k), 0).reshape(h, 3)
    der = cv2.GaussianBlur(der.reshape(h, 1, 3), (1, k), 0).reshape(h, 3)
    return izq, der


def fondo_sintetico(img: np.ndarray, excluir: np.ndarray | None = None) -> np.ndarray:
    """Imagen de fondo completa interpolando linealmente entre izquierda y derecha por fila."""
    h, w = img.shape[:2]
    izq, der = perfil_fondo_filas(img, excluir)
    t = np.linspace(0.0, 1.0, w, dtype=np.float32)[None, :, None]
    fondo = izq[:, None, :] * (1 - t) + der[:, None, :] * t
    return np.clip(fondo, 0, 255).astype(np.uint8)


def borrar_regiones(img: np.ndarray, cajas: list, margen: int = 6,
                    excluir: np.ndarray | None = None, inpaint_residual: bool = True) -> np.ndarray:
    """Rellena las cajas con el fondo sintético; si quedan bordes con tinta, aplica inpainting."""
    h, w = img.shape[:2]
    mascara = np.zeros((h, w), bool)
    for x0, y0, x1, y1 in cajas:
        x0, y0 = max(0, int(x0) - margen), max(0, int(y0) - margen)
        x1, y1 = min(w, int(x1) + margen), min(h, int(y1) + margen)
        mascara[y0:y1, x0:x1] = True
    excl = mascara if excluir is None else (mascara | excluir)
    fondo = fondo_sintetico(img, excl)
    out = img.copy()
    out[mascara] = fondo[mascara]
    if inpaint_residual:
        # tinta residual en el anillo exterior de cada caja (antialiasing que sobresale)
        anillo = cv2.dilate(mascara.astype(np.uint8), np.ones((5, 5), np.uint8)) & ~mascara.astype(np.uint8)
        dif = np.abs(img.astype(np.int16) - fondo.astype(np.int16)).max(axis=2)
        residual = (anillo.astype(bool) & (dif > 25)).astype(np.uint8)
        if residual.any():
            out = cv2.inpaint(out, residual * 255, 3, cv2.INPAINT_TELEA)
    return out
