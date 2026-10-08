# Registro de decisiones (modo autónomo)

Fecha: 2026-10-07. Una línea de justificación por decisión.

## Entorno y dependencias

- **Python 3.13 en `.venv`** (el .md pide 3.11+): es la versión disponible; todo corre sin cambios.
- **PDF → imágenes: imagen nativa embebida (PyMuPDF)** en lugar de rasterizar a 200-300 dpi: cada
  página del PDF contiene exactamente una captura (1206 px de ancho); extraerla evita re-muestrear.
  Plan B implementado: rasterizado PyMuPDF a 220 dpi; plan C: `pdftoppm`.
- **OCR: Tesseract 5.3.4** (plan B del .md). EasyOCR (primario en Linux) se probó sobre 2 slides
  (fat-tails 03 y ergodicity 06): confunde «.» con «:» («constantly:», «formally:»), parte las líneas
  y tarda 8-18 s por slide; Tesseract transcribió el cuerpo sin errores en 0,7 s. Para etiquetas chicas
  de gráficos se usa una segunda pasada de Tesseract en modo disperso (psm 11) con ampliación ×2.
  EasyOCR queda instalado como alternativa (`config.yaml → ocr.motores`).
- **Tipografía: Inter 4.1** descargada del repo `rsms/inter` (licencia OFL, en `fuentes/`).
  **Liberation Serif** (OFL) para rótulos de figuras académicas en estilo Times/LaTeX («Pérdida»,
  «5 % de probabilidad»), para que no desentonen con el resto de la figura.

## Preparación de las slides

- **No hay barra gris uniforme**: las capturas tienen un degradado gris arriba con una flecha «<»
  blanca y sombras suaves en las esquinas. Se resolvió con un **aplanado de iluminación del fondo**
  (campo de fondo por celdas de 40 px, inpainting de celdas con contenido, división) y una limpieza de
  la franja superior (9 % del ancho), en vez de buscar una barra.
- **El borde de la slide no es visible** (blanco sobre blanco): se toma una ventana 4:5 de ancho
  completo **centrada en el contenido** y se lleva a 1080 × 1350 con Lanczos (1206 × 1508 → 1080 × 1350,
  reducción; no hubo escalado hacia arriba).
- **Contador «7 / 7»**: solo aparece en la página 3; se detecta como píldora de gris medio rellena (para
  no confundirla con bordes de texto) y se borra con el color de fondo.

## Orden (verificado mirando las 14 páginas)

- **fat-tails: 2 → 7 → 6 → 1 → 8 → 4 → 3** (por defecto, confirmado): portada en p2; p3 tiene el contador
  «7 / 7» y es el cierre con Ed Thorp; el argumento progresa mito → modelo → concepto → medida → caso.
- **ergodicity: 5 → 9 → 10 → 11 → 12 → 13 → 14** (por defecto, confirmado): portada en p5; la secuencia
  moneda → paradoja → paso a paso → orden invertido → Kelly → aforismo es continua.

## Maquetación

- **Tamaños medidos por ancho**, no por alto de caja: el tamaño que reproduce el ancho real de cada
  línea OCR con Inter (mediana). Calibrado re-renderizando el inglés sobre el original (coincidencia
  línea por línea). Resultado: cuerpo 34 px (ergodicity) y 38-44 px (fat-tails), interlineado ≈ 1,4.
- **Negrita por grosor de trazo** (área/perímetro de la tinta, normalizado por em): Regular ≈ 0,085 em,
  Bold ≈ 0,115 em; umbral 0,103.
- **Columna** = la línea más ancha del original (78-80 % de la slide), con tope de 80 %.
- **Orden de ajuste si el español no entra** (según el .md): reducir hasta 90 % → extender hacia arriba
  → usar todo el aire hasta 24 px del gráfico → recién ahí, acortar. No hizo falta acortar ningún
  texto; fat-tails 02-04 quedaron al 90 %.
- **Balanceo de líneas** en citas, subtítulos y pies (sin palabras huérfanas) y control de viudas en
  párrafos largos.
- **Vertical**: si el español entra en el alto original, se centra en ese alto; si no, crece hacia abajo.
- **`NN_limpia.png`** = slide sin ningún texto de la zona de texto ni pies, con el gráfico en su
  versión en español (A/B/C traducido), para usar de fondo en Canva.

## Estrategia por gráfico

| Slide | Estrategia | Justificación |
|---|---|---|
| fat-tails 01 | C | Densidades con notación P(x), x; el pie se recompone en español. |
| fat-tails 02 | C | Campana con σ y % sobre relleno con textura; solo el rótulo del eje (fondo liso). |
| fat-tails 03 | A | Serie real del S&P 500 (no se reconstruye); título, eje Y y ticks de miles reescritos. |
| fat-tails 04 | C | Figura académica (E(L), VaR, ES); «Loss» y «5% probability» traducidos. |
| fat-tails 05 | B | Valores dados (3, ~10, 15+). |
| fat-tails 06 | D | Línea de tiempo de LTCM con mucho texto chico: traducción completa en `textos_es.md`. |
| fat-tails 07 | C | Ilustración; la definición de «cisne negro» está sobre fondo liso y se traduce. |
| ergodicity 01 | C | Figura de física; solo «Relative probability» y el pie. |
| ergodicity 02 | B | +50 % / −40 % / +5 % y fórmula exacta. |
| ergodicity 03 | B | Simulación con semilla fija 42 (regenerado, no idéntico). |
| ergodicity 04 | B | $100 → $150 → $90, pérdida $60. |
| ergodicity 05 | B | Caminos exactos y serie alternada de 30 tiradas. |
| ergodicity 06 | B | g(f) = 0,5·ln(1 + 0,5f) + 0,5·ln(1 − 0,4f); óptimo 0,25; g(1) = −0,0527. |

- Gráficos regenerados con **Inter** (no DejaVu como el original) para que combinen con el texto.
- «5 % de probabilidad» pisa la curva y la línea de ES: se borró solo la tinta del rótulo (inpainting)
  y se reescribió con halo blanco de 3 px.

## Traducción

- **Comillas tipográficas “…”** y **guion largo estilo RAE** («normal —una campana de Gauss—.»).
  Excepción: en Ed Thorp se conservó el guion separado («de la historia — atravesó 1998») porque el
  original lo usa como pausa entre sujeto y verbo.
- **«The Math Is Lying to You» → «La matemática te miente»** (y no «te está mintiendo»): la versión
  larga no entraba en una línea a 72 px.
- **Primera mención de quants** en la portada de fat-tails: «analistas cuantitativos (quants)».
- **«Crypto?» → «¿Cripto?»** (glosario); **«They go broke» → «Termina en la ruina»** (formal, sin
  «se funde»); **«zoom out» → «mirar el largo plazo»**; **«Here's why it matters» → «Veamos por qué
  importa»**; **«Portfolios» → «carteras»** (uso de la prensa económica argentina).
- **Signo menos tipográfico (−)** en gráficos regenerados y rótulos («−40 %»).
- Términos nuevos agregados al glosario (38 en total; ver `memoria/GLOSARIO.md`), con la forma usual en
  la prensa económica argentina: advertencias legales, modelo de riesgo, Reserva Federal, capital
  propio, fondos de rescate, liquida sus posiciones, cronología, carteras, dimensionar cada apuesta,
  probabilidades (odds), terminar en la ruina, apostar todo (All-In), óptimo de Kelly, Monte Carlo por
  difusión, funciones de onda del estado fundamental, entre otros.

## Memoria y versionado

- **Copia del plan curado** en `memoria/historial/AAAA-MM-DD_<slug>.plan.json`, porque `trabajo/` no se
  versiona y el plan es lo que permite re-renderizar sin repetir el criterio.
- **Script de curación** de la referencia en `scripts/curar_referencia.py` (reproducible).
- **Paleta**: k-means (numpy, k = 8) sobre píxeles de contenido + k-means de acentos (píxeles
  saturados); se guarda en `memoria/paletas.json` y se inserta automáticamente en `ESTILO.md`.
- **Git**: el repositorio ya existía; se commitea en la rama de trabajo asignada
  (`claude/festive-gauss-40z28x`) en lugar de hacer `git init`. El PDF de entrada no se versiona
  (`entrada/` en `.gitignore`).

## TikTok y marca (2026-10-08)

- **Descarga de TikTok**: yt-dlp (2026.08.19) no soporta las URLs `/photo/` («Unsupported URL») y
  TikTok no incluye el detalle en el HTML de `/photo/`. Pidiendo la misma publicación como `/video/`,
  el JSON embebido (`__UNIVERSAL_DATA_FOR_REHYDRATION__` → `imagePost.images[].imageURL.urlList`) trae
  las imágenes originales (1080 × 1920). Ese es el método principal; yt-dlp queda como plan B.
- **Formato**: las imágenes descargadas son originales (sin UI de la app), así que no se recortan ni
  se aplanan, y se **conserva su formato nativo** (9:16) en vez de forzar 1080 × 1350, que obligaría a
  recortar o deformar. Mismo criterio para PNG 4:5 sueltos.
- **Borrado de texto local**: el fondo de cada caja borrada sale de las columnas vecinas, no de los
  bordes de la slide: las imágenes de TikTok tienen degradados de diseño en las esquinas que dejaban un
  rectángulo gris. Para rótulos sobre cajas de color, borrado con el color dominante de la caja.
- **regresion-media, estrategias**: portada C (ilustración, 3 rótulos); 02 A (serie ilustrativa de 30
  días); 03 A (barras apiladas: la partición persistente/variable no está en el texto, no se regenera);
  04 A (flujo con rótulos blancos sobre cajas de color); 06 C (dispersión de Galton, datos reales);
  05 y 07 sin gráfico. «Top 25 %» → «cuartil superior»; «tradeable strategy» → «estrategia de trading».
- **Logo «PE»**: monograma geométrico con el lenguaje de la marca de agua original (trazo grueso,
  panza en anillo, terminaciones diagonales). Se probaron variantes con asta compartida y se descartaron
  porque se leían «AE»/«FE». Color #111111. Se define como geometría y se exporta a SVG y PNG.
- **Aplicación del logo**: si hay marca de agua (componente oscuro, compacto y aislado, centrado en el
  12 % inferior) se reemplaza al mismo alto y lugar; si no, se agrega abajo al centro (alto 7 % del
  ancho) o en una esquina, solo sobre fondo libre y fuera de las zonas de gráfico. Si no hay lugar, se
  avisa en `revisar.md` (pasó en fat-tails 06, la línea de tiempo).

## Instalación automática y entrega (2026-10-08)

- **Hook de inicio** (`.claude/settings.json` → `.claude/hooks/session-start.sh` → `scripts/instalar.sh`),
  sincrónico y para sesión local y web: crea `.venv`, instala `requirements.txt` solo si cambió (sello
  SHA-256) y Tesseract con Homebrew o apt-get (sin pedir contraseña; si no puede, avisa). Desde cero
  tarda ≈ 25 s; las siguientes veces, ≈ 0,5 s.
- **Permisos preaprobados** para los comandos del traductor (`.venv/bin/python -m carrusel …`, scripts,
  tests y lectura/escritura de `trabajo/`), para no pedir confirmación en cada paso.
- **Carpeta de entrega** `listos/<slug>/`: solo las slides finales (01.png …), `revisar.md`,
  `textos_es.md` y `fuente.txt` (link y autor). No se versiona.
- **De a un carrusel por vez** (pedido del usuario): se descartó el procesamiento en paralelo; si se
  pegan varios links, se traducen uno detrás de otro, cada uno completo antes del siguiente.
- `descargar` acepta varios links (`SLUG …` / `ERROR …` por línea) y borra la carpeta si la descarga falla.

## tiktok-quantgent-308355 — «The Birthday Paradox» (2026-10-08)

- **Orden**: el de la publicación (1 → 6); es obvio (portada, pregunta, respuesta, mecanismo, fórmula,
  cierre). El carrusel tiene **6 slides**, no 7: se traduce tal cual y se anota como variante en `ESTILO.md`.
- **Estrategias**: 01 C (superficie 3D sin datos explícitos; se traducen los dos rótulos de ejes rotados
  y se conservan los ticks); 02 y 05 C (fotos sin texto); 03 **B** (barras: los valores salen exactos de
  la fórmula de la slide 5 y coinciden a un decimal con el original); 04 A (diagrama con dos rótulos).
- **Nuevo tipo de gráfico** `barras_umbral` en `carrusel/graficos.py` (barras de porcentajes con línea de
  referencia y valores coloreados según el umbral); los valores se calculan en
  `scripts/curar_cumpleanos.py` con la fórmula exacta.
- **«Expected 50%» → «Esperado: 50 %»**, reubicado arriba de la línea a la izquierda: en el original
  pisaba la barra de 70.
- **Fórmula**: «P(match)» → «P(coincidencia)»; × en lugar de «x», − en lugar de «-» y superíndice ⁿ en
  lugar de «^n»; a 37 px y columna de 920 px para que entre en una línea, como en el original.
- **Términos**: «Birthday Paradox» → «paradoja del cumpleaños» (nombre establecido en español);
  «trading desks» → «mesas de trading»; «unique pairs» → «pares distintos»; «match» → «coincidencia»;
  «Quant Candidates» → «aspirantes a analistas cuantitativos (quants)» (primera mención, según el
  glosario); «You» (rótulo) → «Vos» (voseo); «Here's why» → «Veamos por qué» (como en fat-tails);
  «gut» → «intuición»; «override it» → «imponerse a él».
- **Control de calidad**: la caja de borrado de «People in room» tocaba el tick «40» (inpaint lo
  borroneaba); se ajustó la caja para excluirlo. Script de curación: `scripts/curar_cumpleanos.py`.

## tiktok-quantgent-138326 — «Black-Scholes» (2026-10-08)

- **8 slides** en el orden de la publicación (portada → supuesto y fórmula → cuándo funciona → dónde
  falla → volatilidad implícita → Heston → difusión con saltos → cierre).
- **Estrategias**: 01 C (superficie 3D, solo notación); 02 A (fórmula conservada; columna de siete
  aclaraciones reescrita); 03 A (serie real del S&P 500: nunca se reconstruye; dos rótulos en serif);
  04 C (superficie de volatilidad implícita; título y ejes traducidos en serif, «Moneyness» sin
  traducir); 05 C (rótulo «Tim to Maturity» traducido); 06 A (ficha de Heston: título, rótulo y viñetas
  sobre fondo gris liso); 07 A (título de la simulación de Merton); 08 sin gráfico.
- **Nuevo modo de borrado `plano`** (`carrusel/render.py`): para texto sobre cajas de color liso, se
  rellena la caja con el color del borde. El inpainting arrastraba el halo claro del JPEG y dejaba
  manchas blancas en la ficha de Heston.
- **Utilidades compartidas** de curación en `scripts/curar_tiktok.py` (`et`, `tam_para`, `pad`,
  `con_caja`, `ejecutar`): el tamaño de cada rótulo se calcula para reproducir el ancho medido del
  original y se reduce si el español no entra.
- **Términos**: «random walk» → «paseo aleatorio» (uso consagrado por la traducción de Malkiel);
  «gold standard» → «estándar de referencia»; «Greeks» → «griegas»; «strike» → «precio de ejercicio»;
  «smile» → «sonrisa de volatilidad»; «flash crashes» → «derrumbes relámpago (flash crashes)»;
  «Bottom line» → «En síntesis»; «moneyness» se deja en inglés (sin equivalente asentado).
- Se agregó el punto final que falta en la slide 6 del original.

## tiktok-quantgent-241750 — «The Kelly Criterion» (2026-10-08)

- **7 slides** en el orden de la publicación. Títulos internos en peso regular, como el original (no
  hay negritas en este carrusel).
- **Estrategias**: 01 C (superficie 3D, solo notación); 02 A (diagrama «conservador → suicida»); 03 C
  (retrato de Kelly; el pie es un nombre propio); 04 A (curvas teórica y real según apalancamiento; seis
  rótulos); 05 A (curva g(f); rótulos en itálica serif); 06 C (foto); 07 sin gráfico. Ninguna curva se
  regenera: el texto no da los parámetros.
- **Fuente nueva**: `fuentes/LiberationSerif-Italic.ttf` (OFL, misma familia ya incluida) para los
  rótulos en itálica serif de la slide 5.
- **Leyendas sobre fondo liso** (slide 4): borrado `plano`; el borrado por defecto estiraba la línea de
  la leyenda sobre el texto nuevo.
- **Términos**: «odds you're getting» → «cuota que te pagan» (b es la cuota neta, no una probabilidad);
  «bankroll» → «capital»; «edge» → «ventaja»; «fractional Kelly» → «Kelly fraccional»; «wipes you out» →
  «te deja fuera de juego»; «leave money on the table» → «dejar dinero sobre la mesa» («plata» se evita
  por registro); «Insane» → «Insensato»; «1960s» → «la década de 1960».
- Las rayas que en inglés introducen una conclusión («about — HOW MUCH», «isn't the formula — it's the
  mindset») se pasan a dos puntos, que es la puntuación natural en español; las de inciso se mantienen.

## tiktok-quantgent-735830 — «Fat Tails», versión de TikTok (2026-10-08)

- Es **el mismo carrusel que la referencia `fat-tails`** (Instagram, 4:5), publicado en 9:16. Se
  reutilizan textos, traducciones, estrategias (C, C, A, C, B, D, C) y alertas de
  `scripts/curar_referencia.py`; solo se remidieron las cajas (`scripts/curar_fat_tails_tiktok.py`).
  En la memoria se marca con `version_de: fat-tails` para **no contarlo dos veces** como evidencia en
  `ESTILO.md`.
- Slide 7: el borrador no detectó la zona de texto (la tomó como gráfico); los bloques se escribieron a
  mano con medidas tomadas de la imagen.
- Corrección de puntuación respecto de la referencia: «…más exitosos de la historia — atravesó 1998…»
  llevaba una raya entre sujeto y verbo, que en español no corresponde; se quitó.
- Curtosis (B): el gráfico se ensanchó a 880 px porque a 730 px los subtítulos se pisaban.

## tiktok-quantgent-437398 — «Bayes' Theorem» (2026-10-08)

- **7 slides** en el orden de la publicación. Estrategias: 01 C (imagen decorativa); 02 C (foto);
  03 A (dos barras 99 % / ~9 %: la prevalencia no está en el texto, así que no se regenera); 04 C
  (grabado con pie «Thomas Bayes»); 05 A (curvas a priori / verosimilitud / a posteriori); 06 C (foto);
  07 sin gráfico. Slide 6: el borrador no detectó la zona de texto; bloques escritos a mano.
- **Alerta principal**: el carrusel omite la tasa base. «Menos del 10 %» solo vale con una prevalencia
  de ≈ 1 en 1.000 (con 1 %, da 50 %). Va en `revisar.md` de las slides 2 y 3 con la sugerencia para Canva.
- **Términos**: «test» → «prueba (médica)»; «You test positive» → «Te da positivo»; «Prior / Likelihood /
  Posterior» → «A priori / Verosimilitud / A posteriori» (terminología estadística en español);
  «Bayesian thinkers» → «quienes piensan de forma bayesiana»; «2012 US election» → «la elección
  presidencial de 2012 en EE. UU.».

## tiktok-quantgent-262422 — «Benford's Law» (2026-10-08)

- **8 slides** en el orden de la publicación. Estrategias: 01 C (superficie 3D decorativa); 02, 06, 07 C
  (fotos); 04 **B** (barras con P(d) = log₁₀(1 + 1/d), exactas; rótulo del 11,1 % a la derecha, como en el
  original); 05 C (retrato de Simon Newcomb); 03 y 08 sin gráfico. Slide 7: bloques escritos a mano.
- `barras_umbral` admite ahora el lado del rótulo de la línea, el tamaño y la negrita de los ticks, y
  pone un fondo detrás de cada valor para que la línea punteada no lo tache (se re-renderizó también la
  paradoja del cumpleaños).
- **Términos**: «IRS» → «IRS (el fisco de EE. UU.)» en la primera mención; «tax returns» → «declaraciones
  juradas»; «forensic accountants» → «contadores forenses»; «red flag» → «señal de alerta»; «decay» →
  «deterioro»; «They're wrong» → «Se equivocan.» (se agregó el punto que falta en el original).

## tiktok-quantgent-692630 — «The Law of Large Numbers» (2026-10-08)

- **7 slides** en el orden de la publicación. El OCR agrupó mal casi todo el texto (lo tomó como
  gráfico), así que **todos los bloques se escribieron a mano** con medidas tomadas de la imagen
  (`nuevo()` en `scripts/curar_tiktok.py`).
- **Negritas internas** del original («Flip it **100** times», «**Insurance companies**», «"**casino**"»)
  se conservan con la marca `**…**` del renderer.
- **Estrategias**: 01, 04, 06 C (fotos y retrato de Bernoulli); 03 A (gráfico sobre fondo negro: borrado
  `plano` y rótulos reescritos; las negritas internas del rótulo pasan a mayúsculas, porque las etiquetas
  no admiten negrita parcial); 05 A (simulación sin semilla: leyenda, ticks de miles y rótulos
  reescritos); 02 y 07 sin gráfico.
- **Fórmula** «As n → ∞, X̄ₙ → μ» → «Si n → ∞, X̄ₙ → μ» (Inter tiene el macrón combinante y el subíndice).
- **Términos**: «edge» → «ventaja (de la casa)»; «win rate» → «gana el X % de las veces»; «trades» →
  «operaciones»; «claims» → «siniestros»; «originals» → «producciones propias»; «They're the house» →
  «Son la casa.»

## tiktok-quantgent-284502 — «The Most Expensive Illusion in Trading» (sobreajuste) (2026-10-08)

- **6 slides** en el orden de la publicación. Todos los gráficos van por **A** (ilustrativos, sin datos en
  el texto, salvo las barras 1,2 / −0,2, que tienen solo dos valores y se resuelven reescribiendo los
  rótulos): 01 curva backtest/real; 02 curva con tres métricas; 03 barras de Sharpe; 04 dos paneles
  (20 vs. 2 parámetros); 05 mapa de calor; 06 sin gráfico.
- **Fuente nueva**: `fuentes/Inter-Italic.otf` (OFL) para los rótulos en itálica.
- **Alerta de hecho**: Knight Capital (2012) no perdió por sobreajuste sino por una falla de
  implementación de software, y no «nunca se recuperó» (rescate y fusión con Getco en 2013). Va a
  `revisar.md` como ERROR DE HECHO para corregir en Canva.
- **Términos**: «overfitting» → «sobreajuste (overfitting)» en la primera mención; «backtest» se deja en
  inglés, con «(la prueba con datos históricos)» en la primera mención (uso habitual en la prensa
  financiera); «equity curve» → «curva de capital»; «drawdowns» → «caídas»; «Max DD» → «Caída máx.»;
  «go live» → «operar en real»; «Overfit "edge"» → «“Ventaja” ficticia».

## tiktok-quantgent-158294 — «Spoofing» (2026-10-08)

- **7 slides** en el orden de la publicación. Estrategias: 01 C (ilustración de libro de órdenes; BID /
  ASK / SPREAD quedan, son de uso corriente); 02 A (tres paneles; pies sobre relleno de color con borrado
  `plano`); 03 A (precio y volumen); 04 C (captura de plataforma con anotación ilegible: traducción
  aproximada en `revisar.md`); 05 C (foto); 06 A (cancelaciones: títulos, leyendas y porcentajes); 07 sin
  gráfico.
- **Alertas principales**: contradicción interna (la portada dice que el algoritmo «ganó» US$ 300
  millones; la slide 5, que esas son las pérdidas causadas a terceros); Sarao fue detenido por la policía
  británica a pedido de EE. UU.; el Flash Crash duró ≈ 36 minutos; el caso Thakkar terminó sin condena.
- **Control automático**: `cifras_en` no reconocía la escala con mayúscula («$300 Million», en títulos);
  ahora la expresión regular es insensible a mayúsculas (`carrusel/formato.py`).
- **Términos**: «spoofing», «spoofer» sin traducir (no hay equivalente asentado; «órdenes falsas» para
  «spoof/fake orders»); «order book» → «libro de órdenes»; «filled» → «ejecutada»; «retail traders» →
  «inversores minoristas»; «Level 2 data» → «datos de nivel 2 (el libro de órdenes completo)»; «US
  Treasuries» → «bonos del Tesoro de EE. UU.»; la CFTC se explica en la primera mención.

## tiktok-quantgent-456663 — «Ergodicity», versión de TikTok (2026-10-08)

- Es **el mismo carrusel que la referencia `ergodicity`** (Instagram, 4:5) en 9:16, con los mismos bloques
  detectados. `scripts/curar_ergodicity_tiktok.py` llama a `ergodicity()` de `curar_referencia.py` y solo
  cambia las cajas: misma traducción, mismas estrategias (C, B, B, B, B, B, —), mismos datos exactos de
  los gráficos regenerados y mismas alertas. Marcado `version_de: ergodicity` para no duplicar evidencia.

## tiktok-quantgent-110294 — «Regression to the Mean» (2026-10-08)

- Es **la misma publicación** (ID 7616778102257110294) que `regresion-media`, ya traducida en una sesión
  anterior. No se volvió a curar: se re-renderizó con `curar_regresion_media.curar()` sobre el nuevo slug
  (textos y cajas idénticos a los del plan guardado en memoria) y **no se corrió el paso `memoria`**, para
  no duplicar la ficha ni la evidencia de `ESTILO.md`.
- Control de calidad: dos rótulos de leyenda arrastraban la muestra de color o la línea de la leyenda
  (slide 3 «Persistente» y slide 6 «Regresión (pendiente = 0,58)» / «Sin regresión»). Se pasaron a borrado
  `plano`, en el script y en el plan de la memoria.

## Consolidación de ESTILO.md (11 carruseles, 2026-10-08)

- Evidencia como «n/11»: 11 carruseles distintos. Las versiones de TikTok de fat-tails y ergodicity
  (`version_de`) y la repetición de regresion-media no se cuentan aparte.
- Patrones nuevos que pasan a la guía: estructura portada → planteo → respuesta contraintuitiva → por
  qué falla la intuición → fórmula con retrato → «No es solo teoría» → «La lección de X no es la
  matemática… es…» (8/11); variantes de 6 y 8 slides; fotos de banco (7/11, a evitar); bajada a Wall
  Street (9/11).
- «No hacer» incorpora las alertas de los 9 carruseles nuevos (tasa base omitida, Knight Capital,
  contradicciones internas, probabilidad individual vs. acumulada, tasa de acierto vs. ventaja, gráficos
  ajenos al texto, casos judiciales a medias).
- Sección 10: se resumen kelly, bayes y ergodicity como los más representativos (la guía pide 2-3).
  2.490 palabras.
