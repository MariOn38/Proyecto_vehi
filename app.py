import streamlit as st 
import pandas as pd 
import plotly_express as px 

df_vehi = pd.read_csv('vehicles_us.csv') #Carga de datos 
st.header('Análisis de vehículos') #Encabezado 
hist_button = st.button('Construir un histograma') #Crear botón

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de la venta de vehiculos')
    fig = px.histogram(df_vehi, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
disp_button = st.button('Construir un gráfico de dispersión')

if disp_button:
    st.write('Creando un gráfico de dispersión para el conjunto de datos de la venta de vehiculos')
    disp = px.scatter(df_vehi, x='odometer', y='price')
    st.plotly_chart(disp, use_container_width=True)