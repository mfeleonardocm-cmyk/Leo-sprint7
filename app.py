
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el conjunto de datos
df = pd.read_csv("nombre_del_archivo.csv")  # Reemplaza con el nombre real del archivo

# Mostrar los primeros registros
st.write("Vista previa del conjunto de datos:")
st.dataframe(df.head())
df = pd.read_csv("vehicles_us.csv")

# Título de la app
st.title("Análisis de vehículos en EE.UU.")

# Vista previa del DataFrame
st.write("Vista previa del conjunto de datos:")
st.dataframe(df.head())

# Visualización: precio vs año
st.subheader("Relación entre año y precio")
fig = px.scatter(df, x="model_year", y="price", color="condition",
                 title="Precio de vehículos por año y condición",
                 labels={"model_year": "Año del modelo", "price": "Precio (USD)"})
st.plotly_chart(fig)
# Encabezado de la aplicación
st.header("Análisis interactivo de vehículos en EE.UU.")

# Cargar los datos
car_data = pd.read_csv("vehicles_us.csv")

# Botón para construir el histograma
hist_button = st.button("Construir histograma")

# Acción al hacer clic en el botón
if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

    # Crear el histograma con Plotly
    fig = px.histogram(car_data, x="odometer", nbins=30,
                       title="Distribución del kilometraje (odometer)",
                       labels={"odometer": "Kilometraje (millas)"})

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
# Encabezado de la aplicación
st.header("Análisis interactivo de vehículos en EE.UU.")

# Cargar los datos
car_data = pd.read_csv("vehicles_us.csv")

# Botón para construir el histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer", nbins=30,
                       title="Distribución del kilometraje (odometer)",
                       labels={"odometer": "Kilometraje (millas)"})
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre año del modelo y precio")
    fig = px.scatter(car_data, x="model_year", y="price", color="condition",
                     title="Precio vs Año del Modelo por Condición",
                     labels={"model_year": "Año del modelo", "price": "Precio (USD)"})
    st.plotly_chart(fig, use_container_width=True)




