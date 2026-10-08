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
