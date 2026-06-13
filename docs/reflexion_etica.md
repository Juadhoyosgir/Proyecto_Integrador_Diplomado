# Reflexión Ética.

Esta reflexión actualiza la versión inicial de la Entrega 1 con lo aprendido durante el
desarrollo del modelo y el dashboard.

## 1. Riesgos identificados en el dataset y el modelo
- El modelo aprende una relación fuerte entre el entorno socioeconómico (estrato y nivel
  educativo de los padres) y el desempeño. Usado de forma indebida para clasificar y dar valor al desempeño, señalando o
  penalizando, podría **reforzar desigualdades existentes y estigmatizar** a estudiantes y
  colegios de menores recursos, que generalmente son municipios de categorias inferiores y con menores recursos.
- **Sesgo de muestra:** los datos se concentran en el área metropolitana de Medellín y en
  colegios mayormente no oficiales, y cubren solo 16 de los 125 municipios de Antioquia. El
  modelo no representa a todo el departamento ya que el dataset da un muestreo de la totalidad de los resultados de los icfes.
- **Métrica moderada (F1-macro ≈ 0.58):** el modelo se equivoca con frecuencia, por lo que
  sus predicciones no deben tomarse como certezas, si bien este valor representa una relación, no debe tomarse como verdad, es simplemente en aras del ejercicio.
- Se usan variables sensibles (estrato, género). El análisis no encontró diferencias por
  género, pero el uso de estas variables exige cuidado.

## 2. Grupos que podrían verse afectados por errores del modelo
- **Estudiantes de menores recursos** clasificados erróneamente: un error podría hacer que
  no reciban un apoyo que necesitan, o que se les etiquete injustamente, si el modelo se equivoca puede incurrir
  en que la secretaría de educación que tome la decisión no focalice correctamente.
- **Colegios mal priorizados:** una predicción equivocada podría asignar recursos a quien no
  los necesita tanto y dejar por fuera a quien sí.
- **Municipios no representados** en los datos, a los que el modelo no debería aplicarse.

## 3. Acciones de mitigación implementadas
- Se **excluyeron los puntajes** (`punt_global` y puntajes por área) como variables de
  entrada, para evitar fuga de datos y mantener la coherencia con la pregunta.
- El dashboard muestra una **advertencia ética** visible en cada predicción.
- El sistema se concibe únicamente para **focalizar apoyos** (acción positiva), nunca para
  sancionar ni para puntuar estudiantes.
- Se **documentaron las limitaciones** de la muestra y de la métrica de forma transparente.

## 4. Limitaciones conocidas del sistema
- Muestra no representativa de toda Antioquia (área metropolitana, colegios privados).
- Las variables explicativas están entrelazadas, por lo que no se puede aislar el efecto
  individual de cada una, ejemplo, que un estudiante tenga internet o no, puede estar
  muy relacionado con que los padres hayan tenido una educación superior.
- Corresponde a un solo periodo (2025-1).
- No incluye factores determinantes del aprendizaje (esfuerzo, calidad del colegio,
  acompañamiento, etc.) incluso la alimentación.
- La capacidad predictiva es moderada F1= 0.580.

## 5. Declaración de uso responsable
El resultado del modelo es **un apoyo a la toma de decisiones, no una decisión automática**.
Toda predicción debe ser revisada por una persona responsable antes de tomar cualquier
acción que afecte a estudiantes o colegios.