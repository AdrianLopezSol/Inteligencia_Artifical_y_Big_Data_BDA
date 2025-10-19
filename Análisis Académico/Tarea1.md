# Análisis Académico - Tarea 1: La Primera Inspección

**4.1 - ¿Cuál es el separador de columnas?**  

Para todos los archivos excepto el `Indicadores_Finales.csv` el separador es (`,`) para el archivo de `Indicadores_Finales.csv` el separador es (`;`)

**4.2 - ¿La primera fila contiene los nombres de las columnas (encabezados) y son claros y descriptivos?** 

En todos los archivos la primera linea contiene el nombre de las columnas.

La gran parte de los encabezados son claros pero hay algunos ficheros con algunas columnas que pueden ser mas confusas, estos son:

  -En `Indicadores_Finales.csv` los campos **Valor-A**, **Valor-T1**, **Valor-T2**, **Valor-T3**, **Cod_SQ** y **Cod_PAA** son confusos y poco comprensibles. El resto de archivos parecen tener encabezados descriptivos y funcionales.

**4.3 - Inspecciona visualmente las primeras 20-30 filas. ¿Ves valores que te parezcan extraños o que faltan (celdas vacías, "N/A", "s/d")?**

  -En `Grupos.csv` los campos **ensenanza**, **linea**, **oficial** tienen el mismo valor en todos los registros por lo que parecen innecesarios.

  -En `Calificaciones.csv` hay multiples campos que no tienen casi ningun valor en  registro, como: **medidas_inf** y en **capacidades_inf** donde solo hay en ocasiones un valor: "No hay datos guardados".

  -En `Indicadores_Finales.csv` los campos de **Valor-T1**, **Valor-T2** y **Valor-T3** tienen la gran mayoria de los registros vacios.
  
