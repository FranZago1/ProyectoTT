"""Paso 8: memoria de estilo.

- memoria/historial/AAAA-MM-DD_<slug>.md: ficha del carrusel (por slide: función, texto final,
  gráfico, estrategia, alertas) + copia del plan curado (.plan.json) para poder re-renderizar.
- memoria/GLOSARIO.md: incorpora los términos nuevos de plan["glosario_nuevo"].
- memoria/ESTILO.md: actualiza el bloque de paleta (entre marcadores) con memoria/paletas.json.
  El resto de ESTILO.md se reescribe consolidando, con criterio (comando /estilo), no por script.
"""

from __future__ import annotations

import datetime as dt
import json
import re

from .comun import Rutas, leer_plan, log

MARCA_INI = "<!-- PALETA:INICIO (generado por python -m carrusel memoria) -->"
MARCA_FIN = "<!-- PALETA:FIN -->"


def _plano(t: str) -> str:
    return (t or "").replace(" ", " ").replace("\n", " / ")


def ficha(plan: dict, fecha: str) -> str:
    out = [f"# {fecha} — {plan['slug']}", "",
           f"**Título original:** {plan.get('titulo_en', '')}  ",
           f"**Título en español:** {plan.get('titulo_es', '')}  ",
           f"**Motor OCR:** {plan.get('motor_ocr', '')} · **Orden de páginas:** {plan.get('orden')}", ""]
    for s in plan["slides"]:
        out += [f"## Slide {s['n']} — {s.get('funcion', '')}", ""]
        for b in s.get("bloques", []):
            out.append(f"- *{b.get('rol')}* ({b.get('peso')}, {b.get('tam_px')} px): {_plano(b.get('texto_es'))}")
        for z in s.get("zonas_grafico", []):
            out.append(f"- **Gráfico** ({z.get('tipo', 's/d')}) — estrategia {z.get('estrategia')}: "
                       f"{z.get('justificacion', '')}")
            if z.get("datos"):
                datos = {k: v for k, v in z["datos"].items() if not isinstance(v, str) or len(v) < 60}
                out.append(f"  - datos: `{json.dumps(datos, ensure_ascii=False)}`")
        if not s.get("zonas_grafico"):
            out.append("- **Gráfico**: ninguno.")
        for n in s.get("notas_revisar", []):
            out.append(f"- ⚠ {n}")
        out.append("")
    return "\n".join(out)


def actualizar_glosario(rutas: Rutas, plan: dict) -> int:
    ruta = rutas.memoria / "GLOSARIO.md"
    texto = ruta.read_text(encoding="utf-8")
    existentes = {m.group(1).strip().lower() for m in re.finditer(r"^\| ([^|]+) \|", texto, re.M)}
    nuevos = [g for g in plan.get("glosario_nuevo", []) if g["en"].lower() not in existentes]
    if nuevos:
        filas = "\n".join(f"| {g['en']} | {g['es']} |" for g in nuevos)
        texto = texto.replace("<!-- GLOSARIO:FIN -->", filas + "\n<!-- GLOSARIO:FIN -->")
        ruta.write_text(texto, encoding="utf-8")
    return len(nuevos)


def bloque_paleta(paletas: dict) -> str:
    lineas = [MARCA_INI, "", "| Carrusel | Fondo | Texto | Acentos (proporción entre píxeles saturados) |",
              "|---|---|---|---|"]
    for slug, p in paletas.items():
        acentos = ", ".join(f"{a['hex']} ({a['proporcion']:.0%})" for a in p.get("acentos", []))
        lineas.append(f"| {slug} | {p['fondo']} | {p['texto']} | {acentos} |")
    lineas += ["", MARCA_FIN]
    return "\n".join(lineas)


def actualizar_paleta_estilo(rutas: Rutas) -> bool:
    ruta = rutas.memoria / "ESTILO.md"
    ruta_p = rutas.memoria / "paletas.json"
    if not ruta.exists() or not ruta_p.exists():
        return False
    texto = ruta.read_text(encoding="utf-8")
    if MARCA_INI not in texto:
        return False
    nuevo = bloque_paleta(json.loads(ruta_p.read_text(encoding="utf-8")))
    texto = re.sub(re.escape(MARCA_INI) + r".*?" + re.escape(MARCA_FIN), lambda _: nuevo, texto, flags=re.S)
    ruta.write_text(texto, encoding="utf-8")
    return True


def memoria(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    plan = leer_plan(rutas)
    fecha = dt.date.today().isoformat()
    hist = rutas.memoria / "historial"
    hist.mkdir(parents=True, exist_ok=True)
    # una sola ficha por slug: se reemplaza la anterior si existía
    for viejo in list(hist.glob(f"*_{slug}.md")) + list(hist.glob(f"*_{slug}.plan.json")):
        viejo.unlink()
    (hist / f"{fecha}_{slug}.md").write_text(ficha(plan, fecha), encoding="utf-8")
    plan_min = {k: v for k, v in plan.items() if k != "paginas"}
    for s in plan_min["slides"]:
        s.pop("ocr_lineas", None)
    (hist / f"{fecha}_{slug}.plan.json").write_text(json.dumps(plan_min, ensure_ascii=False, indent=1),
                                                   encoding="utf-8")
    n = actualizar_glosario(rutas, plan) if (rutas.memoria / "GLOSARIO.md").exists() else 0
    ok = actualizar_paleta_estilo(rutas)
    log(f"[memoria] {slug}: ficha {fecha}_{slug}.md; {n} términos nuevos en el glosario; "
        f"paleta en ESTILO.md {'actualizada' if ok else 'sin marcadores (no se tocó)'}")
