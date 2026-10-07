"""OCR con cajas. Motores: ocrmac (macOS) -> easyocr -> tesseract -> ninguno (regiones por OpenCV)."""

from __future__ import annotations

import platform
from dataclasses import dataclass

import cv2
import numpy as np

_LECTORES: dict = {}


@dataclass
class Linea:
    texto: str
    caja: tuple[int, int, int, int]  # x0, y0, x1, y1
    conf: float

    def a_dict(self) -> dict:
        return {"texto": self.texto, "caja": list(self.caja), "conf": round(self.conf, 3)}


def _easyocr(img: np.ndarray, idioma: str) -> list[Linea]:
    import easyocr
    if "easyocr" not in _LECTORES:
        _LECTORES["easyocr"] = easyocr.Reader([idioma], gpu=False, verbose=False)
    res = _LECTORES["easyocr"].readtext(img, paragraph=False, width_ths=0.9, ycenter_ths=0.6)
    lineas = []
    for pts, txt, conf in res:
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        lineas.append(Linea(txt, (int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys))), float(conf)))
    return lineas


def _tesseract(img: np.ndarray, idioma: str) -> list[Linea]:
    import pytesseract
    lang = {"en": "eng", "es": "spa"}.get(idioma, idioma)
    d = pytesseract.image_to_data(img, lang=lang, output_type=pytesseract.Output.DICT, config="--psm 3")
    grupos: dict = {}
    for i, palabra in enumerate(d["text"]):
        if not palabra.strip() or float(d["conf"][i]) < 0:
            continue
        k = (d["block_num"][i], d["par_num"][i], d["line_num"][i])
        x, y, w, h = d["left"][i], d["top"][i], d["width"][i], d["height"][i]
        g = grupos.setdefault(k, {"p": [], "c": [], "x0": x, "y0": y, "x1": x + w, "y1": y + h})
        g["p"].append(palabra)
        g["c"].append(float(d["conf"][i]) / 100)
        g["x0"], g["y0"] = min(g["x0"], x), min(g["y0"], y)
        g["x1"], g["y1"] = max(g["x1"], x + w), max(g["y1"], y + h)
    return [Linea(" ".join(g["p"]), (g["x0"], g["y0"], g["x1"], g["y1"]), float(np.mean(g["c"])))
            for g in grupos.values()]


def _ocrmac(img: np.ndarray, idioma: str) -> list[Linea]:
    from ocrmac import ocrmac
    from PIL import Image
    h, w = img.shape[:2]
    res = ocrmac.OCR(Image.fromarray(img), language_preference=[f"{idioma}-US"]).recognize()
    lineas = []
    for txt, conf, (x, y, bw, bh) in res:  # coordenadas normalizadas, origen abajo-izquierda
        lineas.append(Linea(txt, (int(x * w), int((1 - y - bh) * h), int((x + bw) * w), int((1 - y) * h)), conf))
    return lineas


def _ninguno(img: np.ndarray, idioma: str) -> list[Linea]:
    """Plan C: solo regiones de texto (sin transcripción); el texto lo completa quien revisa."""
    gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, b = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    b = cv2.morphologyEx(b, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (25, 5)))
    n, _, stats, _ = cv2.connectedComponentsWithStats(b)
    out = []
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        if 8 < h < 120 and w > 2 * h:
            out.append(Linea("", (x, y, x + w, y + h), 0.0))
    return out


MOTORES = {"ocrmac": _ocrmac, "easyocr": _easyocr, "tesseract": _tesseract, "ninguno": _ninguno}


def motores_disponibles(preferidos: list[str]) -> list[str]:
    orden = list(preferidos)
    if platform.system() == "Darwin" and "ocrmac" not in orden:
        orden.insert(0, "ocrmac")
    disponibles = []
    for m in orden:
        try:
            if m == "ocrmac":
                import ocrmac  # noqa: F401
            elif m == "easyocr":
                import easyocr  # noqa: F401
            elif m == "tesseract":
                import pytesseract
                pytesseract.get_tesseract_version()
            disponibles.append(m)
        except Exception:
            continue
    return disponibles or ["ninguno"]


def leer_disperso(img: np.ndarray, caja, escala: float = 2.0, idioma: str = "en") -> list[Linea]:
    """Pasada para etiquetas chicas de gráficos: recorte ampliado y Tesseract en modo disperso (psm 11)."""
    import pytesseract
    x0, y0, x1, y1 = caja
    rec = img[y0:y1, x0:x1]
    if rec.size == 0:
        return []
    rec = cv2.resize(rec, None, fx=escala, fy=escala, interpolation=cv2.INTER_CUBIC)
    lang = {"en": "eng", "es": "spa"}.get(idioma, idioma)
    d = pytesseract.image_to_data(rec, lang=lang, output_type=pytesseract.Output.DICT, config="--psm 11")
    grupos: dict = {}
    for i, palabra in enumerate(d["text"]):
        if not palabra.strip() or float(d["conf"][i]) < 30:
            continue
        k = (d["block_num"][i], d["par_num"][i], d["line_num"][i])
        x, y, w, h = (int(v / escala) for v in (d["left"][i], d["top"][i], d["width"][i], d["height"][i]))
        g = grupos.setdefault(k, {"p": [], "c": [], "x0": x, "y0": y, "x1": x + w, "y1": y + h})
        g["p"].append(palabra)
        g["c"].append(float(d["conf"][i]) / 100)
        g["x0"], g["y0"] = min(g["x0"], x), min(g["y0"], y)
        g["x1"], g["y1"] = max(g["x1"], x + w), max(g["y1"], y + h)
    return sorted((Linea(" ".join(g["p"]), (x0 + g["x0"], y0 + g["y0"], x0 + g["x1"], y0 + g["y1"]),
                         float(np.mean(g["c"]))) for g in grupos.values()),
                  key=lambda l: (l.caja[1], l.caja[0]))


def leer(img: np.ndarray, motor: str, idioma: str = "en", conf_min: float = 0.0) -> list[Linea]:
    lineas = MOTORES[motor](img, idioma)
    lineas = [l for l in lineas if motor == "ninguno" or l.conf >= conf_min]
    return sorted(lineas, key=lambda l: (l.caja[1], l.caja[0]))
