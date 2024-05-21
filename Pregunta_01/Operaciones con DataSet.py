# -*- coding: utf-8 -*-
"""
Created on Thu May 16 03:41:25 2024

@author: fredd
"""
from tabulate import tabulate

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


print(DATA_SET[0])

# Platform=0
# Genre=1
# Publisher=2 
# NA_Sales=3
# EU_Sales=4 
# JP_Sales=5
# Other_Sales=6
# Global_Sales=7
# Rating=8
# Critic_Score_Class=9

lista_ordenada = sorted(DATA_SET, key=lambda x: x[7],reverse=False)
tam_ultimoCuartil=int(len(lista_ordenada)*0.75)


for i in range(tam_ultimoCuartil):
    print(lista_ordenada[i])

print(tam_ultimoCuartil)
print(lista_ordenada[tam_ultimoCuartil])

print(lista_ordenada[int(len(lista_ordenada)*0.75)])    

tamPercentil_70=int(len(lista_ordenada)*.7)
tamPercentil_80=int(len(lista_ordenada)*.8)
tamPercentil=int(len(lista_ordenada)*.1)

#Percentil 80 de la Columna 1 (Platform=0)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[0],reverse=False)
lista_percentil80_columna_1=[]

for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_1.append(lista_ordenada[numRegistro])
    
#Percentil 80 de la Columna 2 (Genre=1)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[1],reverse=False)
lista_percentil80_columna_2=[]

for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_2.append(lista_ordenada[numRegistro])

#Percentil 80 de la Columna 3 (Publisher=2)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[2],reverse=False)
lista_percentil80_columna_3=[]

for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_3.append(lista_ordenada[numRegistro])

#Percentil 80 de la Columna 4 (NA_Sales=3)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[3],reverse=False)
lista_percentil80_columna_4=[]
 
for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_4.append(lista_ordenada[numRegistro])

#Percentil 80 de la Columna 5 (EU_Sales=4)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[4],reverse=False)
lista_percentil80_columna_5=[]
 
for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_5.append(lista_ordenada[numRegistro])

#Percentil 80 de la Columna 6 (JP_Sales=5)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[5],reverse=False)
lista_percentil80_columna_6=[]
 
for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_6.append(lista_ordenada[numRegistro])

#Percentil 80 de la Columna 7 (Other_Sales=6)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[6],reverse=False)
lista_percentil80_columna_7=[]
 
for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_7.append(lista_ordenada[numRegistro])

#Percentil 80 de la Columna 8 (Global_Sales=7)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[7],reverse=False)
lista_percentil80_columna_8=[]
 
for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_8.append(lista_ordenada[numRegistro])


#Percentil 80 de la Columna 9 (Rating=8)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[8],reverse=False)
lista_percentil80_columna_9=[]
 
for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_9.append(lista_ordenada[numRegistro])

#Percentil 80 de la Columna 10 (Critic_Score_Class=9)
lista_ordenada = sorted(DATA_SET, key=lambda x: x[9],reverse=False)
lista_percentil80_columna_10=[]
 
for numRegistro in range(tamPercentil_70,tamPercentil_80):
    lista_percentil80_columna_10.append(lista_ordenada[numRegistro])

print(tabulate(lista_percentil80_columna_10, headers="firstrow", tablefmt="grid"))


#print(lista_ordenada[numRegistro])
print(int(len(lista_ordenada)))
print()



