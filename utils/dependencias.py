# Librerias para limpieza, transformación y visualización.
import pandas as pd
import sqlite3
import numpy as np
import os


# Extraer la ruta de donde se encuentra la BBDD.
def mapear_datos(nombre_bd, formato): 
    carpeta = os.path.dirname(__file__)
    db_path = os.path.join(carpeta, '..', 'data', f'{nombre_bd}{formato}')
    return db_path

# Traer todas las tablas que se enceuntran en la BBDD, y que se guarda como diccionario.
def cargar_datos(ruta_archivo):
    conn = sqlite3.connect(ruta_archivo)
    
    dataframes = {}
    
    tablas = pd.read_sql('SELECT name FROM sqlite_master WHERE type = "table"', conn)
    
    for tabla in tablas['name']:
        dataframes[tabla] = pd.read_sql(f'SELECT * FROM "{tabla}"', conn)
    
    conn.close()   
    
    return dataframes


# Se almacena la ruta de la BBDD.
ruta=  mapear_datos("sakila_master",".db")
# Se utiliza la ruta para traer la BBDD.
data = cargar_datos(ruta)

data


# Tablas de la BBDD.
rental = data['rental']
inventory = data['inventory']
film = data['film']
staff = data['staff']
film_category = data['film_category']
category = data['category']
payment = data['payment']

# Filtrado de columnas.
rentas = rental[['rental_id','rental_date','inventory_id','customer_id','staff_id']]
inventario = inventory[['inventory_id', 'film_id' , 'store_id']]
peliculas = film[['film_id', 'title', 'release_year', 'length', 'rating']]
equipo = staff[['staff_id', 'first_name']]
peliculas_categorizadas = film_category[['film_id', 'category_id']]
categorias = category[['category_id', 'name']]
pagos = payment[['payment_id', 'rental_id', 'amount']]

# Unión de tablas para la craeación de un dataframe.
mg1 = rentas.merge(pagos,on='rental_id')
mg2 = mg1.merge(inventario,on='inventory_id')
mg3 = mg2.merge(film,on='film_id')
mg4 = mg3.merge(peliculas_categorizadas,on='film_id')
mg5 = mg4.merge(categorias,on='category_id')
mg6 = mg5.merge(equipo,on='staff_id')

# Borrado de colunmas poco utiles.
df = mg6.drop(columns=['language_id','original_language_id','description','special_features','last_update'])

df['month'] = pd.to_datetime(df['rental_date']).dt.month_name()
df['year'] = pd.to_datetime(df['rental_date']).dt.year
df['day'] = pd.to_datetime(df['rental_date']).dt.day

# Data frame final
dataframe = df

# Gráfico barras.
total = dataframe.groupby('name')['amount'].sum().reset_index(name='total_amount').sort_values(by='total_amount',ascending=False).round(2)


# Gráfico de disperción

displot = dataframe.groupby('name').agg({'amount':'sum','replacement_cost':'mean','length':'mean','film_id':'count'}).reset_index().sort_values(by='amount',ascending=False).round(2)