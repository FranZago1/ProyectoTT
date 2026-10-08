"""Curación del carrusel de TikTok «Fat Tails» (@quantgent, 7 slides, 9:16).

Es la versión de TikTok del carrusel de referencia `fat-tails` (Instagram, 4:5): mismos textos, otra
maquetación. Las traducciones y alertas son las de `scripts/curar_referencia.py` (fat_tails); aquí solo
cambian las cajas, medidas sobre las imágenes 1080 × 1920.
Uso: .venv/bin/python scripts/curar_fat_tails_tiktok.py  (después de `extraer tiktok-quantgent-735830`)
"""

from curar_tiktok import NB, SERIF, bloque, ejecutar, et, nuevo, pct, tam_ancho

SLUG = "tiktok-quantgent-735830"


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Fat Tails: How Quants Profit From the Impossible"
    plan["titulo_es"] = "Colas gruesas: cómo los quants ganan con lo imposible"
    plan["version_de"] = "fat-tails"

    # 1 — portada
    a = S[0]["bloques"]
    pie_en = "Fat tail vs normal distribution"
    S[0].update(funcion="Portada: concepto + promesa", bloques=[
        bloque(a, 0, "titulo", "Fat Tails", "Colas gruesas", "bold"),
        bloque(a, 1, "subtitulo", "How Quants Profit From the Impossible",
               "Cómo los analistas cuantitativos (quants) ganan con lo imposible", "regular"),
        {"rol": "pie", "texto_en": pie_en, "texto_es": "Cola gruesa vs. distribución normal", "peso": "regular",
         "tam_px": tam_ancho(pie_en, 496), "interlineado": 1.25, "color": "#1A1A1A",
         "caja": [290, 1456, 790, 1491], "fijo": True},
    ], zonas_grafico=[{
        "caja": [80, 765, 925, 1445], "estrategia": "C",
        "justificacion": "Figura académica con notación matemática (P(x), x); no tiene texto en lenguaje natural.",
        "tipo": "densidades de probabilidad (cola gruesa vs. normal), figura importada", "etiquetas": [],
    }], notas_revisar=[
        "Gráfico de portada: las curvas no están rotuladas; no se puede saber cuál es la normal y cuál la de "
        "cola gruesa (la verde está centrada en −2). Considerar una figura con leyenda.",
    ])

    # 2 — mito
    a = S[1]["bloques"]
    eje_en = "Standard Deviations from the Mean"
    S[1].update(funcion="Mito: «la matemática te miente» (advertencias y modelo equivocado)", bloques=[
        bloque(a, 0, "titulo", "The Math Is Lying to You", "La matemática te miente", "bold"),
        bloque(a, 1, "cita", "\"Past performance doesn't guarantee future results\"",
               "“Rendimientos pasados no garantizan rendimientos futuros”", "regular"),
        bloque(a, 2, "cuerpo",
               "You've seen the disclaimers. You've heard that crashes are rare. That markets recover. That if you "
               "zoom out, everything goes up. What nobody tells you is that every single one of those reassurances "
               "is based on a math model that is provably, dangerously wrong.",
               "Viste las advertencias legales. Escuchaste que los derrumbes son raros. Que los mercados se "
               "recuperan. Que, si mirás el largo plazo, todo sube. Lo que nadie te dice es que cada una de esas "
               "frases tranquilizadoras se apoya en un modelo matemático que está equivocado de forma demostrable "
               "y peligrosa.", "regular"),
    ], zonas_grafico=[{
        "caja": [130, 1090, 1000, 1648], "estrategia": "C",
        "justificacion": "Campana de Gauss con σ y porcentajes sobre relleno con textura: solo se traduce el "
                         "rótulo del eje, que está sobre fondo liso.",
        "tipo": "campana de Gauss con bandas de ±1σ, ±2σ y ±3σ (68,3 %, 95,4 %, 99,7 %)",
        "etiquetas": [et(eje_en, "Desvíos estándar respecto de la media", [350, 1617, 740, 1642],
                         tam_ancho(eje_en, 382), color="#3A3A3A")],
    }], notas_revisar=[
        "Gráfico: los porcentajes 68.3% / 95.4% / 99.7% quedaron con formato original (están sobre el relleno "
        "con textura). En Canva: reemplazar por 68,3 % / 95,4 % / 99,7 %.",
        "Gráfico: el primer rótulo del eje dice «4σ» y debería ser «−4σ» (error del original).",
    ])

    # 3 — modelo normal y 2008
    a = S[2]["bloques"]
    tit_en = "The S&P 500 looked bearish for all of 2008"
    ticks = [("1,600", "1.600", 1146), ("1,500", "1.500", 1189), ("1,400", "1.400", 1231), ("1,300", "1.300", 1274),
             ("1,200", "1.200", 1316), ("1,100", "1.100", 1360), ("1,000", "1.000", 1403)]
    S[2].update(funcion="El modelo normal y la crisis de 2008", bloques=[
        bloque(a, 0, "cuerpo",
               "Most risk models assume price moves follow something called a normal distribution — a bell curve. "
               "Small moves happen constantly. Big moves almost never. Crashes? Basically impossible. In 2008, this "
               "model said the crash that just wiped out the global economy should only happen once in the lifetime "
               "of the entire universe. Your parents remember it.",
               "La mayoría de los modelos de riesgo supone que los movimientos de precios siguen algo llamado "
               "distribución normal —una campana de Gauss—. Los movimientos pequeños ocurren todo el tiempo. Los "
               "grandes, casi nunca. ¿Los derrumbes? Prácticamente imposibles. En 2008, este modelo decía que el "
               "derrumbe que acababa de arrasar con la economía global debería ocurrir una sola vez en toda la vida "
               "del universo. Tus padres lo recuerdan.", "regular"),
    ], zonas_grafico=[{
        "caja": [220, 1055, 850, 1640], "estrategia": "A",
        "justificacion": "Serie real del S&P 500: no se reconstruye a ojo. Pocos rótulos sobre fondo liso: se "
                         "reescriben título, rótulo del eje y ticks de miles.",
        "tipo": "línea: S&P 500, nivel diario, feb-2007 a dic-2009 (captura de terceros)",
        "etiquetas": [
            et(tit_en, "El S&P 500 se mostró bajista durante todo 2008", [222, 1058, 824, 1092],
               tam_ancho(tit_en, 589, "semibold"), peso="semibold", color="#3D3D3D"),
            et("Index level", "Nivel del índice", [234, 1318, 254, 1420], 15.5, rotacion=90, color="#A3A3A3"),
        ] + [et(en, es, [262, y - 8, 306, y + 8], 15.5, alineacion="izquierda", color="#9E9E9E",
                margen_borrado=1) for en, es, y in ticks],
    }], notas_revisar=[
        "Gráfico: las fechas del eje X están en formato de EE. UU. (mes/día/año, p. ej. 3/23/07). Quedaron "
        "sin tocar (texto rotado y chico); en Canva convendría reemplazarlas por día/mes/año o por meses.",
        "Gráfico: el título dice «todo 2008» pero la serie abarca de febrero de 2007 a diciembre de 2009.",
        "Afirmación imprecisa: «en 2008 este modelo decía que el derrumbe debería ocurrir una vez en la vida "
        "del universo». La frase célebre de ese tipo es de agosto de 2007 (David Viniar, Goldman Sachs: "
        "«movimientos de 25 desvíos estándar, varios días seguidos») y es una hipérbole; no hay un modelo único "
        "que lo «dijera». Verificar o suavizar.",
    ])

    # 4 — concepto: colas gruesas
    a = S[3]["bloques"]
    S[3].update(funcion="Nombre del concepto (colas gruesas) y su definición", bloques=[
        bloque(a, 0, "subtitulo", "This is what quants call :", "Esto es lo que los quants llaman:", "regular"),
        bloque(a, 1, "titulo", "FAT TAILS", "COLAS GRUESAS", "bold"),
        bloque(a, 2, "cuerpo",
               "It just means extreme events happen way more often than the math says they should. The bell curve "
               "says 99.7% of moves stay small and predictable. Reality says closer to 95%. That missing 5% is "
               "where people get rich — or lose everything overnight.",
               f"Simplemente significa que los eventos extremos ocurren mucho más seguido de lo que la matemática "
               f"dice que deberían. La campana de Gauss dice que el {pct('99,7')} de los movimientos se mantiene "
               f"pequeño y predecible. La realidad indica algo más cercano al {pct('95')}. Ese {pct('5')} que falta "
               f"es donde la gente se hace rica —o lo pierde todo de un día para el otro.", "regular"),
    ], zonas_grafico=[{
        "caja": [165, 1090, 900, 1630], "estrategia": "C",
        "justificacion": "Figura académica con notación (E(L), VaR, ES): se traducen solo «Loss» y "
                         "«5% probability».",
        "tipo": "densidad de pérdidas con E(L), VaR y ES; cola del 5 % sombreada (figura importada)",
        "etiquetas": [
            et("Loss", "Pérdida", [544, 1587, 602, 1614], 26, fuente=SERIF, color="#1A1A1A"),
            et("5% probability", f"{pct('5')} de probabilidad", [652, 1480, 824, 1514], 25, fuente=SERIF,
               caja_borrar=[655, 1480, 822, 1518], borrado="inpaint", halo=3, alineacion="izquierda",
               desplazamiento=[-8, -2], color="#1A1A1A"),
        ],
    }], notas_revisar=[
        "Afirmación sin sustento citado: «la realidad dice más cerca del 95 %». No hay fuente; el valor depende "
        "del activo, el período y la frecuencia de los retornos.",
        "Gráfico: el eje X del original muestra 10, 5, 0, 5, 10 (sin signos negativos). Se conservó.",
        "Gráfico: «5 % de probabilidad» se reescribió sobre la cola con un halo blanco; revisar en Canva que "
        "la línea de ES y la curva se lean bien detrás del rótulo.",
    ])

    # 5 — curtosis
    a = S[4]["bloques"]
    S[4].update(funcion="Cómo medirlo: la curtosis", bloques=[
        bloque(a, 0, "cuerpo",
               "There's actually a number that tells you how badly the bell curve is fooling you. It's called "
               "kurtosis. A perfect bell curve scores a 3. The S&P 500? Around 10. Crypto? Regularly above 15. The "
               "higher it is, the more \"once in a lifetime\" events are quietly heading your way. Think of kurtosis "
               "as a lie detector for your risk model.",
               "Existe un número que te dice cuánto te está engañando la campana de Gauss. Se llama curtosis. Una "
               "campana de Gauss perfecta marca 3. ¿El S&P 500? Alrededor de 10. ¿Cripto? Con frecuencia, por "
               "encima de 15. Cuanto más alto es, más eventos “de una vez en la vida” se acercan en silencio hacia "
               "vos. Pensá en la curtosis como un detector de mentiras para tu modelo de riesgo.", "regular"),
    ], zonas_grafico=[{
        "caja": [100, 1075, 980, 1560], "estrategia": "B",
        "justificacion": "Barras con valores dados en el texto (3, ~10, 15+): se regenera exacto.",
        "tipo": "barras: curtosis de la campana de Gauss (3), S&P 500 (~10) y cripto (15+)",
        "datos": {"tipo": "barras_curtosis", "valores": [3, 10, 15],
                  "etiquetas_valor": ["3", "~10", "15+"], "color_valor": ["#CFCFCF", "#FFFFFF", "#FFFFFF"],
                  "colores": ["#CDCDCD", "naranja", "rojo_intenso"],
                  "categorias": ["Campana de Gauss", "S&P 500", "Cripto"],
                  "subtitulos": ["Lo que suponen los modelos", "3 veces más eventos extremos",
                                 "5 veces más eventos extremos"],
                  "rotulo_eje": "CURTOSIS",
                  "titulo_1": "Cuanto más alto el número,", "titulo_2": "más te miente tu modelo."},
    }], notas_revisar=[
        "Afirmación no derivable: «3x / 5x más eventos extremos» no se deduce de una curtosis de 10 o 15; además "
        "la curtosis del S&P 500 depende mucho del período y de la frecuencia (diaria, mensual). Verificar o "
        "quitar.",
        "Precisión técnica: 3 es la curtosis de la normal; muchas fuentes reportan el exceso de curtosis "
        "(normal = 0). Conviene aclarar qué medida se usa.",
    ])

    # 6 — LTCM
    a = S[5]["bloques"]
    S[5].update(funcion="Caso histórico: LTCM (1998)", bloques=[
        bloque(a, 0, "cuerpo",
               "This is exactly how Long-Term Capital Management collapsed. Two Nobel Prize winners. The smartest "
               "quants on the planet. $100 billion in positions. Their models said they were untouchable. In 1998, "
               "a fat tail event nearly took down the entire global financial system. The Federal Reserve had to "
               "organize a $3.6 billion rescue. The models were flawless — reality just didn't cooperate.",
               f"Así exactamente colapsó Long-Term Capital Management. Dos premios Nobel. Los quants más brillantes "
               f"del planeta. US${NB}100.000 millones en posiciones. Sus modelos decían que eran intocables. En "
               f"1998, un evento de cola gruesa casi derriba todo el sistema financiero global. La Reserva Federal "
               f"tuvo que organizar un rescate de US${NB}3.600 millones. Los modelos eran impecables —la realidad "
               f"simplemente no cooperó.", "regular"),
    ], zonas_grafico=[{
        "caja": [0, 1060, 1080, 1645], "estrategia": "D",
        "justificacion": "Línea de tiempo con mucho texto chico: se conserva la imagen y se entrega la "
                         "traducción completa para rehacerla en Canva.",
        "tipo": "línea de tiempo de la crisis de LTCM, 1994-1999 (captura de terceros)",
        "etiquetas": [],
        "textos_es": [
            "Título: CRISIS DE LTCM: CRONOLOGÍA",
            f"1994: John Meriwether funda Long-Term Capital Management (LTCM) con alrededor de US${NB}1.000 "
            f"millones en activos iniciales.",
            "1994-1997: enorme éxito de LTCM.",
            "1997: crisis cambiaria asiática (→ devaluación…).",
            "Noviembre de 1997: comienzo de la crisis rusa.",
            f"1998: debacle de LTCM. Mayo: la cartera pierde un {pct('6')}. Junio: pérdidas del {pct('10')}. "
            f"Julio: caída de la cartera del {pct('18')}. Agosto: las bolsas se desploman; LTCM pierde "
            f"US${NB}553 millones, o el {pct('15')} de su capital: prácticamente todas sus posiciones juegan en "
            f"contra. Fines de agosto: el fondo LTCM pierde el {pct('44')} de su valor. Septiembre: el rendimiento "
            f"de LTCM entra en caída libre y cierra el mes con una baja de más del {pct('83')}.",
            "17 de agosto de 1998: Rusia entra en default de sus bonos soberanos.",
            f"23 de septiembre de 1998: Warren Buffett ofrece comprar LTCM por US${NB}250 millones y "
            f"recapitalizarlo con US${NB}4.000 millones (US${NB}3.000 millones de Berkshire Hathaway, "
            f"US${NB}700 millones de AIG y US${NB}300 millones de Goldman Sachs). Buffett le da a LTCM apenas "
            f"unas horas para decidir sobre su propuesta. Por diversas razones, la oferta es rechazada.",
            "26-27 de septiembre de 1998: se reúnen 100 abogados que representan al consorcio de 14 bancos. Pasan "
            "el fin de semana tratando de entender los complejos activos, deudas, estructura y gestión de LTCM.",
            f"28 de septiembre de 1998: el capital propio de LTCM cae de US${NB}2.300 millones a US${NB}400 "
            f"millones entre el 1 y el 28 de septiembre de 1998. La deuda sigue por encima de US${NB}100.000 "
            f"millones, lo que implica un apalancamiento de más de 250 a 1. El consorcio de 14 bancos aporta "
            f"US${NB}3.600 millones en fondos de rescate, a cambio de los cuales recibe el {pct('90')} de la "
            f"propiedad de LTCM.",
            f"Diciembre de 1999: bajo la conducción del consorcio, LTCM liquida sus posiciones antes de diciembre "
            f"de 1999 y devuelve US${NB}3.600 millones de capital al consorcio.",
        ],
    }], notas_revisar=[
        "Gráfico (estrategia D): REHACER EN CANVA la línea de tiempo con los textos de textos_es.md "
        "(se conservó la imagen original en inglés).",
        "Afirmación imprecisa: la Reserva Federal (de Nueva York) coordinó el rescate, pero los US$ 3.600 millones "
        "los pusieron 14 bancos privados, no la Fed. La traducción es fiel; considerar aclararlo.",
        "Cifra a verificar: «US$ 100.000 millones en posiciones». Las fuentes hablan de unos US$ 125.000 millones "
        "en activos y más de US$ 1 billón (1 trillion) de nocional en derivados.",
        "Línea de tiempo: la fecha de cierre del fondo (dic-1999 / principios de 2000) y la devolución de "
        "«US$ 3.600 millones de capital» deberían verificarse antes de rehacerla.",
    ])

    # 7 — Ed Thorp + cisne negro (el borrador no detectó la zona de texto: bloques escritos a mano)
    def_en = ("An unpredictable event that is beyond what is normally expected of a situation and has potentially "
              "severe consequences.")
    S[6].update(funcion="Figura ejemplar y moraleja (Ed Thorp) + definición de «cisne negro»", bloques=[
        nuevo("titulo", "Ed Thorp", "Ed Thorp", [428, 369, 645, 417], "bold", 47, color="#111111"),
        nuevo("cuerpo",
              "The same man who used the Kelly Criterion to beat casinos and then built one of the most successful "
              "hedge funds in history — survived 1998 without a scratch. Why? He never trusted the bell curve. He "
              "built every model expecting fat tails. The quants who survive decades aren't the ones with the "
              "smartest math. They're the ones who respect what the math can't see.",
              "El mismo hombre que usó el criterio de Kelly para ganarles a los casinos y después construyó uno de "
              "los fondos de cobertura más exitosos de la historia atravesó 1998 sin un rasguño. ¿Por qué? Nunca "
              "confió en la campana de Gauss. Construyó cada modelo esperando colas gruesas. Los quants que "
              "sobreviven décadas no son los que tienen la matemática más sofisticada. Son los que respetan lo que "
              "la matemática no puede ver.", [121, 507, 964, 1117], "regular", 42, interlineado=1.5,
              color="#111111", espacio_antes=60),
    ], zonas_grafico=[{
        "caja": [125, 1210, 880, 1650], "estrategia": "C",
        "justificacion": "Ilustración: se conserva; el bloque de definición está sobre fondo liso y se traduce.",
        "tipo": "ilustración de un cisne negro con definición de diccionario",
        "etiquetas": [
            et("Black Swan", "Cisne negro", [614, 1300, 830, 1338], tam_ancho("Black Swan", 205, "semibold"),
               peso="semibold", alineacion="izquierda", color="#111115"),
            et(def_en, "Un evento impredecible\nque excede lo que\nnormalmente se espera\nde una situación y que\n"
                       "tiene consecuencias\npotencialmente graves.", [614, 1388, 872, 1568], 21.5,
               interlineado=1.38, alineacion="izquierda", color="#3A3B40"),
        ],
    }], notas_revisar=[
        "Verificar: «sobrevivió 1998 sin un rasguño». En 1998 Thorp ya no dirigía Princeton Newport Partners "
        "(cerrado en 1988-1989); gestionaba Ridgeline Partners. No hay una fuente citada sobre su resultado en "
        "1998.",
        "Precisión: Thorp «les ganó a los casinos» con el conteo de cartas en el blackjack; el criterio de Kelly "
        "lo usó para dimensionar las apuestas.",
    ])
    plan["glosario_nuevo"] = []


if __name__ == "__main__":
    ejecutar(SLUG, curar)
