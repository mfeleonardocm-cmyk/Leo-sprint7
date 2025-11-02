
import streamlit as st
import pandas as pd
import plotly.express as px

# Título y encabezado
st.title("Análisis de vehículos en EE.UU.")
st.header("Exploración interactiva del conjunto de datos")

# Cargar el conjunto de datos
df = pd.read_csv("vehicles_us.csv")

# Vista previa del DataFrame
st.write("Vista previa del conjunto de datos:")
st.dataframe(df.head())

# Botón para construir el histograma
hist_button = st.button("Construir histograma", key="hist_button")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(df, x="odometer", nbins=30,
                       title="Distribución del kilometraje (odometer)",
                       labels={"odometer": "Kilometraje (millas)"})
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión", key="scatter_button")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre año del modelo y precio")
    fig = px.scatter(df, x="model_year", y="price", color="condition",
                     title="Precio vs Año del Modelo por Condición",
                     labels={"model_year": "Año del modelo", "price": "Precio (USD)"})
    st.plotly_chart(fig, use_container_width=True)






