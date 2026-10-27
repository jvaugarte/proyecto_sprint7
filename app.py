
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Configuración de la aplicación
st.set_page_config(
    page_title="Análisis de vehículos - Versión 2",
    page_icon="🚗",
    layout="wide"
)

# Encabezado principal
st.header("Análisis de anuncios de vehículos usados")

st.write(
    "Explora los datos de anuncios de vehículos usados "
    "en Estados Unidos mediante gráficos interactivos."
)

# Cargar datos
ruta_csv = Path(__file__).resolve().parent / "vehicles_us.csv"

car_data = pd.read_csv(ruta_csv)

# Información general
st.subheader("Información del conjunto de datos")
st.write("Número de vehículos:", len(car_data))

# Sección de visualizaciones
st.subheader("Selecciona los gráficos que deseas visualizar")

# Casillas de verificación
build_histogram = st.checkbox("Construir un histograma")

build_scatter = st.checkbox("Construir un gráfico de dispersión")

# HISTOGRAMA
if build_histogram:
    st.write("Distribución del kilometraje de los vehículos")

    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del odómetro",
        labels={
            "odometer": "Kilometraje (millas)"
        }
    )

    st.plotly_chart(fig_hist, width="stretch")


# GRÁFICO DE DISPERSIÓN
if build_scatter:
    st.write("Relación entre el kilometraje y el precio")

    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre kilometraje y precio",
        labels={
            "odometer": "Kilometraje (millas)",
            "price": "Precio (USD)"
        },
        opacity=0.5
    )

    st.plotly_chart(fig_scatter, width="stretch")
