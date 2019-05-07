# Tópicos Especiales En Telemática - Proyecto 3 Big Data

## Creado por: Maria Clara Sanchez V, Tomas Alvarez G y Juan Esteban Fonseca P.

  Para este proyecto se realizaron diferentes algoritmos, uno de limpieza de datos, uno de contador de palabras por medio de índice inverso y uno de análisis de semejanza de textos. Todos los algoritmos anteriormente mencionados se basan en la lectura de diferentes Datasets (.csv).

El algoritmo de limpieza funciona quitando todas las stop-words del lenguaje en cuestión de los contenidos de las noticias, así como su título, dejando un arreglo de sólo las palabras relevantes las cuales son cruciales para los siguientes pasos.  

El algoritmo de contador de palabras por medio de índice inverso funciona a partir de una entrada de usuario de una palabra en específico, el algoritmo luego, a partir de esta palabra, usará el arreglo del contenido y título ya limpios para así contar el número de iteraciones que tiene de esta. El output será  de máximo 10 noticias, frecuencia de la palabra de la noticia, identificación de la noticia, título de la noticia.

El algoritmo de análisis de semejanza de textos funciona a partir de una entrada de usuario de un id de una noticia, con este se buscará la noticia en cuestión y comparara su frecuencia de palabras con las demás noticias; Entre más palabras comparta una noticia con la noticia en cuestión, el algoritmo determinara que es más probable que sea parecida. el output será el id de la noticia ingresada, su título, un arreglo de 5 id's de las 5 noticias más parecidas.

## Modo de compilación

Se requiere usar Databricks para la ejecución de estos algoritmos, cada paso está dividido por carpetas y por tanto así debe de correrse en el Notebook. 

Cada archivo .py se copia y se pega en un cuadro de comando en el Notebook (para mejorar su eficiencia y no correr el código varias veces innecesariamente)  
