# 2026-10-08 — tiktok-quantgent-284502

**Título original:** The Most Expensive Illusion in Trading: How Overfitting Turns Perfect Backtests Into Real Losses  
**Título en español:** La ilusión más cara del trading: cómo el sobreajuste convierte backtests perfectos en pérdidas reales  
**Motor OCR:** tesseract · **Orden de páginas:** [1, 2, 3, 4, 5, 6]

## Slide 1 — Portada: concepto + promesa + gancho

- *titulo* (bold, 71 px): La ilusión más cara del trading
- *subtitulo* (bold, 40 px): Cómo el sobreajuste (overfitting) convierte backtests perfectos en pérdidas reales
- *cuerpo* (regular, 34 px): Un modelo de trading con un 95 % de acierto en el backtest (la prueba con datos históricos) puede perder hasta el último dólar en el mercado real. Es la causa de muerte más común en las finanzas cuantitativas. Veamos por qué ocurre.
- **Gráfico** (línea: capital en el backtest (sube) y en real (cae)) — estrategia A: Curva ilustrativa sin datos: se reescriben los dos rótulos.
- ⚠ Exageración sin fuente: «la causa de muerte más común en las finanzas cuantitativas».

## Slide 2 — Planteo: el backtest perfecto

- *cuerpo* (regular, 34 px): Armás un modelo. Le hacés un backtest.
- *cuerpo* (regular, 34 px): La curva de capital sube sin parar. 95 % de acierto. Ratio de Sharpe por encima de 3. Casi sin caídas.
- *cuerpo* (regular, 34 px): Encontraste la ventaja. Estás listo para operar en real.
- *destacado* (bold, 34 px): Salvo que no encontraste nada. Tu modelo solo memorizó el pasado.
- **Gráfico** (línea: curva de capital del backtest con tasa de acierto 94,7 %, Sharpe 3,41 y caída máx. −2,1 %) — estrategia A: Curva ilustrativa con tres métricas rotuladas: se reescriben valores y rótulos con formato argentino.
- ⚠ Diferencia texto-gráfico: el texto dice 95 % de acierto y el gráfico 94,7 % (redondeo).

## Slide 3 — Evidencia: estudios y el caso Knight Capital (2012)

- *destacado* (bold, 34 px): El 44 % de las estrategias de trading publicadas fracasa apenas se enfrenta a datos nuevos.
- *cuerpo* (regular, 34 px): AQR Capital probó una estrategia de medias móviles. Su ratio de Sharpe se desplomó de 1,2 a −0,2 con datos nuevos.
- *cuerpo* (regular, 34 px): En 2012, Knight Capital puso en marcha un algoritmo sobreajustado. Perdió US$ 440 millones en 45 minutos. La firma nunca se recuperó.
- **Gráfico** (barras: ratio de Sharpe en backtest (1,2) y en real (−0,2)) — estrategia A: Dos barras con los valores del texto (1,2 y −0,2): pocos rótulos sobre fondo liso; se reescriben con formato argentino.
- ⚠ ERROR DE HECHO: la pérdida de Knight Capital (1 de agosto de 2012, US$ 440 millones en unos 45 minutos) se debió a una falla de implementación de software (se reactivó un código viejo en un servidor), no a un algoritmo sobreajustado. Además, la firma sí sobrevivió: fue rescatada por inversores y se fusionó con Getco en 2013 (KCG Holdings). Corregir o quitar en Canva.
- ⚠ Sin fuente: «el 44 % de las estrategias publicadas fracasa» y el caso de AQR (Sharpe de 1,2 a −0,2). Verificar o citar el estudio.

## Slide 4 — Mecanismo: aprender el ruido; el elefante de Von Neumann

- *titulo* (bold, 40 px): Entonces, ¿qué salió mal en realidad?
- *cuerpo* (regular, 34 px): Tu modelo no aprendió el mercado. Aprendió el ruido. Cada salto aleatorio, cada hecho aislado, cada coincidencia quedó incorporada a las reglas.
- *cita* (regular, 34 px): Von Neumann lo dijo mejor que nadie: “Con cuatro parámetros puedo ajustar un elefante, y con cinco puedo hacer que mueva la trompa”.
- *destacado* (bold, 34 px): Más parámetros implican más flexibilidad. Más flexibilidad implica que el modelo puede ajustarse a cualquier cosa, incluso a patrones que nunca se van a repetir.
- **Gráfico** (dos paneles: modelo sobreajustado (20 parámetros) vs. modelo robusto (2 parámetros)) — estrategia A: Dos paneles ilustrativos con cuatro rótulos sobre fondo blanco: se reescriben.
- ⚠ Cita correcta en sustancia: la atribuye Enrico Fermi a John von Neumann, según relató Freeman Dyson (Nature, 2004).

## Slide 5 — Diagnóstico: cómo saber si el modelo miente

- *titulo* (bold, 40 px): Cómo saber si tu modelo te miente
- *cuerpo* (regular, 34 px): Si el ratio de Sharpe supera 3, desconfiá. Si cambiar un parámetro un 10 % da vuelta la estrategia de ganadora a perdedora, está sobreajustada.
- *cuerpo* (regular, 34 px): La prueba de verdad: reservá el 30 % de tus datos. No los toques nunca. Corré tu modelo final sobre ellos una sola vez. Si el rendimiento se derrumba, el backtest era un espejismo.
- *destacado* (bold, 34 px): El objetivo de un backtest es descartar modelos malos. No mejorarlos.
- **Gráfico** (mapa de calor: rendimiento según dos parámetros; una zona verde aislada («ventaja» sobreajustada)) — estrategia A: Mapa de calor ilustrativo con tres rótulos: se reescriben (el del centro, sobre las celdas, por inpainting).
- ⚠ Reglas prácticas (Sharpe mayor que 3, ±10 % en un parámetro, reservar el 30 % de los datos) sin fuente; son heurísticas habituales, no umbrales universales.
- ⚠ Mapa de calor: el rótulo central es muy chico (8,5 px) y está sobre celdas de color; si no se lee bien, rehacerlo en Canva.

## Slide 6 — Cierre: disciplina ante los patrones, sin gráfico

- *cuerpo* (regular, 34 px): La lección del sobreajuste no es técnica…
- *destacado* (bold, 34 px): Es que los humanos estamos programados para ver patrones que no existen.
- *cuerpo* (regular, 34 px): Encontramos señal en el ruido, ventajas en el azar, sentido en la coincidencia. Los mejores quants no solo construyen mejores modelos. Construyen más disciplina.
- *cuerpo* (regular, 34 px): La operación más difícil de las finanzas es abandonar un backtest hermoso.
- **Gráfico**: ninguno.
