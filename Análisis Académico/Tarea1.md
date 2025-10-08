# Análisis Académico - Tarea 1: La Primera Inspección

## Objetivo
Desarrollar un "ojo crítico" para la calidad de los datos.  
Es una de las habilidades más importantes de un profesional del dato.

## Instrucciones

1. **Crear un repositorio en GitHub**  
   - Este repositorio será el lugar donde se añadirá todo el trabajo del proyecto.

2. **Descargar los ficheros CSV**  
   - Descarga todos los ficheros del proyecto académico.

3. **Abrir los ficheros CSV**  
   - Puedes usar Microsoft Excel, Google Sheets o cualquier visor de CSV.  
   - **Importante:** No modifiques nada todavía.

4. **Inspección inicial de los datos**  
   Conviértete en un detective y responde a las siguientes preguntas para cada fichero:

   - ¿Cuál es el **separador de columnas**?  
     - Coma (`,`) o punto y coma (`;`)  
     
   - ¿La primera fila contiene los **nombres de las columnas (encabezados)**?  
     - ¿Son claros y descriptivos?

   - Inspecciona visualmente las primeras 20-30 filas:  
     - ¿Ves valores que te parezcan **extraños o que faltan**?  
       - Ejemplos: celdas vacías, `"N/A"`, `"s/d"`.

   - ¿Los **formatos son consistentes**?  
     - Ejemplo: ¿Las fechas siempre están en `DD/MM/AAAA` o cambian en algunas filas?

   - Identifica las **claves o IDs** que podrían servir para relacionar ficheros:  
     - Ejemplo: `id_alumno` en `calificaciones.csv` y también en `alumnos.csv`.

5. **Documentar los hallazgos**  
   - Apunta tus observaciones en un **documento de texto**.  
   - Este documento será el **punto de partida** para la limpieza de datos en módulos posteriores.



**4.1 - ¿Cuál es el separador de columnas?**  

Para todos los archivos excepto el `Indicadores_Finales.csv` el separador es (`,`) para el archivo de `Indicadores_Finales.csv` el separador es (`;`)

**4.2 - ¿La primera fila contiene los nombres de las columnas (encabezados) y son claros y descriptivos?** 

En todos los archivos la primera linea contiene el nombre de las columnas.

La gran parte de los encabezados son claros pero hay algunos ficheros con algunas columnas que pueden ser mas confusas, estos son:

  -En `Indicadores_Finales.csv` los campos **Valor-A**, **Valor-T1**, **Valor-T2**, **Valor-T3**, **Cod_SQ** y **Cod_PAA** son confusos y poco comprensibles.

  -En `Grupos.csv` los campos **ensenanza**, **linea**, **oficial** es complejo saber a que se refieren y tienen el mismo valor en todos los registros por lo que parecen innecesarios.

  -En `Calificaciones.csv` hay multiples campos que no tienen casi ningun valor en  registro, como: **medidas_inf** y en **capacidades_inf** donde solo hay en ocasiones un valor: "No hay datos guardados".

  
