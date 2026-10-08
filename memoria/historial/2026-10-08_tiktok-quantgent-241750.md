# 2026-10-08 — tiktok-quantgent-241750

**Título original:** The Kelly Criterion: The Formula That Tells You Exactly How Much to Risk  
**Título en español:** El criterio de Kelly: la fórmula que te dice exactamente cuánto arriesgar  
**Motor OCR:** tesseract · **Orden de páginas:** [1, 2, 3, 4, 5, 6, 7]

## Slide 1 — Portada: concepto + promesa + gancho

- *titulo* (bold, 85 px): El criterio de Kelly
- *subtitulo* (regular, 43 px): La fórmula que te dice exactamente cuánto arriesgar.
- *cuerpo* (regular, 38 px): Jugadores profesionales de póker, fondos de cobertura y hasta leyendas del blackjack usan la misma ecuación. Veamos cómo funciona.
- **Gráfico** (superficie 3D sin rótulos explicativos (ejes a y v)) — estrategia C: Superficie 3D con ejes en notación (a, v) y ticks; sin texto en lenguaje natural.
- ⚠ Generalización sin fuente: «jugadores profesionales de póker, fondos de cobertura y leyendas del blackjack usan la misma ecuación».
- ⚠ Gráfico de portada sin explicación: no se indica qué miden los ejes a y v ni el eje vertical.

## Slide 2 — Planteo: no qué apostar, sino cuánto

- *cuerpo* (regular, 42 px): La mayoría se concentra en QUÉ apostar. Kelly responde la pregunta en la que nadie piensa: CUÁNTO.
- *cuerpo* (regular, 42 px): Si apostás muy poco, dejás dinero sobre la mesa. Si apostás demasiado, una mala racha te deja fuera de juego. En el medio hay un monto matemáticamente perfecto, y Kelly lo encuentra.
- **Gráfico** (diagrama: rendimiento según el riesgo asumido, de conservador a suicida) — estrategia A: Diagrama conceptual (rendimiento según riesgo) con siete rótulos sobre fondo blanco: se reescriben; la «K» queda.
- ⚠ Precisión: el monto es «perfecto» solo si se conocen las probabilidades reales (ver slide 5).
- ⚠ Diagrama conceptual sin escala ni fuente; «Agresivo» marca el máximo (Kelly completo).

## Slide 3 — La fórmula y sus variables + quién la creó

- *titulo* (regular, 53 px): La fórmula es engañosamente simple
- *otro* (regular, 51 px): f = (bp − q) / b
- *cuerpo* (regular, 44 px): Donde b es la cuota que te pagan, p es tu probabilidad de ganar y q, tu probabilidad de perder. Te dice la fracción exacta de tu capital que tenés que poner en cada apuesta para crecer lo más rápido posible sin terminar en la ruina.
- **Gráfico** (foto: retrato de John Larry Kelly Jr.) — estrategia C: Retrato con pie que es un nombre propio (John Larry Kelly Jr.): se conserva.
- ⚠ Precisión: b es la cuota neta (lo que se gana por cada unidad apostada). Kelly maximiza el crecimiento logarítmico esperado; «sin terminar en la ruina» supone que se conocen p y b exactamente.
- ⚠ Retrato sin fuente: verificar derechos de uso.

## Slide 4 — Clave: maximiza la tasa de crecimiento, no el valor esperado

- *titulo* (regular, 54 px): Esta es la clave
- *cuerpo* (regular, 42 px): Kelly maximiza la TASA DE CRECIMIENTO de largo plazo de tu patrimonio, no tu ganancia esperada en una apuesta individual. Es una diferencia enorme. Maximizar el valor esperado puede indicarte que apuestes todo. Kelly nunca hace eso, porque respeta la matemática del interés compuesto y de la ruina.
- **Gráfico** (líneas: crecimiento según apalancamiento, curva teórica (Kelly) vs. real, zona óptima) — estrategia A: Curvas sin datos en el texto: no se regeneran; se reescriben los seis rótulos (ticks sin tocar).
- ⚠ Contradicción texto-gráfico: el gráfico ubica el óptimo de Kelly en un apalancamiento de ≈ 2 (más del 100 % del capital), mientras el texto dice que Kelly «nunca» apuesta todo. Con p < 1 y sin apalancamiento, la fracción de Kelly es menor que 1.
- ⚠ Gráfico sin fuente ni unidades en el eje vertical; los ticks (6.00, 5.00…) se conservaron.

## Slide 5 — La trampa: conocer la ventaja real; Kelly fraccional

- *titulo* (regular, 61 px): ¿La trampa?
- *cuerpo* (regular, 42 px): Kelly supone que conocés tu verdadera ventaja. Si sobreestimás qué tan buena es tu apuesta, Kelly te va a hacer apostar montos demasiado grandes. Por eso la mayoría de los traders profesionales usa el “Kelly fraccional”: apuesta la mitad o un cuarto de lo que indica la fórmula, como margen de seguridad por si se equivoca sobre su propia ventaja.
- **Gráfico** (curva: tasa de crecimiento g según la fracción apostada f, zonas de riesgo calculado, irracional y ruina) — estrategia A: Curva g(f) sin parámetros en el texto: no se regenera; se reescriben los tres rótulos en itálica serif, como el original.
- ⚠ Sin fuente: «la mayoría de los traders profesionales usa Kelly fraccional».
- ⚠ Gráfico sin parámetros: no se sabe a qué apuesta corresponde la curva (el óptimo cae cerca de f = 0,8). Los rótulos pisan la curva, igual que en el original.

## Slide 6 — Casos: Ed Thorp, Buffett, Renaissance

- *titulo* (regular, 62 px): No es solo teoría
- *cuerpo* (regular, 42 px): Ed Thorp usó Kelly para ganarles a los casinos al blackjack en la década de 1960; después lo llevó a Wall Street y construyó uno de los fondos de cobertura más exitosos de la historia. Las apuestas concentradas de Warren Buffett siguen la lógica de Kelly. Según se informa, Renaissance Technologies usa esquemas de dimensionamiento basados en la misma matemática.
- **Gráfico** (foto: hombre de esmoquin en una mesa de blackjack) — estrategia C: Foto recortada sin texto: se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva. Verificar también que la persona retratada sea Ed Thorp: el original no lo indica.
- ⚠ Interpretación sin fuente: que las apuestas de Buffett «siguen la lógica de Kelly» es una lectura de terceros, no algo que Buffett haya declarado. Lo de Renaissance es trascendido («según se informa»).
- ⚠ Ed Thorp: el fondo fue Princeton Newport Partners (1969-1988); precisar si se quiere dar el nombre.

## Slide 7 — Cierre: la mentalidad (sobrevivir primero), sin gráfico

- *cuerpo* (regular, 46 px): La mayor lección de Kelly no es la fórmula: es la mentalidad. Primero está sobrevivir. Los traders que duran décadas no son los que apuestan fuerte en cada operación. Son los que dimensionan bien sus posiciones, siguen en juego y dejan que el interés compuesto haga el trabajo pesado. Kelly lo demuestra matemáticamente.
- **Gráfico**: ninguno.
- ⚠ Exageración: Kelly demuestra que su fracción maximiza el crecimiento de largo plazo bajo supuestos (probabilidades conocidas, apuestas repetidas); no «demuestra» cómo duran los traders.
