"""Paso de entrega: copia solo lo que se publica a listos/<slug>/ (una carpeta por carrusel).

listos/<slug>/
    01.png … NN.png     slides finales traducidas, con el logo
    revisar.md          pendientes y alertas antes de publicar
    textos_es.md        textos para editar en Canva
    fuente.txt          link original y autor (si se descargó de TikTok)
"""

from __future__ import annotations

import shutil

from .comun import RAIZ, Rutas, leer_plan, log


def entregar(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    plan = leer_plan(rutas)
    destino = RAIZ / "listos" / slug
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    n = 0
    for s in plan["slides"]:
        origen = rutas.salida / f"{s['n']:02d}_es.png"
        if origen.exists():
            shutil.copy(origen, destino / f"{s['n']:02d}.png")
            n += 1
    for nombre in ("revisar.md", "textos_es.md"):
        if (rutas.salida / nombre).exists():
            shutil.copy(rutas.salida / nombre, destino / nombre)
    fuente = plan.get("fuente") or {}
    if fuente:
        (destino / "fuente.txt").write_text(
            f"Original: {fuente.get('url_canonica') or fuente.get('url')}\n"
            f"Autor: {fuente.get('autor', '')} (@{fuente.get('usuario', '')})\n"
            f"Descripción: {fuente.get('descripcion', '')}\n", encoding="utf-8")
    log(f"[entregar] {slug}: {n} slides en {destino}")
