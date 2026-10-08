"""Paso 7: control de calidad automático + revisar.md + hoja de contactos para la revisión visual.

Lo automático no reemplaza mirar cada NN_es.png: la hoja salida/<slug>/control.png junta original y
traducción lado a lado para esa revisión.
"""

from __future__ import annotations

import re

import numpy as np
from fontTools.ttLib import TTFont
from PIL import Image

from . import ocr
from .comun import RAIZ, Rutas, guardar_plan, leer_plan, log
from .formato import cifras_faltantes, formato_sospechoso

PALABRAS_EN = {"the", "and", "of", "to", "you", "your", "is", "are", "that", "what", "with", "for", "it", "this",
               "they", "was", "from", "every", "more", "than", "how", "why", "who", "be", "just", "only",
               "what's", "don't", "doesn't", "can't", "it's", "you're", "math", "bet", "wealth", "flip", "flips",
               "heads", "tails", "loss", "people", "person", "model", "models", "curve", "market"}
_CMAPS: dict = {}


def _cmap(config: dict, archivo: str) -> set[int]:
    if archivo not in _CMAPS:
        _CMAPS[archivo] = set(TTFont(str(RAIZ / config["render"]["fuente_dir"] / archivo)).getBestCmap())
    return _CMAPS[archivo]


def _dentro(caja, zonas) -> bool:
    cx, cy = (caja[0] + caja[2]) / 2, (caja[1] + caja[3]) / 2
    return any(z[0] <= cx <= z[2] and z[1] <= cy <= z[3] for z in zonas)


def revisar_slide(s: dict, img_es: np.ndarray, config: dict, motor: str) -> list[str]:
    problemas: list[str] = []
    h, w = img_es.shape[:2]
    fondo = np.array([int(s.get("color_fondo", "#FFFFFF")[i:i + 2], 16) for i in (1, 3, 5)])

    # 1) restos de inglés fuera de las zonas que conservan texto a propósito (C sin traducir, D)
    zonas_conservadas = [z["caja"] for z in s.get("zonas_grafico", []) if z.get("estrategia") in ("C", "D")]
    for l in ocr.leer(img_es, motor, "en", 0.5):
        if _dentro(l.caja, zonas_conservadas):
            continue
        palabras = re.findall(r"[A-Za-z']+", l.texto.lower())
        en = [p for p in palabras if p in PALABRAS_EN]
        if len(en) >= 2:
            problemas.append(f"posible texto en inglés: «{l.texto}» en {l.caja}")

    # 2) restos de UI de Instagram: píldora del contador (misma detección que en preparar) y flecha '<'
    from .preparar import eliminar_contador
    _, hay_contador = eliminar_contador(img_es, fondo.astype(np.float32), config["preparar"])
    if hay_contador:
        problemas.append("posible resto de UI: contador 'n / 7'")
    reg = img_es[:int(0.045 * h), :int(0.09 * w)].astype(int)
    if (np.abs(reg - fondo).max(axis=2) > 40).sum() > 30:
        problemas.append("posible resto de UI: flecha '<' arriba a la izquierda")

    # 3) glifos: todos los caracteres usados existen en la fuente
    textos = [(b.get("texto_es", ""), config["render"]["fuentes"].get(b.get("peso", "regular"), "Inter-Regular.otf"))
              for b in s.get("bloques", [])]
    for z in s.get("zonas_grafico", []):
        for e in z.get("etiquetas", []):
            if e.get("texto_es") and not e.get("conservar"):
                textos.append((e["texto_es"], e.get("fuente") or config["render"]["fuentes"]["regular"]))
    for t, archivo in textos:
        faltan = sorted({c for c in t.replace("**", "").replace("\n", "") if ord(c) not in _cmap(config, archivo)})
        if faltan:
            problemas.append(f"caracteres sin glifo en {archivo}: {' '.join(faltan)}")

    # 4) cifras: los valores del original deben estar en la traducción, con formato argentino
    for b in s.get("bloques", []):
        falt = cifras_faltantes(b.get("texto_en", ""), b.get("texto_es", "").replace(" ", " "))
        if falt:
            problemas.append(f"cifras del original que no aparecen en la traducción: {falt} "
                             f"(«{b.get('texto_en', '')[:60]}…»)")
        for a in formato_sospechoso(b.get("texto_es", "").replace(" ", " ")):
            problemas.append(f"formato numérico: {a}")

    # 5) el texto no pisa el gráfico
    rt = s.get("_render_texto")
    tops = [z["caja"][1] for z in s.get("zonas_grafico", [])]
    if rt and tops:
        fin = rt["y"] + rt["alto_total"]
        if fin > min(tops) - 4:
            problemas.append(f"el texto llega a y={int(fin)} y el gráfico empieza en y={min(tops)}")
    for a in s.get("avisos_render", []):
        if "NO ENTRA" in a:
            problemas.append(a)
    return problemas


def hoja_control(rutas: Rutas, plan: dict) -> None:
    w0, h0 = Image.open(rutas.salida / f"{plan['slides'][0]['n']:02d}_es.png").size
    W, H = 360, int(round(360 * h0 / w0))
    filas = (len(plan["slides"]) + 3) // 4
    hoja = Image.new("RGB", (W * 2 * 4 + 50, (H + 10) * filas), (200, 200, 200))
    for i, s in enumerate(plan["slides"]):
        x = (i % 4) * (2 * W + 12)
        y = (i // 4) * (H + 10)
        hoja.paste(Image.open(rutas.slides / f"{s['n']:02d}.png").resize((W, H), Image.LANCZOS), (x, y))
        hoja.paste(Image.open(rutas.salida / f"{s['n']:02d}_es.png").resize((W, H), Image.LANCZOS), (x + W + 2, y))
    hoja.save(rutas.salida / "control.png")


def escribir_revisar(rutas: Rutas, plan: dict) -> None:
    out = [f"# Revisar — {plan.get('titulo_es') or rutas.slug}", "",
           "Pendientes y alertas antes de publicar. Cada ítem dice qué hacer en Canva.", ""]
    for s in plan["slides"]:
        items = []
        for z in s.get("zonas_grafico", []):
            if z.get("estrategia") == "D":
                items.append("**Rehacer en Canva**: gráfico conservado en inglés (estrategia D); la traducción "
                             "completa está en `textos_es.md`.")
            if z.get("estrategia") == "B" and (z.get("datos") or {}).get("semilla") is not None:
                items.append("Gráfico **regenerado, no idéntico** (simulación con semilla fija "
                             f"{z['datos']['semilla']}).")
        for a in s.get("avisos_render", []):
            items.append(f"Maquetación: {a}.")
        for p in s.get("control_calidad", []):
            items.append(f"Control automático: {p}.")
        for n in s.get("notas_revisar", []):
            items.append(n)
        out.append(f"## Slide {s['n']:02d}" + (f" — {s['funcion']}" if s.get("funcion") else ""))
        out.append("")
        out += [f"- {i}" for i in items] or ["- Sin pendientes."]
        out.append("")
    (rutas.salida / "revisar.md").write_text("\n".join(out), encoding="utf-8")


def calidad(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    plan = leer_plan(rutas)
    motor = ocr.motores_disponibles(config["ocr"]["motores"])[0]
    total = 0
    for s in plan["slides"]:
        img = np.array(Image.open(rutas.salida / f"{s['n']:02d}_es.png").convert("RGB"))
        problemas = revisar_slide(s, img, config, motor)
        s["control_calidad"] = problemas
        total += len(problemas)
        log(f"  slide {s['n']:02d}: " + ("; ".join(problemas) if problemas else "ok"))
    guardar_plan(rutas, plan)
    escribir_revisar(rutas, plan)
    hoja_control(rutas, plan)
    log(f"[calidad] {slug}: {total} observaciones; revisar.md y control.png en {rutas.salida}")
