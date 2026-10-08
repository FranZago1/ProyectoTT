"""Curación del carrusel de TikTok «The Kelly Criterion» (@quantgent, 7 slides).

Uso: .venv/bin/python scripts/curar_kelly.py  (después de `extraer tiktok-quantgent-241750`)
"""

from curar_tiktok import FOTO, bloque, ejecutar, et, glosario, nuevo, pad, tam_para

SLUG = "tiktok-quantgent-241750"
ITAL = "LiberationSerif-Italic.ttf"


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "The Kelly Criterion: The Formula That Tells You Exactly How Much to Risk"
    plan["titulo_es"] = "El criterio de Kelly: la fórmula que te dice exactamente cuánto arriesgar"

    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "The Kelly Criterion", "El criterio de Kelly", "bold"),
        bloque(a, 1, "subtitulo", "The Formula That Tells You Exactly How Much to Risk.",
               "La fórmula que te dice exactamente cuánto arriesgar.", "regular"),
        bloque(a, 2, "cuerpo",
               "Poker pros, hedge funds, and even Blackjack legends all use the same equation. Here's how it works.",
               "Jugadores profesionales de póker, fondos de cobertura y hasta leyendas del blackjack usan la misma "
               "ecuación. Veamos cómo funciona.", "regular"),
    ], zonas_grafico=[{
        "caja": [180, 990, 870, 1640], "estrategia": "C",
        "justificacion": "Superficie 3D con ejes en notación (a, v) y ticks; sin texto en lenguaje natural.",
        "tipo": "superficie 3D sin rótulos explicativos (ejes a y v)", "etiquetas": [],
    }], notas_revisar=[
        "Generalización sin fuente: «jugadores profesionales de póker, fondos de cobertura y leyendas del "
        "blackjack usan la misma ecuación».",
        "Gráfico de portada sin explicación: no se indica qué miden los ejes a y v ni el eje vertical.",
    ])

    a = S[1]["bloques"]
    S[1].update(funcion="Planteo: no qué apostar, sino cuánto", bloques=[
        bloque(a, 0, "cuerpo",
               "Most people focus on WHAT to bet on. Kelly answers the question nobody thinks about — HOW MUCH.",
               "La mayoría se concentra en QUÉ apostar. Kelly responde la pregunta en la que nadie piensa: "
               "CUÁNTO.", "regular"),
        bloque(a, 1, "cuerpo",
               "Bet too little and you leave money on the table. Bet too much and one bad streak wipes you out. "
               "There's a mathematically perfect amount in between, and Kelly finds it.",
               "Si apostás muy poco, dejás dinero sobre la mesa. Si apostás demasiado, una mala racha te deja "
               "fuera de juego. En el medio hay un monto matemáticamente perfecto, y Kelly lo encuentra.",
               "regular"),
    ], zonas_grafico=[{
        "caja": [150, 1085, 940, 1640], "estrategia": "A",
        "justificacion": "Diagrama conceptual (rendimiento según riesgo) con siete rótulos sobre fondo blanco: "
                         "se reescriben; la «K» queda.",
        "tipo": "diagrama: rendimiento según el riesgo asumido, de conservador a suicida",
        "etiquetas": [
            et("The Kelly criterion", "El criterio de Kelly", [417, 1096, 709, 1130],
               tam_para("The Kelly criterion", 292, peso="semibold"), peso="semibold", color="#4A7A6E"),
            et("Conservative", "Conservador", [275, 1205, 379, 1219], 14, peso="semibold", color="#6E7F7C"),
            et("Aggressive", "Agresivo", [398, 1182, 482, 1196], 14, peso="semibold", color="#6E7F7C"),
            et("Insane", "Insensato", [563, 1219, 615, 1232], 14, peso="semibold", color="#6E7F7C"),
            et("Suicidal", "Suicida", [727, 1612, 795, 1627], 16.5, peso="semibold", color="#4A4748"),
            et("Return", "Rendimiento", [160, 1240, 231, 1257], 19, peso="semibold", color="#3A3839",
               alineacion="derecha"),
            et("Risk", "Riesgo", [885, 1424, 927, 1442], 19, peso="semibold", color="#3A3839",
               alineacion="izquierda"),
        ],
    }], notas_revisar=[
        "Precisión: el monto es «perfecto» solo si se conocen las probabilidades reales (ver slide 5).",
        "Diagrama conceptual sin escala ni fuente; «Agresivo» marca el máximo (Kelly completo).",
    ])

    a = S[2]["bloques"]
    S[2].update(funcion="La fórmula y sus variables + quién la creó", bloques=[
        bloque(a, 0, "titulo", "The formula is deceptively simple", "La fórmula es engañosamente simple",
               "regular"),
        bloque(a, 1, "otro", "f = (bp - q) / b", "f = (bp − q) / b", "regular"),
        bloque(a, 2, "cuerpo",
               "Where b is the odds you're getting, p is your probability of winning, and q is your probability "
               "of losing. It tells you the exact fraction of your bankroll to put on each bet to grow the fastest "
               "without going broke.",
               "Donde b es la cuota que te pagan, p es tu probabilidad de ganar y q, tu probabilidad de perder. Te "
               "dice la fracción exacta de tu capital que tenés que poner en cada apuesta para crecer lo más "
               "rápido posible sin terminar en la ruina.", "regular"),
    ], zonas_grafico=[{
        "caja": [360, 1170, 725, 1615], "estrategia": "C",
        "justificacion": "Retrato con pie que es un nombre propio (John Larry Kelly Jr.): se conserva.",
        "tipo": "foto: retrato de John Larry Kelly Jr.", "etiquetas": [],
    }], notas_revisar=[
        "Precisión: b es la cuota neta (lo que se gana por cada unidad apostada). Kelly maximiza el "
        "crecimiento logarítmico esperado; «sin terminar en la ruina» supone que se conocen p y b exactamente.",
        "Retrato sin fuente: verificar derechos de uso.",
    ])

    a = S[3]["bloques"]
    rc = "Region of\noptimal\nRisk/Reward\ntrade-off"
    S[3].update(funcion="Clave: maximiza la tasa de crecimiento, no el valor esperado", bloques=[
        bloque(a, 0, "titulo", "Here's the key insight", "Esta es la clave", "regular"),
        bloque(a, 1, "cuerpo",
               "Kelly maximizes the long-run GROWTH RATE of your wealth, not your expected profit on any single "
               "bet. That's a huge difference. Maximizing expected value can tell you to bet everything. Kelly "
               "never does that — because it respects the math of compounding and ruin.",
               "Kelly maximiza la TASA DE CRECIMIENTO de largo plazo de tu patrimonio, no tu ganancia esperada en "
               "una apuesta individual. Es una diferencia enorme. Maximizar el valor esperado puede indicarte que "
               "apuestes todo. Kelly nunca hace eso, porque respeta la matemática del interés compuesto y de la "
               "ruina.", "regular"),
    ], zonas_grafico=[{
        "caja": [195, 1115, 945, 1665], "estrategia": "A",
        "justificacion": "Curvas sin datos en el texto: no se regeneran; se reescriben los seis rótulos (ticks "
                         "sin tocar).",
        "tipo": "líneas: crecimiento según apalancamiento, curva teórica (Kelly) vs. real, zona óptima",
        "etiquetas": [
            et("Kelly estimate optimal max bet", "Apuesta máxima óptima según Kelly", [492, 1139, 752, 1157],
               tam_para("Kelly estimate optimal max bet", 260), color="#3D6FC0", borrado="plano", caja_borrar=pad([492, 1139, 752, 1157], 2), alineacion="izquierda"),
            et("Actual optimal max bet", "Apuesta máxima óptima real", [240, 1171, 434, 1188],
               tam_para("Actual optimal max bet", 194), color="#E07B39", borrado="plano", caja_borrar=pad([240, 1171, 434, 1188], 2)),
            et("Theoretical", "Teórica", [755, 1308, 848, 1323], tam_para("Theoretical", 93), color="#3D6FC0", borrado="plano", caja_borrar=pad([755, 1308, 848, 1323], 2),
               alineacion="izquierda"),
            et("Actual", "Real", [754, 1338, 806, 1352], tam_para("Theoretical", 93), color="#E07B39", borrado="plano", caja_borrar=pad([754, 1338, 806, 1352], 2),
               alineacion="izquierda"),
            et(rc, "Zona de\nequilibrio\nóptimo\nriesgo/retorno", [298, 1455, 386, 1522], 12.5,
               interlineado=1.3, color="#3B7D3E", borrado="local", caja_borrar=pad([298, 1455, 384, 1522], 2)),
            et("Leverage", "Apalancamiento", [536, 1640, 614, 1659], tam_para("Leverage", 78), color="#3A3A3A"),
        ],
    }], notas_revisar=[
        "Contradicción texto-gráfico: el gráfico ubica el óptimo de Kelly en un apalancamiento de ≈ 2 (más "
        "del 100 % del capital), mientras el texto dice que Kelly «nunca» apuesta todo. Con p < 1 y sin "
        "apalancamiento, la fracción de Kelly es menor que 1.",
        "Gráfico sin fuente ni unidades en el eje vertical; los ticks (6.00, 5.00…) se conservaron.",
    ])

    a = S[4]["bloques"]
    S[4].update(funcion="La trampa: conocer la ventaja real; Kelly fraccional", bloques=[
        bloque(a, 0, "titulo", "The catch?", "¿La trampa?", "regular"),
        bloque(a, 1, "cuerpo",
               "Kelly assumes you know your real edge. Overestimate how good your bet is, and Kelly will have you "
               "sizing way too big. That's why most professional traders use \"fractional Kelly\" — betting half "
               "or a quarter of what the formula says as a safety margin against being wrong about their own "
               "edge.",
               "Kelly supone que conocés tu verdadera ventaja. Si sobreestimás qué tan buena es tu apuesta, Kelly "
               "te va a hacer apostar montos demasiado grandes. Por eso la mayoría de los traders profesionales "
               "usa el “Kelly fraccional”: apuesta la mitad o un cuarto de lo que indica la fórmula, como margen "
               "de seguridad por si se equivoca sobre su propia ventaja.", "regular"),
    ], zonas_grafico=[{
        "caja": [270, 1130, 860, 1700], "estrategia": "A",
        "justificacion": "Curva g(f) sin parámetros en el texto: no se regenera; se reescriben los tres rótulos "
                         "en itálica serif, como el original.",
        "tipo": "curva: tasa de crecimiento g según la fracción apostada f, zonas de riesgo calculado, "
                "irracional y ruina",
        "etiquetas": [
            et("calculated risk", "riesgo calculado", [418, 1285, 537, 1307], tam_para("calculated risk", 119,
               archivo=ITAL), fuente=ITAL, color="#2626B0", borrado="inpaint", caja_borrar=pad([418, 1285, 537,
                                                                                               1307], 2)),
            et("irrational", "irracional", [743, 1190, 821, 1212], tam_para("irrational", 78, archivo=ITAL),
               fuente=ITAL, color="#C0272D", alineacion="derecha", borrado="inpaint",
               caja_borrar=pad([743, 1190, 821, 1212], 2)),
            et("ruin", "ruina", [815, 1572, 848, 1594], tam_para("ruin", 33, archivo=ITAL), fuente=ITAL,
               color="#3A2A2C", borrado="inpaint", caja_borrar=pad([815, 1572, 848, 1594], 2)),
        ],
    }], notas_revisar=[
        "Sin fuente: «la mayoría de los traders profesionales usa Kelly fraccional».",
        "Gráfico sin parámetros: no se sabe a qué apuesta corresponde la curva (el óptimo cae cerca de f = "
        "0,8). Los rótulos pisan la curva, igual que en el original.",
    ])

    a = S[5]["bloques"]
    S[5].update(funcion="Casos: Ed Thorp, Buffett, Renaissance", bloques=[
        bloque(a, 0, "titulo", "This isn't just theory", "No es solo teoría", "regular"),
        bloque(a, 1, "cuerpo",
               "Ed Thorp used Kelly to beat casinos at Blackjack in the 1960s, then took it to Wall Street and "
               "built one of the most successful hedge funds in history. Warren Buffett's concentrated bets follow "
               "Kelly logic. Renaissance Technologies reportedly uses sizing frameworks rooted in the same math.",
               "Ed Thorp usó Kelly para ganarles a los casinos al blackjack en la década de 1960; después lo llevó "
               "a Wall Street y construyó uno de los fondos de cobertura más exitosos de la historia. Las apuestas "
               "concentradas de Warren Buffett siguen la lógica de Kelly. Según se informa, Renaissance "
               "Technologies usa esquemas de dimensionamiento basados en la misma matemática.", "regular"),
    ], zonas_grafico=[{
        "caja": [220, 1090, 860, 1655], "estrategia": "C",
        "justificacion": "Foto recortada sin texto: se conserva.",
        "tipo": "foto: hombre de esmoquin en una mesa de blackjack", "etiquetas": [],
    }], notas_revisar=[
        FOTO + " Verificar también que la persona retratada sea Ed Thorp: el original no lo indica.",
        "Interpretación sin fuente: que las apuestas de Buffett «siguen la lógica de Kelly» es una lectura de "
        "terceros, no algo que Buffett haya declarado. Lo de Renaissance es trascendido («según se informa»).",
        "Ed Thorp: el fondo fue Princeton Newport Partners (1969-1988); precisar si se quiere dar el nombre.",
    ])

    a = S[6]["bloques"]
    S[6].update(funcion="Cierre: la mentalidad (sobrevivir primero), sin gráfico", bloques=[
        bloque(a, 0, "cuerpo",
               "The biggest lesson from Kelly isn't the formula — it's the mindset. Survival comes first. The "
               "traders who last decades aren't the ones who swing big on every trade. They're the ones who size "
               "correctly, stay in the game, and let compounding do the heavy lifting. Kelly proves that "
               "mathematically.",
               "La mayor lección de Kelly no es la fórmula: es la mentalidad. Primero está sobrevivir. Los traders "
               "que duran décadas no son los que apuestan fuerte en cada operación. Son los que dimensionan bien "
               "sus posiciones, siguen en juego y dejan que el interés compuesto haga el trabajo pesado. Kelly lo "
               "demuestra matemáticamente.", "regular"),
    ], zonas_grafico=[], notas_revisar=[
        "Exageración: Kelly demuestra que su fracción maximiza el crecimiento de largo plazo bajo supuestos "
        "(probabilidades conocidas, apuestas repetidas); no «demuestra» cómo duran los traders.",
    ])

    plan["glosario_nuevo"] = glosario([
        ("bankroll", "capital (de apuesta)"),
        ("odds you're getting (b)", "cuota que te pagan"),
        ("edge", "ventaja"),
        ("fractional Kelly", "Kelly fraccional"),
        ("sizing / size correctly", "dimensionar / dimensionar bien las posiciones"),
        ("compounding", "interés compuesto"),
        ("wipes you out", "te deja fuera de juego"),
        ("leave money on the table", "dejar dinero sobre la mesa"),
        ("calculated risk / irrational / ruin", "riesgo calculado / irracional / ruina"),
        ("Conservative / Aggressive / Insane / Suicidal", "Conservador / Agresivo / Insensato / Suicida"),
        ("Return / Risk", "Rendimiento / Riesgo"),
        ("trade-off", "equilibrio"),
    ])


if __name__ == "__main__":
    ejecutar(SLUG, curar)
