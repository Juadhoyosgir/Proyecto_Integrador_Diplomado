# Ficha de formulación del proyecto integrador

## 1. Datos del estudiante
- JUAN DIEGO HOYOS GIRALDO
- Tecnología en Desarrollo de Software — Diplomado en Desarrollo Web para Analítica de Datos
- 6 junio 2025

## 2. Nombre del proyecto
Clasificación del desempeño en las pruebas Saber 11 en Antioquia según factores socioeconómicos

## 3. Planteamiento del problema
En el contexto de la educación media en el departamento de Antioquia, la secretaría de
educación departamental no cuenta con una herramienta consolidada que le permita
identificar de manera anticipada qué grupos de estudiantes presentan mayor riesgo de
obtener un desempeño bajo en las pruebas Saber 11°, la identificación de factores de riesgo para la población estudiantil dependen de datos que son tomados de excel y no son de fácil acceso para la secretaria en la toma de decisiones, ni qué factores de su entorno se
relacionan con ese resultado. 

Esta situación dificulta focalizar de forma oportuna los programas de refuerzo y los recursos, que suelen asignarse de manera general y reactiva. Por ello, se propone desarrollar una aplicación web analítica que, a partir del dataset de resultados Saber 11° del periodo 2025-1 publicado por el ICFES (colegios de Antioquia, 1.313 registros), permita clasificar el nivel de desempeño global de un estudiante en bajo, medio o alto, usando variables socioeconómicas como el estrato de la vivienda, el acceso a internet, el género y el nivel educativo de la madre y del padre. El propósito es apoyar a la secretaría de educación departamental en la decisión de focalizar colegios y priorizar acciones de refuerzo hacia los grupos con mayor probabilidad de desempeño bajo,
de manera preventiva y apoyar su proceso formativo reduciendo las brechas sociales que se acrecentan cada día más.

## 4. Pregunta analítica
¿Es posible clasificar el nivel de desempeño global (bajo, medio o alto) de un estudiante
de grado 11 de colegios del departamento de Antioquia en las pruebas Saber 11, a partir de
su acceso a internet, el nivel educativo de sus padres, el estrato socioeconómico y su
género, con el fin de que la secretaría de educación departamental focalice colegios para
realizar refuerzos en los grupos con mayor riesgo de bajo desempeño?

## 5. Tipo de tarea y métrica de evaluación
- **Tipo de tarea:** Clasificación.
- **Métrica principal:** F1-score macro
- **Justificación de la métrica:** -
## 6. Descripción del dataset
- **Nombre:** Resultados Examen Saber 11° — Periodo 2025-1
- **Fuente (URL):** ICFES — DataIcfes, https://www.icfes.gov.co/investigaciones/data-icfes/
- **Licencia:** Datos de acceso público publicados por el ICFES; uso académico permitido.
- **Número de filas:** 1.313 (1.109 tras eliminar registros incompletos)
- **Número de columnas:** 85 (se seleccionaron 14 para el análisis)
- **Descripción general:** Resultados a nivel de estudiante del examen Saber 11°
(obligatorio para graduarse del bachillerato), con puntajes por área, puntaje global y
variables del colegio y de la situación socioeconómica familiar. Corresponde en su
totalidad a colegios del departamento de Antioquia.

## 7. Variables
- **Variable objetivo (y):** 'desempeno_global' — nivel de desempeño global (Bajo/Medio/Alto),
  derivado al clasificar el 'punt_global' (0–500).
- **Variables de entrada principales (X):**
  - 'fami_estratovivienda': estrato socioeconómico de la vivienda (1 a 6).
  - 'fami_educacionmadre': máximo nivel educativo de la madre.
  - 'fami_educacionpadre': máximo nivel educativo del padre.
  - 'fami_tieneinternet': si el hogar tiene acceso a internet (Sí/No).
  - 'estu_genero': género del estudiante (F/M).

## 8. Usuario final y decisión
- **Usuario:** Secretaría de Educación departamental de Antioquia (equipo de calidad educativa).
- **Decisión que apoyará:** Focalizar colegios y priorizar programas de refuerzo hacia los
grupos de estudiantes con mayor probabilidad de desempeño bajo, de forma anticipada, los colegios en general tienen una cantidad de estudiantes determinadas por unos estratos, nivel educativo de los padres, es así como fin de el análisis no es identificar estudiantes, sino identificar los colegios donde se encuentran estudiantes con desempeño bajo para así apoyar estas comunidades que son más vulnerables, un ejemplo claro es que un colegio oficial ubicado en el municipio de San Carlos Antioquia tendrá estudiantes en estratos 1, 2 y 3 con padres con nivel educativo muy variable comparado con un colegio ubicado en las palmas en medellín que posiblemente este entre los estrados 5 y 6, con el nivel educativo superior.

## 9. Implicaciones éticas
El análisis muestra una relación fuerte entre el entorno socioeconómico (estrato y educación
de los padres) y el desempeño. Un modelo que aprenda esta relación corre el riesgo de
**estigmatizar o reforzar desigualdades** si se usa para rankear o penalizar estudiantes o
colegios. **Mitigación:** el modelo se usará únicamente para asignar apoyos adicionales, recursos adicionales, grupos de estudios, o cualquier otra acción que una secretaria de educación considere pertinente para mejorar las brechas sociales, nunca para sancionar; se documentarán sus sesgos y limitaciones y se
usará con transparencia. El análisis no encontró diferencias por género, lo que
reduce el riesgo de un sesgo de género en los resultados.)

## 10. URL del repositorio GitHub
https://github.com/Managerfk/Proyecto-Integrador-Diplomado-Web-