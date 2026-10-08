# Guía de estilo — carruseles de finanzas cuantitativas (ES-AR) · Pulso Económico

Consolidada a partir de 11 carruseles distintos (2 de Instagram: fat-tails, ergodicity; 9 de TikTok, todos
de @quantgent: regresion-media, cumpleaños, black-scholes, kelly, bayes, benford, grandes-números,
sobreajuste, spoofing). Las versiones de TikTok de fat-tails y ergodicity no se cuentan dos veces.
Evidencia indicada como «n/11». Se reescribe completa en cada actualización (comando `/estilo`).

## 1. Instrucciones para el modelo que lea esta guía

> Con esta guía, generá un carrusel de 7 slides sobre el tema indicado, en español rioplatense formal con
> voseo. Para cada slide entregá: función narrativa, título (si corresponde), texto con la oración
> destacada en **negrita**, especificación del gráfico (tipo, datos exactos o fórmula, ejes, unidades,
> período, fuente con fecha) y pie de gráfico. Usá solo datos reales y verificables con fuente; si no
> podés verificar un dato, marcalo [DATO A VERIFICAR]. Nunca inventes cifras, fechas ni citas. Preferí
> gráficos que se puedan generar a partir de datos o fórmulas explícitas.

## 2. Estructura narrativa

Largo: 7 slides (7/11); variantes de 6 (cumpleaños, sobreajuste) y de 8 (black-scholes, benford).

| Slide | Función (patrón) | Ejemplos |
|---|---|---|
| 1 | Portada: concepto + promesa + gancho (11/11) | «La paradoja del cumpleaños», «El criterio de Kelly» |
| 2 | Planteo con un ejemplo o una pregunta al lector (11/11) | moneda +50 % / −40 %; «¿Cuántas personas…?»; prueba médica del 99 % |
| 3 | La respuesta contraintuitiva o el mecanismo (11/11) | «La respuesta es 23.»; «Menos del 10 %.»; «El 1 es el primer dígito el 30 %» |
| 4 | Por qué pasa: la intuición falla (9/11) | 253 pares; $100 → $150 → $90; aprender el ruido |
| 5 | La fórmula, con retrato de quien la creó (6/11 fórmula; 4/11 retrato) | Kelly, Bayes, Newcomb, Bernoulli |
| 6 | Aplicación a mercados + casos reales: «No es solo teoría» (7/11) | Thorp, Buffett, Renaissance, Nate Silver, Enron, JP Morgan |
| 7 | Cierre: «La lección de X no es la matemática… es…» (8/11) | «Es la mentalidad.»; «Es la paciencia.» |

Patrones: el concepto se nombra en la portada (11/11); se baja a Wall Street o al trading aunque el
tema sea de probabilidad general (9/11: «Por qué le importa a Wall Street», «Ahora reemplazá
“casino” por “trader”»); un ejemplo cotidiano antes del financiero (6/11: trayecto, cumpleaños, prueba
médica, moneda, primer dígito de una factura). Variantes: historia como cierre del arco (3/11: LTCM,
Kelly 1956, Galton 1886); slide que distingue dos conceptos vecinos (1/11); señales para detectar el
problema (1/11: «Cómo saber si tu modelo te miente»).

## 3. Portadas y títulos

- Título: el concepto en 1-5 palabras, muy grande, en negrita (11/11): «Ergodicidad», «La ley de
  Benford», «La ilusión más cara del trading».
- Subtítulo con promesa, 5-12 palabras (11/11), casi siempre con una cifra o un actor de Wall Street:
  «La pregunta de entrevista que desarma a los aspirantes a analistas cuantitativos (quants)»; «La
  ecuación que detecta fraudes fiscales con solo el primer dígito»; «Por qué los casinos nunca pierden».
- Gancho de 2-3 oraciones (10/11), con una cifra, un actor que «lo usa» y el remate «Veamos por qué.» /
  «Veamos cómo funciona.» (8/11).
- Gráfico, ilustración o foto debajo (11/11). **Debe tener relación con el tema** (en ergodicity,
  black-scholes, bayes y benford era decorativa).
- Títulos internos: afirmación o pregunta de 2-8 palabras, en negrita (11/11): «Por qué tu cerebro
  falla.», «¿La trampa?», «No es solo teoría», «Por qué es casi imposible atraparlo.».

## 4. Cuerpo

- Densidad: 40-90 palabras por slide (11/11), en 2-4 párrafos cortos de 1-3 oraciones.
- Oraciones de 3 a 20 palabras; fragmentos permitidos («Miles de contratos.», «Ínfimo.»).
- Segunda persona con voseo (11/11): «Imaginá», «Escuchás», «Colocás una orden», «No tirás el dado una
  vez».
- Recursos:
  - pregunta-respuesta (9/11): «¿La respuesta real? Menos del 10 %.»; «¿Y los que no? Son la casa.»;
  - tríadas (7/11): «No es un truco. No es una adivinanza. Es probabilidad pura.»;
  - antítesis (11/11): «Tu intuición cuenta personas. La matemática cuenta conexiones.»; «Ganan los
    que cambian de opinión más rápido, no los que más aciertan.»;
  - cifras concretas y redondas en cada slide (23 personas, 253 pares, $100, 10.000 tiradas, US$ 920
    millones).
- Negrita: una oración clave por slide, en párrafo propio, casi siempre al final (10/11): «Pero la
  pregunta no es sobre vos. Es sobre cualquier par.» Negritas internas de palabras sueltas (1/11:
  «¿La tirás **100** veces?»).

## 5. Cierres

- Fórmula fija (8/11): «La (mayor) lección de X no es la matemática / la fórmula / técnica… Es [la
  mentalidad / la paciencia / lo que revela sobre la naturaleza / que los humanos…]», con la segunda
  parte en negrita.
- Remate aforístico con antítesis (11/11): «El mercado no te debe el valor esperado. Solo te debe el
  camino que efectivamente recorrés.»; «La operación más difícil de las finanzas es abandonar un
  backtest hermoso.»; «Es una mentira que dura 50 milisegundos.».
- Sin gráfico (10/11).

## 6. Gráficos

- Uno por slide salvo el cierre (≈ 80 % de las slides); dos paneles lado a lado en 6/11.
- Familias:
  1. **Gráficos propios minimalistas** (11/11) estilo matplotlib: barras con valores en negrita
     (probabilidad por cantidad de personas, primer dígito de Benford, Sharpe 1,2 vs. −0,2), líneas
     finas, ejes grises, sin recuadro superior ni derecho, línea punteada de referencia («Esperado:
     11,1 %», «50 %», punto de equilibrio), anotaciones con flecha.
  2. **Figuras importadas** (8/11): superficies 3D, papers, capturas de plataformas, notación (P(x),
     σ, g(f), C(S, t)).
  3. **Fotos de banco y retratos** (7/11): fiestas, salas de trading, Las Vegas, retratos de Kelly,
     Bayes, Newcomb, Bernoulli. Sin fuente ni derechos claros: evitarlas o usar imágenes propias.
- Colores semánticos (11/11): verde = ganancia, real o robusto; rojo = pérdida, falso o por encima del
  umbral; naranja = intermedio; gris = neutro, inicio o referencia.
- Rótulos chicos (9-17 px), muchas veces en itálica (pies de panel) o en serif (figuras académicas).
- Para carruseles nuevos: gráficos desde datos o fórmulas explícitas (P(n) = 1 − 365! / ((365 − n)! ·
  365ⁿ); P(d) = log₁₀(1 + 1/d); g(f) = 0,5·ln(1 + 0,5f) + 0,5·ln(1 − 0,4f)). Series reales solo con
  fuente y período.

## 7. Diseño

- Formatos: Instagram 1080 × 1350 (4:5); TikTok 1080 × 1920 (9:16, 9/11) con el contenido centrado
  verticalmente (texto desde ≈ 300-640 px, gráfico ≈ 1100-1650 px) y el logo abajo.
- Fondo blanco con degradado gris o durazno muy suave en las esquinas; todo centrado (11/11).
- Columna de texto ≈ 75-80 % del ancho (800-860 px).
- Tipografía: Inter. Título de portada Bold 70-95 px; títulos internos Bold 40-55 px; cuerpo Regular
  34 px (6/11) o 38-45 px (5/11); interlineado ≈ 1,4-1,5; destacados Bold al tamaño del cuerpo.
- **Marca Pulso Económico**: monograma «PE» negro (#111111), trazo grueso, panza circular y terminaciones
  en diagonal (`marca/`). Abajo al centro, alto ≈ 7-8 % del ancho y ≈ 4 % del alto de margen inferior;
  si no hay espacio libre, en una esquina inferior.
- Paleta (extraída automáticamente con k-means de las slides):

<!-- PALETA:INICIO (generado por python -m carrusel memoria) -->

| Carrusel | Fondo | Texto | Acentos (proporción entre píxeles saturados) |
|---|---|---|---|
| fat-tails | #FEFEFE | #070707 | #E4AA58 (32%), #C9443E (31%), #73A3D7 (14%), #627D9C (10%), #4E5D8C (7%), #561F56 (7%) |
| ergodicity | #FEFEFE | #1D1D1D | #568E66 (41%), #B96257 (34%), #3D6E4B (12%), #8B4E47 (9%) |
| regresion-media | #FFFFFF | #1D1D1D | #42906C (43%), #AB1818 (20%), #EBA366 (16%), #EE871A (8%), #B75C5A (8%), #E2AF87 (6%) |
| tiktok-quantgent-308355 | #FFFFFF | #090506 | #70331F (34%), #209A39 (33%), #C4984C (13%), #2F764A (11%), #48E3C8 (4%), #1752EB (4%) |
| tiktok-quantgent-138326 | #FFFFFF | #08080B | #318DB7 (24%), #2B568F (22%), #0E1C5C (20%), #0F1BA1 (16%), #65AAD2 (13%), #A1BE63 (6%) |
| tiktok-quantgent-241750 | #FFFFFF | #080606 | #D1D037 (22%), #F0AC73 (21%), #4C3318 (18%), #B77F57 (14%), #7F5231 (13%), #499E62 (12%) |
| tiktok-quantgent-735830 | #FFFFFF | #0A0A0A | #DB3232 (27%), #F1A130 (24%), #568695 (22%), #5CA8E0 (16%), #6B1E68 (7%), #EFC17D (5%) |
| tiktok-quantgent-437398 | #FFFFFF | #080807 | #BA9F0C (33%), #36754C (28%), #89A00B (18%), #A25D35 (10%), #3BA40E (6%), #0C9D67 (5%) |
| tiktok-quantgent-262422 | #FFFFFF | #070605 | #61A78A (28%), #5093C0 (23%), #82C7ED (23%), #2A7660 (17%), #6A3E2B (6%), #DD936A (4%) |
| tiktok-quantgent-692630 | #FFFFFF | #020202 | #493921 (30%), #AE6959 (21%), #7A542F (20%), #D99A7F (17%), #377B77 (8%), #45DBB2 (4%) |
| tiktok-quantgent-284502 | #FFFFFF | #1D1D1D | #1D7642 (52%), #B23B30 (17%), #CC7A72 (11%), #BF5C53 (8%), #D38A83 (7%), #55936F (6%) |
| tiktok-quantgent-158294 | #FFFFFF | #060405 | #174551 (36%), #2C6D83 (16%), #603631 (15%), #6AC1A2 (12%), #E3A480 (11%), #BF7344 (10%) |
| tiktok-quantgent-456663 | #FFFFFF | #030303 | #438F63 (37%), #C86459 (33%), #246F44 (16%), #91433A (6%), #B2463D (6%) |

<!-- PALETA:FIN -->

  Lectura: fondo blanco; texto #1D1D1D; verde ≈ #2E8B57-#438F63 (oscuro #1D7642); rojo ≈ #B23B30-#C86459;
  naranja ≈ #E0962B-#F0AC73; gris neutro ≈ #9A9A9A. Azules, amarillos y marrones: fotos e
  ilustraciones, no del sistema de colores.

## 8. Tono y registro

Español rioplatense formal y sobrio, como las secciones de economía de la prensa argentina, con voseo.
Tono de «lo que no te cuentan» y de «lo que Wall Street sabe», sin lunfardo ni coloquialismos.

**Hacer**
- Cifras con formato argentino: 99,7 %; 10.000; US$ 920,2 millones; US$ 1 billón (trillion).
- Montos hipotéticos con «$»; montos reales con «US$» y millones.
- Primera mención: «analistas cuantitativos (quants)», «sobreajuste (overfitting)», «backtest (la
  prueba con datos históricos)», «el IRS (el fisco de EE. UU.)», «la CFTC (el regulador de futuros de
  EE. UU.)».
- Fórmulas con ×, −, superíndices y subíndices (365ⁿ, log₁₀, X̄ₙ), no «x», «-», «^n».
- Comillas “…”; raya —inciso— estilo RAE; la raya inglesa que introduce una conclusión pasa a dos
  puntos.
- Una sola oración en negrita por slide; párrafos cortos.
- Citar la fuente de cada estadística (informe, edición, fecha).

**No hacer** (errores detectados en los carruseles analizados)
- Omitir el dato que decide el resultado: «prueba del 99 %, menos del 10 % de probabilidad» sin la
  prevalencia (con 1 %, da 50 %).
- Atribuir mal un caso: Knight Capital (2012) fue una falla de software, no sobreajuste, y la firma
  sobrevivió; Sarao fue detenido por la policía británica; el Flash Crash duró ≈ 36 minutos, no 5.
- Contradecirse: «el algoritmo ganó US$ 300 millones» y después «causó pérdidas por US$ 300
  millones»; «Kelly nunca apuesta todo» con un gráfico que marca un apalancamiento de 2.
- Fechar mal: Ole Peters no «lo probó en 2020» (trabajos de 2011 y 2016; nota de Bloomberg de 2017).
- Confundir probabilidad individual y acumulada («la persona 23 falla más de la mitad de las veces»);
  tasa de acierto con ventaja («ventaja del 52 %»).
- Absolutos falsos: «Termina en la ruina. Todas las veces.»; «garantizado matemáticamente» en un
  número finito de jugadas; «funciona con todo»; «casi todos los datos naturales».
- Generalizar sin fuente: «la mayoría de los traders usa Kelly fraccional», «el 44 % de las estrategias
  publicadas fracasa», «las mesas de Wall Street la usan», «la ventaja del casino es menor al 2 % en la
  mayoría de los juegos» (ruleta americana: 5,26 %).
- Multiplicadores no derivables («3x / 5x más eventos extremos» por una curtosis de 10 o 15).
- Gráficos ajenos al texto: funciones de onda en una portada de finanzas; ganancias de un jugador en
  una slide sobre el casino; un derrumbe en la slide de «mercados tranquilos»; retratos no verificados
  (no existe un retrato auténtico de Bayes).
- Casos judiciales a medias: el ingeniero Thakkar fue acusado pero no condenado; Benford «como prueba
  en Enron» son análisis posteriores.

## 9. Glosario resumido

| EN | ES |
|---|---|
| fat tails | colas gruesas |
| quants | analistas cuantitativos (quants) → quants |
| expected value (EV) | valor esperado |
| ergodicity | ergodicidad |
| regression to the mean / mean reversion | regresión a la media / reversión a la media |
| Kelly Criterion / fractional Kelly | criterio de Kelly / Kelly fraccional |
| edge / house edge | ventaja / ventaja de la casa |
| bankroll | capital (de apuesta) |
| Law of Large Numbers | ley de los grandes números |
| Bayes' Theorem / prior / posterior | teorema de Bayes / a priori / a posteriori |
| base rate | tasa base (prevalencia) |
| Benford's Law | ley de Benford |
| random walk | paseo aleatorio |
| implied volatility / strike | volatilidad implícita / precio de ejercicio |
| overfitting / backtest | sobreajuste (overfitting) / backtest |
| equity curve / drawdown | curva de capital / caída |
| order book / filled | libro de órdenes / ejecutada |
| spoofing / spoof orders | spoofing / órdenes falsas |
| hedge fund / portfolio | fondo de cobertura / cartera |
| leverage | apalancamiento |
| crash / flash crash | derrumbe / derrumbe relámpago (flash crash) |
| coin flip / heads / tails | tirada de moneda / cara / ceca |
| trades / win rate | operaciones / tasa de acierto |
| outlier | valor atípico |
| retail traders | inversores minoristas |
| "Past performance doesn't guarantee future results" | “Rendimientos pasados no garantizan rendimientos futuros” |

Glosario completo: `memoria/GLOSARIO.md`.

## 10. Carruseles de referencia (resumen en español)

**kelly — «El criterio de Kelly: la fórmula que te dice exactamente cuánto arriesgar»** (TikTok, 7)
1. Portada + gancho (póker, fondos, blackjack). 2. «La mayoría se concentra en QUÉ apostar»: muy poco
deja dinero sobre la mesa, demasiado te deja fuera de juego. 3. f = (bp − q) / b + retrato de Kelly.
4. Maximiza la tasa de crecimiento, no el valor esperado (curvas según apalancamiento). 5. «¿La
trampa?»: hay que conocer la ventaja real; Kelly fraccional (curva g(f)). 6. «No es solo teoría»:
Thorp, Buffett, Renaissance. 7. **«La mayor lección de Kelly no es la fórmula: es la mentalidad.»**

**bayes — «El teorema de Bayes: la ecuación que tu cerebro se niega a creer»** (TikTok, 7)
1. Portada + gancho. 2. Prueba del 99 %: **«Te da positivo.»** 3. **«Menos del 10 %.»** (barras
99 % vs. ~9 %). 4. P(A|B) = P(B|A) · P(A) / P(B) + retrato. 5. «Por qué le importa a Wall Street»
(a priori → a posteriori). 6. «No es solo teoría»: Nate Silver, spam, autos autónomos, Renaissance.
7. **«Es la mentalidad.»** Quienes piensan de forma bayesiana actualizan su opinión.

**ergodicity — «Ergodicidad: por qué el valor esperado destruye carteras»** (Instagram y TikTok, 7)
1. Portada + gancho. 2. Moneda +50 % / −40 %: **«La matemática parece infalible.»** 3. 10.000
personas vs. 1. 4. $100 → $150 → $90: **«Los porcentajes parecen justos. Los dólares, no.»** 5. El
orden no importa. 6. Kelly (1956) y Ole Peters; g(f) con óptimo en 25 %. 7. **«Es que no vivís mil
vidas al mismo tiempo.»**
