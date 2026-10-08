"""CLI: python -m carrusel <comando> <slug|link> [slug]

    descargar <link> [<link> ...]   baja uno o más carruseles de TikTok a entrada/<slug>/
    traducir <slug|link> [slug]     corre todos los pasos (con --desde / --hasta)
    <paso> <slug>                   corre un paso suelto
    marca                           genera los archivos del logo en marca/
"""

from __future__ import annotations

import argparse
import sys

from .comun import cargar_config, log

PASOS = ["preparar", "ordenar", "extraer", "graficos", "renderizar", "calidad", "entregar", "paleta", "memoria"]


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
    if nombre == "entregar":
        from .entregar import entregar
        return entregar
    if nombre == "paleta":
        from .paleta import paleta
        return paleta
    if nombre == "memoria":
        from .memoria import memoria
        return memoria
    raise ValueError(nombre)


def _es_link(texto: str) -> bool:
    return texto.startswith(("http://", "https://"))


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="python -m carrusel", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("comando", choices=["descargar", "marca"] + PASOS + ["traducir"])
    p.add_argument("args", nargs="*", help="slug, link(s) de TikTok, o link + slug")
    p.add_argument("--desde", choices=PASOS, help="con 'traducir': empezar desde este paso")
    p.add_argument("--hasta", choices=PASOS, help="con 'traducir': terminar en este paso (incluido)")
    a = p.parse_args(argv)
    config = cargar_config()

    if a.comando == "marca":
        from .marca import marca
        marca("-", config)
        return 0
    if a.comando == "descargar":
        from .descargar import descargar
        links = [x for x in a.args if _es_link(x)]
        if not links:
            raise SystemExit("'descargar' necesita al menos un link: python -m carrusel descargar <link> [<link> ...]")
        # 'descargar <link> <slug>' (un link con nombre) o 'descargar <link1> <link2> ...'
        nombre = a.args[1] if len(a.args) == 2 and not _es_link(a.args[1]) else None
        fallidos = 0
        for link in links:
            try:
                slug = descargar(link, nombre)
                print(f"SLUG {slug} {link}", flush=True)
            except (Exception, SystemExit) as e:
                fallidos += 1
                print(f"ERROR {link} {e}", flush=True)
        return 1 if fallidos else 0

    if not a.args:
        raise SystemExit(f"'{a.comando}' necesita un slug (o un link con 'traducir')")
    slug = a.args[0]
    if _es_link(slug):
        if a.comando != "traducir":
            raise SystemExit("con un link usá 'descargar' o 'traducir'")
        from .descargar import descargar
        slug = descargar(slug, a.args[1] if len(a.args) > 1 else None)
    if a.comando == "traducir":
        ini = PASOS.index(a.desde) if a.desde else 0
        fin = PASOS.index(a.hasta) + 1 if a.hasta else len(PASOS)
        pasos = PASOS[ini:fin]
    else:
        pasos = [a.comando]
    for nombre in pasos:
        _paso(nombre)(slug, config)
    log("listo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
