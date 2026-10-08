"""Curación del carrusel de TikTok «Benford's Law» (@quantgent, 8 slides).

Uso: .venv/bin/python scripts/curar_benford.py  (después de `extraer tiktok-quantgent-262422`)
"""

from math import log10

from curar_tiktok import FOTO, NB, bloque, ejecutar, glosario, nuevo, pct

SLUG = "tiktok-quantgent-262422"


def benford(d):
    """P(d) = log10(1 + 1/d), en % con un decimal."""
    return round(100 * log10(1 + 1 / d), 1)


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Benford's Law: The Equation That Catches Tax Fraud Using Just the First Digit"
    plan["titulo_es"] = "La ley de Benford: la ecuación que detecta fraudes fiscales con solo el primer dígito"

    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "Benford's Law", "La ley de Benford", "bold"),
        bloque(a, 1, "subtitulo", "The Equation That Catches Tax Fraud Using Just the First Digit",
               "La ecuación que detecta fraudes fiscales con solo el primer dígito", "regular"),
        bloque(a, 2, "cuerpo",
               "The IRS, forensic accountants, and even the FBI use this to spot fake numbers instantly. Here's how "
               "it works.",
               "El IRS (el fisco de EE. UU.), los contadores forenses y hasta el FBI la usan para detectar "
               "números falsos al instante. Veamos cómo funciona.", "regular"),
    ], zonas_grafico=[{
        "caja": [290, 1140, 880, 1690], "estrategia": "C",
        "justificacion": "Superficie 3D decorativa (solo ticks numéricos): se conserva.",
        "tipo": "superficie 3D con curvas de nivel, sin relación directa con la ley de Benford",
        "etiquetas": [],
    }], notas_revisar=[
        "Sin fuente: que el IRS y el FBI usen la ley de Benford «para detectar números falsos al instante». "
        "Es una herramienta de auditoría conocida (Nigrini), pero sirve para señalar casos a revisar, no "
        "para detectar fraudes «al instante».",
        "Gráfico de portada decorativo: no representa la ley de Benford.",
    ])

    a = S[1]["bloques"]
    S[1].update(funcion="Planteo: el primer dígito de cada número", bloques=[
        bloque(a, 0, "cuerpo", "Every number starts with a first digit.",
               "Todo número empieza con un primer dígito.", "regular"),
        bloque(a, 1, "cuerpo", "$142 starts with 1. $873 starts with 8. $45 starts with 4.",
               "$142 empieza con 1. $873 empieza con 8. $45 empieza con 4.", "regular"),
        bloque(a, 2, "cuerpo", "There are only 9 possible first digits. 1 through 9.",
               "Hay solo 9 primeros dígitos posibles. Del 1 al 9.", "regular"),
    ], zonas_grafico=[{
        "caja": [160, 1080, 925, 1590], "estrategia": "C",
        "justificacion": "Foto de números (desenfocada): no tiene texto en lenguaje natural; se conserva.",
        "tipo": "foto: columnas de números", "etiquetas": [],
    }], notas_revisar=[FOTO])

    a = S[2]["bloques"]
    S[2].update(funcion="La intuición equivocada: cada dígito, 11 %", bloques=[
        bloque(a, 0, "cuerpo",
               "So if you grabbed thousands of real numbers... Stock prices, tax returns, populations... You'd "
               "expect each digit to show up about equally, right?",
               "Entonces, si tomaras miles de números reales… Precios de acciones, declaraciones juradas, "
               "poblaciones… Esperarías que cada dígito apareciera más o menos la misma cantidad de veces, ¿no?",
               "regular"),
        bloque(a, 1, "destacado", "Each one roughly 11% of the time?",
               f"¿Cada uno, alrededor del {pct(11)} de las veces?", "bold"),
        bloque(a, 2, "cuerpo", "That's what most people think.", "Es lo que piensa la mayoría.", "regular"),
        bloque(a, 3, "destacado", "They're wrong", "Se equivocan.", "bold"),
    ], zonas_grafico=[], notas_revisar=[
        "El original no cierra «They're wrong» con punto; en español se agregó.",
    ])

    a = S[3]["bloques"]
    dig = list(range(1, 10))
    S[3].update(funcion="La revelación: el 1 aparece primero el 30 % de las veces (gráfico)", bloques=[
        bloque(a, 0, "destacado", "The digit 1 appears first 30% of the time. Not 11%.",
               f"El 1 es el primer dígito el {pct(30)} de las veces. No el {pct(11)}.", "bold"),
        bloque(a, 1, "cuerpo",
               "And it gets weirder... each digit after that drops off in a perfect curve. The digit 9 shows up "
               "less than 5% of the time.",
               f"Y se pone más raro… cada dígito siguiente cae en una curva perfecta. El 9 aparece menos del "
               f"{pct(5)} de las veces.", "regular"),
        bloque(a, 2, "cuerpo", "This pattern appears in almost every naturally occurring dataset on Earth.",
               "Este patrón aparece en casi todos los conjuntos de datos naturales del planeta.", "regular"),
    ], zonas_grafico=[{
        "caja": [205, 1225, 905, 1625], "estrategia": "B",
        "justificacion": "Barras que salen exactamente de la fórmula de la slide 5, P(d) = log10(1 + 1/d); "
                         "coinciden con los valores del original.",
        "tipo": "barras: frecuencia del primer dígito según la ley de Benford (1-9) y línea del 11,1 %",
        "datos": {
            "tipo": "barras_umbral", "categorias": [str(d) for d in dig], "valores": [benford(d) for d in dig],
            "formula": "P(d) = log10(1 + 1/d)", "umbral": round(100 / 9, 1), "decimales": 1,
            "color_ini": "#2A8C5A", "color_fin": "#76B597", "color_bajo": "#4E9C77", "color_alto": "#2E8B57",
            "color_umbral": "#C0393B", "rotulo_umbral": f"Esperado: {pct('11,1')}",
            "rotulo_umbral_lado": "derecha", "tam_rotulo_umbral": 13.5, "tam_valor": 14.5,
            "rotulo_x": "Primer dígito", "margen_inferior": 0.17, "tam_ticks": 17, "ticks_negrita": True,
        },
        "etiquetas": [],
    }], notas_revisar=[
        "Exageración: «casi todos los conjuntos de datos naturales». La ley se cumple en datos que abarcan "
        "varios órdenes de magnitud y sin topes (precios, poblaciones, montos); no en alturas, edades, "
        "números de teléfono o precios fijados (p. ej., $9,99).",
        "Gráfico regenerado (B) con la fórmula: 30,1 / 17,6 / 12,5 / 9,7 / 7,9 / 6,7 / 5,8 / 5,1 / 4,6 %, "
        "igual que el original.",
    ])

    a = S[4]["bloques"]
    S[4].update(funcion="La fórmula y la intuición + Simon Newcomb", bloques=[
        bloque(a, 0, "titulo", "The formula", "La fórmula", "regular"),
        bloque(a, 1, "otro", "P(d) = log₁₀(1 + 1/d)", "P(d) = log₁₀(1 + 1/d)", "bold"),
        bloque(a, 2, "cuerpo",
               "Here's the intuition: to go from 1 to 2 requires doubling... A 100% increase. To go from 8 to 9 is "
               "only a 12% increase. Numbers \"spend more time\" starting with lower digits because it takes "
               "longer to roll past them. That's why 1 dominates.",
               f"La intuición es esta: pasar de 1 a 2 requiere duplicarse… Un aumento del {pct(100)}. Pasar de 8 a "
               f"9 es solo un aumento del {pct(12)}. Los números “pasan más tiempo” empezando con dígitos bajos "
               f"porque cuesta más superarlos. Por eso domina el 1.", "regular"),
    ], zonas_grafico=[{
        "caja": [365, 1245, 720, 1705], "estrategia": "C",
        "justificacion": "Retrato con pie que es un nombre propio (Simon Newcomb): se conserva.",
        "tipo": "foto: retrato de Simon Newcomb", "etiquetas": [],
    }], notas_revisar=[
        "Precisión: de 8 a 9 el aumento es del 12,5 % (el original redondea a 12 %).",
        "Contexto que falta: Simon Newcomb (el del retrato) describió el fenómeno en 1881; Frank Benford lo "
        "redescubrió y lo documentó con datos en 1938. El carrusel no lo explica.",
        "La intuición de «pasar más tiempo» vale para cantidades que crecen de forma multiplicativa "
        "(exponencial).",
    ])

    a = S[5]["bloques"]
    S[5].update(funcion="Aplicación: cómo se detecta a quien inventa números", bloques=[
        bloque(a, 0, "titulo", "So how do you catch a liar?", "¿Y cómo se atrapa a un mentiroso?", "bold"),
        bloque(a, 1, "cuerpo",
               "When people fake numbers, they spread digits evenly... Roughly 11% each. Their gut says that looks "
               "\"random.\" But real data follows Benford's curve. So a flat distribution is a giant red flag. "
               "Forensic accountants overlay real data against Benford's curve... And the fakes light up instantly.",
               f"Cuando la gente inventa números, reparte los dígitos de forma pareja… Alrededor del {pct(11)} cada "
               f"uno. Su intuición le dice que eso parece “aleatorio”. Pero los datos reales siguen la curva de "
               f"Benford. Así que una distribución plana es una enorme señal de alerta. Los contadores forenses "
               f"comparan los datos con la curva de Benford… Y los falsos saltan a la vista al instante.",
               "regular"),
    ], zonas_grafico=[{
        "caja": [225, 1225, 860, 1640], "estrategia": "C",
        "justificacion": "Foto de una planilla con lupa (texto ilegible, de ambientación): se conserva.",
        "tipo": "foto: planilla contable bajo una lupa", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Simplificación: quien inventa números no siempre los reparte de forma pareja; la prueba de Benford "
        "señala desvíos a investigar, no prueba un fraude.",
    ])

    S[6].update(funcion="Casos: Enron, elecciones de Irán 2009, tribunales de EE. UU.", bloques=[
        nuevo("titulo", "It's already been used in court", "Ya se usó en los tribunales",
              [148, 472, 939, 525], "bold", 50, color="#0A0A0A"),
        nuevo("cuerpo",
              "Benford's Law was used as evidence in the Enron scandal. It flagged irregularities in the 2009 "
              "Iranian election results. It's been admitted as evidence in US federal courts. And it works on "
              "everything... From earthquake magnitudes to Twitter follower counts to your electricity bill.",
              "La ley de Benford se usó como prueba en el escándalo de Enron. Detectó irregularidades en los "
              "resultados de la elección de 2009 en Irán. Fue admitida como prueba en tribunales federales de "
              "EE. UU. Y funciona con todo… Desde la magnitud de los terremotos hasta la cantidad de "
              "seguidores en Twitter o tu factura de luz.",
              [114, 655, 963, 1050], "regular", 41, interlineado=1.43, color="#1C1C1C", espacio_antes=130),
    ], zonas_grafico=[{
        "caja": [110, 1225, 975, 1655], "estrategia": "C",
        "justificacion": "Foto (audiencia) sin texto: se conserva.",
        "tipo": "foto: audiencia en una sala", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Verificar: «se usó como prueba en el escándalo de Enron». Lo documentado son análisis posteriores de "
        "los estados contables de Enron con la ley de Benford, no su uso como prueba en el juicio.",
        "Matizar: sobre Irán 2009 hubo análisis con Benford (p. ej., Mebane), pero su validez para detectar "
        "fraude electoral es discutida.",
        "Imprecisión: «funciona con todo». No funciona con datos acotados o asignados (ver slide 4). La "
        "factura de luz y los seguidores de Twitter son ejemplos citados en estudios puntuales.",
    ])

    a = S[7]["bloques"]
    S[7].update(funcion="Cierre: lo que revela sobre la naturaleza, sin gráfico", bloques=[
        bloque(a, 0, "titulo", "The lesson from Benford isn't the math...",
               "La lección de Benford no es la matemática…", "regular"),
        bloque(a, 1, "destacado", "It's what it reveals about nature.", "Es lo que revela sobre la naturaleza.",
               "bold"),
        bloque(a, 2, "cuerpo",
               "The universe doesn't distribute things evenly. Growth, decay, and randomness all leave fingerprints "
               "in the numbers. Benford's Law just taught us how to read them.",
               "El universo no distribuye las cosas de forma pareja. El crecimiento, el deterioro y el azar dejan "
               "huellas en los números. La ley de Benford simplemente nos enseñó a leerlas.", "regular"),
    ], zonas_grafico=[], notas_revisar=[])

    plan["glosario_nuevo"] = glosario([
        ("Benford's Law", "ley de Benford"),
        ("first digit", "primer dígito"),
        ("IRS", "IRS (el fisco de EE. UU.)"),
        ("forensic accountants", "contadores forenses"),
        ("tax returns", "declaraciones juradas"),
        ("tax fraud", "fraude fiscal"),
        ("red flag", "señal de alerta"),
        ("naturally occurring dataset", "conjunto de datos natural"),
        ("decay", "deterioro"),
        ("Expected 11.1%", "Esperado: 11,1 %"),
    ])


if __name__ == "__main__":
    ejecutar(SLUG, curar)
