"""Curación del carrusel de TikTok «Bayes' Theorem» (@quantgent, 7 slides).

Uso: .venv/bin/python scripts/curar_bayes.py  (después de `extraer tiktok-quantgent-437398`)
"""

from curar_tiktok import FOTO, NB, bloque, ejecutar, et, glosario, nuevo, pad, pct, tam_para

SLUG = "tiktok-quantgent-437398"
TASA_BASE = ("CLAVE — falta la tasa base: «menos del 10 %» solo vale si la enfermedad afecta a ≈ 1 de cada 1.000 "
             "personas y la prueba tiene 99 % de sensibilidad y 99 % de especificidad (0,99 × 0,001 / (0,99 × 0,001 "
             "+ 0,01 × 0,999) ≈ 9 %). Con una prevalencia del 1 %, la respuesta sería 50 %. El original no da la "
             "prevalencia; conviene agregarla en Canva (p. ej., «la enfermedad afecta a 1 de cada 1.000 personas»).")


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Bayes' Theorem: The Equation Your Brain Refuses to Believe"
    plan["titulo_es"] = "El teorema de Bayes: la ecuación que tu cerebro se niega a creer"

    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "Bayes' Theorem", "El teorema de Bayes", "bold"),
        bloque(a, 1, "subtitulo", "The Equation Your Brain Refuses to Believe.",
               "La ecuación que tu cerebro se niega a creer.", "regular"),
        bloque(a, [2, 3], "cuerpo",
               "Doctors, hedge funds, and even the FBI depend on it... And almost everyone gets it wrong.",
               "Médicos, fondos de cobertura y hasta el FBI dependen de ella… Y casi todos se equivocan con ella.",
               "regular"),
    ], zonas_grafico=[{
        "caja": [85, 1250, 1000, 1605], "estrategia": "C",
        "justificacion": "Imagen decorativa (superficie 3D tipo relieve) sin texto: se conserva.",
        "tipo": "ilustración: superficie 3D coloreada, sin ejes", "etiquetas": [],
    }], notas_revisar=[
        "Generalización sin fuente: «médicos, fondos de cobertura y hasta el FBI dependen de ella».",
        "La imagen de portada es decorativa: no representa nada del teorema de Bayes.",
    ])

    a = S[1]["bloques"]
    S[1].update(funcion="Planteo: la prueba médica del 99 %", bloques=[
        bloque(a, 0, "cuerpo", "A medical test is 99% accurate.",
               f"Una prueba médica tiene un {pct(99)} de precisión.", "regular"),
        bloque(a, 1, "destacado", "You test positive.", "Te da positivo.", "bold"),
        bloque(a, 2, "cuerpo", "What are the chances you actually have the disease?",
               "¿Qué probabilidad hay de que realmente tengas la enfermedad?", "regular"),
    ], zonas_grafico=[{
        "caja": [255, 1125, 945, 1540], "estrategia": "C",
        "justificacion": "Foto recortada sin texto: se conserva.",
        "tipo": "foto: hisopado a un paciente", "etiquetas": [],
    }], notas_revisar=[FOTO, TASA_BASE])

    a = S[2]["bloques"]
    S[2].update(funcion="Respuesta contraintuitiva: menos del 10 %", bloques=[
        bloque(a, 0, "cuerpo", "The real answer?", "¿La respuesta real?", "regular"),
        bloque(a, 1, "destacado", "Less than 10%.", f"Menos del {pct(10)}.", "bold"),
        bloque(a, 2, "cuerpo",
               "Your brain just failed a basic probability test. So does almost everyone's. This isn't a flaw — "
               "it's biology. Our brains weren't built for conditional probability. Bayes' Theorem was built to fix "
               "that.",
               "Tu cerebro acaba de reprobar un examen básico de probabilidad. Igual que el de casi todo el mundo. "
               "No es una falla: es biología. Nuestro cerebro no está hecho para la probabilidad condicional. El "
               "teorema de Bayes se creó para corregir eso.", "regular"),
    ], zonas_grafico=[{
        "caja": [400, 1295, 690, 1645], "estrategia": "A",
        "justificacion": "Dos barras con valores rotulados y pies sobre fondo liso: se reescriben los cuatro "
                         "rótulos (la base de prevalencia no está en el texto, así que no se regenera).",
        "tipo": "barras: lo que pensabas (99 %) vs. la respuesta real (~9 %)",
        "etiquetas": [
            et("99%", pct(99), [419, 1307, 512, 1337], tam_para("99%", 93, peso="bold"), peso="bold",
               color="#2E8B57", caja_borrar=pad([419, 1307, 512, 1337], 2)),
            et("~9%", f"~{pct(9)}", [573, 1506, 669, 1536], tam_para("~9%", 96, peso="bold"), peso="bold",
               color="#C0393B", caja_borrar=pad([573, 1506, 669, 1536], 2)),
            et("What you\nthought", "Lo que\npensabas", [418, 1594, 511, 1637], 17, interlineado=1.3,
               color="#8E8E8E", caja_borrar=pad([423, 1596, 506, 1635], 2)),
            et("The real\nanswer", "La respuesta\nreal", [570, 1594, 668, 1637], 17, interlineado=1.3,
               color="#8E8E8E", caja_borrar=pad([584, 1596, 654, 1631], 2)),
        ],
    }], notas_revisar=[
        TASA_BASE,
        "Afirmación sin sustento: «no es una falla: es biología». El sesgo de ignorar la tasa base está "
        "documentado (Kahneman y Tversky), pero atribuirlo a la biología es especulativo.",
    ])

    a = S[3]["bloques"]
    S[3].update(funcion="La fórmula y sus términos + Thomas Bayes", bloques=[
        bloque(a, 0, "titulo", "The formula is elegant", "La fórmula es elegante", "bold"),
        bloque(a, 1, "otro", "P(A|B) = P(B|A) · P(A) / P(B)", "P(A|B) = P(B|A) · P(A) / P(B)", "regular"),
        bloque(a, [2, 3], "cuerpo",
               "Where P(A|B) is what you want to know, P(B|A) is what the test tells you, P(A) is how rare the "
               "disease is, and P(B) is the total chance of testing positive. It updates what you believe using "
               "the evidence you actually have.",
               "Donde P(A|B) es lo que querés saber, P(B|A) es lo que te dice la prueba, P(A) es qué tan rara es "
               "la enfermedad y P(B) es la probabilidad total de dar positivo. Actualiza lo que creés con la "
               "evidencia que realmente tenés.", "regular"),
    ], zonas_grafico=[{
        "caja": [355, 1270, 730, 1705], "estrategia": "C",
        "justificacion": "Grabado de Thomas Bayes con su nombre como pie (nombre propio): se conserva.",
        "tipo": "ilustración: retrato de Thomas Bayes", "etiquetas": [],
    }], notas_revisar=[
        "Fórmula correcta. El retrato «de Thomas Bayes» que circula es de autenticidad dudosa (no hay retratos "
        "verificados de Bayes); conviene aclararlo o reemplazarlo.",
    ])

    a = S[4]["bloques"]
    S[4].update(funcion="Por qué importa en los mercados: actualizar posiciones", bloques=[
        bloque(a, 0, "titulo", "Here's why Wall Street cares", "Por qué le importa a Wall Street", "bold"),
        bloque(a, 1, "cuerpo",
               "Every time the market moves, traders face the same question: should I update my position? Bayes "
               "gives them the exact framework. New data comes in, beliefs get updated, positions get adjusted. "
               "It's not prediction — it's adaptation. That's why the best quant strategies aren't rigid. They "
               "learn.",
               "Cada vez que el mercado se mueve, los traders enfrentan la misma pregunta: ¿tengo que actualizar mi "
               "posición? Bayes les da el marco exacto. Llegan datos nuevos, se actualizan las creencias, se "
               "ajustan las posiciones. No es predicción: es adaptación. Por eso las mejores estrategias "
               "cuantitativas no son rígidas. Aprenden.", "regular"),
    ], zonas_grafico=[{
        "caja": [135, 1255, 945, 1680], "estrategia": "A",
        "justificacion": "Curvas ilustrativas a priori, verosimilitud y a posteriori, sin parámetros: se "
                         "reescriben los tres rótulos.",
        "tipo": "curvas: distribución a priori, verosimilitud y a posteriori",
        "etiquetas": [
            et("Posterior", "A posteriori", [495, 1290, 587, 1316], tam_para("Posterior", 92), color="#4A4A4A",
               alineacion="derecha", borrado="inpaint", caja_borrar=pad([495, 1290, 587, 1316], 2)),
            et("Likelihood", "Verosimilitud", [652, 1371, 743, 1393], tam_para("Likelihood", 91),
               color="#4A4A4A", alineacion="izquierda", borrado="inpaint", caja_borrar=[651, 1369, 746, 1395]),
            et("Prior", "A priori", [442, 1485, 490, 1505], tam_para("Prior", 48), color="#4A4A4A",
               alineacion="derecha", borrado="inpaint", caja_borrar=pad([442, 1485, 490, 1505], 2)),
        ],
    }], notas_revisar=[
        "Generalización: «las mejores estrategias cuantitativas aprenden» y que Bayes da «el marco exacto» no "
        "tienen fuente; es una descripción idealizada.",
    ])

    S[5].update(funcion="Casos: Nate Silver, filtros de spam, autos autónomos, Renaissance", bloques=[
        nuevo("titulo", "This isn't just theory", "No es solo teoría", [274, 472, 811, 526], "bold", 52,
              color="#0A0A0A"),
        nuevo("cuerpo",
              "Nate Silver used Bayes to correctly predict all 50 states in the 2012 US election. Spam filters in "
              "your inbox run on Bayes. Self-driving cars use it to decide if that shadow is a pedestrian. And "
              "Renaissance Technologies — the most profitable hedge fund in history — builds strategies rooted in "
              "Bayesian inference.",
              "Nate Silver usó Bayes para predecir correctamente los 50 estados en la elección presidencial de 2012 "
              "en EE. UU. Los filtros de spam de tu correo funcionan con Bayes. Los autos autónomos lo usan "
              "para decidir si esa sombra es un peatón. Y Renaissance Technologies —el fondo de cobertura más "
              "rentable de la historia— construye estrategias basadas en la inferencia bayesiana.",
              [119, 655, 958, 1109], "regular", 42, interlineado=1.4, color="#1C1C1C", espacio_antes=129),
    ], zonas_grafico=[{
        "caja": [120, 1250, 965, 1675], "estrategia": "C",
        "justificacion": "Foto sin texto: se conserva.",
        "tipo": "foto: sensores en el techo de un auto autónomo", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Nate Silver acertó los 50 estados en 2012 (dato verificable); su modelo agrega encuestas con métodos "
        "en parte bayesianos, no es una aplicación directa del teorema.",
        "Sin fuente: que Renaissance «construye estrategias basadas en inferencia bayesiana». «El fondo más "
        "rentable de la historia» suele referirse a Medallion, su fondo interno.",
        "Precisión: los filtros de spam clásicos usan Bayes ingenuo; los actuales combinan otros modelos.",
    ])

    a = S[6]["bloques"]
    S[6].update(funcion="Cierre: la mentalidad bayesiana (actualizar), sin gráfico", bloques=[
        bloque(a, 0, "titulo", "The biggest lesson from Bayes isn't the math...",
               "La mayor lección de Bayes no es la matemática…", "bold"),
        bloque(a, 1, "destacado", "It's the mindset.", "Es la mentalidad.", "bold"),
        bloque(a, 2, "cuerpo",
               "Most people form an opinion and defend it. Bayesian thinkers form an opinion and update it. In "
               "markets and in life, the ones who win long-term aren't the ones who are right the most — they're "
               "the ones who change their minds the fastest when the evidence says they should.",
               "La mayoría de la gente se forma una opinión y la defiende. Quienes piensan de forma bayesiana se "
               "forman una opinión y la actualizan. En los mercados y en la vida, los que ganan a largo plazo no "
               "son los que más aciertan: son los que cambian de opinión más rápido cuando la evidencia lo indica.",
               "regular"),
    ], zonas_grafico=[], notas_revisar=[])

    plan["glosario_nuevo"] = glosario([
        ("Bayes' Theorem", "teorema de Bayes"),
        ("(medical) test", "prueba (médica)"),
        ("you test positive", "te da positivo"),
        ("accurate (99%)", "precisión (del 99 %)"),
        ("conditional probability", "probabilidad condicional"),
        ("prior / likelihood / posterior", "a priori / verosimilitud / a posteriori"),
        ("Bayesian inference", "inferencia bayesiana"),
        ("Bayesian thinkers", "quienes piensan de forma bayesiana"),
        ("self-driving cars", "autos autónomos"),
        ("spam filters", "filtros de spam"),
        ("base rate", "tasa base (prevalencia)"),
    ])


if __name__ == "__main__":
    ejecutar(SLUG, curar)
