# proyecto_sprint7
proyecto sprint 7 herramientas de desarrollo de software

# Proyecto Sprint 7 — Análisis de vehículos usados

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web interactiva para realizar un análisis exploratorio de datos sobre anuncios de vehículos usados en Estados Unidos.

La aplicación permite visualizar información del conjunto de datos `vehicles_us.csv`, utilizando Python, pandas, Plotly y Streamlit.

## Funcionalidades

- **Histograma:** muestra la distribución del kilometraje (`odometer`) de los vehículos publicados.
- **Gráfico de dispersión:** muestra la relación entre el kilometraje (`odometer`) y el precio (`price`) de los vehículos.
- **Casillas de verificación:** permiten activar o desactivar cada gráfico de manera independiente.
- **Información general:** muestra la cantidad de registros contenidos en el conjunto de datos.

## Tecnologías utilizadas

- Python
- pandas
- Plotly
- Streamlit
- Jupyter Notebook
- Git y GitHub
- Render

## Estructura del proyecto

```text
proyecto_sprint7/
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── README.md
├── .gitignore
└── notebooks/
    └── EDA.ipynb
```

## Ejecución local

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Iniciar la aplicación:

```bash
streamlit run app.py
```

## Aplicación web

**Enlace de Render:** Pendiente de agregar después del despliegue.

## Autor

jvaugarte

## Propósito académico

Proyecto desarrollado como parte del Sprint 7 del programa de Ciencia de Datos de TripleTen.

## Aplicación web desplegada en Render

**Enlace público:** https://proyecto-sprint7-xvd1.onrender.com/

