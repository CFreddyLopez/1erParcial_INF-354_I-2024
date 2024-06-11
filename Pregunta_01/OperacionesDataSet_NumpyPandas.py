# -*- coding: utf-8 -*-
"""
Created on Tue May 21 08:22:38 2024

@author: fredd
"""
from tabulate import tabulate
import numpy as np

archivo_csv = 'E:/University/INF-354 Inteligencia Artificial/I-2024/1erExamen/DataSet/datos.csv'

DATA_SET = []

# Abrir el archivo CSV en modo lectura y Preprocesar Comillas y Coma en los valores decimales
with open(archivo_csv, 'r') as archivo:
    i=0
    columas=10
    
    for linea in archivo:
        linea = linea.strip()
        valores = linea.split(',')
        dato_concatenado=[]
        indice_c=0
        registro = []
        for indice, dato in enumerate(valores):
            if '"' in dato:
                dato_concatenado.append(valores[indice].replace('"', ""))
                indice_c=indice_c+1
                if indice_c==2:
                    indice_c=0
                    nuevo_dato=dato_concatenado[0]+"."+dato_concatenado[1]
                    registro.append(nuevo_dato)
                    dato_concatenado.clear()
            else:
                registro.append(dato)
        
        DATA_SET.append(registro)

del DATA_SET[0]

# Platform(String)=0
# Genre(String)=1
# Publisher(String)=2 
# NA_Sales(float)=3
# EU_Sales(float)=4 
# JP_Sales(float)=5
# Other_Sales(float)=6
# Global_Sales(float)=7
# Rating(String)=8
# Critic_Score_Class(String)=9

# Definir el tipo de datos para cada columna
dtype = [('Platform', 'U100'), 
         ('Genre', 'U100'), 
         ('Publisher', 'U100'), 
         ('NA_Sales', 'f4'), 
         ('EU_Sales', 'f4'), 
         ('JP_Sales', 'f4'),
         ('Other_Sales', 'f4'),
         ('Global_Sales', 'f4'),
         ('Rating', 'U100'),
         ('Critic_Score', 'U100')
         ]


#Ordenar Datos por la Columna NA_Sales 
lista_ordenada = sorted(DATA_SET, key=lambda x: float(x[3]),reverse=False)
datos = np.array([tuple(row) for row in lista_ordenada], dtype=dtype)

print('---USO NUMPY---')

Q3_col = np.percentile(datos['NA_Sales'], 75, axis=0)
print(f"Ultimo Cuartil (Q3) de la Columna NA_Sales: {Q3_col}")
tam_Cuartil=int(len(datos)*.75)
print(datos[tam_Cuartil][3])

P80_col=np.percentile(datos['NA_Sales'], 80, axis=0)
print(f"Percentil 80 de la Columna NA_Sales: {P80_col}")
tam_Percentil80=int(len(datos)*.80)
print(datos[tam_Percentil80][3])
print()

#Ordenar Datos por la Columna EU_Sales
lista_ordenada=sorted(DATA_SET, key=lambda x: float(x[4]),reverse=False)
datos=np.array([tuple(row) for row in lista_ordenada],dtype=dtype)

Q3_col = np.percentile(datos['EU_Sales'], 75, axis=0)
print(f"Ultimo Cuartil (Q3) de la Columna EU_Sales: {Q3_col}")
tam_Cuartil=int(len(datos)*.75)
print(datos[tam_Cuartil][4])

P80_col = np.percentile(datos['EU_Sales'], 80, axis = 0)
print(f"Percentil 80 de la Columna EU_Sales: {P80_col}")
tam_Percentil80=int(len(datos)*.80)
print(datos[tam_Percentil80][4])
print()

#Ordenar Datos por la Columna JP_Sales
lista_ordenada=sorted(DATA_SET, key=lambda x: float(x[5]),reverse=False)
datos = np.array([tuple(row) for row in lista_ordenada], dtype=dtype)

Q3_col = np.percentile(datos['JP_Sales'], 75, axis=0)
print(f"Ultimo Cuartil (Q3) de la COlumna JP_Sales: {Q3_col}")
tam_Cuartil=int(len(datos)*.75)
print(datos[tam_Cuartil][5])

P80_col = np.percentile(datos['JP_Sales'], 80, axis=0)
print(f"Percentil 80 de la Columna JP_Sales: {P80_col}")
tam_Percentil80=int(len(datos)*.80)
print(datos[tam_Percentil80][5])
print()

#Ordenar Datos por la Columna Other_Sales
lista_ordenada = sorted(DATA_SET, key=lambda x: float(x[6]), reverse=False)
datos = np.array([tuple(row) for row in lista_ordenada], dtype=dtype)

Q3_col = np.percentile(datos['Other_Sales'], 75, axis=0)
print(f"Ultimo Cuartil (Q3) de la Columna Other_Sales: {Q3_col}")
tam_Cuartil = int(len(datos)*.75)
print(datos[tam_Cuartil][6])
P80_col = np.percentile(datos['Other_Sales'], 80, axis=0)
print(f"Percentil 80 de la Columna Other_Sales: {P80_col}")
tam_Percentil80 = int(len(datos)*.80)
print(datos[tam_Percentil80][6])
print()

#Ordenar Datos por la Columna Global_Sales
lista_ordenada = sorted(DATA_SET, key = lambda x: float(x[7]), reverse=False)
datos = np.array([tuple(row) for row in lista_ordenada], dtype=dtype)

Q3_col = np.percentile(datos['Global_Sales'], 75, axis=0)
print(f"Ultimo Cuartil (Q3) de la Columna Global_Sales: {Q3_col}")
tam_Cuartil = int(len(datos)*.75)
print(datos[tam_Cuartil][7])
P80_col = np.percentile(datos['Global_Sales'], 80, axis=0)
print(f"Percentil 80 de la Columna Global_Sales: {P80_col}")
tam_Percentil80 = int(len(datos)*.80)
print(datos[tam_Percentil80][7])
print()


import pandas as pd

columnas =    [ 'Platform',
                'Genre', 
                'Publisher', 
                'NA_Sales', 
                'EU_Sales', 
                'JP_Sales', 
                'Other_Sales', 
                'Global_Sales', 
                'Rating',
                'Critic_Score']

datos = pd.DataFrame(DATA_SET,columns=columnas)

datos['Platform']=datos['Platform'].astype(str)
datos['Genre']=datos['Genre'].astype(str)
datos['Publisher']=datos['Publisher'].astype(str)
datos['NA_Sales']=datos['NA_Sales'].astype(float)
datos['EU_Sales']=datos['EU_Sales'].astype(float)
datos['JP_Sales']=datos['JP_Sales'].astype(float)
datos['Other_Sales']=datos['Other_Sales'].astype(float)
datos['Global_Sales']=datos['Global_Sales'].astype(float)
datos['Rating']=datos['Rating'].astype(str)
datos['Critic_Score']=datos['Critic_Score'].astype(str)

#Columna NA_Sales
registro_ordenado = sorted(DATA_SET,key=lambda x: float(x[3]), reverse=False)
datos = pd.DataFrame(registro_ordenado,columns=columnas)
datos['NA_Sales']=datos['NA_Sales'].astype(float)

Q3 = datos['NA_Sales'].quantile(.75)
P80 = datos['NA_Sales'].quantile(.80)
print(Q3)
print(P80)


#Columna EU_Sales
registro_ordenado = sorted(DATA_SET,key=lambda x: float(x[4]), reverse=False)
datos = pd.DataFrame(registro_ordenado,columns=columnas)
datos['EU_Sales'] = datos['EU_Sales'].astype(float)

Q3 = datos['EU_Sales'].quantile(.75)
P80 = datos['EU_Sales'].quantile(.80)
print(Q3)
print(P80)
    
#Columna JP_Sales    
registro_ordenado = sorted(DATA_SET,key=lambda x: float(x[5]), reverse=False)
datos = pd.DataFrame(registro_ordenado,columns=columnas)
datos['JP_Sales'] = datos['JP_Sales'].astype(float)

Q3 = datos['JP_Sales'].quantile(.75)
P80 = datos['JP_Sales'].quantile(.80)
print(Q3)
print(P80)

#Columna Other_Sales
registro_ordenado = sorted(DATA_SET,key=lambda x: float(x[6]), reverse=False)
datos = pd.DataFrame(registro_ordenado,columns=columnas)
datos['Other_Sales'] = datos['Other_Sales'].astype(float)

Q3 = datos['Other_Sales'].quantile(.75)
P80 = datos['Other_Sales'].quantile(.80)
print(Q3)
print(P80)
 
#Columna Global_Sales
registro_ordenado = sorted(DATA_SET,key=lambda x: float(x[7]), reverse=False)
datos = pd.DataFrame(registro_ordenado,columns=columnas)
datos['Global_Sales'] = datos['Global_Sales'].astype(float)

Q3 = datos['Global_Sales'].quantile(.75)
P80 = datos['Global_Sales'].quantile(.80)
print(Q3)
print(P80)






