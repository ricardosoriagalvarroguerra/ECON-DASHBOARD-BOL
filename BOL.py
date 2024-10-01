import streamlit as st
from streamlit_option_menu import option_menu

# Configuración de la página
st.set_page_config(
    page_title="Bolivia Economic Dashboard",
    page_icon="📊",
    layout="wide"
)

# Barra de navegación con option_menu
page = option_menu(
    menu_title=None,  # No mostrar el título del menú
    options=["Overview", "Indicadores Clave", "Comercio Exterior", "Coyuntura Laboral"],
    icons=["house", "bar-chart", "briefcase", "clipboard"],  # Puedes cambiar los iconos
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal"
)

# Contenido de las páginas
if page == "Overview":
    st.markdown("<h3 style='text-align: left; margin-top: -50px;'>Overview</h3>", unsafe_allow_html=True)
    st.write("Contenido de la página Overview")

elif page == "Indicadores Clave":
    st.title("Indicadores Clave")
    st.write("Contenido de Indicadores Clave")

elif page == "Comercio Exterior":
    st.title("Comercio Exterior")
    st.write("Contenido de Comercio Exterior")

elif page == "Coyuntura Laboral":
    st.title("Coyuntura Laboral")
    st.write("Contenido de Coyuntura Laboral")
