
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Análisis de vehículos",
    page_icon="🚗",
    layout="wide"
)

# Encabezado principal
st.header("Análisis de anuncios de vehículos usados")

# Descripción
st.write(
    "Esta aplicación permite explorar los datos "
    "de anuncios de vehículos usados en Estados Unidos."
)

# Localizar el archivo CSV
ruta_csv = Path(__file__).resolve().parent / "vehicles_us.csv"

# Leer los datos
car_data = pd.read_csv(ruta_csv)

# Mostrar información general
st.subheader("Información del conjunto de datos")

st.write("Número de vehículos:", len(car_data))

# Crear botón
hist_button = st.button("Construir histograma")

# Ejecutar al presionar el botón
if hist_button:

    st.write(
        "Distribución del kilometraje de los vehículos"
    )

    # Crear histograma
    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del odómetro",
        labels={
            "odometer": "Kilometraje (millas)"
        }
    )

    # Mostrar gráfico interactivo
    st.plotly_chart(
        fig,
        use_container_width=True
    )
