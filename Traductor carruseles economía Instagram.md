# Traductor de carruseles de Instagram (EN → ES-AR) + memoria de estilo

## Objetivo

Herramienta local, sin interfaz gráfica, para:

1. Traducir carruseles de Instagram de 7 slides sobre finanzas cuantitativas y economía, del inglés al español rioplatense formal, **conservando gráficos y diseño**.
2. Dejar cada slide lista para subir o para retocar en Canva.
3. Construir, carrusel a carrusel, una **memoria de estilo** (`memoria/ESTILO.md`) que yo pueda pegar en un chat para generar carruseles nuevos sin material de origen.

Prioridad: que funcione y sea confiable. Cero esfuerzo en estética, UI o empaquetado.

## Cómo trabajo (respetar)

- Incremental: antes de programar cada fase, explicá brevemente qué vas a hacer; al terminar, mostrá resultados y **frená en el checkpoint** hasta que apruebe.
- Comandos de terminal listos para copiar y pegar, con una línea que explique cada uno.
- Respondeme en español.
- Si una decisión tiene alternativas con trade-offs reales, planteámelas antes de elegir.
- Ante dudas sobre una cifra, un término o qué es parte de un gráfico: preguntá, no supongas.

## Material de referencia

`entrada/referencia/Carrusel_2.pdf`: 14 páginas con **dos carruseles completos** (7 + 7), capturados como screenshots de Instagram dentro de un PDF y **no necesariamente en orden**. Es el caso de prueba de todas las fases y la semilla de la memoria (ver sección "Semilla de estilo").

## Formato de entrada (importante)

La entrada puede venir como:

- **PDF** con una captura por página (como el de referencia), o
- **PNG/JPG** sueltos, idealmente las imágenes originales descargadas (1080×1350).

Las capturas traen elementos de la interfaz de Instagram que **no son parte de la slide** y hay que eliminar: barra gris superior con la flecha "<", márgenes blancos de la página del PDF, el contador tipo "7 / 7" (píldora gris arriba a la derecha) y sombras o degradados en los bordes.

Salida siempre en **1080×1350**. Si la fuente es de menor resolución, escalar con Lanczos y anotarlo en `revisar.md` (la calidad final depende de la fuente).

## Stack

- **Python 3.11+**, entorno en `.venv`. CLI: `python -m carrusel <comando> <slug>`. Configuración en `config.yaml`.
- PDF → imágenes: PyMuPDF (`fitz`), a 200–300 dpi.
- OCR con cajas: evaluar en Fase 0 **`ocrmac` (Apple Vision, si estoy en macOS)** vs **EasyOCR** sobre las páginas del PDF de referencia. Tesseract solo como último recurso.
- Imagen: OpenCV (recorte, detección de zonas, inpainting) + Pillow (render de texto).
- Gráficos regenerados: matplotlib.
- Paleta: k-means sobre píxeles (numpy o scikit-learn).

## Arquitectura: Claude Code como orquestador

No hay llamadas a la API de Anthropic desde el código. Los scripts hacen lo mecánico; **vos (Claude Code) hacés lo que requiere criterio**: ordenar slides, corregir OCR mirando las imágenes, decidir la estrategia de cada gráfico, traducir y mantener la memoria. Abrí las imágenes para verificar siempre que haga falta.

### Estructura del repo

```
entrada/<slug>/                     # PDF o PNGs tal como los descargo
entrada/referencia/Carrusel_2.pdf
trabajo/<slug>/
    slides/01.png … 07.png          # recortadas, sin UI de Instagram, en orden
    plan.json                       # zonas, bloques, traducción, estrategia por gráfico
salida/<slug>/
    01_es.png …                     # slide final traducida
    01_limpia.png …                 # slide sin texto (fondo para Canva)
    graficos/01_grafico_es.png …    # gráficos traducidos o regenerados, sueltos
    textos_es.md                    # textos por slide, listos para copiar
    revisar.md                      # pendientes, dudas y alertas
memoria/
    ESTILO.md                       # memoria destilada (lo que pego en chats)
    GLOSARIO.md                     # decisiones terminológicas EN → ES
    historial/AAAA-MM-DD_<slug>.md  # ficha de cada carrusel procesado
fuentes/                            # .ttf configurables (Inter por defecto)
carrusel/                           # código
config.yaml
```

## Modelo de la slide

Todas las slides de referencia siguen el mismo esquema: **fondo claro casi liso** (blanco o gris muy claro con degradado suave), **zona de texto** arriba, centrada, y opcionalmente **una zona de gráfico** abajo (a veces dos gráficos lado a lado, a veces ninguno), con un pie de gráfico chico en gris.

Por eso **no reemplazar texto línea por línea**: la zona de texto completa se borra y se **recompone entera** en español (reflujo libre del párrafo). Esto absorbe sin problemas que el español sea 20–30 % más largo.

### `plan.json` por slide

- `zona_texto`: bbox; `bloques`: lista ordenada con `rol` (titulo | subtitulo | cuerpo | destacado | cita | pie | otro), `texto_en`, `texto_es`, `peso` (regular | semibold | bold), `tam_px` estimado, `color`.
- `zonas_grafico`: lista con bbox, `tipo` (ver estrategias), `estrategia`, `etiquetas` (texto_en, texto_es, bbox) y `datos` si se regenera.
- `elementos_ui_eliminados`: qué se borró y dónde.

## Flujo (comando que uso: "traducí <slug>")

1. `preparar`: rasterizar el PDF si corresponde, detectar el rectángulo de la slide, recortar, eliminar la UI de Instagram, normalizar a 1080×1350.
2. **Agrupar y ordenar**: si la entrada tiene más de 7 páginas o el orden no es evidente, proponé cómo se agrupan en carruseles y en qué orden. Pistas: la portada tiene título grande y subtítulo; el contador "n / 7" si aparece; la continuidad del argumento; el cierre suele ser aforístico y a veces no tiene gráfico. ✋ **Confirmar conmigo antes de seguir.**
3. `extraer`: OCR, zonas y bloques → `plan.json`. Revisión tuya mirando cada imagen.
4. **Estrategia por gráfico** (proponer una por gráfico, justificar en una línea):
   - **A. Etiquetas en el lugar**: borrar y reescribir solo los rótulos (ejes, leyendas, valores destacados). Para gráficos con pocos textos y fondo liso.
   - **B. Regenerar con matplotlib**: solo si los datos se pueden **derivar exactamente** del contenido (p. ej. la moneda +50 % / −40 %, la curva de Kelly g(f) = 0,5·ln(1+0,5f) + 0,5·ln(1−0,4f), barras de valores dados). Imitar estilo: fondo transparente o igual al de la slide, colores de la paleta, ejes finos grises, etiquetas de valor en negrita. Si los datos vienen de una **simulación aleatoria**, se puede regenerar con semilla fija pero queda marcado en `revisar.md` como "regenerado, no idéntico al original". **Nunca** regenerar series de datos reales (p. ej. S&P 500) reconstruyéndolas a ojo.
   - **C. Conservar**: figuras académicas con notación matemática (P(x), E(L), VaR, ES, σ), ilustraciones o imágenes sin texto relevante. Se traduce solo lo que tenga texto en lenguaje natural (p. ej. "Loss" → "Pérdida", "5% probability" → "5 % de probabilidad") si se puede hacer limpio; si no, se deja y se anota.
   - **D. Manual**: gráficos con mucho texto chico (p. ej. una línea de tiempo densa). Se entrega la traducción completa de sus textos en `textos_es.md` para rehacerlo en Canva, y se marca en `revisar.md`. Opcionalmente proponé reconstruirlo simplificado (B) **solo si yo lo apruebo** y transcribiendo los datos exactos.
5. Traducción: completar `texto_es` según reglas, `GLOSARIO.md` y `ESTILO.md`.
6. ✋ **Checkpoint**: tabla EN → ES por slide + estrategia por gráfico. No renderizar hasta que apruebe o corrija.
7. `renderizar`: reconstruir el fondo de la zona de texto (fondo casi liso: muestrear el color por fila para respetar el degradado; inpainting solo si hace falta), recomponer el texto, aplicar la estrategia de cada gráfico, generar `salida/<slug>/` completo.
8. Actualizar memoria.

### Reglas de traducción

**Registro.** Español rioplatense formal y sobrio. El original interpela al lector todo el tiempo ("you"), así que se usa **voseo** ("Imaginá", "tenés", "perdés"), sin lunfardo ni coloquialismos ("che", "posta", "guita": nunca). Referencia: secciones de economía de la prensa argentina.

**Conservar los recursos retóricos** del original, que son parte del estilo: oraciones cortas, fragmentos en pregunta-respuesta ("¿Los derrumbes? Prácticamente imposibles."), tríadas ("Misma apuesta. Mismas probabilidades. Misma matemática."), antítesis de cierre, guiones largos (—). La oración en negrita del original sigue en negrita.

**Números (los valores nunca cambian, solo el formato):**
- Decimal con coma, miles con punto: 99.7% → 99,7 %; 10,000 → 10.000; 0.5 x 1.50 → 0,5 × 1,50.
- Montos de mercados reales en dólares: estilo prensa argentina. $3.6 billion → US$ 3.600 millones; $100 billion → US$ 100.000 millones; $553 million → US$ 553 millones. trillion → billones.
- Montos de ejemplos hipotéticos (el juego de la moneda, "$100"): mantener "$" sin "US".
- Fechas en formato día/mes con meses en español ("17 de agosto de 1998").
- En gráficos regenerados, ticks con formato argentino. En gráficos conservados (C), los ticks no se tocan.

**No traducir**: notación matemática, siglas técnicas con uso establecido (VaR, ES, EV si aparece como sigla junto a su traducción), nombres propios, instituciones sin traducción establecida, handles, tickers, "S&P 500".

**Glosario inicial** (proponer, confirmar en el primer checkpoint, luego fijar en `GLOSARIO.md`):

| EN | ES |
|---|---|
| fat tails | colas gruesas (alternativa técnica: colas pesadas) |
| quants | quants (en la primera mención: "analistas cuantitativos (quants)") |
| bell curve | campana de Gauss |
| normal distribution | distribución normal |
| standard deviation | desvío estándar |
| kurtosis | curtosis |
| expected value / EV | valor esperado |
| ergodicity | ergodicidad |
| Kelly Criterion | criterio de Kelly |
| geometric growth rate | tasa de crecimiento geométrica |
| hedge fund | fondo de cobertura |
| black swan | cisne negro |
| coin flip / heads / tails | tirar una moneda / cara / ceca |
| break even | punto de equilibrio |
| crash | derrumbe / crac (según contexto) |
| bearish | bajista |
| bailout / rescue | rescate |
| leverage | apalancamiento |
| defaults on its bonds | entra en default de sus bonos |
| wealth | patrimonio (riqueza, si el contexto es abstracto) |
| crypto | cripto / criptomonedas |
| "Past performance doesn't guarantee future results" | "Rendimientos pasados no garantizan rendimientos futuros" |
| Loss / Flips / Wealth ($) | Pérdida / Tiradas / Patrimonio ($) |

### Verificación de contenido

No corregir el contenido del original al traducir, pero **anotar en `revisar.md`** las afirmaciones dudosas, imprecisas o no verificables (fechas, cifras, atribuciones, gráficos que no muestran lo que dice el pie). Si yo decido corregir algo, lo hago en el checkpoint. Esto también alimenta la memoria: el estilo se imita, los errores no.

### Render

- Tipografía: las slides de referencia parecen **Inter** (títulos Bold/ExtraBold, cuerpo Regular/Medium, destacados SemiBold/Bold). Confirmar comparando visualmente; descargar Inter (licencia OFL) a `fuentes/`. Configurable en `config.yaml`.
- Texto centrado, ancho de columna ≈ 75 % de la slide, interlineado y tamaños medidos sobre el original y guardados en `config.yaml`.
- Si el texto en español no entra en la zona original: primero reducir el tamaño hasta 90 %, después ampliar la zona hacia arriba si hay aire, y recién después proponer una versión más corta (marcada en `revisar.md`). Nunca pisar el gráfico.
- Probar cada cambio del renderer sobre una sola slide antes de correr las 7.

## Semilla de estilo (de los 2 carruseles de referencia)

Usar esto para crear la primera versión de `ESTILO.md` (evidencia: 2/2 salvo que se indique). Verificar contra las imágenes y corregir lo que esté mal observado.

**Carrusel A — "Fat Tails: How Quants Profit From the Impossible".** Orden inferido (el PDF viene desordenado; confirmar): págs. 2 → 7 → 6 → 1 → 8 → 4 → 3. Arco: portada con concepto y promesa → "la matemática te miente" (mito) → el modelo normal y la crisis de 2008 → nombre del concepto (colas gruesas) → cómo medirlo (curtosis) → caso histórico (LTCM, 1998) → figura ejemplar y moraleja (Ed Thorp) + definición de "cisne negro".

**Carrusel B — "Ergodicity: The Reason Expected Value Destroys Portfolios".** Orden: págs. 5 → 9 → 10 → 11 → 12 → 13 → 14. Arco: portada con concepto y promesa → experimento mental (moneda +50 % / −40 %) → paradoja (promedio de 10.000 personas vs. una persona en el tiempo) → explicación paso a paso con $100 → el orden no importa, siempre se pierde → la solución (criterio de Kelly) + historia (Kelly 1956, Ole Peters) → cierre aforístico **sin gráfico**.

**Patrones observados:**
- Tema: conceptos de finanzas cuantitativas y probabilidad explicados para público general, con tono de "lo que no te cuentan".
- Portada: concepto en una o dos palabras (título muy grande) + subtítulo con promesa o paradoja ("Cómo los quants ganan con lo imposible") + a veces un párrafo gancho + gráfico técnico de aspecto académico.
- Cuerpo: 50–90 palabras por slide, oraciones de 3 a 15 palabras, segunda persona, preguntas retóricas, cifras concretas, una oración clave en negrita por slide (frecuente en B).
- Cierre: frase aforística con antítesis ("El mercado no te debe el valor esperado. Solo te debe el camino que efectivamente recorrés.").
- Gráficos: uno por slide (salvo el cierre de B); dos familias: (1) figuras importadas de papers, libros o sitios (notación LaTeX, screenshots), (2) gráficos propios estilo matplotlib/seaborn minimalista, con valores destacados en negrita y verde/rojo para ganancia/pérdida.
- Diseño: fondo blanco o gris muy claro con degradado suave; texto casi negro; todo centrado; pie de gráfico chico en gris.
- Paleta aproximada (confirmar con extracción automática): verde ganancia ~#4F8A5B, rojo pérdida ~#B85A4E, gris neutro ~#9A9A9A, naranja ~#E8A048, rojo intenso ~#C9433A, texto ~#1A1A1A.

## Memoria de estilo

Después de cada carrusel aprobado:

1. `memoria/historial/AAAA-MM-DD_<slug>.md`: tema, cuenta de origen (si la sé), y por slide: función narrativa, texto final en español, tipo de gráfico y qué muestra, fuente de datos citada, alertas de verificación.
2. `memoria/GLOSARIO.md`: términos nuevos y **cada corrección que yo haga** (mis correcciones tienen prioridad sobre tu criterio).
3. `memoria/ESTILO.md`: **reescribir consolidando, no agregar al final**. Cada patrón con su evidencia ("6/8 carruseles"). Paleta extraída automáticamente.

### Estructura obligatoria de `ESTILO.md`

1. **Instrucciones para el modelo que lo lea** (bloque inicial): "Con esta guía, generá un carrusel de 7 slides sobre el tema indicado, en español rioplatense formal con voseo. Para cada slide entregá: función narrativa, título (si corresponde), texto con la oración destacada en negrita, especificación del gráfico (tipo, datos exactos o fórmula, ejes, unidades, período, fuente con fecha) y pie de gráfico. Usá solo datos reales y verificables con fuente; si no podés verificar un dato, marcalo [DATO A VERIFICAR]. Nunca inventes cifras, fechas ni citas. Preferí gráficos que se puedan generar a partir de datos o fórmulas explícitas."
2. Estructura narrativa (función típica de cada slide 1–7 y variantes observadas).
3. Portadas y títulos: largo, recursos, ejemplos reales.
4. Cuerpo: densidad, largo de oraciones, recursos retóricos, uso de la negrita.
5. Cierres.
6. Gráficos: tipos, origen (importado vs. propio), rotulado, pies, colores semánticos.
7. Diseño: paleta (hex), tipografía y jerarquía, márgenes, ubicación de elementos.
8. Tono y registro + "hacer / no hacer" (incluye los errores de contenido detectados en los originales, para no repetirlos).
9. Glosario resumido (20–30 términos; el completo en `GLOSARIO.md`).
10. Dos o tres carruseles ejemplares resumidos slide por slide.

Límite: **≤ 2.500 palabras**. Si se acerca, condensar.

## Comandos de Claude Code (crear en Fase 4)

- `.claude/commands/traducir.md` → flujo completo sobre `entrada/$ARGUMENTS`.
- `.claude/commands/estilo.md` → revisa y consolida `ESTILO.md` y me resume qué cambió.

## Fases (frenar en cada checkpoint)

- **Fase 0 — Setup, preparación y OCR**: estructura, `.venv`, dependencias, `config.yaml`, Inter en `fuentes/`. Comando `preparar` sobre el PDF de referencia: recorte, limpieza de UI, agrupación en 2 carruseles y orden propuesto. Comparar motores de OCR sobre 2 páginas (una de texto + gráfico propio, una con figura académica). ✋
- **Fase 1 — Extracción y plan**: `extraer` + `plan.json` + estrategia por gráfico para los 14 slides. ✋ Checkpoint con tabla de bloques y estrategias.
- **Fase 2 — Render de dos slides**: una con gráfico estrategia A o C y una con estrategia B. Mostrar antes/después. ✋
- **Fase 3 — Flujo completo**: los dos carruseles completos + `salida/` completa. ✋
- **Fase 4 — Memoria**: historial de ambos, `GLOSARIO.md`, `ESTILO.md` a partir de la semilla y lo verificado, paleta automática, comandos `/traducir` y `/estilo`. ✋
- **Fase 5 (futura, no implementar sin que lo pida)**: comando `generar` que tome la especificación de 7 slides que devuelve un chat usando `ESTILO.md` y renderice las slides completas (texto + gráficos matplotlib) con la plantilla, paleta y tipografía registradas. El módulo de gráficos de la estrategia B se diseña desde ya pensando en reutilizarlo acá.

## Reglas generales

- `.gitignore`: `entrada/`, `trabajo/`, `salida/`, `.venv/`. Sí commitear `memoria/`, `config.yaml` y `fuentes/` (Inter es OFL).
- Mantener este `CLAUDE.md` actualizado si cambian decisiones (motor de OCR, convenciones, tipografía, glosario base).
