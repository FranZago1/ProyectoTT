"""Curación del carrusel de TikTok «The Most Expensive Illusion in Trading» (sobreajuste; @quantgent, 6 slides).

Uso: .venv/bin/python scripts/curar_sobreajuste.py  (después de `extraer tiktok-quantgent-284502`)
"""

from curar_tiktok import NB, bloque, ejecutar, et, glosario, pad, pct

SLUG = "tiktok-quantgent-284502"
ITAL = "Inter-Italic.otf"
VERDE, ROJO, GRIS = "#2C744D", "#B5443D", "#9A9A9A"


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "The Most Expensive Illusion in Trading: How Overfitting Turns Perfect Backtests Into Real Losses"
    plan["titulo_es"] = "La ilusión más cara del trading: cómo el sobreajuste convierte backtests perfectos en pérdidas reales"

    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "The Most Expensive Illusion in Trading", "La ilusión más cara del trading", "bold"),
        bloque(a, 1, "subtitulo", "How Overfitting Turns Perfect Backtests Into Real Losses",
               "Cómo el sobreajuste (overfitting) convierte backtests perfectos en pérdidas reales", "bold"),
        bloque(a, 2, "cuerpo",
               "A trading model with 95% backtest accuracy can lose every dollar in live markets. This is the most "
               "common killer in quantitative finance. Here's why it happens.",
               f"Un modelo de trading con un {pct(95)} de acierto en el backtest (la prueba con datos históricos) "
               f"puede perder hasta el último dólar en el mercado real. Es la causa de muerte más común en las "
               f"finanzas cuantitativas. Veamos por qué ocurre.", "regular"),
    ], zonas_grafico=[{
        "caja": [285, 1165, 800, 1500], "estrategia": "A",
        "justificacion": "Curva ilustrativa sin datos: se reescriben los dos rótulos.",
        "tipo": "línea: capital en el backtest (sube) y en real (cae)",
        "etiquetas": [
            et("Backtest", "Backtest", [442, 1194, 479, 1203], 12, peso="bold", color=VERDE, conservar=True),
            et("Live", "En real", [690, 1175, 735, 1188], 11.5, peso="bold", color=ROJO,
               caja_borrar=pad([700, 1177, 722, 1186], 2)),
        ],
    }], notas_revisar=[
        "Exageración sin fuente: «la causa de muerte más común en las finanzas cuantitativas».",
    ])

    a = S[1]["bloques"]
    S[1].update(funcion="Planteo: el backtest perfecto", bloques=[
        bloque(a, 0, "cuerpo", "You build a model. You backtest it.",
               "Armás un modelo. Le hacés un backtest.", "regular"),
        bloque(a, 1, "cuerpo",
               "The equity curve goes up and to the right. 95% accuracy. Sharpe ratio above 3. Almost no drawdowns.",
               f"La curva de capital sube sin parar. {pct(95)} de acierto. Ratio de Sharpe por encima de 3. Casi "
               f"sin caídas.", "regular"),
        bloque(a, 2, "cuerpo", "You've found the edge. You're ready to go live.",
               "Encontraste la ventaja. Estás listo para operar en real.", "regular"),
        bloque(a, 3, "destacado",
               "Except you haven't found anything. Your model just memorised the past.",
               "Salvo que no encontraste nada. Tu modelo solo memorizó el pasado.", "bold"),
    ], zonas_grafico=[{
        "caja": [240, 1085, 840, 1450], "estrategia": "A",
        "justificacion": "Curva ilustrativa con tres métricas rotuladas: se reescriben valores y rótulos con "
                         "formato argentino.",
        "tipo": "línea: curva de capital del backtest con tasa de acierto 94,7 %, Sharpe 3,41 y caída máx. −2,1 %",
        "etiquetas": [
            et("94.7%", pct("94,7"), [318, 1107, 386, 1125], 15.5, peso="bold", color="#3F7A5A",
               caja_borrar=pad([323, 1109, 381, 1123], 2)),
            et("Win Rate", "Tasa de acierto", [310, 1134, 395, 1145], 8.5, color="#B5B5B5",
               caja_borrar=pad([333, 1136, 372, 1143], 2)),
            et("3.41", "3,41", [516, 1189, 563, 1207], 15.5, peso="bold", color="#3F7A5A",
               caja_borrar=pad([521, 1191, 558, 1205], 2)),
            et("Sharpe", "Sharpe", [525, 1219, 555, 1227], 8.5, color="#B5B5B5", conservar=True),
            et("-2.1%", f"−{pct('2,1')}", [673, 1259, 733, 1277], 15.5, peso="bold", color="#3F7A5A",
               borrado="plano", caja_borrar=pad([678, 1261, 728, 1275], 2)),
            et("Max DD", "Caída máx.", [672, 1287, 735, 1298], 8.5, color="#A9B2AD", borrado="plano",
               caja_borrar=pad([687, 1289, 720, 1296], 2)),
        ],
    }], notas_revisar=[
        "Diferencia texto-gráfico: el texto dice 95 % de acierto y el gráfico 94,7 % (redondeo).",
    ])

    a = S[2]["bloques"]
    S[2].update(funcion="Evidencia: estudios y el caso Knight Capital (2012)", bloques=[
        bloque(a, 0, "destacado", "44% of published trading strategies fail the moment they touch new data.",
               f"El {pct(44)} de las estrategias de trading publicadas fracasa apenas se enfrenta a datos nuevos.",
               "bold"),
        bloque(a, 1, "cuerpo",
               "AQR Capital tested a moving average strategy. Its Sharpe ratio collapsed from 1.2 to negative 0.2 "
               "on fresh data.",
               "AQR Capital probó una estrategia de medias móviles. Su ratio de Sharpe se desplomó de 1,2 a −0,2 "
               "con datos nuevos.", "regular"),
        bloque(a, 2, "cuerpo",
               "In 2012, Knight Capital deployed an overfitted algorithm. It lost $440 million in 45 minutes. The "
               "firm never recovered.",
               f"En 2012, Knight Capital puso en marcha un algoritmo sobreajustado. Perdió US${NB}440 millones en "
               f"45 minutos. La firma nunca se recuperó.", "regular"),
    ], zonas_grafico=[{
        "caja": [240, 1075, 830, 1475], "estrategia": "A",
        "justificacion": "Dos barras con los valores del texto (1,2 y −0,2): pocos rótulos sobre fondo liso; se "
                         "reescriben con formato argentino.",
        "tipo": "barras: ratio de Sharpe en backtest (1,2) y en real (−0,2)",
        "etiquetas": [
            et("1.2", "1,2", [405, 1087, 456, 1112], 23, peso="bold", color=VERDE,
               caja_borrar=pad([412, 1089, 449, 1110], 2)),
            et("-0.2", "−0,2", [640, 1404, 708, 1430], 23, peso="bold", color=ROJO,
               caja_borrar=pad([646, 1406, 702, 1428], 2)),
            et("Same\nstrategy", "Misma\nestrategia", [598, 1231, 668, 1262], 11, interlineado=1.15,
               fuente=ITAL, color="#ABABAB", borrado="inpaint", caja_borrar=pad([600, 1233, 661, 1260], 1)),
            et("Sharpe Ratio", "Ratio de Sharpe", [258, 1190, 276, 1305], 11.5, rotacion=90, color="#A0A0A0",
               caja_borrar=pad([260, 1204, 274, 1289], 2)),
            et("Live", "En real", [645, 1450, 705, 1465], 12, color="#848484",
               caja_borrar=pad([660, 1451, 688, 1463], 2)),
        ],
    }], notas_revisar=[
        "ERROR DE HECHO: la pérdida de Knight Capital (1 de agosto de 2012, US$ 440 millones en unos 45 minutos) "
        "se debió a una falla de implementación de software (se reactivó un código viejo en un servidor), no a "
        "un algoritmo sobreajustado. Además, la firma sí sobrevivió: fue rescatada por inversores y se fusionó "
        "con Getco en 2013 (KCG Holdings). Corregir o quitar en Canva.",
        "Sin fuente: «el 44 % de las estrategias publicadas fracasa» y el caso de AQR (Sharpe de 1,2 a −0,2). "
        "Verificar o citar el estudio.",
    ])

    a = S[3]["bloques"]
    S[3].update(funcion="Mecanismo: aprender el ruido; el elefante de Von Neumann", bloques=[
        bloque(a, 0, "titulo", "So what actually went wrong?", "Entonces, ¿qué salió mal en realidad?", "bold"),
        bloque(a, 1, "cuerpo",
               "Your model didn't learn the market. It learned the noise. Every random spike, every one-off event, "
               "every coincidence got baked into the rules.",
               "Tu modelo no aprendió el mercado. Aprendió el ruido. Cada salto aleatorio, cada hecho aislado, cada "
               "coincidencia quedó incorporada a las reglas.", "regular"),
        bloque(a, 2, "cita",
               "Von Neumann said it best: \"With four parameters I can fit an elephant, and with five I can make him "
               "wiggle his trunk.\"",
               "Von Neumann lo dijo mejor que nadie: “Con cuatro parámetros puedo ajustar un elefante, y con cinco "
               "puedo hacer que mueva la trompa”.", "regular"),
        bloque(a, 3, "destacado",
               "More parameters means more flexibility. More flexibility means the model can fit anything, "
               "including patterns that will never repeat.",
               "Más parámetros implican más flexibilidad. Más flexibilidad implica que el modelo puede ajustarse a "
               "cualquier cosa, incluso a patrones que nunca se van a repetir.", "bold"),
    ], zonas_grafico=[{
        "caja": [325, 1180, 880, 1530], "estrategia": "A",
        "justificacion": "Dos paneles ilustrativos con cuatro rótulos sobre fondo blanco: se reescriben.",
        "tipo": "dos paneles: modelo sobreajustado (20 parámetros) vs. modelo robusto (2 parámetros)",
        "etiquetas": [
            et("Overfit model", "Modelo sobreajustado", [331, 1195, 520, 1210], 14.5, peso="bold",
               alineacion="izquierda", color="#B5443D", caja_borrar=pad([331, 1197, 425, 1208], 2)),
            et("Robust model", "Modelo robusto", [610, 1195, 795, 1210], 14.5, peso="bold", color="#2C744D",
               caja_borrar=pad([655, 1197, 750, 1208], 2)),
            et("20 parameters", "20 parámetros", [341, 1494, 440, 1506], 12.5, fuente=ITAL,
               alineacion="izquierda", color="#B7605A", caja_borrar=pad([341, 1495, 415, 1505], 2)),
            et("2 parameters", "2 parámetros", [655, 1494, 750, 1506], 12.5, fuente=ITAL, color="#4F8A68",
               caja_borrar=pad([668, 1495, 736, 1505], 2)),
        ],
    }], notas_revisar=[
        "Cita correcta en sustancia: la atribuye Enrico Fermi a John von Neumann, según relató Freeman Dyson "
        "(Nature, 2004).",
    ])

    a = S[4]["bloques"]
    S[4].update(funcion="Diagnóstico: cómo saber si el modelo miente", bloques=[
        bloque(a, 0, "titulo", "How to know if your model is lying", "Cómo saber si tu modelo te miente", "bold"),
        bloque(a, 1, "cuerpo",
               "If the Sharpe ratio is above 3, be suspicious. If adjusting one parameter by 10% flips the strategy "
               "from profitable to losing, it's overfit.",
               f"Si el ratio de Sharpe supera 3, desconfiá. Si cambiar un parámetro un {pct(10)} da vuelta la "
               f"estrategia de ganadora a perdedora, está sobreajustada.", "regular"),
        bloque(a, 2, "cuerpo",
               "The real test: hold back 30% of your data. Never touch it. Run your final model on it once. If "
               "performance collapses, the backtest was a mirage.",
               f"La prueba de verdad: reservá el {pct(30)} de tus datos. No los toques nunca. Corré tu modelo final "
               f"sobre ellos una sola vez. Si el rendimiento se derrumba, el backtest era un espejismo.",
               "regular"),
        bloque(a, 3, "destacado", "The purpose of a backtest is to discard bad models. Not to improve them.",
               "El objetivo de un backtest es descartar modelos malos. No mejorarlos.", "bold"),
    ], zonas_grafico=[{
        "caja": [280, 1150, 800, 1525], "estrategia": "A",
        "justificacion": "Mapa de calor ilustrativo con tres rótulos: se reescriben (el del centro, sobre las "
                         "celdas, por inpainting).",
        "tipo": "mapa de calor: rendimiento según dos parámetros; una zona verde aislada («ventaja» sobreajustada)",
        "etiquetas": [
            et("Overfit\n\"edge\"", "“Ventaja”\nficticia", [566, 1271, 616, 1294], 8.5, peso="bold",
               interlineado=1.15, color="#2E6B48", borrado="inpaint", caja_borrar=[573, 1272, 607, 1293]),
            et("Parameter A", "Parámetro A", [281, 1290, 297, 1365], 9.5, rotacion=90, color="#A9A9A9", borrado="plano",
               caja_borrar=pad([284, 1296, 293, 1358], 2)),
            et("Parameter B", "Parámetro B", [500, 1506, 600, 1518], 9.5, color="#AAAAAA",
               caja_borrar=pad([519, 1508, 580, 1516], 2)),
        ],
    }], notas_revisar=[
        "Reglas prácticas (Sharpe mayor que 3, ±10 % en un parámetro, reservar el 30 % de los datos) sin "
        "fuente; son heurísticas habituales, no umbrales universales.",
        "Mapa de calor: el rótulo central es muy chico (8,5 px) y está sobre celdas de color; si no se lee bien, "
        "rehacerlo en Canva.",
    ])

    a = S[5]["bloques"]
    S[5].update(funcion="Cierre: disciplina ante los patrones, sin gráfico", bloques=[
        bloque(a, 0, "cuerpo", "The lesson from overfitting isn't technical...",
               "La lección del sobreajuste no es técnica…", "regular"),
        bloque(a, 1, "destacado", "It's that humans are wired to see patterns that aren't there.",
               "Es que los humanos estamos programados para ver patrones que no existen.", "bold"),
        bloque(a, 2, "cuerpo",
               "We find signal in noise, edges in randomness, meaning in coincidence. The best quants don't just "
               "build better models. They build better discipline.",
               "Encontramos señal en el ruido, ventajas en el azar, sentido en la coincidencia. Los mejores quants "
               "no solo construyen mejores modelos. Construyen más disciplina.", "regular"),
        bloque(a, 3, "cuerpo", "The hardest trade in finance is walking away from a beautiful backtest.",
               "La operación más difícil de las finanzas es abandonar un backtest hermoso.", "regular"),
    ], zonas_grafico=[], notas_revisar=[])

    plan["glosario_nuevo"] = glosario([
        ("overfitting / overfit", "sobreajuste (overfitting) / sobreajustado"),
        ("backtest", "backtest (prueba con datos históricos)"),
        ("equity curve", "curva de capital"),
        ("drawdown / Max DD", "caída / caída máx."),
        ("Sharpe ratio", "ratio de Sharpe"),
        ("win rate", "tasa de acierto"),
        ("go live / live markets", "operar en real / mercado real"),
        ("moving average", "media móvil"),
        ("noise / signal", "ruido / señal"),
        ("hold back (data)", "reservar (datos)"),
        ("Robust model", "modelo robusto"),
    ])


if __name__ == "__main__":
    ejecutar(SLUG, curar)
