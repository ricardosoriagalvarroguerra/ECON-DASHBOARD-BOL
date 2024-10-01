import streamlit as st
from streamlit_option_menu import option_menu

# Configuración de la página
st.set_page_config(
    page_title="Bolivia Economic Dashboard",
    page_icon="📊",
    layout="wide"
)

# CSS para hacer el fondo del menú de navegación transparente
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: transparent;
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
    st.write("Contenido de la página General.")

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
