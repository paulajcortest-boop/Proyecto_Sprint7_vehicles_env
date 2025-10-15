# Librerias
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Datos
df = pd.read_csv(r"C:\Users\HP\Downloads\vehicles_us.csv")

# Titulo
st.header('Anuncio de venta de coches', divider="gray")
st.write("Esta aplicación permite visualizar la distribución de los kilómetros recorridos (odómetro) y la relación entre precio y odómetro de los coches en venta.")

st.divider()

#Filtro tipo de carro
tipos_disponibles = df['type'].dropna().unique().tolist()

tipo_seleccionado = st.multiselect(
    label="Seleccione máximo 2 tipos de carro:",
    options=tipos_disponibles,
    max_selections=2
)

# Validación si no se selecciona ningún tipo
if not tipo_seleccionado:
    st.warning("Por favor, seleccione al menos un tipo de carro para continuar.")
    st.stop()

# Aplicar filtro
df_filtrado = df[df['type'].isin(tipo_seleccionado)]

st.divider()

# Casilla de selección de gráficos
show_hist = st.checkbox('Mostrar histograma de odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión Precio vs Odómetro')

st.divider()

# Gráficos y métricas
if show_hist or show_scatter:
    col1, col2 = st.columns(2)

# Histograma
if show_hist:
    st.subheader("Histograma de odómetro")
    fig_hist = px.histogram(df_filtrado, x='odometer', title='Distribución de odómetro', height=400)
    st.plotly_chart(fig_hist, use_container_width=True)

    st.subheader("Métricas del odómetro")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Media", round(np.mean(df_filtrado['odometer']), 1))
    with c2:
        st.metric("Mediana", round(np.median(df_filtrado['odometer']), 1))
    with c3:
        st.metric("Desviación", round(np.std(df_filtrado['odometer']), 1))

# Gráfico de dispersión
if show_scatter:
    st.subheader("Gráfico de dispersión Precio vs Odómetro")
    fig_scatter = px.scatter(df_filtrado, x='odometer', y='price', color='type',
                             title='Precio vs Odómetro', height=400)
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Métricas del precio")
    c4, c5, c6 = st.columns(3)
    with c4:
        st.metric("Media", round(np.mean(df_filtrado['price']), 1))
    with c5:
        st.metric("Mediana", round(np.median(df_filtrado['price']), 1))
    with c6:
        st.metric("Desviación", round(np.std(df_filtrado['price']), 1))

st.divider()

st.write("¡Listo! Usa las casillas para visualizar los gráficos y métricas según el tipo de carro seleccionado.")