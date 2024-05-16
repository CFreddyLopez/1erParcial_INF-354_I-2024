# -*- coding: utf-8 -*-
"""
Created on Thu May 16 03:41:25 2024

@author: fredd
"""

# Nombre del archivo CSV
archivo_csv = 'E:/University/INF-354 Inteligencia Artificial/I-2024/1erExamen/DataSet/datos.csv'

# Lista para almacenar los datos
datos = []

# Abrir el archivo CSV en modo lectura
with open(archivo_csv, 'r') as archivo:
    # Leer cada línea del archivo
    for linea in archivo:
        # Eliminar el carácter de nueva línea al final de la línea
        linea = linea.strip()
        # Dividir la línea en valores separados por comas
        valores = linea.split(',')
        # Agregar los valores a la lista de datos
        datos.append(valores)

# Imprimir los datos
for fila in datos:
    print(fila)
