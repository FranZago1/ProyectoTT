"""Rutas, configuración y lectura/escritura de plan.json."""

from __future__ import annotations

import json
import unicodedata
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
EXT_IMAGEN = {".png", ".jpg", ".jpeg", ".webp"}


def cargar_config() -> dict:
    with open(RAIZ / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def nfc(texto: str) -> str:
    return unicodedata.normalize("NFC", texto)


class Rutas:
    def __init__(self, slug: str, config: dict | None = None):
        self.slug = slug
        self.config = config or cargar_config()
        cfg_slug = (self.config.get("carruseles") or {}).get(slug, {})
        self.entrada = RAIZ / "entrada" / cfg_slug.get("entrada", slug)
        self.paginas_elegidas = cfg_slug.get("paginas")
        self.trabajo = RAIZ / "trabajo" / slug
        self.paginas = self.trabajo / "paginas"     # páginas recortadas, orden de origen
        self.slides = self.trabajo / "slides"       # 01..07 en orden
        self.plan = self.trabajo / "plan.json"
        self.salida = RAIZ / "salida" / slug
        self.graficos = self.salida / "graficos"
        self.memoria = RAIZ / "memoria"

    def crear(self) -> None:
        for d in (self.trabajo, self.paginas, self.slides, self.salida, self.graficos):
            d.mkdir(parents=True, exist_ok=True)


def leer_plan(rutas: Rutas) -> dict:
    if rutas.plan.exists():
        with open(rutas.plan, encoding="utf-8") as f:
            return json.load(f)
    return {"slug": rutas.slug, "slides": []}


def guardar_plan(rutas: Rutas, plan: dict) -> None:
    rutas.trabajo.mkdir(parents=True, exist_ok=True)
    with open(rutas.plan, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)


def hex_a_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_a_hex(rgb) -> str:
    return "#{:02X}{:02X}{:02X}".format(*(int(round(c)) for c in rgb[:3]))


def log(msg: str) -> None:
    print(msg, flush=True)
