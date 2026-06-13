# Diccionario de datos

**Dataset procesado:** `data/processed/dataset_limpio.csv` (1.109 registros, 11 columnas).
Resultados del examen Saber 11° 2025-1 (ICFES) de colegios del departamento de Antioquia.

| Variable | Tipo | Rol | Descripción |
|---|---|---|---|
| `desempeno_global` | Categórica (Bajo/Medio/Alto) | **Variable objetivo** | Nivel de desempeño global del estudiante, derivado de `punt_global` (Bajo ≤220, Medio 221–320, Alto >320). |
| `estu_genero` | Categórica (F/M) | Feature | Género del estudiante. |
| `fami_estratovivienda` | Categórica (Estrato 1–6) | Feature | Estrato socioeconómico de la vivienda. |
| `fami_tieneinternet` | Categórica (Sí/No) | Feature | Indica si el hogar tiene acceso a internet. |
| `fami_educacionmadre` | Categórica | Feature | Máximo nivel educativo alcanzado por la madre. |
| `fami_educacionpadre` | Categórica | Feature | Máximo nivel educativo alcanzado por el padre. |
| `punt_global` | Numérica (0–500) | Apoyo / origen del objetivo | Puntaje global de la prueba; base para derivar `desempeno_global` y para gráficas exploratorias. |
| `cole_mcpio_ubicacion` | Categórica (texto) | Contexto | Nombre del municipio donde está el colegio. |
| `cole_cod_mcpio_ubicacion` | Numérica (código DANE) | Contexto | Código DANE del municipio, para enlazar con el mapa. |
| `cole_naturaleza` | Categórica (Oficial/No oficial) | Contexto | Naturaleza del colegio. |
| `cole_area_ubicacion` | Categórica (Urbana/Rural) | Contexto | Zona de ubicación del colegio. |