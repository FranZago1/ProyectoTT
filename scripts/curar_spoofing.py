"""Curación del carrusel de TikTok «Spoofing» (@quantgent, 7 slides).

Uso: .venv/bin/python scripts/curar_spoofing.py  (después de `extraer tiktok-quantgent-158294`)
"""

from curar_tiktok import FOTO, NB, bloque, ejecutar, et, glosario, pad, pct

SLUG = "tiktok-quantgent-158294"
ITAL = "Inter-Italic.otf"
US = f"US${NB}"


def curar(plan):
    S = plan["slides"]
    plan["titulo_en"] = "Spoofing: The Illegal Algorithm That Made $300 Million From Fake Orders"
    plan["titulo_es"] = "Spoofing: el algoritmo ilegal que ganó US$ 300 millones con órdenes falsas"

    a = S[0]["bloques"]
    S[0].update(funcion="Portada: concepto + promesa + gancho (caso JP Morgan)", bloques=[
        bloque(a, 0, "titulo", "Spoofing", "Spoofing", "bold"),
        bloque(a, 1, "subtitulo", "The Illegal Algorithm That Made $300 Million From Fake Orders",
               f"El algoritmo ilegal que ganó {US}300 millones con órdenes falsas", "bold"),
        bloque(a, 2, "cuerpo",
               "JP Morgan ran this strategy for 8 years across gold, silver, and US Treasuries. 15 traders. "
               "Hundreds of thousands of orders that were never meant to be filled.",
               "JP Morgan aplicó esta estrategia durante 8 años en oro, plata y bonos del Tesoro de EE. UU. "
               "15 traders. Cientos de miles de órdenes que nunca tuvieron intención de ejecutarse.", "regular"),
        bloque(a, 3, "cuerpo",
               "The fine: $920 million. The largest in CFTC history. Here's how it worked.",
               f"La multa: {US}920 millones. La mayor en la historia de la CFTC (el regulador de futuros de "
               f"EE. UU.). Veamos cómo funcionaba.", "regular"),
    ], zonas_grafico=[{
        "caja": [230, 1190, 850, 1570], "estrategia": "C",
        "justificacion": "Ilustración de un libro de órdenes con rótulos técnicos de uso corriente en el mercado "
                         "local (BID, ASK, SPREAD) y textos ilegibles en las celdas: se conserva.",
        "tipo": "ilustración: libro de órdenes con puntas compradora (verde) y vendedora (roja)",
        "etiquetas": [],
    }], notas_revisar=[
        "Contradicción con la slide 5: la portada dice que el algoritmo «ganó US$ 300 millones», pero según "
        "la slide 5 esos US$ 300 millones son las pérdidas que causó a otros participantes. Unificar en Canva "
        "(p. ej., «que causó pérdidas por US$ 300 millones»).",
        "Precisión: los US$ 920,2 millones (2020) suman las sanciones del Departamento de Justicia, la CFTC y "
        "la SEC; lo que la CFTC calificó de récord fue el monto en un caso de spoofing. «15 traders» no figura "
        "así en los comunicados oficiales: verificar.",
        "Rótulos BID / ASK / SPREAD conservados en inglés (uso habitual en el mercado argentino: «punta "
        "compradora / vendedora» y «spread»).",
    ])

    a = S[1]["bloques"]
    S[1].update(funcion="Mecanismo paso a paso (gráfico de tres paneles)", bloques=[
        bloque(a, 0, "titulo", "How It Works", "Cómo funciona", "bold"),
        bloque(a, 1, "cuerpo",
               "Place a massive buy order. Thousands of contracts. The market sees sudden demand and the price "
               "starts rising.",
               "Colocás una orden de compra enorme. Miles de contratos. El mercado ve una demanda repentina y el "
               "precio empieza a subir.", "regular"),
        bloque(a, 2, "cuerpo", "Other algorithms detect the pressure and start buying too.",
               "Otros algoritmos detectan la presión y también empiezan a comprar.", "regular"),
        bloque(a, 3, "cuerpo", "Then cancel your order before it fills. The demand was never real.",
               "Después cancelás tu orden antes de que se ejecute. La demanda nunca fue real.", "regular"),
        bloque(a, 4, "destacado", "You just moved the price without spending a dollar.",
               "Acabás de mover el precio sin gastar un dólar.", "bold"),
    ], zonas_grafico=[{
        "caja": [240, 1240, 840, 1560], "estrategia": "A",
        "justificacion": "Tres paneles ilustrativos con títulos y pies chicos: se reescriben (los pies, sobre el "
                         "relleno de color, con borrado plano).",
        "tipo": "tres paneles: 1) órdenes falsas, 2) el precio sube, 3) cancelar y ganar",
        "etiquetas": [
            et("1. Place fake orders", "1. Órdenes falsas", [282, 1255, 381, 1269], 9.5, peso="bold",
               color="#3DAA62", caja_borrar=pad([286, 1258, 377, 1266], 2)),
            et("2. Price moves up", "2. El precio sube", [494, 1255, 586, 1270], 9.5, peso="bold",
               color="#E0962B", caja_borrar=pad([498, 1257, 582, 1268], 2)),
            et("3. Cancel and profit", "3. Cancelar y ganar", [698, 1255, 798, 1270], 9.5, peso="bold",
               color="#D24A42", caja_borrar=pad([702, 1258, 794, 1268], 2)),
            et("Huge buy orders appear", "Aparecen órdenes de compra enormes", [272, 1517, 396, 1528], 7.5,
               fuente=ITAL, color="#A8B5AD", borrado="plano", caja_borrar=[281, 1514, 389, 1531]),
            et("Algos react and buy", "Los algoritmos reaccionan y compran", [480, 1524, 600, 1535], 7.5,
               fuente=ITAL, color="#B9AE9A", borrado="plano", caja_borrar=[497, 1521, 582, 1538]),
            et("Fake orders vanish", "Las órdenes falsas desaparecen", [690, 1521, 805, 1532], 7.5,
               fuente=ITAL, color="#BFA9A7", borrado="plano", caja_borrar=[705, 1518, 790, 1535]),
        ],
    }], notas_revisar=[
        "Rótulos del gráfico muy chicos (7,5-9,5 px, como el original): si en Canva no se leen, ampliarlos.",
    ])

    a = S[2]["bloques"]
    S[2].update(funcion="Por qué funciona: el inversor minorista no ve la intención", bloques=[
        bloque(a, 0, "titulo", "So why does anyone fall for it?", "¿Y por qué alguien cae en la trampa?", "bold"),
        bloque(a, 1, "cuerpo",
               "Most retail traders never see the order book. They see price moving and volume spiking. Both look "
               "completely real.",
               "La mayoría de los inversores minoristas nunca ve el libro de órdenes. Ve que el precio se mueve y "
               "que el volumen se dispara. Las dos cosas parecen completamente reales.", "regular"),
        bloque(a, 2, "cuerpo",
               "Even traders with Level 2 data can see the orders sitting there, but they can't see intent. A 5,000 "
               "contract buy order from a spoofer looks identical to a real one.",
               "Incluso los traders con datos de nivel 2 (el libro de órdenes completo) pueden ver las órdenes "
               "ahí, pero no pueden ver la intención. Una orden de compra de 5.000 contratos de un spoofer se ve "
               "idéntica a una real.", "regular"),
        bloque(a, 3, "destacado", "By the time the fake orders vanish, the price has already moved.",
               "Para cuando las órdenes falsas desaparecen, el precio ya se movió.", "bold"),
    ], zonas_grafico=[{
        "caja": [300, 1185, 760, 1540], "estrategia": "A",
        "justificacion": "Serie ilustrativa de precio y volumen con cuatro rótulos chicos: se reescriben.",
        "tipo": "líneas y barras: precio con un pico (spoofing) y volumen con un salto",
        "etiquetas": [
            et("Spoof here", "Spoofing acá", [622, 1200, 676, 1216], 9.5, peso="bold", color="#D0605A",
               caja_borrar=pad([628, 1202, 670, 1215], 2)),
            et("Volume spike looks real", "El salto de volumen parece real", [490, 1447, 606, 1460], 8,
               peso="bold", color="#D46A64", caja_borrar=pad([505, 1448, 591, 1462], 1)),
            et("Price", "Precio", [312, 1322, 324, 1355], 8.5, rotacion=90, color="#BEBEBE",
               caja_borrar=pad([314, 1329, 322, 1348], 2)),
            et("Volume", "Volumen", [312, 1474, 324, 1510], 8.5, rotacion=90, color="#BEBEBE",
               caja_borrar=pad([313, 1478, 322, 1506], 2)),
        ],
    }], notas_revisar=[])

    a = S[3]["bloques"]
    S[3].update(funcion="Cómo se ve en el libro de órdenes (captura)", bloques=[
        bloque(a, 0, "titulo", "This is how it looks in the order book.", "Así se ve en el libro de órdenes.",
               "bold"),
        bloque(a, 1, "cuerpo",
               "A spoofer floods one side with fake orders, creating an illusion of supply or demand. Other traders "
               "and algorithms react to what they think is real pressure.",
               "Un spoofer inunda una de las puntas con órdenes falsas y crea la ilusión de oferta o de demanda. "
               "Otros traders y algoritmos reaccionan a lo que creen que es presión real.", "regular"),
        bloque(a, 2, "cuerpo",
               "The spoofer trades on the opposite side, profits from the move, and cancels the fake orders in "
               "milliseconds.",
               "El spoofer opera en la punta contraria, gana con el movimiento y cancela las órdenes falsas en "
               "milisegundos.", "regular"),
        bloque(a, 3, "cita",
               "One JP Morgan trader described it as \"a little razzle dazzle to juke the algos.\"",
               "Un trader de JP Morgan lo describió como “un poco de razzle dazzle para engañar a los algoritmos”.",
               "regular"),
    ], zonas_grafico=[{
        "caja": [290, 1210, 815, 1530], "estrategia": "C",
        "justificacion": "Captura de una plataforma (mapa de calor del libro de órdenes) con una anotación en "
                         "letra minúscula sobre fondo oscuro: se conserva y se traduce en las notas.",
        "tipo": "captura: mapa de calor de un libro de órdenes con una anotación",
        "etiquetas": [],
    }], notas_revisar=[
        "Captura de terceros (sin fuente): verificar derechos de uso. La anotación en inglés (≈ 8 px, casi "
        "ilegible) dice aproximadamente: «Un algoritmo de seguimiento apiló órdenes exactamente a 8 centavos "
        "unas de otras en 5 niveles. ¿Tal vez spoofing, intentando llenar en 78,74 y tomar ganancia en 78,47? "
        "Una acción curiosa…». Si se quiere, rehacerla en Canva.",
        "«razzle dazzle» (truco vistoso) se dejó en inglés porque es la cita textual; verificar la atribución "
        "en los documentos del caso (Departamento de Justicia, 2020).",
    ])

    a = S[4]["bloques"]
    S[4].update(funcion="Casos: JP Morgan (2008-2016) y Navinder Sarao (Flash Crash de 2010)", bloques=[
        bloque(a, 0, "titulo", "JP Morgan did this for 8 years.", "JP Morgan lo hizo durante 8 años.", "bold"),
        bloque(a, 1, "cuerpo",
               "From 2008 to 2016, 15 traders placed hundreds of thousands of spoof orders in gold, silver, "
               "platinum, and US Treasury futures. They caused over $300 million in losses to other market "
               "participants.",
               f"Entre 2008 y 2016, 15 traders colocaron cientos de miles de órdenes falsas en futuros de oro, "
               f"plata, platino y bonos del Tesoro de EE. UU. Causaron pérdidas por más de {US}300 millones "
               f"a otros participantes del mercado.", "regular"),
        bloque(a, 2, "destacado", "The fine: $920.2 million. The largest penalty in CFTC history.",
               f"La multa: {US}920,2 millones. La mayor sanción en la historia de la CFTC.", "bold"),
        bloque(a, 3, "cuerpo",
               "In 2015, Navinder Sarao, a solo trader from his parents' house in London, was arrested by the FBI. "
               "His spoofing algorithm helped trigger the 2010 Flash Crash, which erased $1 trillion in market "
               "value in 5 minutes.",
               f"En 2015, Navinder Sarao, un trader que operaba solo desde la casa de sus padres en Londres, fue "
               f"detenido a pedido del FBI. Su algoritmo de spoofing contribuyó a desatar el Flash Crash de 2010, "
               f"que borró {US}1 billón de valor de mercado en 5 minutos.", "regular"),
    ], zonas_grafico=[{
        "caja": [300, 1285, 790, 1610], "estrategia": "C",
        "justificacion": "Foto (operadores en el recinto, con el cartel «JPMorgan»): se conserva.",
        "tipo": "foto: operadores en un recinto de bolsa", "etiquetas": [],
    }], notas_revisar=[
        FOTO,
        "Precisión: Sarao fue detenido en abril de 2015 por la policía británica a pedido de EE. UU. (no «por "
        "el FBI»); se tradujo «detenido a pedido del FBI». Su papel en el Flash Crash es discutido.",
        "Precisión: en el Flash Crash (6 de mayo de 2010) se evaporó cerca de US$ 1 billón en minutos, pero el "
        "episodio duró unos 36 minutos, no 5.",
        "Ver la contradicción de la portada (US$ 300 millones: ganancia vs. pérdidas causadas).",
    ])

    a = S[5]["bloques"]
    S[5].update(funcion="Por qué es difícil de probar: la intención (gráfico de cancelaciones)", bloques=[
        bloque(a, 0, "titulo", "Why it's almost impossible to catch.", "Por qué es casi imposible atraparlo.",
               "bold"),
        bloque(a, 1, "cuerpo", "Placing and cancelling orders isn't illegal. Every trader does it.",
               "Colocar y cancelar órdenes no es ilegal. Todos los traders lo hacen.", "regular"),
        bloque(a, 2, "destacado",
               "The crime is intent. Regulators have to prove the orders were never meant to be filled.",
               "El delito es la intención. Los reguladores tienen que probar que las órdenes nunca tuvieron "
               "intención de ejecutarse.", "bold"),
        bloque(a, 3, "cuerpo",
               "Spoofing was only explicitly banned in 2010 under the Dodd-Frank Act. In 2018, Jitesh Thakkar "
               "became the first software engineer charged simply for writing the code.",
               "El spoofing recién se prohibió de forma explícita en 2010, con la ley Dodd-Frank. En 2018, Jitesh "
               "Thakkar se convirtió en el primer ingeniero de software acusado solo por escribir el código.",
               "regular"),
    ], zonas_grafico=[{
        "caja": [255, 1130, 830, 1470], "estrategia": "A",
        "justificacion": "Dos paneles ilustrativos con títulos, leyendas y porcentajes chicos: se reescriben.",
        "tipo": "barras: órdenes ejecutadas vs. canceladas, operatoria normal (~25 %) vs. spoofing (~96 %)",
        "etiquetas": [
            et("Normal trading", "Operatoria normal", [340, 1142, 441, 1158], 10, peso="bold", color="#3DAA62",
               caja_borrar=pad([350, 1144, 431, 1156], 2)),
            et("Spoofing", "Spoofing", [667, 1144, 718, 1156], 10, peso="bold", color="#D24A42", conservar=True),
            et("~96% cancel rate", f"~{pct(96)} de cancelación", [645, 1179, 755, 1191], 8, peso="bold",
               fuente=ITAL, color="#D9706A", caja_borrar=pad([659, 1181, 739, 1189], 2)),
            et("Filled", "Ejecutadas", [275, 1169, 298, 1177], 6, alineacion="izquierda", color="#555555",
               borrado="plano", caja_borrar=[273, 1166, 312, 1178]),
            et("Cancelled", "Canceladas", [275, 1178, 310, 1187], 6, alineacion="izquierda", color="#555555",
               borrado="plano", caja_borrar=[273, 1178, 312, 1187]),
            et("Filled", "Ejecutadas", [580, 1169, 603, 1177], 6, alineacion="izquierda", color="#555555",
               borrado="plano", caja_borrar=[578, 1166, 617, 1178]),
            et("Cancelled", "Canceladas", [580, 1178, 615, 1187], 6, alineacion="izquierda", color="#555555",
               borrado="plano", caja_borrar=[578, 1178, 617, 1187]),
            et("~25% cancel rate", f"~{pct(25)} de cancelación", [350, 1395, 440, 1409], 8, fuente=ITAL, color="#A7A7A7",
               caja_borrar=pad([355, 1398, 434, 1406], 3)),
        ],
    }], notas_revisar=[
        "Precisión: Jitesh Thakkar fue acusado en 2018, pero el juicio terminó sin condena (jurado sin "
        "acuerdo en 2019 y cargos retirados). Conviene aclararlo.",
        "Porcentajes de cancelación del gráfico ilustrativos, sin fuente. Leyendas «Ejecutadas / Canceladas» "
        "muy chicas (6 px, como el original): ampliarlas en Canva si hace falta.",
    ])

    a = S[6]["bloques"]
    S[6].update(funcion="Cierre: una orden que nunca fue real, sin gráfico", bloques=[
        bloque(a, 0, "cuerpo", "The strangest part of spoofing isn't that it's illegal.",
               "Lo más extraño del spoofing no es que sea ilegal.", "regular"),
        bloque(a, 1, "destacado", "It's that the entire strategy is built on an order that was never real.",
               "Es que toda la estrategia se basa en una orden que nunca fue real.", "bold"),
        bloque(a, 2, "cuerpo",
               "No capital at risk. No position taken. Just a signal designed to trick other machines into moving "
               "first. In a market dominated by algorithms, the most dangerous weapon isn't speed or data.",
               "Sin capital en riesgo. Sin tomar posición. Solo una señal diseñada para engañar a otras máquinas y "
               "que se muevan primero. En un mercado dominado por algoritmos, el arma más peligrosa no es la "
               "velocidad ni los datos.", "regular"),
        bloque(a, 3, "cuerpo", "It's a lie that lasts 50 milliseconds.", "Es una mentira que dura 50 milisegundos.",
               "regular"),
    ], zonas_grafico=[], notas_revisar=[
        "Imprecisión: «sin capital en riesgo». Las órdenes falsas pueden ejecutarse antes de cancelarse, y el "
        "spoofer sí toma posición en la punta contraria (slide 4). «50 milisegundos» no tiene fuente.",
    ])

    plan["glosario_nuevo"] = glosario([
        ("spoofing / spoofer", "spoofing / spoofer (sin traducir; «órdenes falsas» para spoof orders)"),
        ("order book", "libro de órdenes"),
        ("bid / ask", "punta compradora / vendedora (BID / ASK en gráficos)"),
        ("filled / to fill (an order)", "ejecutada / ejecutarse"),
        ("cancel rate", "tasa de cancelación"),
        ("retail traders", "inversores minoristas"),
        ("Level 2 data", "datos de nivel 2 (libro de órdenes completo)"),
        ("US Treasuries / Treasury futures", "bonos del Tesoro de EE. UU. / futuros sobre bonos del Tesoro"),
        ("CFTC", "CFTC (regulador de futuros de EE. UU.)"),
        ("fine / penalty", "multa / sanción"),
        ("Flash Crash", "Flash Crash (derrumbe relámpago de 2010)"),
        ("Dodd-Frank Act", "ley Dodd-Frank"),
    ])


if __name__ == "__main__":
    ejecutar(SLUG, curar)
