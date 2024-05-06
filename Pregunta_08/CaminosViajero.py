# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:04:44 2024

@author: fredd
"""
from itertools import permutations

# Lista de ciudades
ciudades = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Generar todos los posibles caminos
todosLosCaminos = []

todosLosCaminos.extend(list(permutations(ciudades, len(ciudades))))

# Imprimir todas las combinaciones
for caminos in todosLosCaminos:
    print(caminos)

print(len(todosLosCaminos))