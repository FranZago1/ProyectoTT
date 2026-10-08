"""Paso 6: reconstrucción del fondo, recomposición del texto en español y aplicación de la estrategia
de cada gráfico. Genera salida/<slug>/NN_es.png, NN_limpia.png, graficos/ y textos_es.md."""

from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .comun import RAIZ, Rutas, guardar_plan, hex_a_rgb, leer_plan, log
from .fondo import borrar_regiones

CAP_EM = 0.727  # altura de mayúsculas de Inter
_FUENTES: dict = {}


def fuente(config: dict, peso: str, tam: float, archivo: str | None = None) -> ImageFont.FreeTypeFont:
    """peso: clave de config.render.fuentes; archivo: nombre de un archivo en fuentes/ (opcional)."""
    clave = (archivo or peso, round(tam, 1))
    if clave not in _FUENTES:
        archivo = archivo or config["render"]["fuentes"].get(peso) or config["render"]["fuentes"]["regular"]
        ruta = RAIZ / config["render"]["fuente_dir"] / archivo
        _FUENTES[clave] = ImageFont.truetype(str(ruta), size=max(1, int(round(tam))))
    return _FUENTES[clave]


# --- texto enriquecido y reflujo ------------------------------------------------------

@dataclass
class Palabra:
    texto: str
    negrita: bool
    salto: bool = False  # salto de línea forzado antes de esta palabra


def tokenizar(texto: str) -> list[Palabra]:
    """'**negrita**' marca tramos en negrita; '\\n' fuerza salto. El espacio duro (U+00A0) no corta."""
    palabras: list[Palabra] = []
    negrita = False
    salto = False
    ultimo = " "  # último carácter de texto visto
    for parte in re.split(r"(\*\*|\n)", texto):
        if parte == "**":
            negrita = not negrita
            continue
        if parte == "\n":
            salto, ultimo = True, " "
            continue
        if not parte:
            continue
        for i, t in enumerate(parte.split(" ")):
            if not t:
                continue
            if i == 0 and ultimo != " " and palabras and not salto:
                # continúa la palabra anterior (p. ej. '**$90**.' -> puntuación pegada a la negrita)
                palabras.append(Palabra(t, negrita, None))
            else:
                palabras.append(Palabra(t, negrita, salto))
            salto = False
        ultimo = parte[-1]
    return palabras


def _peso_negrita(base: str) -> str:
    return {"regular": "bold", "medium": "bold", "semibold": "bold", "bold": "extrabold"}.get(base, "bold")


def maquetar(texto: str, peso: str, tam: float, ancho: float, config: dict) -> list[list[tuple[str, str, float]]]:
    """Devuelve líneas: [(texto, peso, ancho_px)] por tramo; los tramos llevan su espacio previo."""
    lineas: list[list[tuple[str, str, float]]] = [[]]
    ancho_linea = 0.0
    espacio = fuente(config, peso, tam).getlength(" ")
    for p in tokenizar(texto):
        w_peso = _peso_negrita(peso) if p.negrita else peso
        f = fuente(config, w_peso, tam)
        w = f.getlength(p.texto)
        sin_espacio = p.salto is None
        sep = 0.0 if (sin_espacio or not lineas[-1]) else espacio
        if p.salto or (lineas[-1] and not sin_espacio and ancho_linea + sep + w > ancho):
            lineas.append([])
            ancho_linea, sep = 0.0, 0.0
        prefijo = " " if sep else ""
        lineas[-1].append((prefijo + p.texto, w_peso, sep + w))
        ancho_linea += sep + w
    return [l for l in lineas if l]


def maquetar_balanceado(texto: str, peso: str, tam: float, ancho: float, config: dict, max_lineas: int = 3,
                        rol: str = "pie"):
    """Como maquetar, pero en bloques de 2-3 líneas busca el ancho mínimo que conserva la cantidad de líneas
    (evita palabras huérfanas en citas, subtítulos y pies)."""
    lineas = maquetar(texto, peso, tam, ancho, config)
    if "\n" in texto or len(lineas) <= 1:
        return lineas
    if rol in ("cuerpo", "destacado") and len(lineas) > 2:
        max_lineas = 2
    if len(lineas) > max_lineas:
        # párrafo largo: solo se evita la viuda (una palabra sola en el último renglón)
        if len(lineas[-1]) >= 2:
            return lineas
        for k in range(1, 16):
            prueba = maquetar(texto, peso, tam, ancho * (1 - 0.01 * k), config)
            if len(prueba) == len(lineas) and len(prueba[-1]) >= 2:
                return prueba
        return lineas
    lo, hi = ancho * 0.5, ancho
    for _ in range(14):
        mid = (lo + hi) / 2
        if len(maquetar(texto, peso, tam, mid, config)) == len(lineas):
            hi = mid
        else:
            lo = mid
    return maquetar(texto, peso, tam, hi + 0.5, config)


def dibujar_lineas(draw: ImageDraw.ImageDraw, lineas, x_centro: float, y_top: float, tam: float,
                   interlineado: float, color, config: dict, alineacion: str = "centro") -> float:
    alto_linea = tam * interlineado
    for i, linea in enumerate(lineas):
        ancho = sum(w for _, _, w in linea)
        x = x_centro - ancho / 2 if alineacion == "centro" else x_centro
        base = y_top + i * alto_linea + (alto_linea + CAP_EM * tam) / 2
        for txt, peso, w in linea:
            draw.text((x, base), txt, font=fuente(config, peso, tam), fill=color, anchor="ls")
            x += w
    return len(lineas) * alto_linea


# --- composición de la zona de texto -----------------------------------------------

def _params_bloque(b: dict, config: dict) -> tuple[str, float, float, tuple]:
    rol = b.get("rol", "cuerpo")
    r = config["render"]
    peso = b.get("peso") or r["peso_por_rol"].get(rol, "regular")
    tam = b.get("tam_px") or r["tam_por_rol"].get(rol, 34)
    inter = b.get("interlineado") or r["interlineado"]
    color = hex_a_rgb(b.get("color") or (r["color_pie"] if rol == "pie" else r["color_texto"]))
    return peso, float(tam), float(inter), color


def componer_zona(bloques: list[dict], escala: float, ancho: float, config: dict):
    """Mide la altura total de los bloques reflujo a una escala dada."""
    piezas = []
    total = 0.0
    for i, b in enumerate(bloques):
        peso, tam, inter, color = _params_bloque(b, config)
        tam *= escala
        lineas = maquetar_balanceado(b["texto_es"], peso, tam, b.get("ancho_max_px") or ancho, config,
                                     rol=b.get("rol", "cuerpo"))
        alto = len(lineas) * tam * inter
        antes = 0.0 if i == 0 else float(b.get("espacio_antes", config["render"]["espacio_entre_bloques"] * tam)) * escala
        piezas.append((b, lineas, tam, inter, color, antes))
        total += antes + alto
    return piezas, total


def renderizar_slide(img: np.ndarray, s: dict, config: dict, graficos_b: dict) -> tuple[np.ndarray, np.ndarray, list[str], dict]:
    """Devuelve (slide_es, slide_limpia, avisos, recortes_de_graficos)."""
    h, w = img.shape[:2]
    r = config["render"]
    avisos: list[str] = []
    fondo_rgb = hex_a_rgb(s.get("color_fondo", "#FFFFFF"))
    margen = r["margen_borrado_px"]

    reflujo = [b for b in s.get("bloques", []) if not b.get("fijo") and b.get("rol") != "pie"]
    fijos = [b for b in s.get("bloques", []) if b.get("fijo") or b.get("rol") == "pie"]
    zonas = s.get("zonas_grafico", [])

    # 1) borrar texto original: zona de texto completa y bloques fijos
    cajas_borrar = []
    if s.get("zona_texto"):
        cajas_borrar.append(s["zona_texto"])
    cajas_borrar += [b["caja"] for b in fijos if b.get("caja")]
    base = borrar_regiones(img, cajas_borrar, margen=margen) if cajas_borrar else img.copy()

    # 2) gráficos
    recortes = {}
    for k, z in enumerate(zonas, start=1):
        est = z.get("estrategia", "C")
        x0, y0, x1, y1 = z.get("caja_salida") or z["caja"]
        if est == "B" and k in graficos_b:
            # se borra la zona original completa y se pega el gráfico regenerado
            base = borrar_regiones(base, [z["caja"]], margen=4, inpaint_residual=False)
            g = np.array(Image.open(graficos_b[k]).convert("RGB"))
            base[y0:y0 + g.shape[0], x0:x0 + g.shape[1]] = g[:min(g.shape[0], h - y0), :min(g.shape[1], w - x0)]
        elif est in ("A", "C"):
            et = [e for e in z.get("etiquetas", []) if e.get("texto_es") not in (None, "", e.get("texto_en"))
                  and not e.get("conservar")]
            if et:
                planas = [e for e in et if e.get("borrado", "fondo") == "fondo"]
                if planas:
                    base = borrar_regiones(base, [e.get("caja_borrar") or e["caja"] for e in planas],
                                           margen=e_margen(planas), inpaint_residual=False)
                for e in et:
                    if e.get("borrado") == "inpaint":
                        base = borrar_tinta(base, e.get("caja_borrar") or e["caja"], fondo_rgb)
                    elif e.get("borrado") == "local":
                        # texto sobre una caja de color: la referencia es el color dominante de la caja
                        x0, y0, x1, y1 = e.get("caja_borrar") or e["caja"]
                        local = np.median(base[y0:y1, x0:x1].reshape(-1, 3), axis=0)
                        base = borrar_tinta(base, [x0, y0, x1, y1], local)
                base = dibujar_etiquetas(base, et, config)
        recortes[k] = (x0, y0, x1, y1)

    limpia = base.copy()

    # 3) zona de texto recompuesta
    pil = Image.fromarray(base)
    draw = ImageDraw.Draw(pil)
    if reflujo:
        zt = s.get("zona_texto") or [0, r["margen_superior_min"], w, h // 2]
        # columna: la más ancha del original (≈ 75-78 % de la slide), o la de config
        medidos = [b.get("ancho_px", 0) for b in reflujo if b.get("rol") != "titulo"]
        ancho_col = min(max(medidos + [0]) or r["ancho_columna"] * w, r["ancho_columna_max"] * w)
        tope_inf = min([z["caja"][1] for z in zonas if z["caja"][1] > zt[1]] + [h]) - r["separacion_grafico_min"]
        # zona disponible: la original, más la mitad del aire hasta el gráfico
        z_top = zt[1]
        z_bot = min(tope_inf, zt[3] + max(0, (tope_inf - zt[3]) // 2))
        if not zonas:
            z_bot = max(z_bot, h - 2 * r["margen_superior_min"])
        escala, piezas, total = 1.0, None, None
        while True:
            piezas, total = componer_zona(reflujo, escala, ancho_col, config)
            if total <= z_bot - z_top or escala <= r["reduccion_minima"] + 1e-6:
                break
            escala = round(escala - 0.02, 2)
        if escala < 1.0:
            avisos.append(f"texto reducido al {int(round(escala * 100))} % para entrar en la zona")
        # posición: el primer renglón arranca donde arrancaba el original
        b0, l0, t0, i0 = piezas[0][0], None, piezas[0][2], piezas[0][3]
        top_orig = zt[1] - (t0 * i0) / 2 + 0.38 * t0
        alto_orig = zt[3] - top_orig + 0.2 * t0
        if total <= alto_orig:
            # entra en el lugar del original: se centra en ese mismo alto
            y = top_orig + (alto_orig - total) / 2 if r["alineacion_vertical"] == "centro" else top_orig
        elif top_orig + total <= z_bot:
            y = top_orig  # crece hacia abajo usando el aire hasta el gráfico
        else:
            # extender hacia arriba si hay aire; después, usar todo el aire hasta el gráfico
            y = max(r["margen_superior_min"], z_bot - total)
            if y < top_orig:
                avisos.append(f"zona de texto extendida hacia arriba {int(top_orig - y)} px")
            if y + total > z_bot + 1:
                y = max(r["margen_superior_min"], min(y, tope_inf - total))
                avisos.append(f"zona de texto extendida hasta {r['separacion_grafico_min']} px del gráfico")
                if y + total > tope_inf + 1:
                    avisos.append("EL TEXTO NO ENTRA: acortar la redacción (desborda "
                                  f"{int(y + total - tope_inf)} px)")
        z_top = y
        x_c = w / 2
        for b, lineas, tam, inter, color, antes in piezas:
            y += antes
            y += dibujar_lineas(draw, lineas, x_c, y, tam, inter, color, config)
        s["_render_texto"] = {"escala": escala, "alto_total": round(total, 1), "y": int(z_top), "limite": int(z_bot)}

    # 4) bloques fijos (pies, rótulos sueltos) en su lugar
    for b in fijos:
        peso, tam, inter, color = _params_bloque(b, config)
        x0, y0, x1, y1 = b["caja"]
        ancho = b.get("ancho_px") or max(x1 - x0, r["ancho_columna"] * w)
        lineas = maquetar_balanceado(b["texto_es"], peso, tam, ancho, config)
        cx = min(max((x0 + x1) / 2, ancho / 2 + 20), w - ancho / 2 - 20)
        alto = len(lineas) * tam * inter
        top = (y0 + y1) / 2 - alto / 2 if b.get("centrar_vertical", True) else y0
        dibujar_lineas(draw, lineas, cx, top, tam, inter, color, config)
    return np.array(pil), limpia, avisos, recortes


def borrar_tinta(img: np.ndarray, caja, fondo_rgb) -> np.ndarray:
    """Borra solo los píxeles de tinta de una caja (texto sobre líneas finas) por inpainting."""
    import cv2
    x0, y0, x1, y1 = caja
    sub = img[y0:y1, x0:x1].astype(int)
    tinta = (np.abs(sub - np.array(fondo_rgb)).max(axis=2) > 40).astype(np.uint8)
    tinta = cv2.dilate(tinta, np.ones((3, 3), np.uint8))
    mascara = np.zeros(img.shape[:2], np.uint8)
    mascara[y0:y1, x0:x1] = tinta * 255
    return cv2.inpaint(img, mascara, 4, cv2.INPAINT_TELEA)


def e_margen(etiquetas: list[dict]) -> int:
    return int(min(e.get("margen_borrado", 4) for e in etiquetas))


def dibujar_etiquetas(img: np.ndarray, etiquetas: list[dict], config: dict) -> np.ndarray:
    pil = Image.fromarray(img).convert("RGBA")
    for e in etiquetas:
        x0, y0, x1, y1 = e["caja"]
        tam = float(e.get("tam_px") or max(10, (y1 - y0) * 0.9))
        peso = e.get("peso", "regular")
        color = hex_a_rgb(e.get("color", "#555555"))
        f = fuente(config, peso, tam, e.get("fuente"))
        lineas = e["texto_es"].split("\n")
        ancho = max(f.getlength(l) for l in lineas)
        alto_l = tam * e.get("interlineado", 1.2)
        capa = Image.new("RGBA", (int(ancho + 8 + 2 * e.get("halo", 0)), int(alto_l * len(lineas) + 8)), (0, 0, 0, 0))
        d = ImageDraw.Draw(capa)
        halo = int(e.get("halo", 0))
        fondo_halo = hex_a_rgb(e.get("color_halo", "#FFFFFF")) + (255,)
        for i, l in enumerate(lineas):
            ax = {"centro": (capa.width / 2, "ms"), "izquierda": (4, "ls"), "derecha": (capa.width - 4, "rs")}
            xx, anc = ax[e.get("alineacion", "centro")]
            d.text((xx, 4 + i * alto_l + (alto_l + CAP_EM * tam) / 2), l, font=f, fill=color + (255,), anchor=anc,
                   stroke_width=halo, stroke_fill=fondo_halo)
            if halo:
                d.text((xx, 4 + i * alto_l + (alto_l + CAP_EM * tam) / 2), l, font=f, fill=color + (255,), anchor=anc)
        if e.get("rotacion"):
            capa = capa.rotate(e["rotacion"], expand=True, resample=Image.BICUBIC)
        al = e.get("alineacion", "centro")
        if e.get("rotacion"):
            px, py = (x0 + x1) / 2 - capa.width / 2, (y0 + y1) / 2 - capa.height / 2
        elif al == "izquierda":
            px, py = x0 - 4, (y0 + y1) / 2 - capa.height / 2
        elif al == "derecha":
            px, py = x1 - capa.width + 4, (y0 + y1) / 2 - capa.height / 2
        else:
            px, py = (x0 + x1) / 2 - capa.width / 2, (y0 + y1) / 2 - capa.height / 2
        dx, dy = e.get("desplazamiento", [0, 0])
        pil.alpha_composite(capa, (int(round(px + dx)), int(round(py + dy))))
    return np.array(pil.convert("RGB"))


# --- textos_es.md ---------------------------------------------------------------------

def _plano(t: str) -> str:
    return (t or "").replace(" ", " ")


def escribir_textos(rutas: Rutas, plan: dict) -> None:
    out = [f"# Textos en español — {plan.get('titulo_es') or rutas.slug}", "",
           "Listos para copiar en Canva. Las negritas están marcadas con **…**.", ""]
    for s in plan["slides"]:
        out.append(f"## Slide {s['n']:02d}" + (f" — {s['funcion']}" if s.get("funcion") else ""))
        out.append("")
        for b in s.get("bloques", []):
            out.append(f"*{b.get('rol', 'cuerpo')}*")
            out.append("")
            texto = _plano(b.get("texto_es", "")).replace("\n", "  \n")
            if b.get("peso") in ("bold", "extrabold") and b.get("rol") not in ("titulo",) and "**" not in texto:
                texto = f"**{texto}**"
            out.append(texto)
            out.append("")
        for k, z in enumerate(s.get("zonas_grafico", []), start=1):
            textos = [e for e in z.get("etiquetas", []) if e.get("texto_es") and not e.get("conservar")]
            datos = z.get("datos") or {}
            if not textos and not z.get("textos_es") and not datos:
                continue
            out.append(f"*gráfico {k} (estrategia {z.get('estrategia')})*")
            out.append("")
            for e in textos:
                out.append(f"- {_plano(e['texto_es']).replace(chr(10), ' / ')}")
            for t in z.get("textos_es", []):
                out.append(f"- {_plano(t)}")
            out.append("")
    (rutas.salida / "textos_es.md").write_text("\n".join(out), encoding="utf-8")


# --- comando --------------------------------------------------------------------------

def renderizar(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    rutas.crear()
    plan = leer_plan(rutas)
    for viejo in rutas.graficos.glob("*.png"):
        viejo.unlink()
    for s in plan["slides"]:
        faltan = [b for b in s.get("bloques", []) if not b.get("texto_es")]
        if faltan:
            raise SystemExit(f"slide {s['n']:02d}: hay bloques sin texto_es; completá plan.json")
        img = np.array(Image.open(rutas.slides / f"{s['n']:02d}.png").convert("RGB"))
        graficos_b = {k: rutas.trabajo / "graficos" / f"{s['n']:02d}_{k}.png"
                      for k, z in enumerate(s.get("zonas_grafico", []), start=1) if z.get("estrategia") == "B"}
        es, limpia, avisos, recortes = renderizar_slide(img, s, config, graficos_b)
        if (config.get("marca") or {}).get("activa"):
            from .marca import aplicar_marca
            zonas = [z.get("caja_salida") or z["caja"] for z in s.get("zonas_grafico", [])]
            (es, limpia), aviso = aplicar_marca([es, limpia], hex_a_rgb(s.get("color_fondo", "#FFFFFF")), config,
                                                prohibidas=zonas)
            avisos.append(aviso)
        Image.fromarray(es).save(rutas.salida / f"{s['n']:02d}_es.png")
        # limpia: sin ningún texto de slide (el gráfico queda en su versión en español)
        Image.fromarray(limpia).save(rutas.salida / f"{s['n']:02d}_limpia.png")
        for k, (x0, y0, x1, y1) in recortes.items():
            sufijo = "" if len(recortes) == 1 else f"_{k}"
            Image.fromarray(limpia[y0:y1, x0:x1]).save(rutas.graficos / f"{s['n']:02d}_grafico{sufijo}_es.png")
        s["avisos_render"] = avisos
        log(f"  slide {s['n']:02d}: " + ("; ".join(avisos) if avisos else "ok"))
    guardar_plan(rutas, plan)
    escribir_textos(rutas, plan)
    log(f"[renderizar] {slug}: salida en {rutas.salida}")
