# Sistema de clasificación del desempeño en las pruebas Saber 11 (Antioquia)

## Descripción
Una Secretaría de Educación no cuenta con una herramienta consolidada para identificar
anticipadamente qué grupos de estudiantes presentan mayor riesgo de desempeño bajo en las
pruebas Saber 11°. Este proyecto desarrolla una aplicación web analítica que clasifica el
nivel de desempeño global (Bajo, Medio o Alto) a partir de variables socioeconómicas, para
apoyar la focalización de programas de refuerzo en los municipios de Antioquia.

## Pregunta analítica
¿Es posible clasificar el nivel de desempeño global (bajo, medio o alto) de un estudiante de
grado 11 de colegios del departamento de Antioquia en las pruebas Saber 11, a partir de su
acceso a internet, el nivel educativo de sus padres, el estrato socioeconómico y su género,
con el fin de que la secretaría de educación departamental focalice colegios para realizar
refuerzos en los grupos con mayor riesgo de bajo desempeño?

## Dataset
- **Fuente:** ICFES – DataIcfes (https://www.icfes.gov.co/investigaciones/data-icfes/)
- **Periodo:** 2025-1 (colegios de Antioquia)
- **Licencia:** datos de acceso público del ICFES; uso académico citando la fuente.
- **Variables principales:** género, estrato de la vivienda, acceso a internet, nivel
  educativo de la madre y del padre (entradas); `desempeno_global` (objetivo).

## Arquitectura de la solución
El flujo va desde los datos crudos del ICFES, pasando por la limpieza y el entrenamiento del
modelo, hasta el dashboard que consume el usuario final. Ver `docs/arquitectura.md` y el
diagrama `docs/arquitectura.png`.

## Estructura del repositorio
```
.
├── app_final.py                  # Dashboard Streamlit
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                      # Dataset original
│   ├── processed/                # Dataset limpio
│   └── antioquia_municipios.geojson
├── notebooks/
│   ├── 01_exploracion.ipynb      # Entrega 1
│   ├── 02_eda_limpieza.ipynb     # Pipeline de limpieza
│   └── 03_modelado.ipynb         # Entrenamiento y comparación
├── src/ml/
│   └── entrenar_modelo.py        # Script de entrenamiento reproducible
├── models/
│   ├── modelo_final.pkl          # Modelo serializado
│   └── model_metadata.json       # Métricas y metadatos
└── docs/
    ├── ficha_proyecto.md
    ├── analisis_dataset.md
    ├── diccionario_datos.md
    ├── arquitectura.md
    ├── arquitectura.png
    ├── wireframe_dashboard.png
    └── reflexion_etica.md
```

## Instalación y ejecución
```bash
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1   |   Git Bash: source venv/Scripts/activate
pip install -r requirements.txt
streamlit run app_final.py
```

## Resultados del modelo
- **Modelo:** Regresión Logística (comparada con Random Forest).
- **Métrica principal:** F1-score macro = **0.582** (Accuracy ≈ 0.599).
- La métrica es moderada porque las variables socioeconómicas explican una parte real, pero
  no total, del desempeño. Detalle en `notebooks/03_modelado.ipynb`.

## Consideraciones éticas
El modelo asocia el entorno socioeconómico con el desempeño, por lo que debe usarse solo para
focalizar apoyos, nunca para penalizar o rankear. El resultado es un apoyo a la decisión, no
una decisión automática. Detalle completo en `docs/reflexion_etica.md`.

## Autor
Juan Diego Hoyos Giraldo — Tecnología en Desarrollo de Software, Diplomado en Desarrollo Web
para Analítica de Datos. 2026.