"""
Dashboard de Streamlit para la clasificación del desempeño en las pruebas
Saber 11 de Antioquia (niveles Bajo / Medio / Alto) según variables
socioeconómicas.

Ejecutar con:  streamlit run app_final.py
"""

import json
from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------------------------------- #
# Rutas (relativas a este archivo usando pathlib)
# --------------------------------------------------------------------------- #
BASE_DIR = Path(__file__).resolve().parent
RUTA_MODELO = BASE_DIR / "models" / "modelo_final.pkl"
RUTA_METRICAS = BASE_DIR / "models" / "model_metadata.json"
RUTA_DATOS = BASE_DIR / "data" / "processed" / "dataset_limpio.csv"

# Orden lógico de los niveles de desempeño (para gráficas consistentes)
ORDEN_NIVELES = ["Bajo", "Medio", "Alto"]

# Columnas usadas como variables de entrada del modelo
COLUMNAS_ENTRADA = [
    "estu_genero",
    "fami_estratovivienda",
    "fami_tieneinternet",
    "fami_educacionmadre",
    "fami_educacionpadre",
]

# --------------------------------------------------------------------------- #
# Configuración de la página
# --------------------------------------------------------------------------- #
st.set_page_config(
    page_title="Desempeño Saber 11 - Antioquia",
    layout="wide",
)
st.title("📊 Clasificación del desempeño en las pruebas Saber 11 - Antioquia")
st.caption(
    "Análisis exploratorio y predicción del nivel de desempeño "
    "(Bajo / Medio / Alto) según variables socioeconómicas."
)


# --------------------------------------------------------------------------- #
# Carga de recursos (una sola vez gracias al cacheo de Streamlit)
# --------------------------------------------------------------------------- #
@st.cache_resource
def cargar_modelo():
    """Carga el Pipeline de sklearn entrenado."""
    return joblib.load(RUTA_MODELO)


@st.cache_data
def cargar_metricas():
    """Lee las métricas del modelo desde el JSON de metadatos."""
    with open(RUTA_METRICAS, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def cargar_datos():
    """Lee el dataset procesado."""
    return pd.read_csv(RUTA_DATOS)


# Cargamos los tres recursos
modelo = cargar_modelo()
metricas = cargar_metricas()
df = cargar_datos()


# --------------------------------------------------------------------------- #
# Pestañas principales
# --------------------------------------------------------------------------- #
tab_eda, tab_pred = st.tabs(["🔎 Análisis exploratorio", "🤖 Predicción"])


# =========================================================================== #
# PESTAÑA 1 — ANÁLISIS EXPLORATORIO
# =========================================================================== #
with tab_eda:
    st.header("Análisis exploratorio de datos")

    # --- Filtro por municipio (afecta a las gráficas 1 y 2) --------------- #
    municipios = sorted(df["cole_mcpio_ubicacion"].dropna().unique())
    opciones_municipio = ["Todos"] + municipios
    municipio_sel = st.selectbox(
        "Filtrar por municipio (afecta a las gráficas 1 y 2):",
        opciones_municipio,
        index=0,
    )

    # Aplicamos el filtro: si es "Todos" usamos el dataset completo
    if municipio_sel == "Todos":
        df_filtrado = df
    else:
        df_filtrado = df[df["cole_mcpio_ubicacion"] == municipio_sel]

    # --- Gráfica 1: Distribución del nivel de desempeño ------------------- #
    st.subheader("1. Distribución del nivel de desempeño")
    conteo = (
        df_filtrado["desempeno_global"]
        .value_counts()
        .reindex(ORDEN_NIVELES)          # orden Bajo / Medio / Alto
        .dropna()
        .reset_index()
    )
    conteo.columns = ["Nivel de desempeño", "Cantidad de estudiantes"]

    fig1 = px.bar(
        conteo,
        x="Nivel de desempeño",
        y="Cantidad de estudiantes",
        color="Nivel de desempeño",
        category_orders={"Nivel de desempeño": ORDEN_NIVELES},
        title=f"Distribución del nivel de desempeño ({municipio_sel})",
        text="Cantidad de estudiantes",
    )
    fig1.update_layout(
        xaxis_title="Nivel de desempeño",
        yaxis_title="Cantidad de estudiantes",
    )
    st.plotly_chart(fig1, use_container_width=True)

    # --- Gráfica 2: Desempeño según estrato (barras apiladas en %) -------- #
    st.subheader("2. Nivel de desempeño según estrato (% apilado)")
    # Tabla cruzada estrato x nivel, normalizada por fila (porcentaje)
    tabla = pd.crosstab(
        df_filtrado["fami_estratovivienda"],
        df_filtrado["desempeno_global"],
        normalize="index",
    ) * 100

    # Reordenamos las columnas según el orden lógico de niveles (si existen)
    columnas_presentes = [n for n in ORDEN_NIVELES if n in tabla.columns]
    tabla = tabla[columnas_presentes].reset_index()

    # Pasamos a formato largo para plotly
    tabla_larga = tabla.melt(
        id_vars="fami_estratovivienda",
        var_name="Nivel de desempeño",
        value_name="Porcentaje",
    )

    fig2 = px.bar(
        tabla_larga,
        x="fami_estratovivienda",
        y="Porcentaje",
        color="Nivel de desempeño",
        category_orders={"Nivel de desempeño": ORDEN_NIVELES},
        title=f"Composición del desempeño por estrato ({municipio_sel})",
    )
    fig2.update_layout(
        barmode="stack",
        xaxis_title="Estrato de vivienda",
        yaxis_title="Porcentaje de estudiantes (%)",
    )
    st.plotly_chart(fig2, use_container_width=True)

    # --- Gráfica 3: Ranking de municipios por % de desempeño "Bajo" ------- #
    # Esta gráfica usa SIEMPRE todos los municipios (ignora el filtro).
    st.subheader("3. Ranking de municipios por % de desempeño Bajo (prioridad)")

    # Porcentaje de "Bajo" por municipio
    cruce_mcpio = pd.crosstab(
        df["cole_mcpio_ubicacion"],
        df["desempeno_global"],
        normalize="index",
    ) * 100

    # Aseguramos que exista la columna "Bajo"
    pct_bajo = (
        cruce_mcpio.get("Bajo", 0)
        .sort_values(ascending=True)   # ascendente -> el mayor queda arriba en barra horizontal
        .reset_index()
    )
    pct_bajo.columns = ["Municipio", "Porcentaje Bajo"]

    fig3 = px.bar(
        pct_bajo,
        x="Porcentaje Bajo",
        y="Municipio",
        orientation="h",
        title="Municipios priorizados por mayor % de desempeño Bajo",
    )
    fig3.update_layout(
        xaxis_title="Porcentaje de estudiantes con desempeño Bajo (%)",
        yaxis_title="Municipio",
        # Altura dinámica para que se vean todos los municipios
        height=max(400, 22 * len(pct_bajo)),
    )
    st.plotly_chart(fig3, use_container_width=True)


# =========================================================================== #
# PESTAÑA 2 — PREDICCIÓN
# =========================================================================== #
with tab_pred:
    st.header("Predicción del nivel de desempeño")

    # --- Métricas del modelo leídas del JSON (no escritas a mano) --------- #
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Modelo", metricas["modelo"])
    col_m2.metric("Métrica principal", metricas["metrica_principal"])
    col_m3.metric("Valor de la métrica", f"{metricas['valor_metrica']:.3f}")

    st.divider()

    # --- Formulario con las 5 variables de entrada ------------------------ #
    st.subheader("Ingresa las variables socioeconómicas")

    with st.form("formulario_prediccion"):
        cols = st.columns(2)

        # Cada selectbox toma como opciones los valores únicos reales del CSV.
        # Como siempre hay un valor por defecto (índice 0), el form nunca falla
        # aunque el usuario no cambie ningún campo.
        genero = cols[0].selectbox(
            "Género del estudiante",
            sorted(df["estu_genero"].dropna().unique()),
        )
        estrato = cols[1].selectbox(
            "Estrato de vivienda",
            sorted(df["fami_estratovivienda"].dropna().unique()),
        )
        internet = cols[0].selectbox(
            "¿Tiene internet en el hogar?",
            sorted(df["fami_tieneinternet"].dropna().unique()),
        )
        educ_madre = cols[1].selectbox(
            "Nivel educativo de la madre",
            sorted(df["fami_educacionmadre"].dropna().unique()),
        )
        educ_padre = cols[0].selectbox(
            "Nivel educativo del padre",
            sorted(df["fami_educacionpadre"].dropna().unique()),
        )

        boton_predecir = st.form_submit_button("Predecir", type="primary")

    # --- Lógica de predicción --------------------------------------------- #
    if boton_predecir:
        # Armamos un DataFrame de una fila con los mismos nombres de columna
        # que espera el Pipeline del modelo.
        entrada = pd.DataFrame(
            [
                {
                    "estu_genero": genero,
                    "fami_estratovivienda": estrato,
                    "fami_tieneinternet": internet,
                    "fami_educacionmadre": educ_madre,
                    "fami_educacionpadre": educ_padre,
                }
            ],
            columns=COLUMNAS_ENTRADA,
        )

        # Predicción del nivel y de las probabilidades por clase
        nivel_predicho = modelo.predict(entrada)[0]
        probabilidades = modelo.predict_proba(entrada)[0]

        # Buscamos la probabilidad asociada a la clase predicha
        clases = list(modelo.classes_)
        idx_clase = clases.index(nivel_predicho)
        prob_clase = probabilidades[idx_clase]

        # --- Resultado en grande ----------------------------------------- #
        st.subheader("Resultado de la predicción")
        st.markdown(f"## Nivel estimado: **{str(nivel_predicho).upper()}**")
        st.markdown(f"### Probabilidad: **{prob_clase:.0%}**")

        # Mensaje en lenguaje natural
        st.success(
            f"El modelo estima un desempeño **{str(nivel_predicho).upper()}**, "
            f"con probabilidad de {prob_clase:.0%}."
        )

        # Detalle de probabilidades por cada clase
        st.write("Probabilidad estimada por nivel:")
        df_probs = pd.DataFrame(
            {"Nivel": clases, "Probabilidad": probabilidades}
        ).sort_values("Probabilidad", ascending=False)
        df_probs["Probabilidad"] = (df_probs["Probabilidad"] * 100).round(1)
        st.dataframe(
            df_probs.rename(columns={"Probabilidad": "Probabilidad (%)"}),
            hide_index=True,
            use_container_width=True,
        )

    # --- Advertencia ética (se muestra SIEMPRE) --------------------------- #
    st.info(
        "El resultado es una estimación generada por el modelo. Debe ser "
        "revisado por una persona responsable antes de tomar cualquier "
        "decisión."
    )
