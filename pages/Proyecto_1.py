import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import sys
from pathlib import Path

root = Path(__file__).parent.parent
sys.path.append(str(root))
from utils.dependencias import *

st.markdown(''' 
## Análisis a Sakila
            ''')



fig = px.bar(
    dt_graf,
    x="category_id",
    y="name"
)

st.plotly_chart(fig)


fig = px.bar(
    rentas_en_tiempo,
    x="rental_date" ,
    y= "inventory_id"
)
st.plotly_chart(fig)


fig = make_subplots(rows=4, cols=4, column_widths=[0.6, 0.4, 0.6, 0.4], row_heights=[0.4, 0.6, 0.4, 0.6])


row = 1
col = 1
for name in table2['name'].unique():  

    category_data = table2[table2['name'] == name]


    trace = go.Scatter(
        x=table2['veces_remplazada'],
        y=table2['replacement_cost'],
        mode='markers',
        name=name
    )

    fig.add_trace(trace, row=row, col=col)

    col += 1
    if col > 4:
        row += 1
        col = 1

fig.update_layout(
    height=900,
    width=900,
    title_text="Veces de Remplazo por Costo de Reemplazo por cada Categoría"
)

st.plotly_chart(fig)