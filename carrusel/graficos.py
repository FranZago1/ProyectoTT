"""Paso 4b: regeneración de gráficos (estrategia B) con matplotlib.

Cada zona con estrategia "B" trae en plan.json un bloque "datos" con "tipo" y parámetros.
Los datos se derivan EXACTAMENTE del contenido (fórmulas o valores dados); si hay simulación
aleatoria, se usa semilla fija y se marca "regenerado, no idéntico".
Estilo: minimalista tipo seaborn, ejes finos grises, valores destacados en negrita,
verde = ganancia, rojo = pérdida, gris = neutro, fondo igual al de la slide.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.ticker import FuncFormatter, LogLocator  # noqa: E402

from .comun import RAIZ, Rutas, leer_plan, log  # noqa: E402
from .formato import NBSP, num_ar  # noqa: E402

DPI = 100  # 1 pt = DPI/72 px


def _px(p: float) -> float:
    """Tamaño en px de la slide -> puntos de matplotlib."""
    return p * 72 / DPI


def _registrar_fuentes(cfg: dict) -> str:
    carpeta = RAIZ / cfg["render"]["fuente_dir"]
    for f in carpeta.glob("*.otf"):
        font_manager.fontManager.addfont(str(f))
    try:
        font_manager.findfont("Inter", fallback_to_default=False)
        return "Inter"
    except Exception:
        return "DejaVu Sans"


def _estilo(ax, c: dict, fondo: str, ejes_y=True):
    ax.set_facecolor(fondo)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("left", "bottom"):
        ax.spines[lado].set_color(c["ejes"])
        ax.spines[lado].set_linewidth(1.0)
    ax.tick_params(colors="#8C8C8C", labelsize=_px(17), length=4, width=0.8)
    if not ejes_y:
        ax.spines["left"].set_visible(False)
        ax.set_yticks([])


def _fmt(decimales=None, prefijo="", sufijo=""):
    return FuncFormatter(lambda v, _: f"{prefijo}{num_ar(v, decimales)}{sufijo}")


def _figura(ancho_px: int, alto_px: int, fondo: str, ncols: int = 1, **kw):
    fig, axs = plt.subplots(1, ncols, figsize=(ancho_px / DPI, alto_px / DPI), dpi=DPI, **kw)
    fig.patch.set_facecolor(fondo)
    return fig, axs


# --- tipos de gráfico -----------------------------------------------------------------

def barras_curtosis(d: dict, c: dict, fondo: str, tam):
    """Barras con valores dados (curtosis 3 / ~10 / 15+). Sin eje Y, valores dentro de la barra."""
    fig, ax = _figura(*tam, fondo)
    cats = d["categorias"]
    x = np.arange(len(cats))
    colores = [c.get(k, k) for k in d["colores"]]
    ax.bar(x, d["valores"], width=0.68, color=colores, zorder=2)
    for i, (v, etq, txtc) in enumerate(zip(d["valores"], d["etiquetas_valor"], d["color_valor"])):
        dentro = v > max(d["valores"]) * 0.25
        y = v - max(d["valores"]) * 0.07 if dentro else v + max(d["valores"]) * 0.03
        ax.text(i, y, etq, ha="center", va="top" if dentro else "bottom", fontsize=_px(40),
                fontweight="bold", color=txtc)
    ax.axhline(0, color="#E6E6E6", lw=1.2, zorder=1)
    _estilo(ax, c, fondo, ejes_y=False)
    ax.spines["bottom"].set_visible(False)
    ax.set_xticks(x)
    ax.set_xticklabels([])
    for i, (cat, sub) in enumerate(zip(cats, d["subtitulos"])):
        ax.annotate(cat, (i, 0), xytext=(0, -14), textcoords="offset points", ha="center", va="top",
                    fontsize=_px(21), fontweight="bold", color="#333333", annotation_clip=False)
        ax.annotate(sub, (i, 0), xytext=(0, -34), textcoords="offset points", ha="center", va="top",
                    fontsize=_px(14.5), color="#8C8C8C", annotation_clip=False)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(0, max(d["valores"]) * 1.02)
    ax.set_xlim(-0.6, len(cats) - 0.4)
    if d.get("rotulo_eje"):
        ax.text(-0.62, max(d["valores"]) * 0.58, d["rotulo_eje"], ha="left", va="center",
                fontsize=_px(17), color="#B0B0B0")
    fig.suptitle(d["titulo_1"], y=0.985, fontsize=_px(18.5), color="#666666")
    fig.text(0.5, 0.905, d["titulo_2"], ha="center", va="top", fontsize=_px(21), fontweight="bold",
             color="#444444")
    fig.subplots_adjust(left=0.06, right=0.98, top=0.76, bottom=0.17)
    return fig


def moneda_valor_esperado(d: dict, c: dict, fondo: str, tam):
    """Moneda +50 % / −40 % y valor esperado +5 %: 0,5 × 1,50 + 0,5 × 0,60 = 1,05."""
    fig, ax = _figura(*tam, fondo)
    g, p = d["ganancia_pct"], d["perdida_pct"]
    ve = 0.5 * g - 0.5 * p
    valores = [g, -p, ve]
    colores = [c["verde"], c["rojo"], "#3E7A4C"]
    x = np.arange(3)
    ax.bar(x, valores, width=0.54, color=colores, zorder=2)
    for i, v in enumerate(valores):
        txt = ("+" if v > 0 else "−") + num_ar(abs(v)) + NBSP + "%"
        ax.text(i, v + (3 if v >= 0 else -3), txt, ha="center", va="bottom" if v >= 0 else "top",
                fontsize=_px(29), fontweight="bold", color="#1A1A1A")
    ax.axhline(0, color="#E3E3E3", lw=1.2, zorder=1)
    _estilo(ax, c, fondo)
    ax.set_xticks(x)
    ax.set_xticklabels(d["etiquetas"], fontsize=_px(18), color="#8C8C8C", linespacing=1.1)
    ax.yaxis.set_major_formatter(_fmt())
    ax.set_yticks([-40, -20, 0, 20, 40, 60])
    ax.set_ylim(-p - 24, g + 18)
    ax.set_xlim(-0.6, 2.6)
    ax.set_title(d["formula"], fontsize=_px(19), color="#8C8C8C", style="italic", pad=16)
    fig.subplots_adjust(left=0.12, right=0.98, top=0.86, bottom=0.17)
    return fig


def caminos_barras(d: dict, c: dict, fondo: str, tam):
    """$100 -> $150 -> $90: barras con línea de punto de equilibrio y flecha de la pérdida."""
    fig, ax = _figura(*tam, fondo)
    ini = d["inicial"]
    v1 = ini * (1 + d["ganancia_pct"] / 100)
    v2 = v1 * (1 - d["perdida_pct"] / 100)
    valores = [ini, v1, v2]
    colores = [c["gris"], c["verde"], c["rojo"]]
    x = np.arange(3)
    ax.bar(x, valores, width=0.48, color=colores, zorder=2)
    ax.axhline(ini, color="#C8C8C8", lw=1.2, ls=(0, (4, 3)), zorder=1, xmax=0.86)
    for i, v in enumerate(valores):
        ax.text(i - (0.0), v + 5, f"${num_ar(v)}", ha="center", va="bottom", fontsize=_px(30),
                fontweight="bold", color="#1A1A1A", zorder=4)
    ax.annotate("", xy=(2.34, v2 + 1), xytext=(2.34, v1), arrowprops=dict(arrowstyle="-|>", color=c["rojo_intenso"],
                                                                    lw=2.2, ls=(0, (3, 2)), mutation_scale=16),
                zorder=3)
    ax.text(2.44, (ini + v1) / 2 - 5, f"−${num_ar(v1 - v2)}", ha="left", va="center", fontsize=_px(23),
            fontweight="bold", color=c["rojo_intenso"])
    ax.text(2.44, ini - 1, d["etiqueta_equilibrio"], ha="left", va="top", fontsize=_px(16), color="#8C8C8C")
    _estilo(ax, c, fondo)
    ax.set_xticks(x)
    ax.set_xticklabels(d["etiquetas"], fontsize=_px(18), color="#8C8C8C", linespacing=1.1)
    ax.set_ylim(0, 178)
    ax.set_yticks(range(0, 176, 25))
    ax.yaxis.set_major_formatter(_fmt())
    ax.set_ylabel(d["rotulo_y"], fontsize=_px(17), color="#8C8C8C")
    ax.set_xlim(-0.5, 3.25)
    fig.subplots_adjust(left=0.13, right=0.99, top=0.95, bottom=0.19)
    return fig


def simulacion_conjunto(d: dict, c: dict, fondo: str, tam):
    """Promedio de N personas vs. trayectorias individuales (simulación con semilla fija, escala log)."""
    rng = np.random.default_rng(d["semilla"])
    n, t = d["personas"], d["tiradas"]
    g, p = 1 + d["ganancia_pct"] / 100, 1 - d["perdida_pct"] / 100
    caras = rng.random((n, t)) < 0.5
    factores = np.where(caras, g, p)
    riqueza = d["inicial"] * np.cumprod(factores, axis=1)
    riqueza = np.hstack([np.full((n, 1), d["inicial"]), riqueza])
    promedio = riqueza.mean(axis=0)
    xs = np.arange(t + 1)
    fig, (a1, a2) = _figura(*tam, fondo, ncols=2)
    a1.plot(xs, promedio, color="#2E6B3C", lw=2.6)
    a1.fill_between(xs, promedio, d["inicial"], color=c["verde"], alpha=0.14, lw=0)
    for i in range(d["trayectorias"]):
        a2.plot(xs, riqueza[i], color=c["rojo"], lw=1.2, alpha=0.85)
    for ax, tit, col in ((a1, d["titulo_1"], "#2E6B3C"), (a2, d["titulo_2"], c["rojo_intenso"])):
        _estilo(ax, c, fondo)
        ax.set_yscale("log")
        ax.yaxis.set_major_locator(LogLocator(base=10, numticks=8))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"10$^{{{int(round(np.log10(v)))}}}$"))
        ax.yaxis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
        ax.set_xticks(range(0, t + 1, 100))
        ax.xaxis.set_major_formatter(_fmt())
        ax.set_xlabel(d["rotulo_x"], fontsize=_px(17), color="#8C8C8C")
        ax.set_title(tit, fontsize=_px(18), fontweight="bold", color=col, linespacing=1.15)
        ax.tick_params(labelsize=_px(14))
    fig.subplots_adjust(left=0.1, right=0.98, top=0.83, bottom=0.17, wspace=0.32)
    return fig


def caminos_y_ruina(d: dict, c: dict, fondo: str, tam):
    """Izq.: ganar primero / perder primero terminan en $90. Der.: alternar cara/ceca N veces."""
    ini = d["inicial"]
    g, p = 1 + d["ganancia_pct"] / 100, 1 - d["perdida_pct"] / 100
    fig, (a1, a2) = _figura(*tam, fondo, ncols=2)
    gana = [ini, ini * g, ini * g * p]
    pierde = [ini, ini * p, ini * p * g]
    a1.axhline(ini, color="#D5D5D5", lw=1, ls=(0, (4, 3)))
    a1.plot([0, 1, 2], gana, color="#2E7D46", lw=2.6, marker="o", ms=9, label=d["leyenda_gana"])
    a1.plot([0, 1, 2], pierde, color=c["rojo_intenso"], lw=2.6, marker="o", ms=9, label=d["leyenda_pierde"])
    a1.text(1, gana[1] + 6, f"${num_ar(gana[1])}", ha="center", va="bottom", fontsize=_px(19),
            fontweight="bold", color="#2E7D46")
    a1.text(1, pierde[1] - 6, f"${num_ar(pierde[1])}", ha="center", va="top", fontsize=_px(19),
            fontweight="bold", color=c["rojo_intenso"])
    a1.text(2.07, gana[2] - 1, f"${num_ar(gana[2])}", ha="left", va="center", fontsize=_px(20),
            fontweight="bold", color="#1A1A1A")
    a1.set_xticks([0, 1, 2])
    a1.set_xticklabels(d["etiquetas_x"])
    a1.set_ylim(35, 168)
    a1.set_yticks(range(40, 161, 20))
    a1.set_xlim(-0.15, 2.45)
    a1.legend(loc="center left", bbox_to_anchor=(0.04, 0.48), frameon=False, fontsize=_px(14),
              handlelength=1.6, borderaxespad=0)
    a1.set_title(d["titulo_1"], fontsize=_px(18), fontweight="bold", color="#1A1A1A")
    # serie alternada: cara, ceca, cara, ceca... (determinística)
    n = d["tiradas_ruina"]
    serie = [ini]
    for i in range(n):
        serie.append(serie[-1] * (g if i % 2 == 0 else p))
    for i in range(n):
        a2.plot([i, i + 1], serie[i:i + 2], color="#2E7D46" if i % 2 == 0 else c["rojo_intenso"], lw=1.8)
    a2.axhline(ini, color="#D5D5D5", lw=1, ls=(0, (4, 3)))
    a2.set_ylim(0, 165)
    a2.set_yticks(range(0, 161, 20))
    a2.set_xticks(range(0, n + 1, 10))
    a2.set_xlabel(d["rotulo_x"], fontsize=_px(17), color="#8C8C8C")
    a2.set_title(d["titulo_2"], fontsize=_px(18), fontweight="bold", color=c["rojo_intenso"])
    for ax in (a1, a2):
        _estilo(ax, c, fondo)
        ax.yaxis.set_major_formatter(_fmt())
        ax.tick_params(labelsize=_px(15))
    fig.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.14, wspace=0.28)
    return fig


def kelly(d: dict, c: dict, fondo: str, tam):
    """g(f) = p·ln(1 + b·f) + q·ln(1 − a·f); óptimo y apuesta total marcados."""
    pg, b, a = d["p"], d["ganancia_pct"] / 100, d["perdida_pct"] / 100
    q = 1 - pg
    f = np.linspace(0, 1, 501)
    gf = pg * np.log1p(b * f) + q * np.log1p(-a * f)
    f_opt = pg / a - q / b
    g_opt = pg * np.log1p(b * f_opt) + q * np.log1p(-a * f_opt)
    g1 = pg * np.log1p(b) + q * np.log1p(-a)
    fig, ax = _figura(*tam, fondo)
    ax.axhline(0, color="#D5D5D5", lw=1, ls=(0, (4, 3)))
    ax.fill_between(f, gf, 0, where=gf >= 0, color=c["verde"], alpha=0.16, lw=0)
    ax.fill_between(f, gf, 0, where=gf < 0, color=c["rojo"], alpha=0.16, lw=0)
    ax.plot(f, gf, color="#1A1A1A", lw=2.6)
    ax.plot([f_opt], [g_opt], "o", color="#2E7D46", ms=11, zorder=4)
    ax.plot([1], [g1], "o", color=c["rojo_intenso"], ms=11, zorder=4, clip_on=False)
    ax.annotate(d["texto_optimo"].format(f=num_ar(f_opt * 100, 0) + NBSP + "%"),
                xy=(f_opt, g_opt), xytext=(f_opt - 0.11, g_opt + 0.017), fontsize=_px(17),
                fontweight="bold", color="#2E7D46", ha="left", va="bottom",
                arrowprops=dict(arrowstyle="-|>", color="#2E7D46", lw=1.4))
    ax.annotate(d["texto_total"].format(g=num_ar(g1, 3)), xy=(1, g1), xytext=(0.74, g1 + 0.012),
                fontsize=_px(17), fontweight="bold", color=c["rojo_intenso"], ha="right", va="bottom",
                arrowprops=dict(arrowstyle="-|>", color=c["rojo_intenso"], lw=1.4))
    _estilo(ax, c, fondo)
    ax.set_xlim(0, 1.03)
    ax.set_ylim(g1 - 0.006, g_opt + 0.03)
    ax.set_xticks(np.arange(0, 1.01, 0.2))
    ax.set_yticks([0, -0.02, -0.04])
    ax.xaxis.set_major_formatter(_fmt(1))
    ax.yaxis.set_major_formatter(_fmt(2))
    ax.set_xlabel(d["rotulo_x"], fontsize=_px(18), color="#8C8C8C")
    ax.set_ylabel(d["rotulo_y"], fontsize=_px(17), color="#8C8C8C")
    fig.subplots_adjust(left=0.15, right=0.97, top=0.97, bottom=0.17)
    return fig


TIPOS = {
    "barras_curtosis": barras_curtosis,
    "moneda_valor_esperado": moneda_valor_esperado,
    "caminos_barras": caminos_barras,
    "simulacion_conjunto": simulacion_conjunto,
    "caminos_y_ruina": caminos_y_ruina,
    "kelly": kelly,
}


def generar(datos: dict, tam: tuple[int, int], fondo: str, config: dict, destino: Path) -> Path:
    fam = _registrar_fuentes(config)
    plt.rcParams.update({"font.family": fam, "axes.unicode_minus": False, "mathtext.fontset": "custom",
                         "mathtext.rm": fam, "mathtext.it": fam, "mathtext.bf": fam,
                         "mathtext.cal": fam, "mathtext.sf": fam})
    colores = dict(config["graficos"])
    fig = TIPOS[datos["tipo"]](datos, colores, fondo, tam)
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, dpi=DPI, facecolor=fondo)
    plt.close(fig)
    return destino


def graficos(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    plan = leer_plan(rutas)
    n = 0
    for s in plan["slides"]:
        for k, z in enumerate(s.get("zonas_grafico", []), start=1):
            if z.get("estrategia") != "B":
                continue
            x0, y0, x1, y1 = z.get("caja_salida") or z["caja"]
            destino = rutas.trabajo / "graficos" / f"{s['n']:02d}_{k}.png"
            generar(z["datos"], (x1 - x0, y1 - y0), s.get("color_fondo", "#FFFFFF"), config, destino)
            n += 1
            log(f"  slide {s['n']:02d} zona {k}: {z['datos']['tipo']} -> {destino.name}")
    log(f"[graficos] {slug}: {n} gráficos regenerados")
