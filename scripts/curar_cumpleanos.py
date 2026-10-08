"""Curación (criterio) del carrusel de TikTok «The Birthday Paradox» (@quantgent).

Uso: .venv/bin/python scripts/curar_cumpleanos.py  (después de `extraer tiktok-quantgent-308355`)
"""

import copy
import json
import sys
from math import prod
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from curar_referencia import NB, RAIZ, bloque, pct, zona_texto  # noqa: E402

SLUG = "tiktok-quantgent-308355"
FOTO = ("La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o "
        "reemplazarla en Canva.")


def et(en, es, caja, tam, **kw):
    return {"texto_en": en, "texto_es": es, "caja": caja, "tam_px": tam, **kw}


def con_caja(auto, i, caja):
    b = copy.deepcopy(auto[i])
    b["caja"] = caja
    b["ancho_px"] = caja[2] - caja[0]
    return b


def p_cumple(n, dias=365):
    """P(al menos una coincidencia entre n personas) = 1 − 365! / ((365 − n)! · 365ⁿ), en %."""
    return round(100 * (1 - prod((dias - i) / dias for i in range(n))), 1)


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "The Birthday Paradox: The Interview Question That Breaks Quant Candidates"
    plan["titulo_es"] = "La paradoja del cumpleaños: la pregunta de entrevista que desarma a los aspirantes a quants"

    # 1 — portada
    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "The Birthday Paradox", "La paradoja del cumpleaños", "bold"),
        bloque(a, 1, "subtitulo", "The Interview Question That Breaks Quant Candidates",
               "La pregunta de entrevista que desarma a los aspirantes a analistas cuantitativos (quants)",
               "bold"),
        bloque(a, 2, "cuerpo",
               "Wall Street trading desks use this to test probabilistic intuition. Most people get it wrong "
               "instantly. Here's why.",
               "Las mesas de trading de Wall Street la usan para evaluar la intuición probabilística. La mayoría "
               "se equivoca al instante. Veamos por qué.", "regular"),
    ], zonas_grafico=[{
        "caja": [310, 1170, 800, 1605], "estrategia": "C",
        "justificacion": "Superficie 3D (matplotlib) sin datos explícitos en el texto: se conserva; se traducen "
                         "los dos rótulos de ejes (rotados) y los ticks quedan sin tocar.",
        "tipo": "superficie 3D: probabilidad de coincidencia según personas en la sala (0-80) y días del año "
                "(100-500)",
        "etiquetas": [
            et("People in room", "Personas en la sala", [377, 1550, 450, 1586], 10.5, rotacion=-21,
               color="#222222", borrado="inpaint"),  # caja ajustada para no tocar el tick «40»
            et("Days in year", "Días del año", [664, 1535, 722, 1577], 10.5, rotacion=32, color="#222222",
               borrado="inpaint"),
        ],
    }], notas_revisar=[
        "Afirmación sin fuente: «Las mesas de trading de Wall Street la usan para evaluar la intuición "
        "probabilística» y «la mayoría se equivoca al instante». Es una pregunta conocida de entrevistas, pero "
        "no hay evidencia citada.",
        "Gráfico 3D: los rótulos de ejes son chicos y rotados; si en Canva se ven borrosos, reescribirlos a "
        "mano. Los ticks (0.0-1.0 con punto decimal) se conservaron (estrategia C).",
    ])

    # 2 — planteo de la pregunta
    a = S[1]["bloques"]
    S[1].update(funcion="Planteo: la pregunta y las respuestas intuitivas", bloques=[
        bloque(a, 0, "cuerpo", "How many people need to be in a room before two of them share a birthday?",
               "¿Cuántas personas tiene que haber en una sala para que dos de ellas cumplan años el mismo día?",
               "regular"),
        bloque(a, 1, "cuerpo", "There are 365 possible birthdays. So you'd need a big crowd, right?",
               "Hay 365 cumpleaños posibles. Entonces necesitarías una multitud, ¿no?", "regular"),
        bloque(a, 2, "cuerpo", "Most people guess around 180. Some say 100. A few say 50.",
               "La mayoría arriesga alrededor de 180. Algunos dicen 100. Unos pocos, 50.", "regular"),
        bloque(a, 3, "destacado", "They're all way off.", "Todos están muy lejos.", "bold"),
    ], zonas_grafico=[{
        "caja": [156, 1115, 924, 1557], "estrategia": "C",
        "justificacion": "Fotografía (gente en una fiesta) sin texto: se conserva.",
        "tipo": "foto: grupo de personas en una fiesta", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Sin fuente: «La mayoría arriesga alrededor de 180. Algunos dicen 100. Unos pocos, 50.» No se cita "
        "encuesta ni estudio.",
    ])

    # 3 — la respuesta: 23
    a = S[2]["bloques"]
    ns = [5, 10, 15, 23, 30, 40, 50, 60, 70]
    S[2].update(funcion="Respuesta y evidencia: 23 personas (gráfico de probabilidades)", bloques=[
        bloque(a, 0, "titulo", "The answer is 23.", "La respuesta es 23.", "bold"),
        con_caja(a, 1, [129, 493, 950, 617]) | {
            "rol": "cuerpo", "peso": "regular",
            "texto_en": "Just 23 people gives you a better than even chance that two share a birthday. At 70 "
                        "people, it's 99.9%.",
            "texto_es": f"Con solo 23 personas, la probabilidad de que dos cumplan años el mismo día ya es mayor "
                        f"al {pct(50)}. Con 70 personas, es del {pct('99,9')}."},
        con_caja(a, 1, [150, 684, 929, 816]) | {
            "rol": "cuerpo", "peso": "regular", "espacio_antes": 67,
            "texto_en": "This isn't a trick. It's not a riddle. It's pure probability. And almost everyone's "
                        "intuition gets destroyed by it.",
            "texto_es": "No es un truco. No es una adivinanza. Es probabilidad pura. Y destruye la intuición de "
                        "casi todo el mundo."},
    ], zonas_grafico=[{
        "caja": [180, 1000, 900, 1425], "estrategia": "B",
        "justificacion": "Barras con valores que salen exactamente de la fórmula de la slide 5 "
                         "(P(n) = 1 − 365! / ((365 − n)! · 365ⁿ)); coinciden con las del original a un decimal.",
        "tipo": "barras: probabilidad de al menos una coincidencia para 5-70 personas, línea del 50 %",
        "datos": {
            "tipo": "barras_umbral", "categorias": [str(n) for n in ns], "valores": [p_cumple(n) for n in ns],
            "formula": "P(n) = 1 − 365! / ((365 − n)! · 365^n)", "umbral": 50, "decimales": 1,
            "color_ini": "#2E6B4A", "color_fin": "#22A03C", "color_bajo": "#2E7D46", "color_alto": "#B83A32",
            "color_umbral": "#C9433A", "rotulo_umbral": f"Esperado: {pct(50)}",
            "rotulo_x": "Personas en la sala",
        },
        "etiquetas": [],
    }], notas_revisar=[
        "Cifras verificadas con la fórmula (365 días equiprobables, sin 29 de febrero ni mellizos): 23 → "
        "50,7 %; 70 → 99,9 % (99,916 %). Con la distribución real de nacimientos, la probabilidad es apenas "
        "mayor.",
        "Gráfico regenerado (B): mismos valores que el original. El rótulo «Expected 50%» (que en el original "
        "pisaba la barra de 70) se reubicó arriba de la línea, a la izquierda, como «Esperado: 50 %».",
    ])

    # 4 — por qué falla la intuición
    a = S[3]["bloques"]
    S[3].update(funcion="Mecanismo: no es tu cumpleaños, son todos los pares", bloques=[
        bloque(a, 0, "titulo", "Here's why your brain breaks.", "Por qué tu cerebro falla.", "bold"),
        bloque(a, 1, "cuerpo",
               "You hear \"birthday match\" and think... someone matching MY birthday. That's 1 in 365. Tiny.",
               "Escuchás “coincidencia de cumpleaños” y pensás… en alguien que cumpla años el mismo día que YO. "
               "Eso es 1 en 365. Ínfimo.", "regular", tam_px=34),
        bloque(a, 2, "destacado", "But the question isn't about you. It's about any pair.",
               "Pero la pregunta no es sobre vos. Es sobre cualquier par.", "bold"),
        bloque(a, 3, "cuerpo",
               "With 23 people there are 253 unique pairs. Each one is a chance for a match. You're not rolling "
               "the dice once. You're rolling it 253 times.",
               "Con 23 personas hay 253 pares distintos. Cada uno es una oportunidad de coincidencia. No tirás el "
               "dado una vez. Lo tirás 253 veces.", "regular"),
    ], zonas_grafico=[{
        "caja": [385, 1030, 700, 1375], "estrategia": "A",
        "justificacion": "Diagrama con dos rótulos sobre fondo casi liso: se borran y se reescriben.",
        "tipo": "diagrama: 23 personas en círculo; se resaltan los 22 pares que te incluyen y, tenues, los 253",
        "etiquetas": [
            et("unique pairs", "pares distintos", [503, 1205, 577, 1220], 11.5, color="#666666",
               borrado="inpaint"),
            et("You", "Vos", [530, 1354, 551, 1367], 11, peso="bold", color="#B03A2E"),
        ],
    }], notas_revisar=[
        "Precisión: «1 en 365» es la probabilidad de coincidir con una persona puntual; con 22 personas más, la "
        "de que alguien comparta tu cumpleaños es ≈ 5,9 %.",
        "Precisión: los 253 pares no son tiradas independientes; 1 − (364/365)^253 ≈ 50,0 % es una "
        "aproximación (el valor exacto es 50,7 %). La traducción es fiel a la metáfora del dado.",
    ])

    # 5 — la fórmula
    a = S[4]["bloques"]
    S[4].update(funcion="Fórmula y método (complemento) + qué buscan los entrevistadores", bloques=[
        bloque(a, 0, "titulo", "The formula", "La fórmula", "regular"),
        bloque(a, 1, "otro", "P(match) = 1 - (365! / ((365-n)! x 365^n))",
               "P(coincidencia) = 1 − (365! / ((365 − n)! × 365ⁿ))", "bold", tam_px=37, ancho_max_px=920),
        bloque(a, 2, "cuerpo",
               "Instead of counting matches, count the probability everyone is different. Then subtract from 1. "
               "Each new person has to dodge every birthday already taken. By person 23, the dodging fails more "
               "than half the time.",
               "En lugar de contar coincidencias, calculá la probabilidad de que todos cumplan años en días "
               "distintos. Después, restala de 1. Cada persona nueva tiene que esquivar todos los cumpleaños ya "
               "ocupados. Para la persona 23, el esquive falla más de la mitad de las veces.", "regular"),
        bloque(a, 3, "destacado",
               "Quant interviewers don't want you to memorise the number. They want to see you reach for this.",
               "Quienes entrevistan a quants no quieren que memorices el número. Quieren ver que recurras a esto.",
               "bold"),
    ], zonas_grafico=[{
        "caja": [107, 1124, 973, 1535], "estrategia": "C",
        "justificacion": "Fotografía (sala de trading) sin texto legible: se conserva.",
        "tipo": "foto: sala de trading", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Fórmula correcta (supone 365 días equiprobables). Se tradujo «match» (coincidencia) y se usaron × y "
        "superíndice ⁿ en lugar de «x» y «^n».",
        "Imprecisión: «para la persona 23, el esquive falla más de la mitad de las veces» describe la "
        "probabilidad acumulada; la persona 23 por sí sola falla solo 22/365 ≈ 6 % de las veces.",
        "Sin fuente: qué buscan «quienes entrevistan a quants».",
    ])

    # 6 — cierre
    a = S[5]["bloques"]
    S[5].update(funcion="Cierre aforístico sin gráfico", bloques=[
        bloque(a, 0, "cuerpo", "The lesson from the Birthday Paradox isn't the number 23...",
               "La lección de la paradoja del cumpleaños no es el número 23…", "regular"),
        bloque(a, 1, "destacado", "It's that humans think linearly about combinatorial problems.",
               "Es que los humanos razonan de forma lineal ante problemas combinatorios.", "bold", tam_px=34),
        bloque(a, 2, "cuerpo",
               "Pairs grow with the square of the group. Your gut counts heads. The math counts connections. The "
               "best quants learn to catch that instinct, and override it.",
               "Los pares crecen con el cuadrado del grupo. Tu intuición cuenta personas. La matemática cuenta "
               "conexiones. Los mejores quants aprenden a detectar ese instinto y a imponerse a él.", "regular"),
    ], zonas_grafico=[], notas_revisar=[
        "Precisión: los pares son n(n − 1)/2, que crece aproximadamente con el cuadrado del grupo (fiel al "
        "original).",
    ])

    for s in S:
        s["zona_texto"] = zona_texto(s["bloques"])
        s["curado"] = True
    plan["glosario_nuevo"] = [{"en": en, "es": es} for en, es in [
        ("Birthday Paradox", "paradoja del cumpleaños"),
        ("trading desk", "mesa de trading"),
        ("quant candidates", "aspirantes a analistas cuantitativos (quants)"),
        ("share a birthday", "cumplir años el mismo día"),
        ("(birthday) match", "coincidencia (de cumpleaños)"),
        ("unique pairs", "pares distintos"),
        ("better than even chance", "probabilidad mayor al 50 %"),
        ("combinatorial problems", "problemas combinatorios"),
        ("gut (instinct)", "intuición / instinto"),
        ("People in room", "Personas en la sala"),
        ("Days in year", "Días del año"),
        ("Expected 50%", "Esperado: 50 %"),
    ]]


def main():
    ruta = RAIZ / "trabajo" / SLUG / "plan.json"
    plan = json.loads(ruta.read_text(encoding="utf-8"))
    borrador = ruta.with_name("plan_borrador.json")
    if not borrador.exists() or not plan["slides"][0].get("curado"):
        borrador.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    plan = json.loads(borrador.read_text(encoding="utf-8"))
    curar(plan)
    ruta.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"curado: {ruta}")


if __name__ == "__main__":
    main()
