"""Paso 3: OCR + detección de zonas -> borrador de plan.json.

El borrador lo corrige quien tiene criterio (mirando cada imagen): texto exacto, roles, negritas,
traducción y estrategia de gráficos. Al re-ejecutar, los campos ya curados no se pisan:
si una slide tiene "curado": true, solo se actualizan las líneas OCR crudas.
"""

from __future__ import annotations

import cv2
import numpy as np
from PIL import Image

from . import ocr
from .comun import Rutas, guardar_plan, leer_plan, log, rgb_a_hex

# Inter: alto de una línea con ascendentes y descendentes ≈ 0,96 em
ALTO_LINEA_EM = 0.96
# Inter: altura de mayúsculas/ascendentes ≈ 0,74 em
ASCENDENTE_EM = 0.74


def _tinta(img: np.ndarray, fondo: np.ndarray, umbral: int) -> np.ndarray:
    return np.abs(img.astype(int) - fondo.astype(int)).max(axis=2) > umbral


def _medir_linea(img: np.ndarray, tinta: np.ndarray, caja) -> dict:
    """Mide em (desde la altura de ascendentes), grosor de trazo relativo y color de una línea."""
    x0, y0, x1, y1 = caja
    sub = tinta[y0:y1, x0:x1]
    filas = np.flatnonzero(sub.any(axis=1))
    alto = (filas[-1] - filas[0] + 1) if len(filas) else (y1 - y0)
    gris = cv2.cvtColor(img[y0:y1, x0:x1], cv2.COLOR_RGB2GRAY)
    nucleo = (gris < 128).astype(np.uint8)
    em, trazo = alto / ALTO_LINEA_EM, 0.0
    if nucleo.sum() > 30:
        perfil = nucleo.sum(axis=1)
        con_tinta = np.flatnonzero(perfil > 0)
        base = np.flatnonzero(perfil > 0.25 * perfil.max())[-1]   # línea base (fin de la altura x)
        em = (base - con_tinta[0] + 1) / ASCENDENTE_EM
        contornos, _ = cv2.findContours(nucleo, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        perimetro = sum(cv2.arcLength(c, True) for c in contornos)
        trazo = 2 * nucleo.sum() / max(perimetro, 1) / max(em, 1)   # grosor en em
    px = img[y0:y1, x0:x1][sub]
    if len(px):
        lum = px.mean(axis=1)
        color = np.median(px[lum <= np.percentile(lum, 25)], axis=0)
    else:
        color = np.array([26, 26, 26])
    return {"alto": int(alto), "em": float(em), "trazo": float(trazo), "color": rgb_a_hex(color)}


def _tam_por_ancho(grupo: list[dict], config_render: dict) -> int | None:
    """Tamaño de fuente que reproduce el ancho medido de cada línea (mediana entre líneas)."""
    from .render import fuente
    peso = "bold" if grupo[0]["negrita"] else "regular"
    estimaciones = []
    for l in grupo:
        if len(l["texto"]) < 8 or l["conf"] < 0.6:
            continue
        w100 = fuente(config_render, peso, 100).getlength(l["texto"])
        if w100 > 0:
            estimaciones.append(100 * (l["caja"][2] - l["caja"][0]) / w100)
    return int(round(float(np.median(estimaciones)))) if estimaciones else None


def _filas_grafico(tinta: np.ndarray, cajas: list, margen: int = 6) -> np.ndarray:
    """Cantidad de píxeles de tinta por fila que NO pertenecen a líneas de texto detectadas."""
    resto = tinta.copy()
    h, w = tinta.shape
    for x0, y0, x1, y1 in cajas:
        resto[max(0, y0 - margen):min(h, y1 + margen), max(0, x0 - margen):min(w, x1 + margen)] = False
    return resto.sum(axis=1), resto


def _agrupar_bloques(lineas: list[dict], factor: float) -> list[list[dict]]:
    """Agrupa líneas en párrafos por separación vertical y peso. Las líneas cortas (sin
    descendentes, p. ej. 'bet.') se comparan por em, no por alto de caja."""
    bloques: list[list[dict]] = []
    for l in lineas:
        if bloques:
            prev = bloques[-1][-1]
            ref = max(x["alto"] for x in bloques[-1])
            em_ref = float(np.median([x["em"] for x in bloques[-1]]))
            gap = l["caja"][1] - prev["caja"][3]
            alto_ok = abs(l["em"] - em_ref) <= 0.15 * em_ref
            if gap <= factor * ref and alto_ok and l["negrita"] == prev["negrita"]:
                bloques[-1].append(l)
                continue
        bloques.append([l])
    return bloques


def extraer_slide(img: np.ndarray, fondo: np.ndarray, cfg: dict, motor: str) -> dict:
    h, w = img.shape[:2]
    ce = cfg["extraer"]
    tinta = _tinta(img, fondo, ce["umbral_fondo"])
    crudas = ocr.leer(img, motor, cfg["ocr"]["idioma"], cfg["ocr"]["confianza_min"])
    # líneas de texto "de cuerpo": con letras, alto razonable
    lineas = []
    for l in crudas:
        letras = sum(c.isalpha() for c in l.texto)
        if letras < 2:
            continue
        m = _medir_linea(img, tinta, l.caja)
        if m["alto"] < 18:
            continue
        lineas.append({"texto": l.texto, "caja": list(l.caja), "conf": l.conf, **m})

    por_fila, resto = _filas_grafico(tinta, [l["caja"] for l in lineas])
    graf = por_fila > ce.get("min_tinta_fila", 12)
    # primera franja de gráfico: corrida de >= 20 filas con tinta no-textual
    y_g = None
    corrida = 0
    for y in range(h):
        corrida = corrida + 1 if graf[y] else 0
        if corrida >= 20:
            y_g = y - 19
            break

    texto, otras = [], []
    for l in lineas:
        (texto if (y_g is None or l["caja"][3] <= y_g) else otras).append(l)

    # negrita: grosor de trazo relativo al tamaño (Inter Regular ≈ 0,09 em; Bold ≈ 0,15 em)
    for l in texto:
        l["negrita"] = bool(l["trazo"] > ce["umbral_negrita"])
    grupos = _agrupar_bloques(texto, ce["separacion_parrafo_factor"])
    bloques = []
    for i, g in enumerate(grupos):
        alto = float(np.median([l["alto"] for l in g]))
        tam = _tam_por_ancho(g, config_render=cfg) or int(round(np.median([l["em"] for l in g])))
        caja = [min(l["caja"][0] for l in g), min(l["caja"][1] for l in g),
                max(l["caja"][2] for l in g), max(l["caja"][3] for l in g)]
        paso = np.median(np.diff([l["caja"][1] for l in g])) if len(g) > 1 else None
        bloques.append({
            "rol": "titulo" if (i == 0 and tam >= 1.5 * np.median([l["em"] for l in texto])) else "cuerpo",
            "texto_en": " ".join(l["texto"] for l in g),
            "texto_es": "",
            "peso": "bold" if g[0]["negrita"] else "regular",
            "tam_px": tam,
            "interlineado": round(float(paso) / tam, 2) if paso else None,
            "color": g[0]["color"],
            "caja": caja,
            "ancho_px": int(round(max(l["caja"][2] - l["caja"][0] for l in g) * 1.03)),
        })
    # espacio entre bloques en coordenadas de maquetado (ver render.dibujar_lineas)
    for prev, b in zip(bloques, bloques[1:]):
        tp, tn = prev["tam_px"], b["tam_px"]
        lp = tp * (prev["interlineado"] or cfg["render"]["interlineado"])
        ln = tn * (b["interlineado"] or cfg["render"]["interlineado"])
        top_n = b["caja"][1] - ln / 2 + 0.38 * tn
        bot_p = prev["caja"][3] + lp / 2 - 0.585 * tp
        b["espacio_antes"] = int(round(max(0, top_n - bot_p)))

    zonas = []
    if y_g is not None:
        filas = np.flatnonzero(resto.any(axis=1) & (np.arange(h) >= y_g))
        cols = np.flatnonzero(resto[y_g:].any(axis=0))
        if len(filas) and len(cols):
            caja = [int(cols[0]), int(y_g), int(cols[-1] + 1), int(filas[-1] + 1)]
            for l in otras:
                caja = [min(caja[0], l["caja"][0]), caja[1], max(caja[2], l["caja"][2]), max(caja[3], l["caja"][3])]
            etiquetas = ocr.leer_disperso(img, caja, cfg["ocr"]["escala_etiquetas"], cfg["ocr"]["idioma"])
            zonas.append({"caja": caja, "estrategia": "", "justificacion": "",
                          "etiquetas": [{"texto_en": e.texto, "texto_es": "", "caja": list(e.caja)}
                                        for e in etiquetas],
                          "lineas_ocr_bajo_grafico": [{"texto": l["texto"], "caja": l["caja"]} for l in otras]})

    zona_texto = None
    if bloques:
        zona_texto = [min(b["caja"][0] for b in bloques), min(b["caja"][1] for b in bloques),
                      max(b["caja"][2] for b in bloques), max(b["caja"][3] for b in bloques)]
    return {"zona_texto": zona_texto, "bloques": bloques, "zonas_grafico": zonas,
            "ocr_lineas": [l.a_dict() for l in crudas]}


def extraer(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    plan = leer_plan(rutas)
    motores = ocr.motores_disponibles(config["ocr"]["motores"])
    motor = motores[0]
    plan["motor_ocr"] = motor
    log(f"[extraer] {slug}: motor OCR = {motor} (disponibles: {motores})")
    paginas = {p["pagina"]: p for p in plan.get("paginas", [])}
    for s in plan["slides"]:
        img = np.array(Image.open(rutas.slides / f"{s['n']:02d}.png").convert("RGB"))
        fondo = np.array(paginas.get(s["pagina_origen"], {}).get("color_fondo", [255, 255, 255]))
        borrador = extraer_slide(img, fondo, config, motor)
        s["color_fondo"] = rgb_a_hex(fondo)
        if s.get("curado"):
            s["ocr_lineas"] = borrador["ocr_lineas"]
            log(f"  slide {s['n']:02d}: curada, solo se actualiza OCR crudo")
            continue
        s.update(borrador)
        log(f"  slide {s['n']:02d}: {len(borrador['bloques'])} bloques, {len(borrador['zonas_grafico'])} zonas de gráfico")
    guardar_plan(rutas, plan)
