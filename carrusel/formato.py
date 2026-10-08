"""Formato numérico argentino y verificación de cifras EN vs ES."""

from __future__ import annotations

import re

NBSP = " "  # espacio duro antes de %


def num_ar(valor: float, decimales: int | None = None) -> str:
    """1234.5 -> '1.234,5'. Si decimales es None se usan los mínimos necesarios (máx. 3)."""
    if decimales is None:
        texto = f"{valor:.3f}".rstrip("0").rstrip(".")
        decimales = len(texto.split(".")[1]) if "." in texto else 0
    texto = f"{abs(valor):,.{decimales}f}"
    texto = texto.replace(",", "\x00").replace(".", ",").replace("\x00", ".")
    return ("−" if valor < 0 else "") + texto


def pct_ar(valor: float, decimales: int | None = None, signo: bool = False) -> str:
    """0.5 en puntos porcentuales -> '0,5 %'. signo=True antepone '+'."""
    base = num_ar(valor, decimales)
    if signo and valor > 0:
        base = "+" + base
    return f"{base}{NBSP}%"


def usd_ar(valor: float, decimales: int | None = None) -> str:
    return f"US${NBSP}{num_ar(valor, decimales)}"


# --- verificación de cifras ---------------------------------------------------

_ESCALAS_EN = {"thousand": 1e3, "million": 1e6, "billion": 1e9, "trillion": 1e12}
_ESCALAS_ES = {"mil": 1e3, "millón": 1e6, "millones": 1e6, "billón": 1e12, "billones": 1e12,
               "mil millones": 1e9}

_RE_EN = re.compile(r"(\d[\d,]*(?:\.\d+)?)\s*(thousand|million|billion|trillion|[kKmMbB]\b)?", re.IGNORECASE)
_RE_ES = re.compile(r"(\d[\d.]*(?:,\d+)?)\s*(mil millones|millones|millón|billones|billón|mil\b)?")


def _valor_en(num: str, escala: str | None) -> float:
    v = float(num.replace(",", ""))
    if escala:
        e = escala.lower()
        v *= {"k": 1e3, "m": 1e6, "b": 1e9}.get(e, _ESCALAS_EN.get(e, 1))
    return v


def _valor_es(num: str, escala: str | None) -> float:
    # '10.000' -> 10000 ; '3.600' -> 3600 ; '0,5' -> 0.5 ; '1.5' (sin formatear) -> ambiguo
    if re.fullmatch(r"\d{1,3}(\.\d{3})+(,\d+)?", num) or "," in num:
        v = float(num.replace(".", "").replace(",", "."))
    else:
        v = float(num)
    if escala:
        v *= _ESCALAS_ES.get(escala.lower(), 1)
    return v


def cifras_en(texto: str) -> list[float]:
    return [_valor_en(n, e) for n, e in _RE_EN.findall(texto or "")]


def cifras_es(texto: str) -> list[float]:
    return [_valor_es(n, e) for n, e in _RE_ES.findall(texto or "")]


def cifras_faltantes(texto_en: str, texto_es: str) -> list[float]:
    """Cifras del original que no aparecen (con el mismo valor) en la traducción."""
    es = cifras_es(texto_es)
    faltan = []
    for v in cifras_en(texto_en):
        if not any(abs(v - w) <= 1e-9 * max(1.0, abs(v)) for w in es):
            faltan.append(v)
    return faltan


def formato_sospechoso(texto_es: str) -> list[str]:
    """Patrones de formato anglosajón que no deberían quedar en la traducción."""
    alertas = []
    for m in re.finditer(r"\d\.\d{1,2}(?!\d)", texto_es or ""):
        alertas.append(f"punto decimal: '{m.group(0)}'")
    for m in re.finditer(r"\d,\d{3}(?!\d)", texto_es or ""):
        alertas.append(f"coma de miles: '{m.group(0)}'")
    for m in re.finditer(r"\d%", texto_es or ""):
        alertas.append(f"falta espacio antes de %: '{m.group(0)}'")
    return alertas
