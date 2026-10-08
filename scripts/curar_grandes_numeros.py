"""Curación del carrusel de TikTok «The Law of Large Numbers» (@quantgent, 7 slides).

Uso: .venv/bin/python scripts/curar_grandes_numeros.py  (después de `extraer tiktok-quantgent-692630`)
"""

from curar_tiktok import FOTO, NB, ejecutar, et, glosario, nuevo, pad, pct

SLUG = "tiktok-quantgent-692630"
TEAL = "#3FB499"


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "The Law of Large Numbers: The Reason Casinos Never Lose"
    plan["titulo_es"] = "La ley de los grandes números: por qué los casinos nunca pierden"

    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        nuevo("titulo", "The Law of Large Numbers", "La ley de los grandes números", [174, 348, 906, 541], "bold",
              88, interlineado=1.2, color="#0A0A0A", ancho_px=800),
        nuevo("subtitulo", "The Reason Casinos Never Lose", "Por qué los casinos nunca pierden",
              [150, 635, 930, 675], "bold", 40, color="#0A0A0A", espacio_antes=69),
        nuevo("cuerpo",
              "A casino's edge on most games is less than 2%. Barely better than a coin flip. So how do they make "
              "billions?",
              f"La ventaja de un casino en la mayoría de los juegos es menor al {pct(2)}. Apenas mejor que tirar "
              f"una moneda. Entonces, ¿cómo ganan miles de millones?",
              [172, 761, 907, 992], "regular", 38, interlineado=1.5, espacio_antes=68),
        nuevo("cuerpo", "The answer is one of the most powerful equations in mathematics.",
              "La respuesta es una de las ecuaciones más poderosas de la matemática.", [186, 1069, 927, 1175],
              "regular", 38, interlineado=1.5, espacio_antes=56),
    ], zonas_grafico=[{
        "caja": [235, 1255, 845, 1660], "estrategia": "C",
        "justificacion": "Foto (cartas en una mesa de juego) sin texto relevante: se conserva.",
        "tipo": "foto: cartas sobre una mesa de casino", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Precisión: la ventaja de la casa es menor al 2 % en algunos juegos (blackjack con buena estrategia, "
        "punto y banca, craps), pero no en «la mayoría»: ruleta europea 2,7 %, americana 5,26 %, "
        "tragamonedas 2-15 %. Además, «la ley de los grandes números» es un teorema, no una ecuación.",
    ])

    S[1].update(funcion="Ejemplo: tirar una moneda 10, 100 y 10.000 veces", bloques=[
        nuevo("titulo", "Flip a coin 10 times", "Tirá una moneda 10 veces", [289, 500, 792, 555], "bold", 50,
              color="#0A0A0A"),
        nuevo("cuerpo",
              "You might get 7 heads and 3 tails. That's 70% heads... wildly off from the \"true\" 50%.",
              f"Podrías sacar 7 caras y 3 cecas. Eso es un {pct(70)} de caras… muy lejos del {pct(50)} “real”.",
              [127, 658, 952, 814], "regular", 38, interlineado=1.4, espacio_antes=103),
        nuevo("cuerpo", "Flip it **100** times? You'll probably land closer to 55/45.",
              "¿La tirás **100** veces? Probablemente quedes más cerca de 55/45.", [165, 904, 916, 1003], "regular",
              38, interlineado=1.4, espacio_antes=90),
        nuevo("cuerpo", "Flip it **10,000** times? You'll be almost exactly at 50%.",
              f"¿La tirás **10.000** veces? Vas a estar casi exactamente en el {pct(50)}.",
              [169, 1089, 914, 1192], "regular", 38, interlineado=1.4, espacio_antes=86),
        nuevo("destacado", "The more you play, the more the randomness disappears.",
              "Cuanto más jugás, más desaparece el azar.", [161, 1299, 919, 1414], "bold", 44,
              interlineado=1.35, espacio_antes=107),
    ], zonas_grafico=[], notas_revisar=[
        "Precisión: con 100 tiradas, quedar «cerca de 55/45» es plausible (desvío estándar de 5 puntos), pero "
        "no es lo «probable» en sentido estricto; el valor más probable sigue siendo 50/50.",
        "Imprecisión: «desaparece el azar». Lo que se reduce es la proporción; la diferencia absoluta entre "
        "caras y cecas, en promedio, crece con la cantidad de tiradas.",
    ])

    S[2].update(funcion="Definición: la ley de los grandes números (gráfico)", bloques=[
        nuevo("titulo", "This is the **Law of Large Numbers**", "Esta es la **ley de los grandes números**",
              [98, 485, 982, 539], "regular", 48, color="#0A0A0A"),
        nuevo("cuerpo",
              "As the number of trials increases, the average result converges to the expected value. Not "
              "approximately. Mathematically guaranteed.",
              "A medida que aumenta la cantidad de intentos, el resultado promedio converge al valor esperado. No "
              "de forma aproximada. Está garantizado matemáticamente.", [132, 647, 947, 865], "regular", 38,
              interlineado=1.5, espacio_antes=91),
        nuevo("cuerpo",
              "A casino doesn't need to win every hand. It just needs to play enough hands... And the math does "
              "the rest.",
              "Un casino no necesita ganar cada mano. Solo necesita jugar suficientes manos… Y la matemática hace "
              "el resto.", [114, 952, 966, 1102], "regular", 38, interlineado=1.5, espacio_antes=68),
    ], zonas_grafico=[{
        "caja": [150, 1210, 930, 1640], "estrategia": "A",
        "justificacion": "Gráfico ilustrativo sobre fondo negro con pocos rótulos: se reescriben sobre el negro "
                         "(borrado plano); la curva se conserva.",
        "tipo": "línea: ganancia acumulada (£) en el tiempo, con oscilaciones y tendencia creciente",
        "etiquetas": [
            et("Doing only\n+EV Casino Offers", "Solo ofertas de casino\ncon valor esperado positivo",
               [378, 1243, 640, 1283], 16.5, interlineado=1.2, alineacion="izquierda", color="#D9D9D9",
               borrado="plano", caja_borrar=[376, 1241, 532, 1285]),
            et("PROFIT (£)", "GANANCIA (£)", [240, 1238, 266, 1370], 19, peso="bold", rotacion=90, color=TEAL,
               borrado="plano", caja_borrar=[240, 1243, 267, 1363]),
            et("Lots of ups and\ndowns in profits\noccur", "Las ganancias\nsuben y bajan\nmucho",
               [425, 1466, 560, 1527], 16, interlineado=1.25, alineacion="izquierda", color="#D9D9D9",
               borrado="plano", caja_borrar=[425, 1466, 560, 1527]),
            et("But, the OVERALL TREND\non average is a steady,\ncontinuous INCREASE in\nprofits over time",
               "Pero la TENDENCIA GENERAL,\nen promedio, es un AUMENTO\nconstante y continuo de las\n"
               "ganancias con el tiempo", [645, 1381, 880, 1465], 15.5, interlineado=1.25,
               alineacion="izquierda", color="#D9D9D9", borrado="plano", caja_borrar=[644, 1381, 862, 1465]),
            et("TIME", "TIEMPO", [790, 1586, 858, 1607], 19, peso="bold", alineacion="derecha", color=TEAL,
               borrado="plano", caja_borrar=pad([805, 1589, 856, 1604], 3)),
        ],
    }], notas_revisar=[
        "Imprecisión: «garantizado matemáticamente» vale para el límite (convergencia en probabilidad o casi "
        "segura), no para una cantidad finita de manos.",
        "Gráfico ajeno al texto: muestra las ganancias (en libras) de un jugador que aprovecha ofertas de "
        "casino con valor esperado positivo, no las del casino. Sin fuente. Las negritas internas del original "
        "(«only», «OVERALL TREND», «INCREASE») se reflejan en mayúsculas.",
    ])

    S[3].update(funcion="La fórmula + Jacob Bernoulli", bloques=[
        nuevo("titulo", "The formula looks like it's written in another language",
              "La fórmula parece escrita en otro idioma", [106, 485, 973, 611], "regular", 46, interlineado=1.25,
              color="#0A0A0A"),
        nuevo("otro", "As n → ∞, X̄ₙ → μ", "Si n → ∞, X̄ₙ → μ", [316, 699, 765, 750], "bold", 50,
              color="#0A0A0A", espacio_antes=88),
        nuevo("cuerpo",
              "As the number of trials grows, the average approaches the true expected value. That's it. The "
              "casino's edge is μ. Every single bet is random. But across millions of bets, randomness cancels "
              "out and only the edge remains.",
              "A medida que crece la cantidad de intentos, el promedio se acerca al verdadero valor esperado. Eso "
              "es todo. La ventaja del casino es μ. Cada apuesta individual es aleatoria. Pero a lo largo de "
              "millones de apuestas, el azar se compensa y solo queda la ventaja.", [115, 842, 968, 1201],
              "regular", 40, interlineado=1.45, espacio_antes=92),
    ], zonas_grafico=[{
        "caja": [370, 1300, 715, 1700], "estrategia": "C",
        "justificacion": "Retrato con pie que es un nombre propio (Jacob Bernoulli): se conserva.",
        "tipo": "pintura: retrato de Jacob Bernoulli", "etiquetas": [],
    }], notas_revisar=[
        "Contexto que falta: Jacob Bernoulli demostró la primera versión de la ley (publicada en 1713, en "
        "Ars Conjectandi); el carrusel no lo explica.",
        "Precisión: μ es el valor esperado de cada apuesta; la ventaja del casino es μ solo si X es la ganancia "
        "del casino por unidad apostada.",
    ])

    S[4].update(funcion="Aplicación al trading: muchas apuestas chicas (gráfico)", bloques=[
        nuevo("titulo", "Now replace \"**casino**\" with \"**trader**\"",
              "Ahora reemplazá “**casino**” por “**trader**”", [103, 428, 976, 480], "regular", 48,
              color="#0A0A0A"),
        nuevo("cuerpo",
              "A strategy with a 52% win rate looks like noise after 10 trades. After 100, you might still be "
              "losing. But after 10,000 trades? The edge compounds into a certainty.",
              f"Una estrategia que gana el {pct(52)} de las veces parece ruido después de 10 operaciones. Después "
              f"de 100, todavía podrías estar perdiendo. ¿Pero después de 10.000 operaciones? La ventaja se "
              f"acumula hasta volverse una certeza.", [122, 587, 959, 805], "regular", 38, interlineado=1.5,
              espacio_antes=107),
        nuevo("cuerpo",
              "This is why the best hedge funds don't make one big bet. They make thousands of small ones and let "
              "the Law of Large Numbers turn a tiny edge into a fortune.",
              "Por eso los mejores fondos de cobertura no hacen una gran apuesta. Hacen miles de apuestas chicas y "
              "dejan que la ley de los grandes números convierta una ventaja mínima en una fortuna.",
              [117, 912, 966, 1130], "regular", 38, interlineado=1.5, espacio_antes=107),
    ], zonas_grafico=[{
        "caja": [130, 1195, 945, 1705], "estrategia": "A",
        "justificacion": "Simulación sin semilla ni parámetros completos: no se regenera; se reescriben leyenda, "
                         "ticks y rótulos.",
        "tipo": "líneas: patrimonio simulado de un trader sistemático (52 %) vs. uno intuitivo, 10 a 10.000 "
                "operaciones (escala log)",
        "etiquetas": [
            et("Systematic trader (52% edge, 10,000 trades)",
               f"Trader sistemático (ventaja del {pct(52)}, 10.000 operaciones)", [257, 1204, 700, 1221], 13,
               peso="bold", alineacion="izquierda", color="#3E8A64", caja_borrar=[254, 1203, 640, 1222]),
            et("Gut-feel trader (no edge, big bets)", "Trader intuitivo (sin ventaja, apuestas grandes)",
               [257, 1224, 700, 1242], 13, peso="bold", alineacion="izquierda", color="#B4474D",
               caja_borrar=[254, 1223, 551, 1243]),
            et("Start", "Inicio", [870, 1553, 915, 1566], 11.5, alineacion="izquierda", color="#A8A4A3",
               borrado="inpaint", caja_borrar=pad([875, 1555, 903, 1564], 2)),
            et("1,000", "1.000", [637, 1646, 669, 1660], 11.5, color="#A8A7A6"),
            et("10,000", "10.000", [849, 1646, 889, 1660], 11.5, color="#A8A7A6"),
            et("Number of trades →", "Cantidad de operaciones →", [430, 1681, 665, 1695], 11.5,
               color="#ACACAC", caja_borrar=pad([487, 1683, 608, 1693], 2)),
        ],
    }], notas_revisar=[
        "Contradicción interna: «ventaja del 52 %» en el gráfico es en realidad una tasa de acierto del 52 %; "
        "eso solo es una ventaja si ganancias y pérdidas son del mismo tamaño.",
        "Exageración: «la ventaja se vuelve una certeza» (la probabilidad de terminar en pérdida baja, pero "
        "no se anula; con 10.000 operaciones al 52 % es ≈ 0,003 %). Sin fuente: qué hacen «los mejores fondos».",
        "Gráfico simulado, sin fuente; rótulos reescritos. Revisar en Canva que la leyenda se lea bien.",
    ])

    S[5].update(funcion="Casos: seguros, casinos de Las Vegas, Netflix", bloques=[
        nuevo("cuerpo",
              "**Insurance companies** price every policy using it. That's how they stay profitable while paying "
              "out billions in claims.",
              "Las **aseguradoras** calculan el precio de cada póliza con ella. Así siguen siendo rentables "
              "aunque paguen miles de millones en siniestros.", [141, 501, 940, 661], "regular", 38,
              interlineado=1.45),
        nuevo("cuerpo",
              "**Casinos** in Vegas are designed around it the house edge on roulette is just 2.7%, but across 10 "
              "million spins a year, that's a guaranteed fortune.",
              f"Los **casinos** de Las Vegas están diseñados en torno a ella: la ventaja de la casa en la ruleta es "
              f"de apenas el {pct('2,7')}, pero a lo largo de 10 millones de tiradas por año, es una fortuna "
              f"asegurada.", [111, 775, 968, 994], "regular", 38, interlineado=1.45, espacio_antes=114),
        nuevo("cuerpo",
              "And **Netflix**? They don't need every show to be a hit. Across hundreds of originals, the Law of "
              "Large Numbers turns a small average return into an empire.",
              "¿Y **Netflix**? No necesita que cada serie sea un éxito. A lo largo de cientos de producciones "
              "propias, la ley de los grandes números convierte un rendimiento promedio chico en un imperio.",
              [130, 1105, 950, 1324], "regular", 38, interlineado=1.45, espacio_antes=111),
    ], zonas_grafico=[{
        "caja": [360, 1420, 920, 1680], "estrategia": "C",
        "justificacion": "Foto (cartel de Las Vegas): el texto es un nombre propio; se conserva.",
        "tipo": "foto: cartel «Welcome to Fabulous Las Vegas»", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Precisión: 2,7 % es la ventaja de la ruleta europea (un cero); en Las Vegas predomina la americana "
        "(doble cero), con 5,26 %. «10 millones de tiradas por año» no tiene fuente.",
        "Analogía discutible: Netflix no es un caso de la ley de los grandes números en sentido estricto (sus "
        "series no son ensayos independientes e idénticos); es diversificación de una cartera de contenidos.",
        "El original omite un signo entre «around it» y «the house edge»; en español se usaron dos puntos.",
    ])

    S[6].update(funcion="Cierre: la paciencia, sin gráfico", bloques=[
        nuevo("titulo", "The biggest lesson from the Law of Large Numbers isn't about math... it's about patience.",
              "La mayor lección de la ley de los grandes números no es la matemática… es la paciencia.",
              [121, 620, 960, 796], "bold", 44, interlineado=1.4, color="#0A0A0A"),
        nuevo("cuerpo",
              "One flip means nothing. One trade means nothing. One attempt means nothing. The edge only appears "
              "when you play enough times to let the math work. Most people quit before the numbers converge. "
              "The ones who don't?",
              "Una tirada no significa nada. Una operación no significa nada. Un intento no significa nada. La "
              "ventaja solo aparece cuando jugás suficientes veces como para que la matemática funcione. La "
              "mayoría abandona antes de que los números converjan. ¿Y los que no?",
              [128, 897, 951, 1225], "regular", 38, interlineado=1.45, espacio_antes=101),
        nuevo("destacado", "They're the house", "Son la casa.", [342, 1337, 758, 1382], "bold", 48,
              color="#0A0A0A", espacio_antes=112),
    ], zonas_grafico=[], notas_revisar=[
        "Advertencia de fondo: «la ventaja aparece si jugás suficientes veces» solo vale si la ventaja existe; "
        "con valor esperado negativo (el caso de casi todos los jugadores de casino), jugar más asegura perder.",
        "El original no cierra «They're the house» con punto; en español se agregó.",
    ])

    plan["glosario_nuevo"] = glosario([
        ("Law of Large Numbers", "ley de los grandes números"),
        ("(casino / house) edge", "ventaja (del casino / de la casa)"),
        ("trials", "intentos"),
        ("win rate", "tasa de acierto (gana el X % de las veces)"),
        ("trades", "operaciones"),
        ("insurance companies", "aseguradoras"),
        ("claims", "siniestros"),
        ("policy", "póliza"),
        ("originals (Netflix)", "producciones propias"),
        ("+EV", "con valor esperado positivo"),
        ("Gut-feel trader", "trader intuitivo"),
        ("Number of trades", "cantidad de operaciones"),
        ("PROFIT / TIME (ejes)", "GANANCIA / TIEMPO"),
    ])


if __name__ == "__main__":
    ejecutar(SLUG, curar)
