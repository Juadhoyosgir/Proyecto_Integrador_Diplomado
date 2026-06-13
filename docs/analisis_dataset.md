# Análisis cualitativo del dataset — Saber 11° 2025-1 (Antioquia)

## 1. Descripción general
El dataset contiene los resultados del examen Saber 11° del periodo 2025-1, una
prueba estandarizada que aplica el ICFES y que es requisito para graduarse del
bachillerato en Colombia. Cada registro corresponde a un estudiante e incluye su
puntaje global y por áreas, junto con características de su colegio y de su situación
socioeconómica familiar. Los datos provienen del ICFES (repositorio DataIcfes) y, en
este caso, corresponden en su totalidad a colegios del departamento de Antioquia.

*Resultado Examen Saber 11° - Periodo 2025-1*
*https://www.icfes.gov.co/investigaciones/data-icfes/*
*Datos abiertos Colombia*
*1313 filas*
*85 columnas*
*DataIcfes es el repositorio de datos abiertos del Instituto Colombiano para la Evaluación de la Educación (ICFES), diseñado para centralizar y ofrecer acceso libre a microdatos anonimizados generados a partirde evaluaciones estandarizadas como el Examen Saber 11°, el Examen Saber Pro, el Examen Saber TyT,las Pruebas Saber 3°, 5°, 7° y 9°, Pre Saber y la Prueba Saber 3, 5, 9. Su objetivo principal es 
proporcionar información estructurada que permita a los investigadores, formuladores de políticas y otros actores analizar la calidad educativa y contribuir al mejoramiento del sistema educativo en 
Colombia*

## 2. Estructura
El archivo original tiene 1.313 filas (estudiantes) y 85 columnas. Para este proyecto
se seleccionaron 14 columnas relevantes más la variable objetivo. La mayoría de las
variables son categóricas (estrato, educación de los padres, internet, género), y solo
el puntaje ('punt_global') es numérico, aquí se clasifica el puntaje en bajo, medio y alto para facilitar el análisis.

## 3. Variables relevantes
La variable objetivo es 'desempeno_global', creada al clasificar el puntaje global en
tres niveles (Bajo, Medio, Alto). Las variables explicativas son cinco: género del
estudiante, estrato de la vivienda, acceso a internet, y nivel educativo de la madre y
del padre; se eligieron porque representan factores del entorno socioeconómico que
podrían influir en el desempeño. El resto de variables (código y nombre del colegio,
municipio, jornada, calendario, naturaleza y zona) se usan como contexto para
identificar y agrupar, no como predictoras.

## 4. Calidad de los datos
No se encontraron registros duplicados. Se detectó una inconsistencia en la zona del
colegio, donde aparecían "URBANO" y "URBANA" como categorías distintas para lo mismo;
se unificaron. Las variables socioeconómicas presentaban alrededor del 15% de valores
faltantes. Se decidió eliminar los registros con datos incompletos en esas variables,
para no introducir valores inventados; con ello el dataset pasó de 1.313 a 1.109
estudiantes, esto debido a que si realizaba imputación de los datos no se tenía la realidad del territorio sino un valor que podría no representar la realidad de la familia, ya que estos tipos de datos son recopilados con encuestas antes de realizar la prueba.

## 5. Pertinencia
El dataset sí permite responder la pregunta analítica, pues contiene la variable
objetivo y las variables socioeconómicas de entrada. El análisis exploratorio lo
confirma: existe una relación clara entre el entorno y el desempeño. En el estrato 1,
cerca del 85% de los estudiantes obtuvo desempeño bajo; en el estrato 2 fue del 74%, y
ese porcentaje disminuye a medida que sube el estrato. El acceso a internet también se
asocia con mejores resultados. La educación de los padres muestra una influencia
fuerte: cuando los padres no tienen ningún nivel educativo el bajo desempeño llega al
87% (y al 91% con primaria incompleta), frente a apenas un 11.5% cuando tienen
educación profesional completa. El género, en cambio, no mostró diferencias relevantes
entre hombres y mujeres.

## 6. Limitaciones
- Al eliminar los registros incompletos se pudo introducir un sesgo, si quienes no
reportaron su información socioeconómica tienen un perfil distinto (por ejemplo,
familias con menos recursos o información academica de los padres).

- Las variables explicativas están entrelazadas entre sí (a mayor estrato suele haber
más acceso a internet y padres con más educación), así que no es posible separar el
efecto individual de cada una con este análisis, es decir, que padres com mayor educación pueden tener mayores ingresos, por tanto, acceso a pagar internet, así se puede entrelazar el análisis debido a información relacionada, sin embargo, en Colombia el acceso a estratos bajos en las ciudades es más común que en los pueblos lo que puede ayudar a separarlas.

- Hay factores más complejos no incluidos (estado de la vivienda, entorno social,
acompañamiento familiar) que también influyen en el desempeño y no fueron incluidos, en las variables del dataset se mencionaban temas como calidad de la alimentación y tiempo dedicado a estudiar pero no se determinaron para este análisis.

- Los datos corresponden a un solo periodo (2025-1) y solo a Antioquia, por lo que los
resultados no se pueden generalizar a otros años ni al resto del país.