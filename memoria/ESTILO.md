# Guía de estilo — carruseles de finanzas cuantitativas (ES-AR) · Pulso Económico

Consolidada a partir de 4 carruseles (fat-tails y ergodicity, de Instagram; regresion-media y
cumpleaños —tiktok-quantgent-308355—, de TikTok). Evidencia indicada como «n/4». Se reescribe completa en cada actualización (comando `/estilo`).

## 1. Instrucciones para el modelo que lea esta guía

> Con esta guía, generá un carrusel de 7 slides sobre el tema indicado, en español rioplatense formal con
> voseo. Para cada slide entregá: función narrativa, título (si corresponde), texto con la oración
> destacada en **negrita**, especificación del gráfico (tipo, datos exactos o fórmula, ejes, unidades,
> período, fuente con fecha) y pie de gráfico. Usá solo datos reales y verificables con fuente; si no
> podés verificar un dato, marcalo [DATO A VERIFICAR]. Nunca inventes cifras, fechas ni citas. Preferí
> gráficos que se puedan generar a partir de datos o fórmulas explícitas.

## 2. Estructura narrativa (7 slides; variante de 6)

| Slide | Función | fat-tails | ergodicity | regresion-media | cumpleaños (6) |
|---|---|---|---|---|---|
| 1 | Portada: concepto + promesa | Colas gruesas | Ergodicidad + gancho | Regresión a la media + gancho | Paradoja del cumpleaños + gancho |
| 2 | Romper una creencia / ejemplo | «La matemática te miente» | Moneda +50 % / −40 % | El trayecto de 18 minutos | La pregunta y las respuestas intuitivas |
| 3 | Mecanismo o paradoja | Modelo normal y 2008 | 10.000 personas vs. 1 | Persistente + variable | «La respuesta es 23» (barras) |
| 4 | Nombrar / evidencia | «COLAS GRUESAS» | Paso a paso con $100 | NBA y fondos (S&P) | Por qué falla: 253 pares |
| 5 | Profundizar / distinguir | Curtosis | El orden no importa | No es reversión a la media | La fórmula |
| 6 | Caso, historia o solución | LTCM, 1998 | Kelly (1956) y Ole Peters | Galton (1886) | Cierre (sin gráfico) |
| 7 | Cierre | Ed Thorp + cisne negro | Aforismo sin gráfico | Aforismo sin gráfico | — |

Patrones (4/4): el concepto se nombra en la portada; las slides 2-5 lo explican sin jerga con un
ejemplo concreto; el cierre deja una lección práctica en antítesis. Caso histórico en la anteúltima
(3/4: LTCM, Kelly, Galton); la variante de 6 slides lo reemplaza por la fórmula (1/4). Variantes:
pregunta al lector seguida de las respuestas intuitivas y su refutación (1/4: «Todos están muy
lejos.»); el concepto en mayúsculas en la slide 4 (1/4); una slide para distinguirlo de un concepto
vecino (1/4: regresión vs. reversión a la media).

## 3. Portadas y títulos

- Título: el concepto en 1-4 palabras, muy grande, en negrita (4/4): «Colas gruesas», «Ergodicidad»,
  «Regresión a la media», «La paradoja del cumpleaños».
- Subtítulo con promesa o paradoja, 6 a 12 palabras, en negrita o regular (4/4): «Por qué el valor
  esperado destruye carteras»; «La pregunta de entrevista que desarma a los aspirantes a analistas
  cuantitativos (quants)».
- Gancho (3/4): 2-4 oraciones cortas con un ejemplo y una promesa, a menudo rematado con «Veamos por
  qué.»: «El mejor fondo de este año probablemente sea uno promedio el año que viene. El peor
  probablemente se recupere. Esta sola ley explica las dos cosas.»
- Gráfico o ilustración debajo (4/4). **Debe tener relación con el tema** (en ergodicity no la tenía).
- Títulos internos (en 16 de 27 slides): afirmación o pregunta de 2 a 8 palabras, en negrita: «Por qué
  ocurre», «Dónde se descubrió», «La respuesta es 23.», «Por qué tu cerebro falla.».

## 4. Cuerpo

- Densidad: 50 a 90 palabras por slide (4/4). Dos formas: párrafo único (fat-tails) o 2-4 párrafos
  cortos de 1-3 oraciones (ergodicity, regresion-media).
- Oraciones de 3 a 20 palabras; fragmentos permitidos («Los grandes, casi nunca.»).
- Segunda persona con voseo (4/4): «Imaginá», «Llegás en 18 minutos», «No tirás el dado una vez.».
- Recursos:
  - pregunta-respuesta (3/4): «¿Los derrumbes? Prácticamente imposibles.»; «Entonces necesitarías una
    multitud, ¿no?»;
  - tríadas (3/4): «Misma apuesta. Mismas probabilidades. Misma matemática.»; «No es un truco. No es
    una adivinanza. Es probabilidad pura.»;
  - antítesis (4/4): «Los porcentajes parecen justos. Los dólares, no.»; «Tu intuición cuenta
    personas. La matemática cuenta conexiones.»;
  - ejemplo cotidiano antes del financiero (2/4): trayecto al trabajo → fondos; cumpleaños en una fiesta → entrevistas de trading;
  - cifras concretas y redondas en cada slide ($100, 10.000 personas, 99,7 %, 18 minutos).
- Negrita: una oración clave por slide, en párrafo propio, casi siempre al final (3/4): «El resultado extremo se corrigió solo. Esto es la regresión a la media.»

## 5. Cierres

- Aforismo con antítesis (4/4): «Son los que respetan lo que la matemática no puede ver.»; «El mercado
  no te debe el valor esperado. Solo te debe el camino que efectivamente recorrés.»; «La respuesta
  correcta ante un valor atípico no es perseguirlo ni descartarlo.»
- Sin gráfico (3/4) o con ilustración y definición de diccionario (1/4). Arranque con «La lección …
  no es X…» y la oración clave en negrita (1/4).
- Matiz que evita la lectura simplista (1/4): «no implica que todo se vuelva promedio. Las diferencias
  de habilidad son reales y persistentes».

## 6. Gráficos

- Uno por slide salvo cierre y slides conceptuales (21 de 27 slides; dos paneles lado a lado en 2).
- Dos familias (4/4), más fotos de stock (1/4: fiesta, sala de trading; sin fuente ni derechos claros:
  evitarlas o usar imágenes propias):
  1. **Figuras importadas o ilustraciones**: papers, capturas, notación LaTeX (P(x), E(L), VaR, ES, σ),
     dispersión de datos reales (Galton).
  2. **Gráficos propios minimalistas** estilo matplotlib/seaborn: barras (también apiladas) con valores
     en negrita, líneas finas, ejes grises, sin recuadro superior ni derecho, diagramas de flujo simples.
- Colores semánticos (4/4; en cumpleaños, rojo = supera el umbral del 50 %): verde = ganancia o persistente, rojo = pérdida o peor resultado, naranja =
  intermedio o variable, gris = neutro o punto de partida.
- Rotulado: título corto arriba, a veces con fórmula en itálica gris («(0,5 × 1,50) + (0,5 × 0,60) =
  1,05»); anotaciones con flecha («Óptimo de Kelly, f = 25 %», «18 min»); línea punteada de referencia
  (punto de equilibrio, promedio de largo plazo, media poblacional).
- Pie: una línea chica en gris (2/3 en portadas).
- Para carruseles nuevos: gráficos desde datos o fórmulas explícitas (g(f) = 0,5·ln(1 + 0,5f) +
  0,5·ln(1 − 0,4f); caminos $100 → $150 → $90). Series reales solo con fuente y período: «S&P 500, cierre
  diario, feb-2007 a dic-2009, fuente: S&P Dow Jones Indices».

## 7. Diseño

- Formatos: Instagram 1080 × 1350 (4:5); TikTok 1080 × 1920 (9:16) con el contenido centrado
  verticalmente (texto desde ≈ 400-640 px, gráfico ≈ 1100-1600 px) y el logo abajo.
- Fondo blanco con degradado gris suave en las esquinas; todo centrado (4/4).
- Columna de texto ≈ 75-80 % del ancho (800-860 px).
- Tipografía: Inter. Título de portada Bold 80-100 px; títulos internos Bold 40-72 px; cuerpo Regular
  34 px (39-44 px en fat-tails); interlineado ≈ 1,4; destacados Bold al tamaño del cuerpo; pies 20-36 px
  gris.
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

  Lectura: fondo blanco; texto #1D1D1D; verde ≈ #42906C-#568E66 (oscuro #3D6E4B); rojo ≈ #B96257
  (intenso #AB1818-#C9443E); naranja ≈ #E4AA58-#EBA366; gris neutro ≈ #9A9A9A. Los azules de fat-tails
  vienen de la ilustración del cisne negro, no del sistema de colores.

## 8. Tono y registro

Español rioplatense formal y sobrio, como las secciones de economía de la prensa argentina, con voseo.
Tono de «lo que no te cuentan», sin lunfardo ni coloquialismos.

**Hacer**
- Cifras con formato argentino: 99,7 %; 10.000; US$ 3.600 millones; 17 de agosto de 1998.
- Montos hipotéticos con «$»; montos reales con «US$» y millones.
- Primera mención de quants: «analistas cuantitativos (quants)».
- Espacio duro antes de %; comillas “…”; guion largo estilo RAE.
- Una sola oración en negrita por slide; párrafos cortos.
- Citar la fuente de cada estadística (informe, edición, fecha).

**No hacer** (errores detectados en los carruseles analizados)
- Fechar mal: Ole Peters no «lo probó en 2020» (trabajos de 2011 y 2016; nota de Bloomberg de 2017).
- Multiplicadores no derivables: «3x / 5x más eventos extremos» no sale de una curtosis de 10 o 15.
- Porcentajes sin fuente: «la realidad dice 95 %»; «uno de los hallazgos más replicados».
- Afirmaciones deportivas o anecdóticas sin datos («el novato que más anota casi nunca lidera a su equipo
  en el tercer año»).
- Estadísticas de fondos sin informe citado («9 de cada 10 ya no están arriba»; S&P Persistence
  Scorecard: indicar edición y período). Recordar el sesgo de supervivencia.
- Gráficos ajenos al tema (funciones de onda de Monte Carlo en una portada de finanzas) o sin fuente
  (dispersión «de Galton» con pendiente 0,58 sin aclarar si es simulada).
- Absolutos falsos: «Termina en la ruina. Todas las veces.» (probabilidad 1 solo en el límite);
  «llegás a cero» (asintótico); «cualquier medición exagera la habilidad» (solo las extremas por arriba).
- Afirmar sin verificar: Ed Thorp «sin un rasguño» en 1998; «la Fed organizó un rescate de US$ 3.600
  millones» (lo pagaron 14 bancos privados); «US$ 100.000 millones en posiciones».
- Confundir conceptos: la brecha promedio-trayectoria es la **no** ergodicidad.
- Contradicciones texto-gráfico: «mil tiradas» con 300 en el gráfico; «todo 2008» con serie 2007-2009.
- Frases de autoridad sin fuente: «las mesas de trading de Wall Street la usan»; «la mayoría arriesga
  180»; qué buscan los entrevistadores.
- Mezclar probabilidad individual y acumulada: «la persona 23 falla más de la mitad de las veces» (solo
  22/365 ≈ 6 %; lo que supera el 50 % es la acumulada); tratar los 253 pares como tiradas
  independientes sin decir que es una aproximación.
- Fórmulas en texto plano con «x» y «^»: usar × y superíndices (365ⁿ), signo menos (−).

## 9. Glosario resumido

| EN | ES |
|---|---|
| fat tails | colas gruesas |
| quants | analistas cuantitativos (quants) → quants |
| bell curve / normal distribution | campana de Gauss / distribución normal |
| standard deviation | desvío estándar |
| kurtosis | curtosis |
| expected value (EV) | valor esperado |
| ergodicity | ergodicidad |
| regression to the mean / mean reversion | regresión a la media / reversión a la media |
| Kelly Criterion | criterio de Kelly |
| geometric growth rate | tasa de crecimiento geométrica |
| hedge fund | fondo de cobertura |
| Black Swan | cisne negro |
| coin flip / heads / tails | tirada de moneda / cara / ceca |
| break even | punto de equilibrio |
| crash | derrumbe (crac, si es nombre de un evento) |
| bearish | bajista |
| bailout / rescue | rescate |
| leverage | apalancamiento |
| wealth | patrimonio |
| portfolio | cartera |
| crypto | cripto |
| risk model | modelo de riesgo |
| odds | probabilidades |
| outlier | valor atípico |
| Top 25% / Bottom 25% | cuartil superior / cuartil inferior |
| tradeable strategy | estrategia de trading |
| Birthday Paradox | paradoja del cumpleaños |
| unique pairs / (birthday) match | pares distintos / coincidencia |
| trading desk | mesa de trading |
| "Past performance doesn't guarantee future results" | “Rendimientos pasados no garantizan rendimientos futuros” |

Glosario completo: `memoria/GLOSARIO.md`.

## 10. Carruseles de referencia (resumen en español)

**fat-tails — «Colas gruesas: cómo los quants ganan con lo imposible»** (Instagram)
1. Portada + densidades de cola gruesa vs. normal. 2. «La matemática te miente»: las frases
tranquilizadoras se apoyan en un modelo equivocado (campana ±1σ, ±2σ, ±3σ). 3. Los modelos suponen la
normal; 2008 «debía» ocurrir una vez en la vida del universo (S&P 500 2007-2009). 4. «COLAS GRUESAS»:
99,7 % según la campana vs. ~95 % (VaR y ES). 5. Curtosis: 3 / ~10 / 15+ (barras). 6. LTCM: dos Nobel,
rescate de US$ 3.600 millones (cronología). 7. Ed Thorp: «Son los que respetan lo que la matemática no
puede ver» + cisne negro.

**ergodicity — «Ergodicidad: por qué el valor esperado destruye carteras»** (Instagram)
1. Portada + gancho. 2. Moneda +50 % / −40 %: **«La matemática parece infalible.»** 3. 10.000 personas
vs. 1: **«Termina en la ruina.»** 4. $100 → $150 → $90: **«Los porcentajes parecen justos. Los dólares,
no.»** 5. El orden no importa: **«Siempre terminás más pobre.»** 6. Kelly maximiza la tasa geométrica;
g(f) con óptimo en 25 %. 7. **«Es que no vivís mil vidas al mismo tiempo.»**

**regresion-media — «Regresión a la media: la ley que devuelve cada extremo a la normalidad»** (TikTok)
1. Portada + gancho de fondos (dos campanas: media y extremo). 2. El trayecto de 18 minutos: **«El
resultado extremo se corrigió solo.»** (serie de 30 días). 3. Componente persistente + variable:
**«Cuanto más extremo el resultado, más fuerte la corrección.»** (barras apiladas 60 → 40). 4. NBA y
fondos del cuartil superior (flujo 10 / 25 / 30 / 35 %). 5. Regresión ≠ reversión a la media: **«Confundirlas
es uno de los errores más caros en finanzas.»** 6. Galton, 1886: alturas de padres e hijos (dispersión).
7. **«Es esperar que el próximo resultado sea menos extremo.»**

**cumpleaños — «La paradoja del cumpleaños: la pregunta de entrevista que desarma a los aspirantes a
quants»** (TikTok, 6 slides)
1. Portada + gancho de entrevistas de Wall Street (superficie 3D). 2. ¿Cuántas personas hacen falta?
Las respuestas intuitivas (180, 100, 50): **«Todos están muy lejos.»** (foto). 3. «La respuesta es 23»:
50,7 % con 23 y 99,9 % con 70 (barras con línea del 50 %). 4. No es tu cumpleaños, son los 253 pares:
**«Pero la pregunta no es sobre vos. Es sobre cualquier par.»** (diagrama circular). 5. La fórmula
1 − 365! / ((365 − n)! × 365ⁿ) (foto de sala de trading). 6. **«Es que los humanos razonan de forma
lineal ante problemas combinatorios.»**
