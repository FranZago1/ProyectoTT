# 2026-10-07 — ergodicity

**Título original:** Ergodicity: The Reason Expected Value Destroys Portfolios  
**Título en español:** Ergodicidad: por qué el valor esperado destruye carteras  
**Motor OCR:** tesseract · **Orden de páginas:** [5, 9, 10, 11, 12, 13, 14]

## Slide 1 — Portada: concepto + promesa + gancho

- *titulo* (bold, 91 px): Ergodicidad
- *subtitulo* (bold, 40 px): Por qué el valor esperado destruye carteras
- *cuerpo* (regular, 34 px): Los físicos lo resolvieron hace décadas. Los fondos de cobertura lo usan para dimensionar cada apuesta. La economía todavía se equivoca. Veamos por qué importa.
- *pie* (regular, 20.2 px): Una medida ergódica para funciones de onda del estado fundamental en Monte Carlo por difusión
- **Gráfico** (funciones de onda de Monte Carlo por difusión (figura importada)) — estrategia C: Figura académica (física): se conserva; solo se traduce el rótulo del eje Y.
- ⚠ Gráfico de portada sin relación con el tema: muestra funciones de onda de Monte Carlo por difusión (física cuántica), no ergodicidad en finanzas. Sugerencia: reemplazarlo por el gráfico de 10.000 personas vs. 1 persona.
- ⚠ El pie quedó en dos líneas (el español es más largo); revisar en Canva.

## Slide 2 — Experimento mental: moneda +50 % / −40 %

- *cuerpo* (regular, 34 px): Imaginá una tirada de moneda. Si sale cara, tu patrimonio crece un 50 %. Si sale ceca, cae un 40 %.
- *cuerpo* (regular, 34 px): Ganás 50. Perdés 40. La ganancia es mayor. Si promediás, quedás 5 arriba en cada tirada.
- *cuerpo* (regular, 34 px): Esto es lo que enseña cualquier manual de finanzas. Maximizá el valor esperado. Tomá toda apuesta con valor esperado positivo.
- *destacado* (bold, 34 px): La matemática parece infalible.
- **Gráfico** (barras: cara +50 %, ceca −40 %, valor esperado +5 %) — estrategia B: Valores exactos del texto: +50 %, −40 % y valor esperado +5 % (0,5 × 1,50 + 0,5 × 0,60 = 1,05).
  - datos: `{"tipo": "moneda_valor_esperado", "ganancia_pct": 50, "perdida_pct": 40, "formula": "(0,5 × 1,50) + (0,5 × 0,60) = 1,05", "etiquetas": ["Cara\n+50 %", "Ceca\n−40 %", "Valor\nesperado"]}`

## Slide 3 — Paradoja: promedio de 10.000 personas vs. una persona en el tiempo

- *cuerpo* (regular, 34 px): Jugá exactamente este juego con 10.000 personas a la vez. El patrimonio promedio del grupo se dispara hacia arriba.
- *cuerpo* (regular, 34 px): Ahora jugalo con una sola persona, que tira la moneda mil veces seguidas.
- *destacado* (bold, 34 px): Termina en la ruina. Todas las veces.
- *cuerpo* (regular, 34 px): Misma apuesta. Mismas probabilidades. Misma matemática. Resultado opuesto. El valor esperado era real. Simplemente no era el tuyo.
- **Gráfico** (dos paneles en escala log: patrimonio promedio de 10.000 personas y 5 trayectorias individuales, 300 tiradas) — estrategia B: Simulación del juego (+50 % / −40 %): se regenera con semilla fija (42); regenerado, no idéntico.
  - datos: `{"tipo": "simulacion_conjunto", "semilla": 42, "personas": 10000, "tiradas": 300, "trayectorias": 5, "inicial": 100, "ganancia_pct": 50, "perdida_pct": 40, "titulo_1": "10.000 personas\n(patrimonio promedio)", "titulo_2": "1 persona\n(patrimonio real)", "rotulo_x": "Tiradas"}`
- ⚠ Gráfico: las trayectorias no coinciden con las del original (otra realización aleatoria); el eje Y del panel izquierdo llega a 10³ y no a 10⁵ como en el original.
- ⚠ Afirmación absoluta: «Termina en la ruina. Todas las veces.» Es un resultado con probabilidad 1 en el límite (tiempo infinito), no en cada caso finito: tras 1.000 tiradas, una minoría ínfima sigue arriba del capital inicial.
- ⚠ Inconsistencia: el texto habla de mil tiradas y el gráfico muestra 300.
- ⚠ Precisión: con 10.000 personas el promedio muestral no «se dispara» indefinidamente; termina dominado por pocas trayectorias y cae (se ve en el propio gráfico). El valor esperado sí crece (1,05ⁿ).

## Slide 4 — Explicación paso a paso con $100

- *titulo* (bold, 40 px): Entonces, ¿qué está pasando en realidad?
- *cuerpo* (regular, 34 px): Empezás con $100. Sale cara. Ganás un 50 %. Ahora tenés $150.
- *cuerpo* (regular, 34 px): Siguiente tirada. Sale ceca. Perdés un 40 %. Pero ese 40 % se calcula sobre $150, no sobre tus $100 originales. El 40 % de $150 es $60. Entonces bajás a $90.
- *cuerpo* (regular, 34 px): Una ganancia. Una pérdida. Deberías haber quedado igual. Pero estás $10 abajo.
- *destacado* (bold, 34 px): Esta es la trampa. La ganancia es el 50 % de un número menor. La pérdida es el 40 % de un número mayor. Los porcentajes parecen justos. Los dólares, no.
- **Gráfico** (barras: inicio $100, cara $150, ceca $90; línea de punto de equilibrio en $100) — estrategia B: Valores exactos del texto: $100 → $150 → $90, pérdida de $60.
  - datos: `{"tipo": "caminos_barras", "inicial": 100, "ganancia_pct": 50, "perdida_pct": 40, "etiquetas": ["Inicio", "Cara\n+50 %", "Ceca\n−40 %"], "rotulo_y": "Patrimonio ($)", "etiqueta_equilibrio": "Punto de\nequilibrio"}`

## Slide 5 — El orden no importa: siempre se pierde

- *cuerpo* (regular, 34 px): Ahora invertí el orden. Empezás con $100. Primero sale ceca. Perdés un 40 %. Quedás en $60.
- *cuerpo* (regular, 34 px): Después sale cara. Ganás el 50 % de $60. Son apenas $30. Subís a $90.
- *destacado* (bold, 34 px): Distinto orden. Mismo resultado. $90. No importa si primero ganás o primero perdés. Siempre terminás más pobre.
- *cuerpo* (regular, 34 px): Repetilo suficientes veces y llegás a cero. No es mala suerte. Es matemática.
- **Gráfico** (dos paneles: ambos caminos terminan en $90; alternar cara y ceca 30 veces lleva a ~$20,6) — estrategia B: Datos exactos: caminos $100 → $150 → $90 y $100 → $60 → $90; serie alternada cara/ceca de 30 tiradas (determinística).
  - datos: `{"tipo": "caminos_y_ruina", "inicial": 100, "ganancia_pct": 50, "perdida_pct": 40, "tiradas_ruina": 30, "titulo_1": "Ambos caminos = $90", "titulo_2": "Repetir = ruina", "leyenda_gana": "Gana primero", "leyenda_pierde": "Pierde primero", "etiquetas_x": ["Inicio", "Tirada 1", "Tirada 2"], "rotulo_x": "Tiradas"}`
- ⚠ Precisión: «llegás a cero» es asintótico; el patrimonio tiende a cero pero nunca lo alcanza (tras 30 tiradas alternadas quedan $20,6).

## Slide 6 — Solución (criterio de Kelly) + historia (Kelly 1956, Ole Peters)

- *titulo* (bold, 40 px): Por esto funciona el criterio de Kelly
- *cuerpo* (regular, 34 px): Kelly no maximiza el valor esperado. Maximiza la tasa de crecimiento geométrica. Lo que realmente determina tu patrimonio a lo largo del tiempo.
- *cuerpo* (regular, 34 px): En 1956, Kelly lo resolvió en Bell Labs. En 2020, el físico Ole Peters lo demostró formalmente. Bloomberg lo tituló así: todo lo que aprendimos sobre la economía moderna está mal.
- *destacado* (bold, 34 px): La brecha entre lo que pasa en promedio y lo que te pasa a vos a lo largo del tiempo se llama ergodicidad. Cuando divergen, el valor esperado miente.
- **Gráfico** (curva de Kelly g(f) con el óptimo (f = 25 %) y apostar todo (f = 100 %, g ≈ −0,053)) — estrategia B: Fórmula exacta: g(f) = 0,5·ln(1 + 0,5f) + 0,5·ln(1 − 0,4f); óptimo f = 0,25; g(1) ≈ −0,053.
  - datos: `{"tipo": "kelly", "p": 0.5, "ganancia_pct": 50, "perdida_pct": 40, "texto_optimo": "Óptimo de Kelly\nf = {f}", "texto_total": "Apostar todo (f = 100 %)\ng = {g}", "rotulo_x": "Fracción del patrimonio apostada (f)", "rotulo_y": "Tasa de crecimiento g(f)"}`
- ⚠ Fecha incorrecta: «en 2020 Ole Peters lo probó formalmente». Sus trabajos centrales son de 2011 («Optimal leverage from non-ergodicity») y 2016 (con Murray Gell-Mann, «Evaluating gambles using dynamics»); la nota de Bloomberg con ese titular es de 2017. La traducción es fiel; corregir el año.
- ⚠ Precisión: la brecha entre promedio y trayectoria es la NO ergodicidad; «ergodicidad» es cuando ambos coinciden. La traducción es fiel; considerar «se llama no ergodicidad».
- ⚠ Gráfico regenerado con la fórmula exacta; el original superponía «All-In» sobre el tick 0,8 (corregido).

## Slide 7 — Cierre aforístico sin gráfico

- *cuerpo* (regular, 34 px): Lo que nos enseña la ergodicidad no es matemático…
- *destacado* (bold, 34 px): Es que no vivís mil vidas al mismo tiempo.
- *cuerpo* (regular, 34 px): Vivís una sola vida, en secuencia. Cada apuesta cambia el tamaño de la siguiente. Cada pérdida hace más difícil la recuperación. El promedio de todos los resultados posibles es irrelevante si tu propio camino llega a cero.
- *cuerpo* (regular, 34 px): El mercado no te debe el valor esperado. Solo te debe el camino que efectivamente recorrés.
- **Gráfico**: ninguno.
