"""Logo PE: geometría, detección y reemplazo de la marca de agua."""

import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from carrusel.comun import cargar_config  # noqa: E402
from carrusel.marca import aplicar_marca, detectar_marca, logo_mascara, logo_svg  # noqa: E402

CFG = cargar_config()


def test_logo_tiene_alto_pedido_y_tinta():
    m = np.array(logo_mascara(100))
    assert m.shape[0] == 100
    assert 0.25 < (m > 128).mean() < 0.6
    assert "<svg" in logo_svg() and "Pulso Económico" in logo_svg()


def _slide_con_marca(w=1080, h=1920):
    img = np.full((h, w, 3), 255, np.uint8)
    img[300:340, 200:880] = 20                        # texto
    m = np.array(logo_mascara(86))
    y0, x0 = 1757, (w - m.shape[1]) // 2
    img[y0:y0 + m.shape[0], x0:x0 + m.shape[1]][m > 128] = 10
    return img, (x0, y0, x0 + m.shape[1], y0 + m.shape[0])


def test_detecta_y_reemplaza_marca():
    img, caja = _slide_con_marca()
    det = detectar_marca(img, (255, 255, 255), CFG["marca"])
    assert det is not None and abs(det[1] - caja[1]) <= 2 and abs(det[3] - caja[3]) <= 2
    (out,), aviso = aplicar_marca([img], (255, 255, 255), CFG)
    assert "reemplazada" in aviso


def test_agrega_logo_si_no_hay_y_respeta_zonas():
    img = np.full((1350, 1080, 3), 255, np.uint8)
    (out,), aviso = aplicar_marca([img], (255, 255, 255), CFG)
    assert "agregado" in aviso and (out[1150:] < 128).any()
    (out,), aviso = aplicar_marca([img], (255, 255, 255), CFG, prohibidas=[[0, 1000, 1080, 1350]])
    assert "NO SE AGREGÓ" in aviso
