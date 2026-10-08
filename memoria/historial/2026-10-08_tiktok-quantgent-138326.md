# 2026-10-08 — tiktok-quantgent-138326

**Título original:** Black-Scholes: The one equation that changed Wall Street forever  
**Título en español:** Black-Scholes: la ecuación que cambió Wall Street para siempre  
**Motor OCR:** tesseract · **Orden de páginas:** [1, 2, 3, 4, 5, 6, 7, 8]

## Slide 1 — Portada: concepto + promesa + gancho

- *titulo* (bold, 69 px): Black-Scholes
- *subtitulo* (regular, 42 px): La ecuación que cambió Wall Street para siempre. ¿Cada opción que operaste alguna vez? Se valuó con esto.
- *cuerpo* (regular, 37 px): Veamos cómo funciona en realidad.
- **Gráfico** (superficie 3D: precio de una opción de compra C según el precio S y el tiempo t) — estrategia C: Superficie 3D del precio de la opción C(S, t): solo notación (C, S, t) y ticks; no hay texto en lenguaje natural.
- ⚠ Exageración: «¿Cada opción que operaste alguna vez? Se valuó con esto.» Los precios de las opciones los fija el mercado; Black-Scholes se usa sobre todo para expresarlos como volatilidad implícita, y las opciones americanas suelen valuarse con otros modelos (binomial, diferencias finitas).
- ⚠ Gráfico de portada sin parámetros ni fuente (strike, tasa, volatilidad); se conserva tal cual.

## Slide 2 — Mecanismo: el supuesto (movimiento browniano geométrico) y la fórmula

- *cuerpo* (regular, 45 px): Todo parte de un gran supuesto… Los precios de las acciones siguen un paseo aleatorio llamado movimiento browniano geométrico.
- *cuerpo* (regular, 43 px): A partir de ahí, resolvés una ecuación diferencial y obtenés una fórmula cerrada que da el precio exacto de una opción. Sin simulaciones. Por eso se convirtió en el estándar de referencia.
- **Gráfico** (fórmula de Black-Scholes para una opción de compra europea, con d1, d2 y glosario de variables) — estrategia A: Fórmula (imagen, se conserva) con una columna de siete aclaraciones en texto plano sobre fondo blanco: se reescriben en el lugar.
- ⚠ Fórmula: el original escribe «In(S/K)» en lugar de ln(S/K) (logaritmo natural); se conserva la imagen. Corregir en Canva si se rehace.
- ⚠ Precisión: el precio es «exacto» solo bajo los supuestos del modelo (opción europea, sin dividendos, volatilidad y tasa constantes, retornos lognormales, sin costos de transacción).
- ⚠ Columna de aclaraciones reescrita a 21.4 px (el español es más largo); revisar alineación en Canva.

## Slide 3 — Cuándo funciona: mercados tranquilos

- *cuerpo* (regular, 43 px): Cuando los mercados están tranquilos y la volatilidad se mantiene estable, Black-Scholes es prácticamente imbatible. Superficies de precios suaves, griegas confiables y cálculo instantáneo. Para opciones vainilla en condiciones normales, nada se le acerca en velocidad.
- **Gráfico** (línea: S&P 500 real vs. tendencia de crecimiento constante del 6,3 % anual) — estrategia A: Serie real (S&P 500): nunca se reconstruye; se reescriben los dos rótulos en serif. «S&P 500» y los ticks quedan.
- ⚠ Gráfico sin período ni fuente: parece el S&P 500 de 2015 a 2020 (incluye el derrumbe de marzo de 2020). El «6,3 % anual constante» no se puede verificar. Indicar período y fuente o quitar.
- ⚠ Exageración: «prácticamente imbatible» y «nada se le acerca en velocidad» (hay aproximaciones y modelos igual de rápidos para opciones vainilla).
- ⚠ El gráfico muestra justamente un derrumbe, en una slide que habla de mercados tranquilos.

## Slide 4 — Dónde falla: colas gruesas, asimetría y agrupamiento de volatilidad

- *cuerpo* (regular, 43 px): Pero acá es donde se desarma. Los mercados reales tienen colas gruesas, asimetría y agrupamiento de volatilidad… cosas que un paseo aleatorio simple no puede capturar. Forzá Black-Scholes a esa realidad y obtenés superficies deformadas y coberturas que fallan justo cuando más las necesitás.
- **Gráfico** (superficie 3D: volatilidad implícita σ(T, M) según vencimiento T y moneyness M = S/K) — estrategia C: Figura académica (superficie de volatilidad implícita): se conserva; se traducen el título y los rótulos de ejes en lenguaje natural (serif, como el original).
- ⚠ Figura sin fuente. El original tiene erratas en los ejes («Matutity», «Monevness»); se tradujo «Tiempo al vencimiento T» y se conservó «Moneyness M = S/K» (término usual sin traducir).

## Slide 5 — El parche: volatilidad implícita por strike y vencimiento

- *cuerpo* (regular, 43 px): Entonces los traders idearon un atajo: la volatilidad implícita. Mantenés la fórmula de Black-Scholes, pero usás una volatilidad distinta para cada precio de ejercicio y cada vencimiento. La matemática sigue siendo simple, pero ahora la superficie refleja lo que el mercado realmente está haciendo.
- **Gráfico** (superficie 3D ajustada sobre puntos de volatilidad implícita observados) — estrategia C: Figura importada (superficie ajustada a datos de mercado): se conserva; se traduce el rótulo «Tim to Maturity».
- ⚠ Figura sin fuente ni fecha; los ticks y «Moneyness: m» se conservan. Rótulos muy chicos: revisar nitidez en Canva.

## Slide 6 — Solución 1: modelo de Heston (volatilidad estocástica)

- *titulo* (bold, 49 px): ¿Querés que el propio modelo se adapte?
- *cuerpo* (regular, 43 px): Ahí entra Heston. En lugar de suponer que la volatilidad es fija, la deja moverse por su cuenta —con reversión a la media y volatilidad de la volatilidad incorporadas—. Explica la sonrisa de volatilidad de forma natural, en lugar de solo emparcharla.
- **Gráfico** (ficha: ecuaciones del modelo de Heston, trayectoria simulada y supuestos) — estrategia A: Ficha con título, rótulo y cuatro viñetas sobre fondo gris liso: se borra la tinta con el color de la ficha y se reescribe; ecuaciones y trayectoria se conservan.
- ⚠ Ecuación de la ficha con errores: «κap(θ − v_t)» debería ser κ(θ − v_t) y «σ√v/W_v» debería ser σ√v_t dW_v. Se conserva la imagen; corregir en Canva si se rehace.
- ⚠ Precisión: Heston reproduce bien la asimetría de largo plazo, pero le cuesta la sonrisa de vencimientos muy cortos; «la explica de forma natural» es una simplificación.
- ⚠ Viñetas de la ficha reescritas a 16.4 px para que entren en el ancho; revisar en Canva.
- ⚠ El original no cierra la última oración con punto; en español se agregó.

## Slide 7 — Solución 2: modelos de difusión con saltos (Merton)

- *cuerpo* (regular, 43 px): Para mercados todavía más turbulentos, los modelos de difusión con saltos agregan saltos bruscos de precio sobre el paseo aleatorio. Pensá en los derrumbes relámpago (flash crashes) y en los saltos tras los balances —lo que el movimiento browniano finge que no existe—.
- **Gráfico** (líneas: 5 trayectorias simuladas de 1000 pasos con el modelo de difusión con saltos de Merton) — estrategia A: Simulación sin semilla ni parámetros: no se regenera; se traduce el título del gráfico.
- ⚠ Gráfico simulado sin parámetros ni ejes legibles (los ticks salen cortados en el original).

## Slide 8 — Cierre: conclusión práctica sin gráfico

- *titulo* (bold, 56 px): En síntesis
- *cuerpo* (regular, 43 px): Black-Scholes sigue siendo el punto de partida de todo en opciones. Pero los traders inteligentes saben cuándo confiar en él y cuándo pasar a algo mejor. Aprendé la base y después reconocé cuándo el mercado te está diciendo que no alcanza.
- **Gráfico**: ninguno.
