import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Lectura de datos
df = pd.read_csv("../../../data/final/datos_finales.csv", sep=";")

# Configuración de la página
st.set_page_config(
    page_title="Herramienta de Visualización de Datos - 13MBID",
    page_icon="📊",
    layout="wide",
)

# Título de la aplicación
st.title("Herramienta de Visualización de Datos - 13MBID")
st.write(
    "Esta aplicación permite explorar y visualizar los datos del proyecto en curso."
)
st.write("Desarrollado por: ......................")
st.markdown('----')

# Gráficos
st.header("Gráficos")
st.subheader("Caracterización de los créditos otorgados:")

# Cantidad de créditos por objetivo del mismo
creditos_x_objetivo = px.histogram(df, x='objetivo_credito', 
                                   title='Conteo de créditos por objetivo')
creditos_x_objetivo.update_layout(xaxis_title='Objetivo del crédito', yaxis_title='Cantidad')

# Visualización
st.plotly_chart(creditos_x_objetivo, use_container_width=True)


# Histograma de los importes de créditos otorgados

histograma_importes = px.histogram(df, x='importe_solicitado', nbins=10, title='Importes solicitados en créditos')
histograma_importes.update_layout(xaxis_title='Importe solicitado', yaxis_title='Cantidad')

st.plotly_chart(histograma_importes, use_container_width=True)

# Se agrega un selector para el tipo de crédito y se aplica en los gráficos siguientes

tipo_credito = st.selectbox(
    "Selecciona el tipo de crédito",
    df['objetivo_credito'].unique(),
)

st.write("Tipo de crédito seleccionado:", tipo_credito)

# Filtrar el DataFrame según el tipo de crédito seleccionado    
df_filtrado = df[df['objetivo_credito'] == tipo_credito]


# Gráfico de barras apiladas: Comparar la distribución de créditos por estado y objetivo

col1, col2 = st.columns(2)
with col1:
    barras_apiladas = px.histogram(df_filtrado, x='objetivo_credito', color='estado_credito_N', 
                               title='Distribución de créditos por estado y objetivo',
                               barmode='stack')
    barras_apiladas.update_layout(xaxis_title='Objetivo del crédito', yaxis_title='Cantidad')
    st.plotly_chart(barras_apiladas, use_container_width=True)
with col2:
    # Conteo de ocurrencias por caso
    falta_pago_counts = df_filtrado['falta_pago'].value_counts()

    # Create a Pie chart
    fig = go.Figure(data=[go.Pie(labels=falta_pago_counts.index, values=falta_pago_counts)])
    fig.update_layout(title_text='Distribución de créditos en función de registro de mora')
    st.plotly_chart(fig, use_container_width=True)

