import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Función para cargar la base de datos con caché
@st.cache_data
def cargar_datos():
    file_path = 'BOL-BDD.xlsx'  # Ruta correcta del archivo cargado
    return pd.read_excel(file_path, sheet_name=None)  # Cargar todas las hojas

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
    .metric .delta {
        color: white !important;
    }
    .small-metric .css-1v3fvcr {
        font-size: 20px !important;
    }
    .metric-container {
        display: block;
        gap: 20px;
        margin-top: 20px;
    }
    .metric-card {
        font-size: 14px !important;
        margin-top: -10px;
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
    
    # Cargar los datos de todas las hojas usando la función de caché
    data = cargar_datos()
    diaria_data = data['diario']
    mensual_data = data['mensual']
    
    # Asegurarse de que la columna 'date' sea de tipo datetime
    if 'date' in diaria_data.columns:
        diaria_data['date'] = pd.to_datetime(diaria_data['date'], errors='coerce')
    if 'date_ipc' in mensual_data.columns:
        mensual_data['date_ipc'] = pd.to_datetime(mensual_data['date_ipc'], errors='coerce')
    
    # Eliminar filas con valores nulos en 'paralelo' o 'date'
    diaria_data = diaria_data.dropna(subset=['paralelo', 'date'])
    mensual_data = mensual_data.dropna(subset=['General', 'date_ipc'])
    
    # Mostrar tarjetas métricas una debajo de la otra, de manera vertical
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    
    # Obtener el último valor de la variable 'paralelo' y el valor anterior para calcular la diferencia
    if not diaria_data.empty:
        ultimo_dato = diaria_data.iloc[-1]
        ultimo_valor_paralelo = ultimo_dato['paralelo']
        fecha_ultimo_dato_paralelo = ultimo_dato['date']
        
        if len(diaria_data) > 1:
            valor_anterior_paralelo = diaria_data.iloc[-2]['paralelo']
            delta = ultimo_valor_paralelo - valor_anterior_paralelo
        else:
            delta = 0
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="Tc Paralelo",
                value=f"{ultimo_valor_paralelo:.2f}",  # Reducir el tamaño del valor mostrado
                delta=f"{delta:.2f}"
            )
            st.markdown(f"<div class='metric-card'>{fecha_ultimo_dato_paralelo.date()}</div>", unsafe_allow_html=True)
    
    # Obtener el último valor de la inflación (General)
    if not mensual_data.empty:
        ultimo_dato_mensual = mensual_data.iloc[-1]
        ultimo_valor_general = ultimo_dato_mensual['General']
        fecha_ultimo_dato_mensual = ultimo_dato_mensual['date_ipc']
        
        # Mostrar tarjeta métrica de inflación
        with col2:
            st.metric(
                label="Inflación",
                value=f"{ultimo_valor_general:.2f}"
            )
            st.markdown(f"<div class='metric-card'>{fecha_ultimo_dato_mensual.date()}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

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
