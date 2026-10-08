"""Curación del carrusel de TikTok «Black-Scholes» (@quantgent, 8 slides).

Uso: .venv/bin/python scripts/curar_black_scholes.py  (después de `extraer tiktok-quantgent-138326`)
"""

from curar_tiktok import SERIF, bloque, ejecutar, et, glosario, pad, pct, tam_para

SLUG = "tiktok-quantgent-138326"


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Black-Scholes: The one equation that changed Wall Street forever"
    plan["titulo_es"] = "Black-Scholes: la ecuación que cambió Wall Street para siempre"

    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "Black-Scholes", "Black-Scholes", "bold"),
        bloque(a, 1, "subtitulo",
               "The one equation that changed Wall Street forever. Every option you've ever traded? Priced off "
               "this.",
               "La ecuación que cambió Wall Street para siempre. ¿Cada opción que operaste alguna vez? Se valuó "
               "con esto.", "regular"),
        bloque(a, 2, "cuerpo", "Here's how it actually works.", "Veamos cómo funciona en realidad.", "regular"),
    ], zonas_grafico=[{
        "caja": [110, 900, 940, 1610], "estrategia": "C",
        "justificacion": "Superficie 3D del precio de la opción C(S, t): solo notación (C, S, t) y ticks; no hay "
                         "texto en lenguaje natural.",
        "tipo": "superficie 3D: precio de una opción de compra C según el precio S y el tiempo t",
        "etiquetas": [],
    }], notas_revisar=[
        "Exageración: «¿Cada opción que operaste alguna vez? Se valuó con esto.» Los precios de las opciones "
        "los fija el mercado; Black-Scholes se usa sobre todo para expresarlos como volatilidad implícita, y "
        "las opciones americanas suelen valuarse con otros modelos (binomial, diferencias finitas).",
        "Gráfico de portada sin parámetros ni fuente (strike, tasa, volatilidad); se conserva tal cual.",
    ])

    a = S[1]["bloques"]
    rotulos = [
        ("(call option price)", "(precio de la opción de compra)", 1184, 886),
        ("(cumulative distribution function)", "(función de distribución acumulada)", 1225, 1074),
        ("(time left til maturity (in years))", "(tiempo hasta el vencimiento, en años)", 1266, 1050),
        ("(stock price)", "(precio de la acción)", 1309, 826),
        ("(strike price)", "(precio de ejercicio)", 1350, 828),
        ("(risk free rate)", "(tasa libre de riesgo)", 1391, 848),
        ("(volatility)", "(volatilidad)", 1431, 792),
    ]
    tam = min(tam_para(en, x1 - 676, es, 1066 - 676) for en, es, _, x1 in rotulos)
    S[1].update(funcion="Mecanismo: el supuesto (movimiento browniano geométrico) y la fórmula", bloques=[
        bloque(a, 0, "cuerpo",
               "It starts with one big assumption... Stock prices follow a random walk called geometric Brownian "
               "motion.",
               "Todo parte de un gran supuesto… Los precios de las acciones siguen un paseo aleatorio llamado "
               "movimiento browniano geométrico.", "regular"),
        bloque(a, 1, "cuerpo",
               "From that, you solve a differential equation and get a clean formula that spits out an exact "
               "option price. No simulations needed. That's why it became the gold standard.",
               "A partir de ahí, resolvés una ecuación diferencial y obtenés una fórmula cerrada que da el precio "
               "exacto de una opción. Sin simulaciones. Por eso se convirtió en el estándar de referencia.",
               "regular"),
    ], zonas_grafico=[{
        "caja": [0, 1130, 1080, 1510], "estrategia": "A",
        "justificacion": "Fórmula (imagen, se conserva) con una columna de siete aclaraciones en texto plano sobre "
                         "fondo blanco: se reescriben en el lugar.",
        "tipo": "fórmula de Black-Scholes para una opción de compra europea, con d1, d2 y glosario de variables",
        "etiquetas": [et(en, es, [676, y, x1, y + 26], tam, alineacion="izquierda", color="#333333")
                      for en, es, y, x1 in rotulos],
    }], notas_revisar=[
        "Fórmula: el original escribe «In(S/K)» en lugar de ln(S/K) (logaritmo natural); se conserva la imagen. "
        "Corregir en Canva si se rehace.",
        "Precisión: el precio es «exacto» solo bajo los supuestos del modelo (opción europea, sin dividendos, "
        "volatilidad y tasa constantes, retornos lognormales, sin costos de transacción).",
        f"Columna de aclaraciones reescrita a {tam} px (el español es más largo); revisar alineación en Canva.",
    ])

    a = S[2]["bloques"]
    S[2].update(funcion="Cuándo funciona: mercados tranquilos", bloques=[
        bloque(a, 0, "cuerpo",
               "When markets are calm and volatility stays steady, Black-Scholes is basically unbeatable. Smooth "
               "pricing surfaces, reliable Greeks, and it runs instantly. For vanilla options in normal conditions, "
               "nothing else even comes close on speed.",
               "Cuando los mercados están tranquilos y la volatilidad se mantiene estable, Black-Scholes es "
               "prácticamente imbatible. Superficies de precios suaves, griegas confiables y cálculo instantáneo. "
               "Para opciones vainilla en condiciones normales, nada se le acerca en velocidad.", "regular"),
    ], zonas_grafico=[{
        "caja": [30, 985, 970, 1550], "estrategia": "A",
        "justificacion": "Serie real (S&P 500): nunca se reconstruye; se reescriben los dos rótulos en serif. "
                         "«S&P 500» y los ticks quedan.",
        "tipo": "línea: S&P 500 real vs. tendencia de crecimiento constante del 6,3 % anual",
        "etiquetas": [
            et("actual", "real", [818, 1033, 905, 1060], tam_para("actual", 87, archivo=SERIF), fuente=SERIF,
               alineacion="derecha", color="#2A2A2A", borrado="inpaint", caja_borrar=pad([818, 1033, 905, 1060])),
            et("steady 6.3%\nannual growth", f"crecimiento anual\nconstante del {pct('6,3')}",
               [675, 1316, 889, 1400], tam_para("annual growth", 214, archivo=SERIF), fuente=SERIF,
               alineacion="izquierda", interlineado=1.4, color="#2A2A2A"),
        ],
    }], notas_revisar=[
        "Gráfico sin período ni fuente: parece el S&P 500 de 2015 a 2020 (incluye el derrumbe de marzo de "
        "2020). El «6,3 % anual constante» no se puede verificar. Indicar período y fuente o quitar.",
        "Exageración: «prácticamente imbatible» y «nada se le acerca en velocidad» (hay aproximaciones y "
        "modelos igual de rápidos para opciones vainilla).",
        "El gráfico muestra justamente un derrumbe, en una slide que habla de mercados tranquilos.",
    ])

    a = S[3]["bloques"]
    titulo = "Implied Volatility Surface"
    S[3].update(funcion="Dónde falla: colas gruesas, asimetría y agrupamiento de volatilidad", bloques=[
        bloque(a, 0, "cuerpo",
               "But here's where it falls apart. Real markets have fat tails, skew, and vol clustering... things a "
               "simple random walk can't capture. Force Black-Scholes into that reality and you get warped "
               "surfaces and hedges that blow up when you need them most.",
               "Pero acá es donde se desarma. Los mercados reales tienen colas gruesas, asimetría y agrupamiento "
               "de volatilidad… cosas que un paseo aleatorio simple no puede capturar. Forzá Black-Scholes a esa "
               "realidad y obtenés superficies deformadas y coberturas que fallan justo cuando más las "
               "necesitás.", "regular"),
    ], zonas_grafico=[{
        "caja": [105, 975, 985, 1560], "estrategia": "C",
        "justificacion": "Figura académica (superficie de volatilidad implícita): se conserva; se traducen el "
                         "título y los rótulos de ejes en lenguaje natural (serif, como el original).",
        "tipo": "superficie 3D: volatilidad implícita σ(T, M) según vencimiento T y moneyness M = S/K",
        "etiquetas": [
            et(titulo, "Superficie de volatilidad implícita", [429, 984, 731, 1008],
               tam_para(titulo, 302, archivo=SERIF), fuente=SERIF, color="#3A3A3A"),
            et("Time to Matutity T", "Tiempo al vencimiento T", [118, 1521, 319, 1542],
               tam_para("Time to Matutity T", 201, archivo=SERIF), fuente=SERIF, alineacion="izquierda",
               color="#3A3A3A"),
            et("Implied Volatility σ(T, M)", "Volatilidad implícita σ(T, M)", [113, 1068, 136, 1337],
               round(0.9 * tam_para("Implied Volatility σ(T, M)", 269, archivo=SERIF), 1), fuente=SERIF, rotacion=90,
               color="#3A3A3A", borrado="inpaint"),
        ],
    }], notas_revisar=[
        "Figura sin fuente. El original tiene erratas en los ejes («Matutity», «Monevness»); se tradujo "
        "«Tiempo al vencimiento T» y se conservó «Moneyness M = S/K» (término usual sin traducir).",
    ])

    a = S[4]["bloques"]
    S[4].update(funcion="El parche: volatilidad implícita por strike y vencimiento", bloques=[
        bloque(a, 0, "cuerpo",
               "So traders hacked a workaround: implied volatility. Keep the Black-Scholes formula, but swap in a "
               "different vol for every strike and expiry. The math stays simple, but now the surface reflects "
               "what the market is actually doing.",
               "Entonces los traders idearon un atajo: la volatilidad implícita. Mantenés la fórmula de "
               "Black-Scholes, pero usás una volatilidad distinta para cada precio de ejercicio y cada "
               "vencimiento. La matemática sigue siendo simple, pero ahora la superficie refleja lo que el mercado "
               "realmente está haciendo.", "regular"),
    ], zonas_grafico=[{
        "caja": [50, 980, 1030, 1495], "estrategia": "C",
        "justificacion": "Figura importada (superficie ajustada a datos de mercado): se conserva; se traduce el "
                         "rótulo «Tim to Maturity».",
        "tipo": "superficie 3D ajustada sobre puntos de volatilidad implícita observados",
        "etiquetas": [
            et("Tim to Maturity: τ", "Tiempo al vencimiento: τ", [141, 1455, 237, 1468], 12.5,
               alineacion="izquierda", color="#8A8A8A", caja_borrar=pad([141, 1455, 237, 1468], 2)),
        ],
    }], notas_revisar=[
        "Figura sin fuente ni fecha; los ticks y «Moneyness: m» se conservan. Rótulos muy chicos: revisar "
        "nitidez en Canva.",
    ])

    a = S[5]["bloques"]
    caja_bg = "#E7ECF0"
    viñetas = [
        ("Stochastic volatility model", "Modelo de volatilidad estocástica", 1447),
        ("Volatility mean reverts to long-run level", "La volatilidad revierte a su nivel de largo plazo", 1488),
        ("Volatility and asset price are correlated", "Volatilidad y precio del activo están correlacionados",
         1529),
        ("Volatility cannot become negative", "La volatilidad no puede ser negativa", 1569),
    ]
    tv = round(0.94 * min(tam_para(en, 780 - 351, es, 782 - 351) for en, es, _ in viñetas), 1)
    S[5].update(funcion="Solución 1: modelo de Heston (volatilidad estocástica)", bloques=[
        bloque(a, 0, "titulo", "Want the model itself to adapt?", "¿Querés que el propio modelo se adapte?",
               "bold"),
        bloque(a, 1, "cuerpo",
               "That's where Heston comes in. Instead of assuming vol is fixed, it lets volatility move on its own "
               "— with mean reversion and vol-of-vol baked in. It explains the smile naturally instead of just "
               "patching over it",
               "Ahí entra Heston. En lugar de suponer que la volatilidad es fija, la deja moverse por su cuenta "
               "—con reversión a la media y volatilidad de la volatilidad incorporadas—. Explica la sonrisa de "
               "volatilidad de forma natural, en lugar de solo emparcharla.", "regular"),
    ], zonas_grafico=[{
        "caja": [286, 976, 790, 1648], "estrategia": "A",
        "justificacion": "Ficha con título, rótulo y cuatro viñetas sobre fondo gris liso: se borra la tinta con "
                         "el color de la ficha y se reescribe; ecuaciones y trayectoria se conservan.",
        "tipo": "ficha: ecuaciones del modelo de Heston, trayectoria simulada y supuestos",
        "etiquetas": [
            et("Heston Model", "Modelo de Heston", [385, 1026, 687, 1061],
               tam_para("Heston Model", 302, "Modelo de Heston", 470, "bold"), peso="bold", color="#111317",
               borrado="plano", caja_borrar=pad([385, 1026, 687, 1061])),
            et("Stock Price", "Precio de la acción", [308, 1222, 323, 1362], 15, rotacion=90, color="#55585C",
               borrado="plano", caja_borrar=pad([308, 1222, 323, 1362])),
            et("Assumptions", "Supuestos", [439, 1399, 639, 1430], tam_para("Assumptions", 200, peso="semibold"),
               peso="semibold", color="#17191D", borrado="plano",
               caja_borrar=pad([439, 1399, 639, 1430])),
        ] + [et(en, es, [351, y, 784, y + 24], tv, alineacion="izquierda", color="#2E3034", borrado="plano",
                caja_borrar=[346, y - 4, 786, y + 28]) for en, es, y in viñetas],
    }], notas_revisar=[
        "Ecuación de la ficha con errores: «κap(θ − v_t)» debería ser κ(θ − v_t) y «σ√v/W_v» debería ser "
        "σ√v_t dW_v. Se conserva la imagen; corregir en Canva si se rehace.",
        "Precisión: Heston reproduce bien la asimetría de largo plazo, pero le cuesta la sonrisa de "
        "vencimientos muy cortos; «la explica de forma natural» es una simplificación.",
        f"Viñetas de la ficha reescritas a {tv} px para que entren en el ancho; revisar en Canva.",
        "El original no cierra la última oración con punto; en español se agregó.",
    ])

    a = S[6]["bloques"]
    tit7 = "Simulated stock prices with 1000 steps and 5 price paths, Merton Jump Diffusion Model"
    S[6].update(funcion="Solución 2: modelos de difusión con saltos (Merton)", bloques=[
        bloque(a, 0, "cuerpo",
               "For even wilder markets, jump-diffusion models add sudden price spikes on top of the random walk. "
               "Think flash crashes and earnings gaps — the stuff Brownian motion pretends doesn't exist.",
               "Para mercados todavía más turbulentos, los modelos de difusión con saltos agregan saltos bruscos "
               "de precio sobre el paseo aleatorio. Pensá en los derrumbes relámpago (flash crashes) y en los "
               "saltos tras los balances —lo que el movimiento browniano finge que no existe—.", "regular"),
    ], zonas_grafico=[{
        "caja": [0, 955, 1080, 1500], "estrategia": "A",
        "justificacion": "Simulación sin semilla ni parámetros: no se regenera; se traduce el título del gráfico.",
        "tipo": "líneas: 5 trayectorias simuladas de 1000 pasos con el modelo de difusión con saltos de Merton",
        "etiquetas": [
            et(tit7, "Precios simulados de acciones con 1000 pasos y 5 trayectorias, modelo de difusión con "
                     "saltos de Merton", [297, 966, 789, 979], tam_para(tit7, 492), color="#333333"),
        ],
    }], notas_revisar=[
        "Gráfico simulado sin parámetros ni ejes legibles (los ticks salen cortados en el original).",
    ])

    a = S[7]["bloques"]
    S[7].update(funcion="Cierre: conclusión práctica sin gráfico", bloques=[
        bloque(a, 0, "titulo", "Bottom line", "En síntesis", "bold"),
        bloque(a, 1, "cuerpo",
               "Black-Scholes is still the starting point for everything in options. But smart traders know when "
               "to trust it and when to upgrade. Learn the baseline, then know when the market is telling you "
               "it's not enough.",
               "Black-Scholes sigue siendo el punto de partida de todo en opciones. Pero los traders inteligentes "
               "saben cuándo confiar en él y cuándo pasar a algo mejor. Aprendé la base y después reconocé "
               "cuándo el mercado te está diciendo que no alcanza.", "regular"),
    ], zonas_grafico=[], notas_revisar=[])

    plan["glosario_nuevo"] = glosario([
        ("random walk", "paseo aleatorio"),
        ("geometric Brownian motion", "movimiento browniano geométrico"),
        ("gold standard", "estándar de referencia"),
        ("Greeks", "griegas"),
        ("vanilla options", "opciones vainilla"),
        ("skew", "asimetría"),
        ("vol clustering", "agrupamiento de volatilidad"),
        ("hedges", "coberturas"),
        ("implied volatility", "volatilidad implícita"),
        ("strike (price)", "precio de ejercicio"),
        ("expiry / maturity", "vencimiento"),
        ("call option", "opción de compra"),
        ("cumulative distribution function", "función de distribución acumulada"),
        ("risk free rate", "tasa libre de riesgo"),
        ("stochastic volatility", "volatilidad estocástica"),
        ("vol-of-vol", "volatilidad de la volatilidad"),
        ("(volatility) smile", "sonrisa de volatilidad"),
        ("jump-diffusion model", "modelo de difusión con saltos"),
        ("flash crash", "derrumbe relámpago (flash crash)"),
        ("earnings gaps", "saltos tras los balances"),
        ("moneyness", "moneyness (sin traducir)"),
        ("Bottom line", "En síntesis"),
    ])


if __name__ == "__main__":
    ejecutar(SLUG, curar)
