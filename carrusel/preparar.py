"""Paso 1: rasterizar, detectar la slide, recortar, eliminar UI de Instagram, normalizar a 1080x1350.

Las capturas de Instagram no muestran el borde de la slide (fondo blanco sobre blanco), así que
la slide se reconstruye así:
  1. se extrae la imagen nativa embebida en cada página del PDF (sin pérdida); plan B: rasterizar;
  2. se recortan los márgenes blancos de la página;
  3. se aplana la iluminación del fondo (elimina degradados/sombras de borde y la flecha "<");
  4. se borra el contador "n / 7" si aparece;
  5. se toma una ventana 4:5 del ancho completo centrada en el contenido y se lleva a 1080x1350.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

from .comun import EXT_IMAGEN, Rutas, guardar_plan, leer_plan, log
from .fondo import borrar_regiones


# --- lectura de la entrada -------------------------------------------------------

def _imagenes_nativas(pdf: Path) -> list[np.ndarray] | None:
    """Si cada página tiene exactamente una imagen embebida, la devuelve sin re-muestrear."""
    import pymupdf
    salida = []
    with pymupdf.open(pdf) as doc:
        for pag in doc:
            imgs = pag.get_images(full=True)
            if len(imgs) != 1:
                return None
            pix = pymupdf.Pixmap(doc, imgs[0][0])
            if pix.colorspace is None or pix.colorspace.n != 3 or pix.alpha:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            arr = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, pix.n)
            salida.append(arr[:, :, :3].copy())
    return salida


def rasterizar_pdf(pdf: Path, dpi: int, motor: str = "pymupdf") -> tuple[list[np.ndarray], str]:
    if motor == "pymupdf":
        try:
            nativas = _imagenes_nativas(pdf)
            if nativas:
                return nativas, "imagen nativa embebida (PyMuPDF)"
            import pymupdf
            paginas = []
            with pymupdf.open(pdf) as doc:
                for pag in doc:
                    pix = pag.get_pixmap(dpi=dpi, alpha=False)
                    arr = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, pix.n)
                    paginas.append(arr[:, :, :3].copy())
            return paginas, f"rasterizado PyMuPDF {dpi} dpi"
        except Exception as e:  # plan B
            log(f"  PyMuPDF falló ({e}); uso pdftoppm")
    if not shutil.which("pdftoppm"):
        raise RuntimeError("No hay PyMuPDF ni pdftoppm para rasterizar el PDF")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(pdf), f"{tmp}/p"], check=True)
        return [np.array(Image.open(p).convert("RGB")) for p in sorted(Path(tmp).glob("p*.png"))], \
            f"rasterizado pdftoppm {dpi} dpi"


def cargar_fuentes(entrada: Path, dpi: int, motor: str) -> list[tuple[str, np.ndarray, str]]:
    """[(origen, imagen RGB, método)] en el orden natural de los archivos."""
    if not entrada.exists():
        raise FileNotFoundError(f"No existe {entrada}")
    paginas = []
    for arch in sorted(p for p in entrada.iterdir() if p.is_file()):
        ext = arch.suffix.lower()
        if ext == ".pdf":
            imgs, metodo = rasterizar_pdf(arch, dpi, motor)
            paginas += [(f"{arch.name}#p{i}", img, metodo) for i, img in enumerate(imgs, start=1)]
        elif ext in EXT_IMAGEN:
            paginas.append((arch.name, np.array(Image.open(arch).convert("RGB")), "imagen suelta"))
    if not paginas:
        raise FileNotFoundError(f"{entrada} no tiene PDF ni imágenes")
    return paginas


# --- limpieza --------------------------------------------------------------------

def recortar_margenes(img: np.ndarray, umbral: int) -> tuple[np.ndarray, tuple[int, int, int, int]]:
    gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cont = gris < umbral
    filas = np.flatnonzero(cont.mean(axis=1) > 0.01)
    cols = np.flatnonzero(cont.mean(axis=0) > 0.01)
    if not len(filas) or not len(cols):
        return img, (0, 0, img.shape[1], img.shape[0])
    # la captura es un rectángulo: si los márgenes son de página, son casi blancos puros
    x0, x1, y0, y1 = cols[0], cols[-1] + 1, filas[0], filas[-1] + 1
    h, w = gris.shape
    if x0 < 4 and y0 < 4 and x1 > w - 4 and y1 > h - 4:
        return img, (0, 0, w, h)
    return img[y0:y1, x0:x1], (int(x0), int(y0), int(x1), int(y1))


def mascara_fondo(img: np.ndarray, cfg: dict) -> np.ndarray:
    """Píxeles de fondo: claros, poco saturados y localmente lisos."""
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    gris = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype(np.float32)
    media = cv2.blur(gris, (9, 9))
    var = cv2.blur(gris * gris, (9, 9)) - media * media
    return (gris > cfg["fondo_lum_min"]) & (hsv[..., 1] < cfg["fondo_sat_max"]) & (var < cfg["fondo_var_max"])


def aplanar_fondo(img: np.ndarray, cfg: dict) -> tuple[np.ndarray, np.ndarray]:
    """Corrige la iluminación del fondo hacia un color uniforme. Devuelve (imagen, color_objetivo)."""
    h, w = img.shape[:2]
    m = mascara_fondo(img, cfg)
    celda = cfg["celda_fondo"]
    gh, gw = int(np.ceil(h / celda)), int(np.ceil(w / celda))
    campo = np.full((gh, gw, 3), np.nan, np.float32)
    for gy in range(gh):
        for gx in range(gw):
            sl = (slice(gy * celda, (gy + 1) * celda), slice(gx * celda, (gx + 1) * celda))
            px = img[sl][m[sl]]
            if len(px) > celda * celda * 0.15:
                campo[gy, gx] = np.median(px, axis=0)
    validas = ~np.isnan(campo[..., 0])
    if not validas.any():
        return img, np.array([255, 255, 255], np.float32)
    # rellenar celdas sin fondo (texto, gráficos) interpolando desde las vecinas
    campo_u8 = np.nan_to_num(campo, nan=255).astype(np.uint8)
    campo = cv2.inpaint(campo_u8, (~validas).astype(np.uint8) * 255, 3, cv2.INPAINT_TELEA).astype(np.float32)
    campo = cv2.GaussianBlur(campo, (0, 0), cfg["suavizado_fondo"])
    fondo = cv2.resize(campo, (w, h), interpolation=cv2.INTER_CUBIC)
    objetivo = np.percentile(campo.reshape(-1, 3), 90, axis=0)
    out = img.astype(np.float32) * (objetivo / np.maximum(fondo, 1.0))
    out = np.clip(out, 0, 255).astype(np.uint8)
    # residuos (flecha blanca sobre degradado, puntos sueltos): todo lo muy claro pasa a fondo
    claro = (cv2.cvtColor(out, cv2.COLOR_RGB2GRAY) > cfg["umbral_a_fondo"]) & \
            (cv2.cvtColor(out, cv2.COLOR_RGB2HSV)[..., 1] < cfg["fondo_sat_max"])
    out[claro] = objetivo.astype(np.uint8)
    return out, objetivo


def limpiar_franja_superior(img: np.ndarray, color: np.ndarray, cfg: dict) -> tuple[np.ndarray, bool]:
    """La franja de la barra de Instagram (arriba de todo) nunca tiene contenido de la slide: todo lo
    claro y poco saturado pasa a fondo (restos del degradado que el aplanado no alcanza)."""
    alto = int(cfg["franja_ui_superior"] * img.shape[1])
    franja = img[:alto]
    hsv = cv2.cvtColor(franja, cv2.COLOR_RGB2HSV)
    gris = cv2.cvtColor(franja, cv2.COLOR_RGB2GRAY)
    m = (gris > 180) & (hsv[..., 1] < 20)
    cambia = m & (np.abs(franja.astype(int) - color.astype(int)).max(axis=2) > 3)
    img = img.copy()
    img[:alto][m] = color.astype(np.uint8)
    return img, bool(cambia.sum() > 50)


def eliminar_flecha(img: np.ndarray, color: np.ndarray, cfg: dict) -> tuple[np.ndarray, bool]:
    """Borra cualquier trazo en la esquina superior izquierda (flecha '<' de Instagram)."""
    h, w = img.shape[:2]
    x1, y1 = int(cfg["flecha_region"][0] * w), int(cfg["flecha_region"][1] * w)
    reg = img[:y1, :x1]
    dif = np.abs(reg.astype(int) - color.astype(int)).max(axis=2)
    if (dif > 8).sum() == 0:
        return img, False
    img = img.copy()
    img[:y1, :x1] = color.astype(np.uint8)
    return img, True


def eliminar_contador(img: np.ndarray, color: np.ndarray, cfg: dict) -> tuple[np.ndarray, bool]:
    """Detecta la píldora gris del contador 'n / 7' arriba a la derecha y la borra."""
    h, w = img.shape[:2]
    fx0, fy0, fx1, fy1 = cfg["contador_region"]
    rx0, ry0, rx1, ry1 = int(fx0 * w), int(fy0 * h), int(fx1 * w), int(fy1 * h)
    reg = img[ry0:ry1, rx0:rx1]
    hsv = cv2.cvtColor(reg, cv2.COLOR_RGB2HSV)
    gris = cv2.cvtColor(reg, cv2.COLOR_RGB2GRAY)
    # la píldora es un relleno de gris medio (el texto negro solo deja bordes grises finos)
    crudo = ((hsv[..., 1] < 40) & (gris < 185) & (gris > 85)).astype(np.uint8)
    m = cv2.morphologyEx(crudo, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    n, etiquetas, stats, _ = cv2.connectedComponentsWithStats(m)
    for i in range(1, n):
        x, y, ww, hh, area = stats[i]
        relleno_crudo = crudo[etiquetas == i].mean()
        if 1.3 <= ww / max(hh, 1) <= 4.5 and hh >= h * 0.02 and area / max(ww * hh, 1) > 0.6 \
                and ww < w * 0.25 and relleno_crudo > 0.6:
            img = img.copy()
            img[ry0 + y - 6:ry0 + y + hh + 6, rx0 + x - 6:rx0 + x + ww + 6] = color.astype(np.uint8)
            return img, True
    return img, False


def ventana_slide(img: np.ndarray, color: np.ndarray, relacion: float, umbral: int) -> tuple[np.ndarray, list[int]]:
    """Ventana 4:5 de ancho completo centrada en el contenido; rellena con fondo si falta alto."""
    h, w = img.shape[:2]
    alto = int(round(w * relacion))
    dif = np.abs(img.astype(int) - color.astype(int)).max(axis=2) > umbral
    filas = np.flatnonzero(dif.sum(axis=1) > 2)
    if len(filas):
        centro = (filas[0] + filas[-1]) / 2
        if filas[-1] - filas[0] > alto:
            log("  aviso: el contenido es más alto que la slide 4:5; se recorta abajo")
            centro = filas[0] + alto / 2
    else:
        centro = h / 2
    y0 = int(round(centro - alto / 2))
    lienzo = np.empty((alto, w, 3), np.uint8)
    lienzo[:] = color.astype(np.uint8)
    sy0, sy1 = max(0, y0), min(h, y0 + alto)
    lienzo[sy0 - y0:sy1 - y0] = img[sy0:sy1]
    return lienzo, [0, y0, w, y0 + alto]


def normalizar(slide: np.ndarray, ancho: int, alto: int) -> tuple[np.ndarray, str | None]:
    h, w = slide.shape[:2]
    if (w, h) == (ancho, alto):
        return slide, None
    nota = f"{w}x{h} -> {ancho}x{alto} (Lanczos)"
    if w < ancho:
        nota = "fuente de menor resolución escalada hacia arriba: " + nota
    return np.array(Image.fromarray(slide).resize((ancho, alto), Image.LANCZOS)), nota


# --- comando ---------------------------------------------------------------------

def preparar(slug: str, config: dict) -> None:
    rutas = Rutas(slug, config)
    rutas.crear()
    cfg = config["preparar"]
    ancho, alto = config["salida"]["ancho"], config["salida"]["alto"]
    fuentes = cargar_fuentes(rutas.entrada, config["rasterizado"]["dpi"], config["rasterizado"]["motor"])
    elegidas = rutas.paginas_elegidas or list(range(1, len(fuentes) + 1))
    log(f"[preparar] {slug}: {len(fuentes)} páginas en {rutas.entrada}; se procesan {elegidas}")

    plan = leer_plan(rutas)
    fuente = rutas.entrada / "fuente.json"
    descarga_directa = fuente.exists()
    if descarga_directa:
        plan["fuente"] = json.loads(fuente.read_text(encoding="utf-8"))
        log(f"  descarga directa ({plan['fuente'].get('plataforma')}): se conserva el formato original")
    info = []
    for n in elegidas:
        origen, img, metodo = fuentes[n - 1]
        eliminados = []
        h, w = img.shape[:2]
        # original: imagen 4:5 suelta, o cualquier imagen descargada directamente de la plataforma
        # (entrada/<slug>/fuente.json): no tiene UI que limpiar y conserva su formato
        original_4x5 = (abs(h / w - cfg["relacion_aspecto"]) < 0.01 or descarga_directa) and not origen.count("#p")
        if original_4x5:
            # imagen original (p. ej. 1080x1350): no tiene UI de Instagram; no se recorta ni se aplana
            marg = (0, 0, w, h)
            color = np.median(img.reshape(-1, 3), axis=0)  # el fondo domina la imagen
        else:
            img, marg = recortar_margenes(img, cfg["umbral_blanco"])
            if marg != (0, 0, w, h):
                eliminados.append("márgenes blancos de la página")
            img, color = aplanar_fondo(img, cfg)
            eliminados.append("degradados/sombras de borde (aplanado de fondo)")
        if not original_4x5:
            img, franja = limpiar_franja_superior(img, color, cfg)
            img, hubo = eliminar_flecha(img, color, cfg)
            if hubo or franja:
                eliminados.append("flecha '<' y barra superior de Instagram")
            img, hubo = eliminar_contador(img, color, cfg)
            if hubo:
                eliminados.append("contador 'n / 7'")
            img, ventana = ventana_slide(img, color, cfg["relacion_aspecto"], cfg["umbral_contenido"])
        else:
            ventana = [0, 0, img.shape[1], img.shape[0]]
        alto_n = int(round(ancho * img.shape[0] / img.shape[1])) if descarga_directa else alto
        slide, nota = normalizar(img, ancho, alto_n)
        Image.fromarray(slide).save(rutas.paginas / f"p{n:02d}.png")
        info.append({"pagina": n, "origen": origen, "metodo": metodo, "recorte_margenes": list(marg),
                     "ventana": ventana, "color_fondo": [int(c) for c in color],
                     "elementos_ui_eliminados": eliminados, "escala": nota})
        log(f"  p{n:02d} {origen}: {', '.join(eliminados)}; {nota or ''}")
    plan["paginas"] = info
    guardar_plan(rutas, plan)


def ordenar(slug: str, config: dict) -> None:
    """Paso 2: copia las páginas a slides/01..07 según el orden del plan o de config.yaml."""
    rutas = Rutas(slug, config)
    plan = leer_plan(rutas)
    orden = plan.get("orden") or rutas.paginas_elegidas
    if not orden:
        orden = sorted(int(p.stem[1:]) for p in rutas.paginas.glob("p*.png"))
    if len(orden) != 7:
        log(f"  aviso: el orden tiene {len(orden)} slides (se esperaban 7)")
    rutas.slides.mkdir(parents=True, exist_ok=True)
    for viejo in rutas.slides.glob("*.png"):
        viejo.unlink()
    for i, pag in enumerate(orden, start=1):
        shutil.copy(rutas.paginas / f"p{pag:02d}.png", rutas.slides / f"{i:02d}.png")
    plan["orden"] = orden
    paginas = {p["pagina"]: p for p in plan.get("paginas", [])}
    slides = plan.get("slides") or []
    while len(slides) < len(orden):
        slides.append({})
    for i, pag in enumerate(orden):
        slides[i]["n"] = i + 1
        slides[i]["pagina_origen"] = pag
        slides[i]["elementos_ui_eliminados"] = paginas.get(pag, {}).get("elementos_ui_eliminados", [])
    plan["slides"] = slides[:len(orden)]
    guardar_plan(rutas, plan)
    log(f"[ordenar] {slug}: páginas {orden} -> slides 01..{len(orden):02d}")
