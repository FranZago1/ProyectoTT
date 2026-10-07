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
