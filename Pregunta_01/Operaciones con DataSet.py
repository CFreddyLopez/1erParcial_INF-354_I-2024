# -*- coding: utf-8 -*-
"""
Created on Thu May 16 03:41:25 2024

@author: fredd
"""


archivo_csv = 'E:/University/INF-354 Inteligencia Artificial/I-2024/1erExamen/DataSet/datos.csv'

datos = []

# Abrir el archivo CSV en modo lectura
with open(archivo_csv, 'r') as archivo:
    i=0
    columas=10
    
    for linea in archivo:
        linea = linea.strip()
        valores = linea.split(',')
        dato_concatenado=[]
        registro = []
        for indice, dato in enumerate(valores):
            if '"' in dato:
                
                dato1 = valores[indice].replace('"', "")
                if '"' in valores[indice+1]:
                    dato2 = valores[indice+1].replace('"', "")
                    nuevo_dato=dato1+"."+dato2
                    registro.append(nuevo_dato)
                else:
                    registro.append(dato1)
            else:
                registro.append(dato)
        
        datos.append(registro)


print(datos[0])
print(datos[1])

lista_ordenada = sorted(datos, key=lambda x: x[8],reverse=True)

# print(lista_ordenada[1])

# for registro in lista_ordenada:
#     print(registro)

cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = " ".join([cadena1, cadena2])
print(concatenacion)

cadena = "Hola Mundo"
caracter_a_eliminar = "o"
nueva_cadena = cadena.replace(caracter_a_eliminar, "")
print(nueva_cadena)

for i in range(2):
    print(i)