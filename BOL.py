import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Bolivia Economic Dashboard",
    page_icon="📊",
    layout="wide"
)

# CSS para hacer el fondo del menú de navegación no transparente
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: none;
        box-shadow: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Menú de navegación minimalista en la barra lateral con tamaño de fuente ajustado y título con emoji
with st.sidebar:
    page = option_menu(
        menu_title="🇧🇴 Bolivia",  # Título del menú
        options=["General", "Sector Real", "Sector Fiscal", "Sector Monetario", "Sector Externo", "Sector Financiero"],
        icons=["bi bi-bar-chart", "", "", "", "", ""],  # Iconos para cada opción
        menu_icon="🇧🇴",  # Emoji de la bandera de Bolivia como icono del menú
        default_index=0,
        orientation="vertical",
        styles={
            "nav-link": {
                "font-size": "12px",  # Ajusta el tamaño de la fuente aquí
            },
            "nav-link-selected": {
                "font-size": "12px",  # Asegura que el tamaño sea consistente al seleccionar
            },
            # Mantén el estilo nativo sin modificar más estilos
        }
    )

# Contenido de las páginas con título personalizado y más pequeño
if page == "General":
    st.markdown("<h1 style='text-align: left; margin-top: -50px; font-size: 25px;'>General</h1>", unsafe_allow_html=True)
    
    # Cargar los datos de la hoja 'diario'
    file_path = 'BOL-BDD.xlsx'
    diaria_data = pd.read_excel(file_path, sheet_name='diario')
    
    # Obtener el último valor de la variable 'paralelo' y la fecha del último dato
    ultimo_dato = diaria_data.iloc[-1]
    ultimo_valor_paralelo = ultimo_dato['paralelo']
    fecha_ultimo_dato = ultimo_dato['date']
    
    # Mostrar una tarjeta métrica con el último valor de 'paralelo' y la fecha correspondiente
    st.metric(label="Tipo de Cambio Paralelo", value=f"{ultimo_valor_paralelo}", delta=f"Última fecha: {fecha_ultimo_dato}")

elif page == "Sector Real":
    st.markdown("<h1 style='text-align: left; margin-top: -50px; font-size: 25px;'>Sector Real</h1>", unsafe_allow_html=True)
    st.write("Contenido de la página Sector Real.")

elif page == "Sector Fiscal":
    st.markdown("<h1 style='text-align: left; margin-top: -50px; font-size: 25px;'>Sector Fiscal</h1>", unsafe_allow_html=True)
    st.write("Contenido de la página Sector Fiscal.")

elif page == "Sector Monetario":
    st.markdown("<h1 style='text-align: left; margin-top: -50px; font-size: 25px;'>Sector Monetario</h1>", unsafe_allow_html=True)
    st.write("Contenido de la página Sector Monetario.")

elif page == "Sector Externo":
    st.markdown("<h1 style='text-align: left; margin-top: -50px; font-size: 25px;'>Sector Externo</h1>", unsafe_allow_html=True)
    st.write("Contenido de la página Sector Externo.")

elif page == "Sector Financiero":
    st.markdown("<h1 style='text-align: left; margin-top: -50px; font-size: 25px;'>Sector Financiero</h1>", unsafe_allow_html=True)
    st.write("Contenido de la página Sector Externo.")
