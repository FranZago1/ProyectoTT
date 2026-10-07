"""Curación manual (criterio) de los planes de la referencia: fat-tails y ergodicity.

Toma el borrador de `extraer` y fija: texto exacto en inglés (corregido mirando las imágenes),
traducción, roles, negritas, estrategia de cada gráfico y alertas de verificación.
Uso: .venv/bin/python scripts/curar_referencia.py  (después de `extraer`)
"""

import copy
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))
from carrusel.comun import cargar_config  # noqa: E402
from carrusel.render import fuente  # noqa: E402

CFG = cargar_config()
NB = " "  # espacio duro (antes de % y después de US$)


def tam_ancho(texto, ancho, peso="regular", archivo=None):
    w = fuente(CFG, peso, 100, archivo).getlength(texto)
    return round(100 * ancho / w, 1)


def bloque(auto, i, rol, en, es, peso=None, **extra):
    b = copy.deepcopy(auto[i]) if isinstance(i, int) else fusionar(auto, i)
    b.update({"rol": rol, "texto_en": en, "texto_es": es})
    if peso:
        b["peso"] = peso
    b.update(extra)
    return b


def fusionar(auto, idx):
    bs = [auto[i] for i in idx]
    b = copy.deepcopy(bs[0])
    b["caja"] = [min(x["caja"][0] for x in bs), min(x["caja"][1] for x in bs),
                 max(x["caja"][2] for x in bs), max(x["caja"][3] for x in bs)]
    b["ancho_px"] = max(x["ancho_px"] for x in bs)
    b["interlineado"] = next((x["interlineado"] for x in bs if x.get("interlineado")), None)
    return b


def zona_texto(bloques):
    cs = [b["caja"] for b in bloques if not b.get("fijo") and b["rol"] != "pie"]
    return [min(c[0] for c in cs), min(c[1] for c in cs), max(c[2] for c in cs), max(c[3] for c in cs)]


def pct(v):
    return f"{v}{NB}%"


# ---------------------------------------------------------------------------------------
# FAT TAILS
# ---------------------------------------------------------------------------------------

def fat_tails(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Fat Tails: How Quants Profit From the Impossible"
    plan["titulo_es"] = "Colas gruesas: cómo los quants ganan con lo imposible"

    # 1 — portada
    a = S[0]["bloques"]
    pie_en = "Fat tail vs normal distribution"
    S[0].update(funcion="Portada: concepto + promesa", bloques=[
        bloque(a, 0, "titulo", "Fat Tails", "Colas gruesas", "bold"),
        bloque(a, 1, "subtitulo", "How Quants Profit From the Impossible",
               "Cómo los analistas cuantitativos (quants) ganan con lo imposible", "regular"),
        {"rol": "pie", "texto_en": pie_en, "texto_es": "Cola gruesa vs. distribución normal", "peso": "regular",
         "tam_px": tam_ancho(pie_en, 497), "interlineado": 1.25, "color": "#0A0A0A", "caja": [291, 1193, 788, 1226],
         "fijo": True},
    ], zonas_grafico=[{
        "caja": [88, 556, 916, 1180], "estrategia": "C",
        "justificacion": "Figura académica con notación matemática (P(x), x); no tiene texto en lenguaje natural.",
        "tipo": "densidades de probabilidad (cola gruesa vs. normal), figura importada",
        "etiquetas": [],
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
        "caja": [141, 745, 883, 1300], "estrategia": "C",
        "justificacion": "Campana de Gauss con σ y porcentajes sobre relleno con textura: solo se traduce el "
                         "rótulo del eje, que está sobre fondo liso.",
        "tipo": "campana de Gauss con bandas de ±1σ, ±2σ y ±3σ (68,3 %, 95,4 %, 99,7 %)",
        "etiquetas": [
            {"texto_en": eje_en, "texto_es": "Desvíos estándar respecto de la media", "caja": [350, 1272, 740, 1297],
             "tam_px": tam_ancho(eje_en, 383), "color": "#2A2A2A"},
            {"texto_en": "68.3%", "texto_es": "68.3%", "caja": [0, 0, 0, 0], "conservar": True},
        ],
    }], notas_revisar=[
        "Gráfico: los porcentajes 68.3% / 95.4% / 99.7% quedaron con formato original (están sobre el relleno "
        "con textura). En Canva: reemplazar por 68,3 % / 95,4 % / 99,7 %.",
        "Gráfico: el primer rótulo del eje dice «4σ» y debería ser «−4σ» (error del original).",
    ])

    # 3 — modelo normal y 2008
    a = S[2]["bloques"]
    tit_en = "The S&P 500 looked bearish for all of 2008"
    ticks = [("1,600", "1.600", 808), ("1,500", "1.500", 851), ("1,400", "1.400", 893), ("1,300", "1.300", 936),
             ("1,200", "1.200", 977), ("1,100", "1.100", 1021), ("1,000", "1.000", 1064)]
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
        "caja": [222, 715, 850, 1305], "estrategia": "A",
        "justificacion": "Serie real del S&P 500: no se reconstruye a ojo. Pocos rótulos sobre fondo liso: se "
                         "reescriben título, rótulo del eje y ticks de miles.",
        "tipo": "línea: S&P 500, nivel diario, feb-2007 a dic-2009 (captura de terceros)",
        "etiquetas": [
            {"texto_en": tit_en, "texto_es": "El S&P 500 se mostró bajista durante todo 2008",
             "caja": [222, 717, 824, 753], "tam_px": tam_ancho(tit_en, 589, "semibold"), "peso": "semibold",
             "color": "#3D3D3D"},
            {"texto_en": "Index level", "texto_es": "Nivel del índice", "caja": [232, 980, 260, 1092],
             "tam_px": 15.5, "rotacion": 90, "color": "#A3A3A3"},
        ] + [{"texto_en": en, "texto_es": es, "caja": [260, y - 11, 308, y + 11], "tam_px": 15.5,
              "alineacion": "izquierda", "color": "#9E9E9E", "margen_borrado": 1} for en, es, y in ticks],
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
        "caja": [165, 772, 893, 1300], "estrategia": "C",
        "justificacion": "Figura académica con notación (E(L), VaR, ES): se traducen solo «Loss» y "
                         "«5% probability».",
        "tipo": "densidad de pérdidas con E(L), VaR y ES; cola del 5 % sombreada (figura importada)",
        "etiquetas": [
            {"texto_en": "Loss", "texto_es": "Pérdida", "caja": [544, 1269, 602, 1296], "tam_px": 26,
             "fuente": "LiberationSerif-Regular.ttf", "color": "#1A1A1A"},
            {"texto_en": "5% probability", "texto_es": f"{pct('5')} de probabilidad", "caja": [652, 1156, 824, 1188],
             "caja_borrar": [655, 1156, 822, 1192], "borrado": "inpaint", "halo": 3, "tam_px": 25,
             "fuente": "LiberationSerif-Regular.ttf", "alineacion": "izquierda", "desplazamiento": [-8, -2],
             "color": "#1A1A1A"},
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
        "caja": [120, 768, 960, 1240], "estrategia": "B",
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
        "caja": [0, 780, 1080, 1298], "estrategia": "D",
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

    # 7 — Ed Thorp + cisne negro
    a = S[6]["bloques"]
    def_en = ("An unpredictable event that is beyond what is normally expected of a situation and has potentially "
              "severe consequences.")
    S[6].update(funcion="Figura ejemplar y moraleja (Ed Thorp) + definición de «cisne negro»", bloques=[
        bloque(a, 0, "titulo", "Ed Thorp", "Ed Thorp", "bold"),
        bloque(a, 1, "cuerpo",
               "The same man who used the Kelly Criterion to beat casinos and then built one of the most successful "
               "hedge funds in history — survived 1998 without a scratch. Why? He never trusted the bell curve. He "
               "built every model expecting fat tails. The quants who survive decades aren't the ones with the "
               "smartest math. They're the ones who respect what the math can't see.",
               "El mismo hombre que usó el criterio de Kelly para ganarles a los casinos y después construyó uno de "
               "los fondos de cobertura más exitosos de la historia — atravesó 1998 sin un rasguño. ¿Por qué? Nunca "
               "confió en la campana de Gauss. Construyó cada modelo esperando colas gruesas. Los quants que "
               "sobreviven décadas no son los que tienen la matemática más sofisticada. Son los que respetan lo que "
               "la matemática no puede ver.", "regular"),
    ], zonas_grafico=[{
        "caja": [214, 900, 870, 1310], "estrategia": "C",
        "justificacion": "Ilustración: se conserva; el bloque de definición está sobre fondo liso y se traduce.",
        "tipo": "ilustración de un cisne negro con definición de diccionario",
        "etiquetas": [
            {"texto_en": "Black Swan", "texto_es": "Cisne negro", "caja": [614, 970, 830, 1012],
             "tam_px": tam_ancho("Black Swan", 206, "bold"), "peso": "bold", "alineacion": "izquierda",
             "color": "#1A1A1A"},
            {"texto_en": "[blak 'swän]", "texto_es": "[blak 'swän]", "caja": [0, 0, 0, 0], "conservar": True},
            {"texto_en": def_en,
             "texto_es": "Un evento impredecible\nque excede lo que\nnormalmente se espera\nde una situación y que\n"
                         "tiene consecuencias\npotencialmente graves.",
             "caja": [614, 1060, 872, 1243], "tam_px": 21.5, "interlineado": 1.38, "alineacion": "izquierda",
             "color": "#1A1A1A"},
        ],
    }], notas_revisar=[
        "Verificar: «sobrevivió 1998 sin un rasguño». En 1998 Thorp ya no dirigía Princeton Newport Partners "
        "(cerrado en 1988-1989); gestionaba Ridgeline Partners. No hay una fuente citada sobre su resultado en "
        "1998.",
        "Precisión: Thorp «les ganó a los casinos» con el conteo de cartas en el blackjack; el criterio de Kelly "
        "lo usó para dimensionar las apuestas.",
    ])
    for s in S:
        s["zona_texto"] = zona_texto(s["bloques"])
        s["curado"] = True


# ---------------------------------------------------------------------------------------
# ERGODICITY
# ---------------------------------------------------------------------------------------

def ergodicity(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Ergodicity: The Reason Expected Value Destroys Portfolios"
    plan["titulo_es"] = "Ergodicidad: por qué el valor esperado destruye carteras"

    # 1 — portada
    a = S[0]["bloques"]
    pie_en = "An ergodic measure for Diffusion Monte Carlo ground state wavefunctions"
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "Ergodicity", "Ergodicidad", "bold"),
        bloque(a, 1, "subtitulo", "The Reason Expected Value Destroys Portfolios",
               "Por qué el valor esperado destruye carteras", "bold"),
        bloque(a, 2, "cuerpo",
               "Physicists solved this decades ago. Hedge funds use it to size every bet. Economics still gets it "
               "wrong. Here's why it matters.",
               "Los físicos lo resolvieron hace décadas. Los fondos de cobertura lo usan para dimensionar cada "
               "apuesta. La economía todavía se equivoca. Veamos por qué importa.", "regular"),
        {"rol": "pie", "texto_en": pie_en,
         "texto_es": "Una medida ergódica para funciones de onda del estado fundamental en Monte Carlo por difusión",
         "peso": "regular", "tam_px": tam_ancho(pie_en, 708), "interlineado": 1.3, "color": "#8C8C8C",
         "caja": [186, 1198, 894, 1225], "fijo": True},
    ], zonas_grafico=[{
        "caja": [186, 715, 894, 1180], "estrategia": "C",
        "justificacion": "Figura académica (física): se conserva; solo se traduce el rótulo del eje Y.",
        "tipo": "funciones de onda de Monte Carlo por difusión (figura importada)",
        "etiquetas": [
            {"texto_en": "Relative probability", "texto_es": "Probabilidad relativa", "caja": [209, 864, 231, 986],
             "tam_px": 13.5, "rotacion": 90, "color": "#222222", "font_nota": "Arial en el original"},
        ],
    }], notas_revisar=[
        "Gráfico de portada sin relación con el tema: muestra funciones de onda de Monte Carlo por difusión "
        "(física cuántica), no ergodicidad en finanzas. Sugerencia: reemplazarlo por el gráfico de 10.000 "
        "personas vs. 1 persona.",
        "El pie quedó en dos líneas (el español es más largo); revisar en Canva.",
    ])

    # 2 — experimento mental
    a = S[1]["bloques"]
    S[1].update(funcion="Experimento mental: moneda +50 % / −40 %", bloques=[
        bloque(a, 0, "cuerpo", "Imagine a coin flip. Heads, your wealth grows by 50%. Tails, it drops by 40%.",
               f"Imaginá una tirada de moneda. Si sale cara, tu patrimonio crece un {pct('50')}. Si sale ceca, "
               f"cae un {pct('40')}.", "regular"),
        bloque(a, 1, "cuerpo", "You win 50. You lose 40. The win is bigger. Average it out and you're up 5 every flip.",
               "Ganás 50. Perdés 40. La ganancia es mayor. Si promediás, quedás 5 arriba en cada tirada.", "regular"),
        bloque(a, 2, "cuerpo",
               "This is what every finance textbook teaches. Maximize expected value. Take every positive EV bet.",
               "Esto es lo que enseña cualquier manual de finanzas. Maximizá el valor esperado. Tomá toda apuesta "
               "con valor esperado positivo.", "regular"),
        bloque(a, 3, "destacado", "The math looks bulletproof.", "La matemática parece infalible.", "bold"),
    ], zonas_grafico=[{
        "caja": [262, 798, 818, 1142], "estrategia": "B",
        "justificacion": "Valores exactos del texto: +50 %, −40 % y valor esperado +5 % "
                         "(0,5 × 1,50 + 0,5 × 0,60 = 1,05).",
        "tipo": "barras: cara +50 %, ceca −40 %, valor esperado +5 %",
        "datos": {"tipo": "moneda_valor_esperado", "ganancia_pct": 50, "perdida_pct": 40,
                  "formula": "(0,5 × 1,50) + (0,5 × 0,60) = 1,05",
                  "etiquetas": [f"Cara\n+{pct(50)}", f"Ceca\n−{pct(40)}", "Valor\nesperado"]},
    }], notas_revisar=[])

    # 3 — paradoja
    a = S[2]["bloques"]
    S[2].update(funcion="Paradoja: promedio de 10.000 personas vs. una persona en el tiempo", bloques=[
        bloque(a, 0, "cuerpo",
               "Run this exact game on 10,000 people simultaneously. The average wealth of the group explodes upward.",
               "Jugá exactamente este juego con 10.000 personas a la vez. El patrimonio promedio del grupo se "
               "dispara hacia arriba.", "regular"),
        bloque(a, 1, "cuerpo", "Now run it on one person, flipping a thousand times in a row.",
               "Ahora jugalo con una sola persona, que tira la moneda mil veces seguidas.", "regular"),
        bloque(a, 2, "destacado", "They go broke. Every single time.", "Termina en la ruina. Todas las veces.",
               "bold"),
        bloque(a, 3, "cuerpo",
               "Same bet. Same odds. Same math. Opposite outcome. The expected value was real. It just wasn't yours.",
               "Misma apuesta. Mismas probabilidades. Misma matemática. Resultado opuesto. El valor esperado era "
               "real. Simplemente no era el tuyo.", "regular"),
    ], zonas_grafico=[{
        "caja": [250, 800, 838, 1184], "estrategia": "B",
        "justificacion": "Simulación del juego (+50 % / −40 %): se regenera con semilla fija (42); "
                         "regenerado, no idéntico.",
        "tipo": "dos paneles en escala log: patrimonio promedio de 10.000 personas y 5 trayectorias "
                "individuales, 300 tiradas",
        "datos": {"tipo": "simulacion_conjunto", "semilla": 42, "personas": 10000, "tiradas": 300,
                  "trayectorias": 5, "inicial": 100, "ganancia_pct": 50, "perdida_pct": 40,
                  "titulo_1": "10.000 personas\n(patrimonio promedio)", "titulo_2": "1 persona\n(patrimonio real)",
                  "rotulo_x": "Tiradas"},
    }], notas_revisar=[
        "Gráfico: las trayectorias no coinciden con las del original (otra realización aleatoria); el eje Y del "
        "panel izquierdo llega a 10³ y no a 10⁵ como en el original.",
        "Afirmación absoluta: «Termina en la ruina. Todas las veces.» Es un resultado con probabilidad 1 en el "
        "límite (tiempo infinito), no en cada caso finito: tras 1.000 tiradas, una minoría ínfima sigue "
        "arriba del capital inicial.",
        "Inconsistencia: el texto habla de mil tiradas y el gráfico muestra 300.",
        "Precisión: con 10.000 personas el promedio muestral no «se dispara» indefinidamente; termina "
        "dominado por pocas trayectorias y cae (se ve en el propio gráfico). El valor esperado sí crece "
        "(1,05ⁿ).",
    ])

    # 4 — paso a paso
    a = S[3]["bloques"]
    S[3].update(funcion="Explicación paso a paso con $100", bloques=[
        bloque(a, 0, "titulo", "So what's actually happening?", "Entonces, ¿qué está pasando en realidad?", "bold"),
        bloque(a, 1, "cuerpo", "Start with $100. Heads. You gain 50%. You now have $150.",
               f"Empezás con $100. Sale cara. Ganás un {pct('50')}. Ahora tenés $150.", "regular"),
        bloque(a, 2, "cuerpo",
               "Next flip. Tails. You lose 40%. But that 40% is taken from $150, not from your original $100. 40% of "
               "$150 is $60. So you drop to $90.",
               f"Siguiente tirada. Sale ceca. Perdés un {pct('40')}. Pero ese {pct('40')} se calcula sobre $150, "
               f"no sobre tus $100 originales. El {pct('40')} de $150 es $60. Entonces bajás a $90.", "regular"),
        bloque(a, 3, "cuerpo", "One win. One loss. You should be back to even. But you're down $10.",
               "Una ganancia. Una pérdida. Deberías haber quedado igual. Pero estás $10 abajo.", "regular"),
        bloque(a, 4, "destacado",
               "This is the trick. The gain is 50% of a small number. The loss is 40% of a bigger number. The "
               "percentages look fair. The dollars don't.",
               f"Esta es la trampa. La ganancia es el {pct('50')} de un número menor. La pérdida es el {pct('40')} "
               f"de un número mayor. Los porcentajes parecen justos. Los dólares, no.", "bold"),
    ], zonas_grafico=[{
        "caja": [262, 898, 812, 1230], "estrategia": "B",
        "justificacion": "Valores exactos del texto: $100 → $150 → $90, pérdida de $60.",
        "tipo": "barras: inicio $100, cara $150, ceca $90; línea de punto de equilibrio en $100",
        "datos": {"tipo": "caminos_barras", "inicial": 100, "ganancia_pct": 50, "perdida_pct": 40,
                  "etiquetas": ["Inicio", f"Cara\n+{pct(50)}", f"Ceca\n−{pct(40)}"],
                  "rotulo_y": "Patrimonio ($)", "etiqueta_equilibrio": "Punto de\nequilibrio"},
    }], notas_revisar=[])

    # 5 — el orden no importa
    a = S[4]["bloques"]
    S[4].update(funcion="El orden no importa: siempre se pierde", bloques=[
        bloque(a, 0, "cuerpo", "Now flip the order. Start with $100. Tails first. You lose 40%. You're at $60.",
               f"Ahora invertí el orden. Empezás con $100. Primero sale ceca. Perdés un {pct('40')}. Quedás "
               f"en $60.", "regular"),
        bloque(a, 1, "cuerpo", "Heads next. You gain 50% of $60. That's only $30. You climb to $90.",
               f"Después sale cara. Ganás el {pct('50')} de $60. Son apenas $30. Subís a $90.", "regular"),
        bloque(a, [2, 3], "destacado",
               "Different order. Same result. $90. It doesn't matter whether you win first or lose first. You "
               "always end up poorer.",
               "Distinto orden. Mismo resultado. $90. No importa si primero ganás o primero perdés. Siempre "
               "terminás más pobre.", "bold"),
        bloque(a, 4, "cuerpo", "Do this enough times and you go to zero. Not bad luck. Just math.",
               "Repetilo suficientes veces y llegás a cero. No es mala suerte. Es matemática.", "regular"),
    ], zonas_grafico=[{
        "caja": [250, 812, 835, 1187], "estrategia": "B",
        "justificacion": "Datos exactos: caminos $100 → $150 → $90 y $100 → $60 → $90; serie alternada "
                         "cara/ceca de 30 tiradas (determinística).",
        "tipo": "dos paneles: ambos caminos terminan en $90; alternar cara y ceca 30 veces lleva a ~$20,6",
        "datos": {"tipo": "caminos_y_ruina", "inicial": 100, "ganancia_pct": 50, "perdida_pct": 40,
                  "tiradas_ruina": 30, "titulo_1": "Ambos caminos = $90", "titulo_2": "Repetir = ruina",
                  "leyenda_gana": "Gana primero", "leyenda_pierde": "Pierde primero",
                  "etiquetas_x": ["Inicio", "Tirada 1", "Tirada 2"], "rotulo_x": "Tiradas"},
    }], notas_revisar=[
        "Precisión: «llegás a cero» es asintótico; el patrimonio tiende a cero pero nunca lo alcanza "
        "(tras 30 tiradas alternadas quedan $20,6).",
    ])
    # 'espacio_antes' del bloque fusionado y del siguiente: se toman del original
    S[4]["bloques"][2]["espacio_antes"] = a[2].get("espacio_antes")
    S[4]["bloques"][3]["espacio_antes"] = a[4].get("espacio_antes")

    # 6 — criterio de Kelly
    a = S[5]["bloques"]
    S[5].update(funcion="Solución (criterio de Kelly) + historia (Kelly 1956, Ole Peters)", bloques=[
        bloque(a, 0, "titulo", "This is why the Kelly Criterion works", "Por esto funciona el criterio de Kelly",
               "bold"),
        bloque(a, 1, "cuerpo",
               "Kelly doesn't maximize expected value. It maximizes the geometric growth rate. The thing that "
               "actually determines your wealth over time.",
               "Kelly no maximiza el valor esperado. Maximiza la tasa de crecimiento geométrica. Lo que realmente "
               "determina tu patrimonio a lo largo del tiempo.", "regular"),
        bloque(a, 2, "cuerpo",
               "In 1956, Kelly solved this at Bell Labs. In 2020, physicist Ole Peters proved it formally. Bloomberg "
               "ran the headline: everything we've learned about modern economics is wrong.",
               "En 1956, Kelly lo resolvió en Bell Labs. En 2020, el físico Ole Peters lo demostró formalmente. "
               "Bloomberg lo tituló así: todo lo que aprendimos sobre la economía moderna está mal.", "regular"),
        bloque(a, 3, "destacado",
               "The gap between what happens on average and what happens to you over time is called ergodicity. "
               "When they diverge, expected value lies.",
               "La brecha entre lo que pasa en promedio y lo que te pasa a vos a lo largo del tiempo se llama "
               "ergodicidad. Cuando divergen, el valor esperado miente.", "bold"),
    ], zonas_grafico=[{
        "caja": [262, 892, 812, 1236], "estrategia": "B",
        "justificacion": "Fórmula exacta: g(f) = 0,5·ln(1 + 0,5f) + 0,5·ln(1 − 0,4f); óptimo f = 0,25; "
                         "g(1) ≈ −0,053.",
        "tipo": "curva de Kelly g(f) con el óptimo (f = 25 %) y apostar todo (f = 100 %, g ≈ −0,053)",
        "datos": {"tipo": "kelly", "p": 0.5, "ganancia_pct": 50, "perdida_pct": 40,
                  "texto_optimo": "Óptimo de Kelly\nf = {f}", "texto_total": f"Apostar todo (f = 100{NB}%)\ng = {{g}}",
                  "rotulo_x": "Fracción del patrimonio apostada (f)", "rotulo_y": "Tasa de crecimiento g(f)"},
    }], notas_revisar=[
        "Fecha incorrecta: «en 2020 Ole Peters lo probó formalmente». Sus trabajos centrales son de 2011 "
        "(«Optimal leverage from non-ergodicity») y 2016 (con Murray Gell-Mann, «Evaluating gambles using "
        "dynamics»); la nota de Bloomberg con ese titular es de 2017. La traducción es fiel; corregir el año.",
        "Precisión: la brecha entre promedio y trayectoria es la NO ergodicidad; «ergodicidad» es cuando ambos "
        "coinciden. La traducción es fiel; considerar «se llama no ergodicidad».",
        "Gráfico regenerado con la fórmula exacta; el original superponía «All-In» sobre el tick 0,8 "
        "(corregido).",
    ])

    # 7 — cierre
    a = S[6]["bloques"]
    S[6].update(funcion="Cierre aforístico sin gráfico", bloques=[
        bloque(a, 0, "cuerpo", "What ergodicity teaches us isn't mathematical...",
               "Lo que nos enseña la ergodicidad no es matemático…", "regular"),
        bloque(a, 1, "destacado", "It's that you don't live a thousand lives simultaneously.",
               "Es que no vivís mil vidas al mismo tiempo.", "bold"),
        bloque(a, 2, "cuerpo",
               "You live one life, sequentially. Every bet changes the size of the next one. Every loss makes "
               "recovery harder. The average of all possible outcomes is irrelevant if your personal path hits zero.",
               "Vivís una sola vida, en secuencia. Cada apuesta cambia el tamaño de la siguiente. Cada pérdida hace "
               "más difícil la recuperación. El promedio de todos los resultados posibles es irrelevante si tu "
               "propio camino llega a cero.", "regular"),
        bloque(a, 3, "cuerpo",
               "The market doesn't owe you the expected value. It only owes you the path you actually walk.",
               "El mercado no te debe el valor esperado. Solo te debe el camino que efectivamente recorrés.",
               "regular"),
    ], zonas_grafico=[], notas_revisar=[])
    for s in S:
        s["zona_texto"] = zona_texto(s["bloques"])
        s["curado"] = True


GLOSARIO_NUEVO = {
    "fat-tails": [
        ("disclaimers", "advertencias legales"),
        ("risk model", "modelo de riesgo"),
        ("reassurances", "frases tranquilizadoras"),
        ("zoom out (largo plazo)", "mirar el largo plazo"),
        ("Standard Deviations from the Mean", "desvíos estándar respecto de la media"),
        ("Index level", "nivel del índice"),
        ("probability", "probabilidad"),
        ("\"once in a lifetime\"", "“de una vez en la vida”"),
        ("lie detector", "detector de mentiras"),
        ("positions", "posiciones"),
        ("Nobel Prize winners", "premios Nobel"),
        ("Federal Reserve", "Reserva Federal"),
        ("smartest math", "la matemática más sofisticada"),
        ("equity capital", "capital propio"),
        ("leverage ratio", "apalancamiento (relación de)"),
        ("bailout funds", "fondos de rescate"),
        ("winds down its positions", "liquida sus posiciones"),
        ("consortium", "consorcio"),
        ("free fall", "caída libre"),
        ("timeline", "cronología"),
    ],
    "ergodicity": [
        ("portfolios", "carteras"),
        ("size every bet", "dimensionar cada apuesta"),
        ("finance textbook", "manual de finanzas"),
        ("positive EV bet", "apuesta con valor esperado positivo"),
        ("odds", "probabilidades"),
        ("go broke", "terminar en la ruina"),
        ("the trick", "la trampa"),
        ("Start (eje)", "Inicio"),
        ("Flip 1 / Flip 2", "Tirada 1 / Tirada 2"),
        ("Win first / Lose first", "Gana primero / Pierde primero"),
        ("Kelly Optimal", "óptimo de Kelly"),
        ("All-In", "apostar todo"),
        ("growth rate", "tasa de crecimiento"),
        ("Fraction of Wealth Bet", "fracción del patrimonio apostada"),
        ("Relative probability", "probabilidad relativa"),
        ("ground state wavefunctions", "funciones de onda del estado fundamental"),
        ("Diffusion Monte Carlo", "Monte Carlo por difusión"),
        ("average wealth / actual wealth", "patrimonio promedio / patrimonio real"),
    ],
}


def main():
    for slug, fn in (("fat-tails", fat_tails), ("ergodicity", ergodicity)):
        ruta = RAIZ / "trabajo" / slug / "plan.json"
        plan = json.loads(ruta.read_text(encoding="utf-8"))
        # el borrador se guarda para poder re-curar sin re-extraer
        borrador = ruta.with_name("plan_borrador.json")
        if not borrador.exists() or not plan["slides"][0].get("curado"):
            borrador.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
        plan = json.loads(borrador.read_text(encoding="utf-8"))
        fn(plan)
        plan["glosario_nuevo"] = [{"en": en, "es": es} for en, es in GLOSARIO_NUEVO[slug]]
        ruta.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"curado: {ruta}")


if __name__ == "__main__":
    main()
