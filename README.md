# Proyecto Integrador — Diplomado en Desarrollo Web para Analítica de Datos

Análisis de las pruebas **Saber 11° (ICFES)** del periodo 2025-1 para clasificar el
desempeño de estudiantes de **Antioquia** en niveles **bajo, medio o alto** y explorar su
relación con factores socioeconómicos.

> **Entrega 1 — Planteamiento.** No incluye modelo entrenado ni frontend; contiene la
> documentación del problema, la pregunta analítica y la exploración del dataset.

## Pregunta analítica
¿Es posible clasificar el nivel de desempeño global (bajo, medio o alto) de un estudiante de
grado 11 de colegios del departamento de Antioquia en las pruebas Saber 11, a partir de su
acceso a internet, el nivel educativo de sus padres, el estrato socioeconómico y su género,
con el fin de que la secretaría de educación departamental focalice colegios para realizar
refuerzos en los grupos con mayor riesgo de bajo desempeño?

## Dataset
- **Fuente:** ICFES — DataIcfes (https://www.icfes.gov.co/investigaciones/data-icfes/)
- **Periodo:** 2025-1 (colegios de Antioquia)
- **Tamaño:** 1.313 registros, 85 columnas (1.109 tras la limpieza)
- **Variable objetivo:** `desempeno_global` (Bajo / Medio / Alto)
- **Ubicación:** `data/raw/saber11_2025-1.csv`

## Tipo de tarea y métrica
- Clasificación multiclase.
- Métrica principal: **F1-score macro**.

## Estructura del repositorio
```
.
├── data/
│   └── raw/
│       └── saber11_2025-1.csv      # Dataset original
├── docs/
│   ├── ficha_proyecto.md           # Ficha de formulación del proyecto
│   ├── analisis_dataset.md         # Análisis cualitativo del dataset
│   └── wireframe_dashboard.png     # Boceto del dashboard
├── notebooks/
│   └── 01_exploracion.ipynb        # Exploración y limpieza del dataset
├── .gitignore
├── README.md
└── requirements.txt
```

## Cómo ejecutar el notebook
```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_exploracion.ipynb
```

## Autor
Juan Diego Hoyos Giraldo, estudiante tecnología en desarrollo de software — Diplomado en Desarrollo Web para Analítica de Datos, 2026.
