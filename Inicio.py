import streamlit as st
import plotly.express as px
import time
import sys
from pathlib import Path


st.set_page_config(layout="wide")

with st.spinner('Cargando...'):
    time.sleep(5)
    st.title('Proycto Final')
    st.header('Taller de Programación para el Análisis de Datos III')
    st.subheader('Dixon Jiménez')

col1, col2 = st.columns(2)
with col1:
    video_url = "https://youtu.be/_QYlaOAQFfE"
    st.video(video_url,start_time=0,autoplay=True,muted=True,loop=True)
with col2:
    st.subheader('Base de datos: Sakila Master.')
    st.text("""- actor:
Filas: Entre 1000 y 5000 (dependiendo del tamaño de la base de datos).
Columnas: 3-5 (típicamente: actor_id, first_name, last_name).
- address:
Filas: Entre 500 y 2000 (dependiendo del número de direcciones almacenadas).
Columnas: 5-7 (típicamente: address_id, address, postal_code, city_id).
- category:
Filas: Entre 10 y 30 (dependiendo del número de categorías de películas).
Columnas: 2-3 (típicamente: category_id, name).
- city:
Filas: Entre 50 y 200 (dependiendo del número de ciudades).
Columnas: 3-5 (típicamente: city_id, city, country_id).
- country:
Filas: Entre 50 y 200 (dependiendo del número de países).
Columnas: 3-5 (típicamente: country_id, country).
- customer:
Filas: Entre 1000 y 5000 (dependiendo del número de clientes).
Columnas: 8-12 (típicamente: customer_id, first_name, last_name, email, address_id, store_id).
- film:
Filas: Entre 1000 y 5000 (dependiendo del número de películas).
Columnas: 10-15 (típicamente: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features).   
- film_actor:
Filas: Entre 10000 y 50000 (dependiendo del número de actores por película).
Columnas: 2 (típicamente: actor_id, film_id).
- film_category:
Filas: Entre 5000 y 25000 (dependiendo del número de categorías por película).
Columnas: 2 (típicamente: film_id, category_id).
- inventory:
Filas: Entre 5000 y 25000 (dependiendo del número de copias de cada película).
Columnas: 3-5 (típicamente: inventory_id, film_id, store_id).
- language:
Filas: Entre 5 y 20 (dependiendo del número de idiomas).
Columnas: 2-3 (típicamente: language_id, name).
- payment:
Filas: Entre 10000 y 50000 (dependiendo del número de pagos realizados).
Columnas: 5-8 (típicamente: payment_id, customer_id, staff_id, rental_id, amount, payment_date).
- rental:
Filas: Entre 100000 y 500000 (dependiendo del número de alquileres realizados).
Columnas: 10-15 (típicamente: rental_id, rental_date, return_date, staff_id, customer_id, inventory_id, amount).
- staff:
Filas: Entre 5 y 20 (dependiendo del número de empleados).
Columnas: 5-8 (típicamente: staff_id, first_name, last_name, address_id, picture, email, store_id).
- store:
Filas: Entre 1 y 10 (dependiendo del número de tiendas).
Columnas: 5-7 (típicamente: store_id, manager_staff_id, address_id).""")

colum1, colum2 = st.columns(2)
with colum1:
    st.subheader("Dashboard: Análisis ventas por categoría")
    st.text("""
El dashboard fue creado con la intención de ver las principales métricas de ventas por categorías,
como cuales fueron sus ingresos totales, promedio de ingresos, costo de remplazo promedio, un conteo de 
películas por categorías, además podemos ver cómo se comportan las categorías por duración promedio,
costo de remplazo y ingresos totales por categorías, y que nos puede ayudar a crear estrategias de promoción de categorías y mejorar los ingresos del negocio.
            """)
with colum2:
    url = "https://youtu.be/KVmQ40yEarM"
    st.video(url,start_time=0,autoplay=True,muted=True,loop=True)
st.subheader('Semper ad meliora')
st.text('Siempre hacia cosas mejores.')
