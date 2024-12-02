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
union1 = rentas.merge(inventario, on="inventory_id")
dt_barras = union1.merge(peliculas_categorizadas, on= "film_id")

dt_barras2 = dt_barras[["inventory_id","category_id"]]

dt_graf = pd.merge(dt_barras2,categorias,left_on="category_id",right_on="category_id")