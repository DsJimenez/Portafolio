import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import sys
from pathlib import Path

root = Path(__file__).parent.parent
sys.path.append(str(root))
from utils.dependencias import *

st.set_page_config(layout="wide")

st.markdown(''' 
## Ingresos por categorías
            ''')



cat = dataframe['name'].unique()
cat_seleccionada = st.multiselect(
    "Categoría",
    cat)

if cat_seleccionada:
    mascara = displot['name'].isin(cat_seleccionada)
    total_fil = displot[mascara]
else:
    total_fil = displot

col1, col2, col3, col4 = st.columns(4)

colum1, colum2 = st.columns(2)

with col1:
    st.metric(
        label='Ingreso por Categoria',
        value=f'${total_fil['amount'].sum():.2f}')
    
with colum1:
    fig = px.bar(total_fil,
        x="amount",
        y="name",
        labels={"amount":"Ingreso Total",
                "name":"Categoía"},
        color="name",
        text_auto=True,
        title="Ingresos por categoría")
    fig.update_traces(textfont=dict(size=22))
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)    

#---------------------------------------------------------------------------------------------#

with col2:
    st.metric(
        label='Ingreso Promedio por Categoria',
        value=f'${total_fil['amount'].mean():.2f}')
    
with colum2:
    fig = px.scatter(
        total_fil,
        x='length',
        y='replacement_cost',
        color='name',
        size='amount',
        labels={'length':'Duración(min)',
                'replacement_cost':'Costo de Remplazo',
                'name':'Categoría',
                'amount':'Ingresos'},
                title="Distribución por duración, costo de remplazo y ingresos totales")
    st.plotly_chart(fig)    

#---------------------------------------------------------------------------------------------#

fig = px.bar(
    total_fil,
    x='film_id',
    y='name',
    color='name',
    labels={'film_id':'Conteo de Películas',
            'name':'Categorías'},
            text_auto=True,
            title='Comportamiento de las categorías según duración, costo de remplazo e ingresos percibidos')
fig.update_traces(textfont=dict(size=22))
fig.update_layout(showlegend=False)
st.plotly_chart(fig)

#--------------------------------------------------------------------------------------------#

with col3:
    st.metric(
        label='Costo de remplazo promedio',
        value=f'${total_fil['replacement_cost'].mean():.2f}')
    
with col4:
    st.metric(
        label='Conteo de películas',
        value=f'{total_fil['film_id'].sum():.0f}')