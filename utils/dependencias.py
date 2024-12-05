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
categorias = data["category"]
peliculas = data["film"]
tienda = data["store"]
pagos = data["payment"]
clientes = data["customer"]
rentas = data["rental"]
inventario = data["inventory"]
peliculas_categorizadas = data["film_category"]
equipo_trabajo = data["staff"]


# Datos gráfico

# Gráfico 1
union1 = rentas.merge(inventario, on="inventory_id")
dt_barras = union1.merge(peliculas_categorizadas, on= "film_id")

dt_barras2 = dt_barras[["inventory_id","category_id"]]

dt_graf = pd.merge(dt_barras2,categorias,left_on="category_id",right_on="category_id")

# Gráfico 2
inventario2= inventario[['film_id','inventory_id']]

rentas['rental_date'] = pd.to_datetime(rentas['rental_date'])

rentas['month'] = rentas['rental_date'].dt.month_name()
rentas['year'] = rentas['rental_date'].dt.year
rentas['day'] = rentas['rental_date'].dt.day_name()

date = rentas[['inventory_id','rental_date','year','month','day']]

rentas_en_tiempo = date.groupby(date['rental_date'].dt.to_period('D')).agg({
    'inventory_id': 'count'
}).reset_index()

rentas_en_tiempo['rental_date'] = rentas_en_tiempo['rental_date'].dt.to_timestamp()


# Gráfico 3
veces_remplazada = np.random.randint(0, 6, size=len(peliculas))
peliculas['veces_remplazada'] = veces_remplazada

film_data = peliculas[['film_id','veces_remplazada','replacement_cost']]

table1= pd.merge(film_data, peliculas_categorizadas, left_on= 'film_id', right_on= 'film_id')

table2 = pd.merge(table1,categorias, left_on= 'category_id', right_on= 'category_id')