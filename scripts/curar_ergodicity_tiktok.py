"""Curación del carrusel de TikTok «Ergodicity» (@quantgent, 7 slides, 9:16).

Es la versión de TikTok del carrusel de referencia `ergodicity` (Instagram, 4:5): mismos textos y los
mismos bloques detectados. Se reutiliza `ergodicity()` de `scripts/curar_referencia.py` (traducción,
estrategias, datos de los gráficos regenerados y alertas) y solo se cambian las cajas, medidas sobre
las imágenes 1080 × 1920.
Uso: .venv/bin/python scripts/curar_ergodicity_tiktok.py  (después de `extraer tiktok-quantgent-456663`)
"""

from curar_referencia import ergodicity
from curar_tiktok import ejecutar

SLUG = "tiktok-quantgent-456663"

# caja de cada zona de gráfico (una por slide, en orden) en el formato 9:16
CAJAS = {1: [186, 1030, 895, 1500], 2: [262, 1085, 818, 1432], 3: [245, 1140, 838, 1505],
         4: [262, 1272, 812, 1607], 5: [250, 1145, 835, 1505], 6: [262, 1282, 812, 1630]}


def curar(plan):
    ergodicity(plan)
    plan["version_de"] = "ergodicity"
    S = plan["slides"]
    for n, caja in CAJAS.items():
        S[n - 1]["zonas_grafico"][0]["caja"] = caja
    # portada: pie y rótulo del eje Y de la figura importada
    pie = next(b for b in S[0]["bloques"] if b["rol"] == "pie")
    pie["caja"] = [186, 1508, 895, 1537]
    S[0]["zonas_grafico"][0]["etiquetas"][0]["caja"] = [209, 1176, 231, 1296]
    plan["glosario_nuevo"] = []


if __name__ == "__main__":
    ejecutar(SLUG, curar)
