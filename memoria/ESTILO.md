# Guía de estilo — carruseles de finanzas cuantitativas (ES-AR)

Consolidada a partir de 2 carruseles de referencia (fat-tails, ergodicity). Evidencia indicada como
«n/2». Se reescribe completa en cada actualización (comando `/estilo`), no se agrega al final.

## 1. Instrucciones para el modelo que lea esta guía

> Con esta guía, generá un carrusel de 7 slides sobre el tema indicado, en español rioplatense formal con
> voseo. Para cada slide entregá: función narrativa, título (si corresponde), texto con la oración
> destacada en **negrita**, especificación del gráfico (tipo, datos exactos o fórmula, ejes, unidades,
> período, fuente con fecha) y pie de gráfico. Usá solo datos reales y verificables con fuente; si no
> podés verificar un dato, marcalo [DATO A VERIFICAR]. Nunca inventes cifras, fechas ni citas. Preferí
> gráficos que se puedan generar a partir de datos o fórmulas explícitas.

## 2. Estructura narrativa (7 slides)

| Slide | Función | fat-tails | ergodicity |
|---|---|---|---|
| 1 | Portada: concepto + promesa | «Colas gruesas» + «Cómo los quants ganan con lo imposible» | «Ergodicidad» + «Por qué el valor esperado destruye carteras» + gancho de 4 oraciones |
| 2 | Romper una creencia | «La matemática te miente» (advertencias legales) | Experimento mental: moneda +50 % / −40 % |
| 3 | Mecanismo o paradoja | Modelo normal y crisis de 2008 | 10.000 personas vs. 1 persona |
| 4 | Nombrar o desarmar el concepto | «Esto es lo que los quants llaman: COLAS GRUESAS» | Paso a paso con $100 |
| 5 | Profundizar / medir | Curtosis como «detector de mentiras» | El orden no importa: siempre se pierde |
| 6 | Caso o solución | LTCM, 1998 | Criterio de Kelly + historia (1956, Ole Peters) |
| 7 | Cierre | Figura ejemplar (Ed Thorp) + moraleja + definición de «cisne negro» | Aforismo sin gráfico |

Patrones (2/2): el concepto aparece nombrado en la portada, se explica sin jerga entre las slides 2 y 5,
y la 6 aterriza en un caso histórico o una solución práctica. La 7 cierra con una lección de vida en
antítesis. Variante: el concepto se nombra recién en la slide 4 con un remate en mayúsculas
(«COLAS GRUESAS»; 1/2) o se define en una oración en negrita al final de la 6 (1/2).

## 3. Portadas y títulos

- Título: el concepto en una o dos palabras, muy grande, en negrita (2/2): «Colas gruesas»,
  «Ergodicidad».
- Subtítulo con promesa o paradoja, de 5 a 9 palabras (2/2): «Cómo los analistas cuantitativos (quants)
  ganan con lo imposible»; «Por qué el valor esperado destruye carteras».
- Gancho opcional (1/2): tríada de oraciones cortas + invitación: «Los físicos lo resolvieron hace
  décadas. Los fondos de cobertura lo usan para dimensionar cada apuesta. La economía todavía se
  equivoca. Veamos por qué importa.»
- Gráfico de aspecto académico debajo, con pie chico (2/2). **Debe tener relación con el tema** (en
  ergodicity no la tenía: ver §8).
- Títulos internos (4/14 slides): pregunta o afirmación de 4 a 7 palabras, en negrita: «La matemática
  te miente», «Entonces, ¿qué está pasando en realidad?», «Por esto funciona el criterio de Kelly».

## 4. Cuerpo

- Densidad: 50 a 90 palabras por slide (fat-tails: un párrafo único de 60-85; ergodicity: 3-4 párrafos
  cortos de 1-3 oraciones) (2/2).
- Oraciones de 3 a 15 palabras; fragmentos permitidos («Los grandes, casi nunca.») (2/2).
- Segunda persona con voseo: «Imaginá», «tenés», «perdés», «Pensá en…» (2/2).
- Recursos (2/2):
  - pregunta-respuesta: «¿Los derrumbes? Prácticamente imposibles.», «¿El S&P 500? Alrededor de 10.»;
  - tríadas: «Misma apuesta. Mismas probabilidades. Misma matemática.»;
  - antítesis: «Los porcentajes parecen justos. Los dólares, no.»;
  - guion largo para el giro final: «Los modelos eran impecables —la realidad simplemente no cooperó.»;
  - cifras concretas y redondas en cada slide ($100, 10.000 personas, 99,7 %, US$ 3.600 millones).
- Negrita: una oración clave por slide, en párrafo propio (ergodicity 6/7 slides; fat-tails la reemplaza
  por títulos) — es la frase que resume la slide: «La matemática parece infalible.»,
  «Termina en la ruina. Todas las veces.».

## 5. Cierres

- Aforismo con antítesis (2/2): «Los quants que sobreviven décadas no son los que tienen la matemática
  más sofisticada. Son los que respetan lo que la matemática no puede ver.»; «El mercado no te debe el
  valor esperado. Solo te debe el camino que efectivamente recorrés.»
- Puede ir sin gráfico (1/2) o con una ilustración y una definición de diccionario (1/2).
- Abre con una frase en suspenso («Lo que nos enseña la ergodicidad no es matemático…») y sigue con la
  revelación en negrita (1/2).

## 6. Gráficos

- Uno por slide, salvo el cierre (13/14 slides con gráfico; dos paneles lado a lado en 2 de ellas).
- Dos familias (2/2):
  1. **Figuras importadas**: papers, capturas, notación LaTeX (P(x), E(L), VaR, ES, σ), ilustraciones.
     Se usan en portadas y slides conceptuales.
  2. **Gráficos propios minimalistas** estilo matplotlib/seaborn: barras con valores en negrita sobre
     o dentro de la barra, líneas finas, ejes grises, sin recuadro superior ni derecho.
- Colores semánticos (2/2): verde = ganancia, rojo = pérdida, gris = neutro o punto de partida;
  naranja y rojo intenso para escalar intensidad (curtosis 10 → 15+).
- Rotulado: título del gráfico corto arriba (a veces con fórmula en itálica gris: «(0,5 × 1,50) +
  (0,5 × 0,60) = 1,05»), anotaciones con flecha para los puntos clave («Óptimo de Kelly, f = 25 %»),
  línea punteada de referencia (punto de equilibrio en $100).
- Pie: una línea chica en gris centrada debajo (2/2 en portadas).
- Preferencia para carruseles nuevos: gráficos generados desde datos o fórmulas explícitas (ej.: g(f) =
  0,5·ln(1 + 0,5f) + 0,5·ln(1 − 0,4f); caminos $100 → $150 → $90). Series reales (S&P 500) solo con
  fuente y período: «S&P 500, cierre diario, feb-2007 a dic-2009, fuente: S&P Dow Jones Indices».

## 7. Diseño

- Formato 1080 × 1350 (4:5). Fondo blanco o gris muy claro con degradado suave; todo centrado (2/2).
- Columna de texto ≈ 75-80 % del ancho (810-860 px); márgenes laterales ≈ 110-130 px.
- Tipografía: Inter. Título de portada ExtraBold/Bold 90-100 px; títulos internos Bold 40-72 px;
  cuerpo Regular 34 px (ergodicity) a 39-44 px (fat-tails); interlineado ≈ 1,4; destacados Bold al mismo
  tamaño que el cuerpo; pies Regular 22-36 px gris.
- Ubicación: texto arriba (empieza a 60-180 px del borde), gráfico abajo ocupando ≈ 35-45 % del alto,
  pie debajo del gráfico. Separación texto-gráfico ≥ 60 px.
- Paleta (extraída automáticamente con k-means de las slides; el texto es el cluster más oscuro):

<!-- PALETA:INICIO (generado por python -m carrusel memoria) -->

| Carrusel | Fondo | Texto | Acentos (proporción entre píxeles saturados) |
|---|---|---|---|
| fat-tails | #FEFEFE | #070707 | #E4AA58 (32%), #C9443E (31%), #73A3D7 (14%), #627D9C (10%), #4E5D8C (7%), #561F56 (7%) |
| ergodicity | #FEFEFE | #1D1D1D | #568E66 (41%), #B96257 (34%), #3D6E4B (12%), #8B4E47 (9%) |

<!-- PALETA:FIN -->

  Lectura: fondo #FEFEFE; texto #070707-#1D1D1D; verde ganancia ≈ #568E66 (oscuro #3D6E4B); rojo pérdida
  ≈ #B96257; naranja ≈ #E4AA58; rojo intenso ≈ #C9443E; gris neutro ≈ #9A9A9A. Los azules de fat-tails
  vienen de la ilustración del cisne negro, no del sistema de colores.

## 8. Tono y registro

Español rioplatense formal y sobrio, como las secciones de economía de la prensa argentina, con voseo
porque el original interpela al lector todo el tiempo. Tono de «lo que no te cuentan», sin lunfardo ni
coloquialismos («quedás 5 arriba» sí; «la timba» no).

**Hacer**
- Cifras con formato argentino: 99,7 %; 10.000; US$ 3.600 millones; 17 de agosto de 1998.
- Montos hipotéticos con «$» ($100); montos reales con «US$» y millones.
- Primera mención de quants: «analistas cuantitativos (quants)».
- Separar el número del % con espacio duro; comillas “…”; guion largo estilo RAE.
- Una sola oración en negrita por slide; párrafos cortos.

**No hacer** (errores detectados en la referencia; no repetirlos)
- Fechar mal los hitos: Ole Peters no «lo probó en 2020»; sus trabajos son de 2011 y 2016 (con
  Gell-Mann) y la nota de Bloomberg es de 2017.
- Atribuir multiplicadores no derivables: «3x / 5x más eventos extremos» no se deduce de una curtosis de
  10 o 15, que además depende del período y la frecuencia. Aclarar si es curtosis o exceso de curtosis.
- Dar porcentajes sin fuente: «la realidad dice 95 %».
- Usar un gráfico ajeno al tema (funciones de onda de Monte Carlo por difusión en una portada de finanzas).
- Absolutos falsos: «Termina en la ruina. Todas las veces.» es un resultado con probabilidad 1 en el
  límite, no en cada caso finito. «Llegás a cero» es asintótico.
- Afirmar sin verificar: «Ed Thorp atravesó 1998 sin un rasguño» (en 1998 gestionaba Ridgeline Partners;
  Princeton Newport cerró en 1988-1989); «la Reserva Federal organizó un rescate de US$ 3.600 millones»
  (lo coordinó la Fed de Nueva York, lo pagaron 14 bancos privados); «US$ 100.000 millones en
  posiciones» (≈ US$ 125.000 millones en activos y > US$ 1 billón de nocional).
- Confundir conceptos: la brecha entre promedio y trayectoria es la **no** ergodicidad.
- Contradicciones texto-gráfico: «mil tiradas» con un gráfico de 300; «todo 2008» con una serie
  2007-2009.
- Hipérboles atribuidas a «el modelo» («una vez en la vida del universo»): si se usan, citar la fuente
  (David Viniar, Goldman Sachs, agosto de 2007, «25 desvíos estándar»).

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
| Kelly Criterion | criterio de Kelly |
| geometric growth rate | tasa de crecimiento geométrica |
| hedge fund | fondo de cobertura |
| Black Swan | cisne negro |
| coin flip / heads / tails | tirada de moneda / cara / ceca |
| flips | tiradas |
| break even | punto de equilibrio |
| crash | derrumbe (crac, si es nombre de un evento) |
| bearish | bajista |
| bailout / rescue | rescate |
| leverage | apalancamiento |
| default on bonds | entrar en default de sus bonos |
| wealth | patrimonio |
| portfolio | cartera |
| crypto | cripto |
| risk model | modelo de riesgo |
| disclaimers | advertencias legales |
| odds | probabilidades |
| go broke | terminar en la ruina |
| All-In | apostar todo |
| Federal Reserve | Reserva Federal |
| "Past performance doesn't guarantee future results" | “Rendimientos pasados no garantizan rendimientos futuros” |

Glosario completo: `memoria/GLOSARIO.md`.

## 10. Carruseles de referencia (resumen en español)

**fat-tails — «Colas gruesas: cómo los quants ganan con lo imposible»**
1. Portada: «Colas gruesas» / «Cómo los analistas cuantitativos (quants) ganan con lo imposible».
   Gráfico: densidades de cola gruesa vs. normal (figura importada).
2. «La matemática te miente» + cita «Rendimientos pasados…». Te dijeron que los derrumbes son raros y
   que todo sube a largo plazo; esas frases se apoyan en un modelo equivocado. Gráfico: campana con ±1σ,
   ±2σ, ±3σ (68,3 / 95,4 / 99,7 %).
3. Los modelos de riesgo suponen una distribución normal; en 2008 el derrumbe «debía» ocurrir una vez
   en la vida del universo. «Tus padres lo recuerdan.» Gráfico: S&P 500 2007-2009.
4. «Esto es lo que los quants llaman: COLAS GRUESAS». Los extremos ocurren más de lo que dice la
   matemática: 99,7 % según la campana vs. ~95 % en la realidad. Gráfico: VaR y ES sobre una densidad de
   pérdidas.
5. La curtosis mide cuánto te engaña la campana: 3 en la normal, ~10 en el S&P 500, 15+ en cripto.
   «Un detector de mentiras para tu modelo de riesgo.» Gráfico: barras gris/naranja/rojo.
6. LTCM: dos premios Nobel, US$ 100.000 millones en posiciones, rescate de US$ 3.600 millones en 1998.
   «Los modelos eran impecables —la realidad simplemente no cooperó.» Gráfico: cronología 1994-1999.
7. Ed Thorp usó el criterio de Kelly y nunca confió en la campana. Cierre: «Son los que respetan lo que
   la matemática no puede ver.» Ilustración + definición de «cisne negro».

**ergodicity — «Ergodicidad: por qué el valor esperado destruye carteras»**
1. Portada: «Ergodicidad» / «Por qué el valor esperado destruye carteras» + gancho. Gráfico importado
   (no relacionado).
2. Moneda: cara +50 %, ceca −40 %; el promedio da +5 % por tirada. **«La matemática parece
   infalible.»** Gráfico: barras +50 / −40 / +5 % con la fórmula 0,5 × 1,50 + 0,5 × 0,60 = 1,05.
3. Con 10.000 personas el promedio se dispara; una persona que tira mil veces **termina en la ruina**.
   «El valor esperado era real. Simplemente no era el tuyo.» Gráfico: dos paneles en escala log.
4. «Entonces, ¿qué está pasando en realidad?» $100 → $150 → $90. **«Los porcentajes parecen justos.
   Los dólares, no.»** Gráfico: barras $100 / $150 / $90 con punto de equilibrio.
5. Invertir el orden da lo mismo: $100 → $60 → $90. **«Siempre terminás más pobre.»** «No es mala
   suerte. Es matemática.» Gráfico: ambos caminos = $90; alternar 30 veces = ruina.
6. «Por esto funciona el criterio de Kelly»: maximiza la tasa de crecimiento geométrica (Kelly, 1956;
   Ole Peters). **Definición de ergodicidad en negrita.** Gráfico: g(f) con óptimo en f = 25 % y
   g(1) ≈ −0,053.
7. Cierre sin gráfico: **«Es que no vivís mil vidas al mismo tiempo.»** «El mercado no te debe el valor
   esperado. Solo te debe el camino que efectivamente recorrés.»
