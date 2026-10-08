"""CLI: python -m carrusel <comando> <slug>"""

from __future__ import annotations

import argparse
import sys

from .comun import cargar_config, log

PASOS = ["preparar", "ordenar", "extraer", "graficos", "renderizar", "calidad", "paleta", "memoria"]


def _paso(nombre: str):
    if nombre == "preparar":
        from .preparar import preparar
        return preparar
    if nombre == "ordenar":
        from .preparar import ordenar
        return ordenar
    if nombre == "extraer":
        from .extraer import extraer
        return extraer
    if nombre == "graficos":
        from .graficos import graficos
        return graficos
    if nombre == "renderizar":
        from .render import renderizar
        return renderizar
    if nombre == "calidad":
        from .calidad import calidad
        return calidad
    if nombre == "paleta":
        from .paleta import paleta
        return paleta
    if nombre == "memoria":
        from .memoria import memoria
        return memoria
    raise ValueError(nombre)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="python -m carrusel",
                                description="Traductor de carruseles de Instagram EN -> ES-AR")
    p.add_argument("comando", choices=["descargar", "marca"] + PASOS + ["traducir"],
                   help="paso a ejecutar; 'traducir' corre todos en orden")
    p.add_argument("slug", nargs="?", default="-", help="nombre del carrusel (entrada/<slug>/), o un link de TikTok con "
                                "'descargar' / 'traducir'")
    p.add_argument("nombre", nargs="?", help="con un link: slug a usar (por defecto tiktok-<usuario>-<id>)")
    p.add_argument("--desde", choices=PASOS, help="con 'traducir': empezar desde este paso")
    a = p.parse_args(argv)
    config = cargar_config()
    if a.slug.startswith(("http://", "https://")):
        from .descargar import descargar
        a.slug = descargar(a.slug, a.nombre)
        if a.comando == "descargar":
            return 0
    if a.comando == "marca":
        from .marca import marca
        marca(a.slug, config)
        return 0
    if a.comando == "descargar":
        raise SystemExit("'descargar' necesita un link: python -m carrusel descargar <url> [slug]")
    if a.comando == "traducir":
        pasos = PASOS[PASOS.index(a.desde):] if a.desde else PASOS
    else:
        pasos = [a.comando]
    for nombre in pasos:
        _paso(nombre)(a.slug, config)
    log("listo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
