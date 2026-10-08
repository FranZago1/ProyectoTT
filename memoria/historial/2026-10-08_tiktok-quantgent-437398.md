# 2026-10-08 — tiktok-quantgent-437398

**Título original:** Bayes' Theorem: The Equation Your Brain Refuses to Believe  
**Título en español:** El teorema de Bayes: la ecuación que tu cerebro se niega a creer  
**Motor OCR:** tesseract · **Orden de páginas:** [1, 2, 3, 4, 5, 6, 7]

## Slide 1 — Portada: concepto + promesa + gancho

- *titulo* (bold, 88 px): El teorema de Bayes
- *subtitulo* (regular, 45 px): La ecuación que tu cerebro se niega a creer.
- *cuerpo* (regular, 40 px): Médicos, fondos de cobertura y hasta el FBI dependen de ella… Y casi todos se equivocan con ella.
- **Gráfico** (ilustración: superficie 3D coloreada, sin ejes) — estrategia C: Imagen decorativa (superficie 3D tipo relieve) sin texto: se conserva.
- ⚠ Generalización sin fuente: «médicos, fondos de cobertura y hasta el FBI dependen de ella».
- ⚠ La imagen de portada es decorativa: no representa nada del teorema de Bayes.

## Slide 2 — Planteo: la prueba médica del 99 %

- *cuerpo* (regular, 45 px): Una prueba médica tiene un 99 % de precisión.
- *destacado* (bold, 47 px): Te da positivo.
- *cuerpo* (regular, 43 px): ¿Qué probabilidad hay de que realmente tengas la enfermedad?
- **Gráfico** (foto: hisopado a un paciente) — estrategia C: Foto recortada sin texto: se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva.
- ⚠ CLAVE — falta la tasa base: «menos del 10 %» solo vale si la enfermedad afecta a ≈ 1 de cada 1.000 personas y la prueba tiene 99 % de sensibilidad y 99 % de especificidad (0,99 × 0,001 / (0,99 × 0,001 + 0,01 × 0,999) ≈ 9 %). Con una prevalencia del 1 %, la respuesta sería 50 %. El original no da la prevalencia; conviene agregarla en Canva (p. ej., «la enfermedad afecta a 1 de cada 1.000 personas»).

## Slide 3 — Respuesta contraintuitiva: menos del 10 %

- *cuerpo* (regular, 45 px): ¿La respuesta real?
- *destacado* (bold, 46 px): Menos del 10 %.
- *cuerpo* (regular, 43 px): Tu cerebro acaba de reprobar un examen básico de probabilidad. Igual que el de casi todo el mundo. No es una falla: es biología. Nuestro cerebro no está hecho para la probabilidad condicional. El teorema de Bayes se creó para corregir eso.
- **Gráfico** (barras: lo que pensabas (99 %) vs. la respuesta real (~9 %)) — estrategia A: Dos barras con valores rotulados y pies sobre fondo liso: se reescriben los cuatro rótulos (la base de prevalencia no está en el texto, así que no se regenera).
- ⚠ CLAVE — falta la tasa base: «menos del 10 %» solo vale si la enfermedad afecta a ≈ 1 de cada 1.000 personas y la prueba tiene 99 % de sensibilidad y 99 % de especificidad (0,99 × 0,001 / (0,99 × 0,001 + 0,01 × 0,999) ≈ 9 %). Con una prevalencia del 1 %, la respuesta sería 50 %. El original no da la prevalencia; conviene agregarla en Canva (p. ej., «la enfermedad afecta a 1 de cada 1.000 personas»).
- ⚠ Afirmación sin sustento: «no es una falla: es biología». El sesgo de ignorar la tasa base está documentado (Kahneman y Tversky), pero atribuirlo a la biología es especulativo.

## Slide 4 — La fórmula y sus términos + Thomas Bayes

- *titulo* (bold, 46 px): La fórmula es elegante
- *otro* (regular, 45 px): P(A|B) = P(B|A) · P(A) / P(B)
- *cuerpo* (regular, 42 px): Donde P(A|B) es lo que querés saber, P(B|A) es lo que te dice la prueba, P(A) es qué tan rara es la enfermedad y P(B) es la probabilidad total de dar positivo. Actualiza lo que creés con la evidencia que realmente tenés.
- **Gráfico** (ilustración: retrato de Thomas Bayes) — estrategia C: Grabado de Thomas Bayes con su nombre como pie (nombre propio): se conserva.
- ⚠ Fórmula correcta. El retrato «de Thomas Bayes» que circula es de autenticidad dudosa (no hay retratos verificados de Bayes); conviene aclararlo o reemplazarlo.

## Slide 5 — Por qué importa en los mercados: actualizar posiciones

- *titulo* (bold, 50 px): Por qué le importa a Wall Street
- *cuerpo* (regular, 42 px): Cada vez que el mercado se mueve, los traders enfrentan la misma pregunta: ¿tengo que actualizar mi posición? Bayes les da el marco exacto. Llegan datos nuevos, se actualizan las creencias, se ajustan las posiciones. No es predicción: es adaptación. Por eso las mejores estrategias cuantitativas no son rígidas. Aprenden.
- **Gráfico** (curvas: distribución a priori, verosimilitud y a posteriori) — estrategia A: Curvas ilustrativas a priori, verosimilitud y a posteriori, sin parámetros: se reescriben los tres rótulos.
- ⚠ Generalización: «las mejores estrategias cuantitativas aprenden» y que Bayes da «el marco exacto» no tienen fuente; es una descripción idealizada.

## Slide 6 — Casos: Nate Silver, filtros de spam, autos autónomos, Renaissance

- *titulo* (bold, 52 px): No es solo teoría
- *cuerpo* (regular, 42 px): Nate Silver usó Bayes para predecir correctamente los 50 estados en la elección presidencial de 2012 en EE. UU. Los filtros de spam de tu correo funcionan con Bayes. Los autos autónomos lo usan para decidir si esa sombra es un peatón. Y Renaissance Technologies —el fondo de cobertura más rentable de la historia— construye estrategias basadas en la inferencia bayesiana.
- **Gráfico** (foto: sensores en el techo de un auto autónomo) — estrategia C: Foto sin texto: se conserva.
- ⚠ La foto es de terceros (sin fuente indicada en el original): verificar derechos de uso o reemplazarla en Canva.
- ⚠ Nate Silver acertó los 50 estados en 2012 (dato verificable); su modelo agrega encuestas con métodos en parte bayesianos, no es una aplicación directa del teorema.
- ⚠ Sin fuente: que Renaissance «construye estrategias basadas en inferencia bayesiana». «El fondo más rentable de la historia» suele referirse a Medallion, su fondo interno.
- ⚠ Precisión: los filtros de spam clásicos usan Bayes ingenuo; los actuales combinan otros modelos.

## Slide 7 — Cierre: la mentalidad bayesiana (actualizar), sin gráfico

- *titulo* (bold, 51 px): La mayor lección de Bayes no es la matemática…
- *destacado* (bold, 45 px): Es la mentalidad.
- *cuerpo* (regular, 42 px): La mayoría de la gente se forma una opinión y la defiende. Quienes piensan de forma bayesiana se forman una opinión y la actualizan. En los mercados y en la vida, los que ganan a largo plazo no son los que más aciertan: son los que cambian de opinión más rápido cuando la evidencia lo indica.
- **Gráfico**: ninguno.
