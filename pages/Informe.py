import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide") # Recomendado para informes grandes

st.title("Mi Dashboard de Datos No Estructurados")

# URL que copiaste de Looker Studio
url_looker = "https://lookerstudio.google.com/embed/reporting/13563ba4-4408-449d-9612-f7add8ed1840/page/sgckF"

# Incrustar el informe
components.iframe(url_looker, height=1300, scrolling=True)
