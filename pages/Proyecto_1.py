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