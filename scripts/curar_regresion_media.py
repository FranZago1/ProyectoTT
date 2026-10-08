"""Curación (criterio) del carrusel de TikTok «Regression to the Mean» (@quantgent).

Uso: .venv/bin/python scripts/curar_regresion_media.py  (después de `extraer regresion-media`)
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from curar_referencia import NB, RAIZ, bloque, pct, zona_texto  # noqa: E402

SLUG = "regresion-media"
LOGO = "El logo del autor (abajo) se conserva tal cual."


def et(en, es, caja, tam, **kw):
    return {"texto_en": en, "texto_es": es, "caja": caja, "tam_px": tam, **kw}


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Regression to the Mean: The Law That Pulls Every Extreme Back to Normal"
    plan["titulo_es"] = "Regresión a la media: la ley que devuelve cada extremo a la normalidad"

    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho", bloques=[
        bloque(a, 0, "titulo", "Regression to the Mean", "Regresión a la media", "bold"),
        bloque(a, 1, "subtitulo", "The Law That Pulls Every Extreme Back to Normal",
               "La ley que devuelve cada extremo a la normalidad", "bold"),
        bloque(a, 2, "cuerpo",
               "The best fund this year will probably be average next year. The worst will probably bounce back. "
               "This one law explains both.",
               "El mejor fondo de este año probablemente sea uno promedio el año que viene. El peor probablemente "
               "se recupere. Esta sola ley explica las dos cosas.", "regular"),
    ], zonas_grafico=[{
        "caja": [190, 1095, 890, 1520], "estrategia": "C",
        "justificacion": "Ilustración (dos campanas: media y extremo); se traducen sus tres rótulos.",
        "tipo": "ilustración: distribución centrada en la media y distribución desplazada al extremo",
        "etiquetas": [
            et("Mean", "Media", [434, 1114, 496, 1136], 17, peso="bold", color="#1A1A1A"),
            et("Extreme", "Extremo", [602, 1114, 688, 1136], 17, peso="bold", color="#9A9A9A"),
            et("Extremes\nregress", "Los extremos\nregresan", [262, 1410, 357, 1447], 14.5, peso="bold",
               color="#1A1A1A", interlineado=1.15, alineacion="derecha", borrado="local",
               caja_borrar=[272, 1410, 358, 1447]),
        ],
    }], notas_revisar=[LOGO])

    a = S[1]["bloques"]
    S[1].update(funcion="Ejemplo cotidiano: el trayecto de 18 minutos", bloques=[
        bloque(a, 0, "titulo", "Regression to the mean in everyday life",
               "La regresión a la media en la vida cotidiana", "bold"),
        bloque(a, 1, "cuerpo",
               "Your commute averages 35 minutes. One morning, every light is green, every lane is clear. You make "
               "it in 18 minutes.",
               "Tu trayecto al trabajo dura 35 minutos en promedio. Una mañana, todos los semáforos están en verde "
               "y todos los carriles, libres. Llegás en 18 minutos.", "regular"),
        bloque(a, 2, "cuerpo",
               "Tomorrow, 33 minutes. The route didn't change. The 18 minute run just included conditions that are "
               "unlikely to all align again soon.",
               "Al día siguiente, 33 minutos. La ruta no cambió. El viaje de 18 minutos simplemente reunió "
               "condiciones que difícilmente vuelvan a alinearse todas pronto.", "regular"),
        bloque(a, 3, "destacado", "The extreme result corrected itself. This is regression to the mean.",
               "El resultado extremo se corrigió solo. Esto es la regresión a la media.", "bold"),
    ], zonas_grafico=[{
        "caja": [270, 1150, 810, 1470], "estrategia": "A",
        "justificacion": "Serie ilustrativa de 30 días sin datos exactos en el texto: no se reconstruye; se "
                         "reescriben los rótulos.",
        "tipo": "línea: minutos de viaje por día (30 días), promedio 35 min, mínimo de 18 min",
        "etiquetas": [
            et("Commute (min)", "Trayecto (min)", [271, 1214, 296, 1348], 16, rotacion=90, color="#8C8C8C",
               borrado="local"),
            et("Day", "Día", [544, 1442, 592, 1469], 16, color="#8C8C8C", borrado="local"),
            et("Average: 35 min", "Promedio: 35 min", [664, 1236, 806, 1254], 13.5, peso="bold",
               color="#2E6B3C", alineacion="derecha", borrado="inpaint", halo=3),
        ],
    }], notas_revisar=[
        LOGO,
        "Gráfico: el rótulo «Promedio: 35 min» pisa la serie, igual que en el original (se reescribió con halo "
        "blanco); revisar en Canva.",
    ])

    a = S[2]["bloques"]
    S[2].update(funcion="Mecanismo: componente persistente + componente variable", bloques=[
        bloque(a, 0, "titulo", "Why it happens", "Por qué ocurre", "bold"),
        bloque(a, 1, "cuerpo",
               "Every measured outcome contains a persistent component and a variable component. The persistent "
               "part repeats. The variable part does not.",
               "Todo resultado que se mide tiene un componente persistente y un componente variable. La parte "
               "persistente se repite. La variable, no.", "regular"),
        bloque(a, 2, "cuerpo",
               "When a result is far from the average, the variable component was likely large. On the next "
               "measurement, that component resets. The result moves closer to the long-term average.",
               "Cuando un resultado está lejos del promedio, probablemente el componente variable fue grande. En "
               "la siguiente medición, ese componente se reinicia. El resultado se acerca al promedio de largo "
               "plazo.", "regular"),
        bloque(a, 3, "destacado",
               "The more extreme the result, the larger the variable component, and the stronger the correction.",
               "Cuanto más extremo el resultado, más grande el componente variable y más fuerte la corrección.",
               "bold"),
    ], zonas_grafico=[{
        "caja": [270, 1250, 810, 1575], "estrategia": "A",
        "justificacion": "Barras apiladas ilustrativas: los totales (60 y 40) están en el gráfico, pero la "
                         "partición persistente/variable no está en el texto; se reescriben los rótulos.",
        "tipo": "barras apiladas: medición 1 (extrema, total 60) y medición 2 (corregida, total 40)",
        "etiquetas": [
            et("Result", "Resultado", [274, 1362, 295, 1424], 16, rotacion=90, color="#8C8C8C", borrado="local"),
            et("Persistent", "Persistente", [656, 1271, 732, 1289], 14, alineacion="izquierda", color="#333333"),
            et("Long-term\naverage", "Promedio de\nlargo plazo", [740, 1352, 812, 1381], 12, interlineado=1.1,
               alineacion="izquierda", color="#9A9A9A"),
            et("Measurement 1\n(Extreme)", "Medición 1\n(extrema)", [340, 1531, 476, 1572], 16, interlineado=1.15,
               color="#8C8C8C", borrado="local"),
            et("Measurement 2\n(Corrected)", "Medición 2\n(corregida)", [596, 1531, 732, 1572], 16,
               interlineado=1.15, color="#8C8C8C", borrado="local"),
        ],
    }], notas_revisar=[LOGO])

    a = S[3]["bloques"]
    S[3].update(funcion="Evidencia en distintos ámbitos (NBA, fondos)", bloques=[
        bloque(a, 0, "titulo", "The data is consistent across different fields",
               "Los datos son consistentes en distintos ámbitos", "bold"),
        bloque(a, 1, "cuerpo",
               "In the NBA, the highest-scoring rookie almost never leads their team in scoring by year three. "
               "Their first season included a streak that was unlikely to hold.",
               "En la NBA, el novato que más anota casi nunca es el máximo anotador de su equipo en su tercer "
               "año. Su primera temporada incluyó una racha que difícilmente se iba a sostener.", "regular"),
        bloque(a, 2, "cuerpo",
               "The same pattern appears in finance. S&P Dow Jones tracks funds that finish in the top 25%. Five "
               "years later, 9 out of 10 of those funds are no longer in the top group.",
               f"El mismo patrón aparece en finanzas. S&P Dow Jones sigue a los fondos que terminan en el "
               f"{pct(25)} superior. Cinco años después, 9 de cada 10 de esos fondos ya no están en el grupo de "
               f"arriba.", "regular"),
        bloque(a, 3, "destacado", "It is one of the most replicated findings in statistics.",
               "Es uno de los hallazgos más replicados de la estadística.", "bold"),
    ], zonas_grafico=[{
        "caja": [340, 1305, 740, 1570], "estrategia": "A",
        "justificacion": "Diagrama de flujo con pocos rótulos (texto blanco sobre cajas de color): se borra la "
                         "tinta con el color de cada caja y se reescribe.",
        "tipo": "flujo: fondos del cuartil superior → posición 5 años después (10 / 25 / 30 / 35 %)",
        "etiquetas": [
            et("YEAR 1-5", "AÑOS 1-5", [356, 1320, 420, 1334], 11, peso="bold", color="#8A8A8A"),
            et("5 YEARS LATER", "5 AÑOS DESPUÉS", [620, 1314, 720, 1329], 11, peso="bold", color="#8A8A8A"),
            et("Top 25%\nFunds", "Fondos del\ncuartil\nsuperior", [350, 1360, 426, 1402], 12.5, peso="bold",
               color="#FFFFFF", interlineado=1.05, borrado="local", caja_borrar=[352, 1362, 424, 1398]),
            et("Top 25%\n10%", f"Cuartil superior\n{pct(10)}", [612, 1350, 730, 1380], 12.5, peso="bold",
               color="#FFFFFF", interlineado=1.05, borrado="local"),
            et("25-50%\n25%", f"25-50{NB}%\n{pct(25)}", [612, 1409, 730, 1438], 12.5, peso="bold",
               color="#FFFFFF", interlineado=1.05, borrado="local"),
            et("50-75%\n30%", f"50-75{NB}%\n{pct(30)}", [612, 1468, 730, 1497], 12.5, peso="bold",
               color="#FFFFFF", interlineado=1.05, borrado="local"),
            et("Bottom 25%\n35%", f"Cuartil inferior\n{pct(35)}", [612, 1526, 730, 1555], 12.5, peso="bold",
               color="#FFFFFF", interlineado=1.05, borrado="local"),
        ],
    }], notas_revisar=[
        LOGO,
        "Afirmación dudosa y sin fuente: «el novato que más anota casi nunca es el máximo anotador de su equipo "
        "en su tercer año». Hay contraejemplos conocidos; verificar con datos o quitar.",
        "Verificar con el S&P Persistence Scorecard (S&P Dow Jones Indices): qué fondos, qué período y si "
        "«9 de cada 10» y la distribución 10 / 25 / 30 / 35 % del gráfico corresponden al mismo informe. "
        "Citar la edición y la fecha.",
        "Precisión: si los fondos se repartieran al azar, el 25 % seguiría arriba; que solo quede el 10 % "
        "indica algo más que regresión a la media (cierres de fondos, sesgo de supervivencia). "
        "«Uno de los hallazgos más replicados» no tiene fuente.",
    ])

    a = S[4]["bloques"]
    S[4].update(funcion="Distinción: regresión a la media vs. reversión a la media", bloques=[
        bloque(a, 0, "titulo", "Regression to the mean is not Mean reversion",
               "La regresión a la media no es reversión a la media", "bold"),
        bloque(a, 1, "subtitulo", "known as a tradeable strategy", "conocida como estrategia de trading",
               "regular", ancho_max_px=700),
        bloque(a, 2, "cuerpo",
               "Mean reversion assumes a force pulling prices back to fair value. Regression to the mean requires "
               "no force at all.",
               "La reversión a la media supone una fuerza que lleva los precios de vuelta a su valor justo. La "
               "regresión a la media no requiere ninguna fuerza.", "regular"),
        bloque(a, 3, "cuerpo",
               "A stock drops 50%. Traders call it \"due for a bounce.\" But regression to the mean doesn't say it "
               "will go back up. It says the next move will probably be less extreme. That could mean falling 10% "
               "instead of another 50%.",
               f"Una acción cae un {pct(50)}. Los traders dicen que “le toca rebotar”. Pero la regresión a la "
               f"media no dice que vaya a volver a subir. Dice que el próximo movimiento probablemente sea menos "
               f"extremo. Eso podría significar caer un {pct(10)} en lugar de otro {pct(50)}.", "regular"),
        bloque(a, 4, "destacado",
               "One is a tradeable strategy. The other is a statistical property of variance. Confusing them is one "
               "of the most expensive mistakes in finance.",
               "Una es una estrategia de trading. La otra es una propiedad estadística de la varianza. "
               "Confundirlas es uno de los errores más caros en finanzas.", "bold"),
    ], zonas_grafico=[], notas_revisar=[
        LOGO,
        "En el original, el subtítulo gris («known as a tradeable strategy») describe a la reversión a la "
        "media, pero queda debajo del título completo; en Canva podría quedar más claro como "
        "«Reversión a la media: conocida como estrategia de trading».",
    ])

    a = S[5]["bloques"]
    S[5].update(funcion="Origen histórico: Galton (1886)", bloques=[
        bloque(a, 0, "titulo", "Where it was first discovered", "Dónde se descubrió", "bold"),
        bloque(a, 1, "cuerpo",
               "Francis Galton first documented this in 1886. He measured the heights of parents and their adult "
               "children.",
               "Francis Galton lo documentó por primera vez en 1886. Midió la altura de padres y de sus hijos "
               "adultos.", "regular"),
        bloque(a, 2, "cuerpo",
               "Tall parents produced tall children, but slightly shorter on average. Short parents produced short "
               "children, but slightly taller. Both groups drifted toward the population mean.",
               "Los padres altos tenían hijos altos, pero en promedio un poco más bajos. Los padres bajos tenían "
               "hijos bajos, pero un poco más altos. Ambos grupos se desplazaron hacia la media de la población.",
               "regular"),
        bloque(a, 3, "destacado",
               "Extreme observations require multiple factors to align. On the next measurement, that alignment is "
               "unlikely to repeat.",
               "Las observaciones extremas requieren que se alineen varios factores. En la siguiente medición, es "
               "poco probable que esa alineación se repita.", "bold"),
    ], zonas_grafico=[{
        "caja": [270, 1240, 800, 1575], "estrategia": "C",
        "justificacion": "Dispersión de datos (Galton): no se reconstruye; se traducen leyenda y rótulos de ejes; "
                         "los ticks (en pulgadas) quedan sin tocar.",
        "tipo": "dispersión: altura de padres vs. hijos (pulgadas), recta de regresión con pendiente 0,58",
        "etiquetas": [
            et("Regression (slope=0.58)", "Regresión (pendiente = 0,58)", [395, 1251, 545, 1269], 12.5,
               alineacion="izquierda", color="#1A1A1A"),
            et("If no regression", "Sin regresión", [395, 1268, 492, 1286], 12.5, alineacion="izquierda",
               color="#1A1A1A"),
            et("Population mean", "Media poblacional", [373, 1367, 476, 1384], 12.5, alineacion="izquierda",
               color="#9A9A9A", borrado="inpaint", halo=2),
            et("Child Height (inches)", "Altura de los hijos (pulgadas)", [282, 1300, 304, 1468], 16, rotacion=90,
               color="#8C8C8C"),
            et("Parent Height (inches)", "Altura de los padres (pulgadas)", [480, 1553, 660, 1574], 16,
               color="#8C8C8C"),
        ],
    }], notas_revisar=[
        LOGO,
        "Verificar la pendiente 0,58 y el origen de los puntos: el gráfico no cita fuente (¿datos de Galton o "
        "simulados?). Con los datos de Galton (altura media de los padres) la pendiente usual es ≈ 0,65.",
        "Ticks en pulgadas con punto decimal (62.5): se conservaron (estrategia C). En Canva, si se rehace, "
        "usar 62,5 o convertir a centímetros.",
    ])

    a = S[6]["bloques"]
    S[6].update(funcion="Cierre aforístico sin gráfico", bloques=[
        bloque(a, 0, "cuerpo",
               "Regression to the mean does not imply that everything becomes average. Skill differences are real "
               "and persistent.",
               "La regresión a la media no implica que todo se vuelva promedio. Las diferencias de habilidad son "
               "reales y persistentes.", "regular"),
        bloque(a, 1, "cuerpo",
               "What it does mean is that any single measurement overstates the role of skill. The more extreme the "
               "result, the larger the overstatement.",
               "Lo que sí implica es que cualquier medición aislada exagera el papel de la habilidad. Cuanto más "
               "extremo el resultado, mayor la exageración.", "regular"),
        bloque(a, 2, "destacado",
               "The correct response to an outlier is not to chase it or to dismiss it. It is to expect the next "
               "result to be less extreme.",
               "La respuesta correcta ante un valor atípico no es perseguirlo ni descartarlo. Es esperar que el "
               "próximo resultado sea menos extremo.", "bold"),
    ], zonas_grafico=[], notas_revisar=[
        LOGO,
        "Imprecisión: «cualquier medición aislada exagera el papel de la habilidad» vale para las mediciones "
        "extremas (por arriba); una medición muy mala lo subestima. La traducción es fiel.",
    ])
    for s in S:
        s["zona_texto"] = zona_texto(s["bloques"])
        s["curado"] = True
    plan["glosario_nuevo"] = [{"en": en, "es": es} for en, es in [
        ("regression to the mean", "regresión a la media"),
        ("mean reversion", "reversión a la media"),
        ("tradeable strategy", "estrategia de trading"),
        ("due for a bounce", "le toca rebotar"),
        ("commute", "trayecto (al trabajo)"),
        ("rookie", "novato"),
        ("outlier", "valor atípico"),
        ("skill", "habilidad"),
        ("persistent / variable component", "componente persistente / variable"),
        ("long-term average", "promedio de largo plazo"),
        ("population mean", "media poblacional"),
        ("Top 25% / Bottom 25%", "cuartil superior / cuartil inferior"),
        ("fair value", "valor justo"),
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
