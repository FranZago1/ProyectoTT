"""Utilidades comunes para los scripts de curación de carruseles de TikTok (scripts/curar_*.py).

Cada script define `SLUG` y `curar(plan)` y llama a `ejecutar(SLUG, curar)`.
"""

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from curar_referencia import CFG, NB, RAIZ, bloque, pct, tam_ancho, zona_texto  # noqa: E402,F401
from carrusel.render import fuente  # noqa: E402

SERIF = "LiberationSerif-Regular.ttf"
FOTO = ("La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o "
        "reemplazarla en Canva.")


def et(en, es, caja, tam, **kw):
    """Etiqueta de gráfico (texto_en, texto_es, caja, tam_px y opciones de render)."""
    return {"texto_en": en, "texto_es": es, "caja": caja, "tam_px": tam, **kw}


def tam_para(en, ancho_en, es=None, ancho_max=None, peso="regular", archivo=None):
    """Tamaño que reproduce el ancho medido del texto en inglés; si el español (línea más larga)
    excede `ancho_max`, se reduce hasta que entre."""
    t = tam_ancho(max(en.split("\n"), key=len), ancho_en, peso, archivo)
    if es and ancho_max:
        w = max(fuente(CFG, peso, 100, archivo).getlength(l) for l in es.split("\n")) * t / 100
        if w > ancho_max:
            t = round(t * ancho_max / w, 1)
    return t


def con_caja(auto, i, caja, **kw):
    """Copia un bloque del borrador con otra caja (bloques que el OCR asignó mal)."""
    b = copy.deepcopy(auto[i])
    b["caja"] = caja
    b["ancho_px"] = caja[2] - caja[0]
    b.update(kw)
    return b


def nuevo(rol, en, es, caja, peso="regular", tam=34, **kw):
    """Bloque escrito a mano (cuando el borrador no tiene uno utilizable)."""
    return {"rol": rol, "texto_en": en, "texto_es": es, "peso": peso, "tam_px": tam, "interlineado": 1.44,
            "color": "#1D1D1D", "caja": caja, "ancho_px": caja[2] - caja[0], **kw}


def glosario(pares):
    return [{"en": en, "es": es} for en, es in pares]


def ejecutar(slug, curar):
    ruta = RAIZ / "trabajo" / slug / "plan.json"
    plan = json.loads(ruta.read_text(encoding="utf-8"))
    borrador = ruta.with_name("plan_borrador.json")
    if not borrador.exists() or not plan["slides"][0].get("curado"):
        borrador.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    plan = json.loads(borrador.read_text(encoding="utf-8"))
    curar(plan)
    for s in plan["slides"]:
        s["zona_texto"] = zona_texto(s["bloques"]) if s["bloques"] else None
        s["curado"] = True
    ruta.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"curado: {ruta}")


def pad(caja, n=3):
    """Caja agrandada n px por lado (para borrar también el antialias del texto original)."""
    x0, y0, x1, y1 = caja
    return [x0 - n, y0 - n, x1 + n, y1 + n]
