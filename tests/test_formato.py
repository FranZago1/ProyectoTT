"""Pruebas de formato numérico, verificación de cifras, tokenizado y fórmulas de los gráficos B."""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from carrusel.formato import NBSP, cifras_faltantes, formato_sospechoso, num_ar, pct_ar, usd_ar  # noqa: E402
from carrusel.render import tokenizar  # noqa: E402


def test_num_ar():
    assert num_ar(99.7) == "99,7"
    assert num_ar(10000) == "10.000"
    assert num_ar(1.05, 2) == "1,05"
    assert num_ar(-0.0527, 3) == "−0,053"
    assert pct_ar(99.7) == f"99,7{NBSP}%"
    assert usd_ar(3600) == f"US${NBSP}3.600"


def test_cifras_montos_y_escalas():
    assert cifras_faltantes("a $3.6 billion rescue", "un rescate de US$ 3.600 millones") == []
    assert cifras_faltantes("$100 billion in positions", "US$ 100.000 millones en posiciones") == []
    assert cifras_faltantes("99.7% of moves", "el 99,7 % de los movimientos") == []
    assert cifras_faltantes("10,000 people", "10.000 personas") == []
    assert cifras_faltantes("lost 6%", "perdió un 7 %") == [6.0]


def test_formato_sospechoso():
    assert formato_sospechoso("el 99.7% de") != []
    assert formato_sospechoso("el 99,7 % de") == []


def test_tokenizar_negrita_y_puntuacion():
    p = tokenizar("Mismo resultado. **$90**. No importa")
    assert [x.texto for x in p] == ["Mismo", "resultado.", "$90", ".", "No", "importa"]
    assert p[2].negrita and not p[1].negrita
    assert p[3].salto is None   # el punto va pegado a la negrita
    assert p[2].salto is False  # '$90' lleva espacio antes


def test_kelly_exacto():
    g = lambda f: 0.5 * math.log1p(0.5 * f) + 0.5 * math.log1p(-0.4 * f)  # noqa: E731
    f_opt = 0.5 / 0.4 - 0.5 / 0.5
    assert abs(f_opt - 0.25) < 1e-12
    assert abs(g(1) - (-0.0527)) < 1e-4
    assert g(0.25) > g(0.2) and g(0.25) > g(0.3)


def test_caminos_exactos():
    assert round(100 * 1.5 * 0.6, 9) == 90 == round(100 * 0.6 * 1.5, 9)
    assert abs(100 * 0.9 ** 15 - 20.59) < 0.01  # 30 tiradas alternadas
