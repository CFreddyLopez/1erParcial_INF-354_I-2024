# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:30:26 2024

@author: fredd
"""

from kanren import var, eq, run, Relation, facts, conde, membero
hijos=var()
padres=var()
abuelos=var()
tios=var()
primos=var()

hijosList=var()
tiosList=var()



parentescos=Relation()
facts(parentescos, 
      ("Freddy","FreddyII"),("Freddy","Diana"),("Fanny","FreddyII"),("Fanny","Diana"),
      ("Eduardo","Fanny"),("Eduardo","David"),("Eduardo","Oscar"),("Eduardo","Franklin"),("Eduardo","Jhon"),
      ("Agustina","Fanny"),("Agustina","David"),("Agustina","Oscar"),("Agustina","Franklin"),("Agustina","Jhon"),
      ("Franklin","Angeles"),("Franklin","Franko"))

#Hijos de Freddy y Fanny
print("Hijos de Freddy y Fanny")
hijosList=run(4, hijos, parentescos("Freddy",hijos),parentescos("Fanny",hijos))
print(hijosList)
print()


#Padres de FreddyII
print("Mis Padres")
padresList=run(2, padres, parentescos(padres,"FreddyII"))
print(padresList)
print()

#Abuelos de FreddyII
print("Mis Abuelos")
abuelosList=run(2, abuelos, parentescos(abuelos,padres),parentescos(padres,"FreddyII"))
print(abuelosList)
print()

#Tios de FreddyII
print("Mis Tios")
tiosList=list()
def parentescoAbuelo(res, obj):
    """
    Parameters
    ----------
    res : var() by Kanren
        DESCRIPTION.
    obj : string
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    aux = var()
    return conde([parentescos(aux,obj),parentescos(res,aux)])


hijosAbuelo=run(5, tios, parentescoAbuelo(abuelos,"FreddyII"),parentescos(abuelos,tios))
padresAux=run(2,padres,parentescos(padres,"FreddyII"))

print(hijosAbuelo)
print(padresAux)


#XD=run(0, tios, eq("",tios))
#print(XD)

for i in range(len(hijosAbuelo)):
    if hijosAbuelo[i]==padresAux[0] or hijosAbuelo[i]==padresAux[1] :
        print("...")
    else:
        print("XD")
        tiosList.append(hijosAbuelo[i])
        

print()
      
def parentescoTios(res,obj):
    aux2=var();
    



relaciones = ['Ada', 'Bec', 'Cad', 'Dan']

# Definir una variable lógica
x = var()

# Verificar si "B" está en la lista de relaciones
esta_presente = membero("B", relaciones)

# Imprimir el resultado
#print(esta_presente.)

# Encontrar todas las variables que están en la lista de relaciones

resultados = run(5, x, membero(x, relaciones))
print(resultados)










def parentescoTio(res,obj):
    """
    

    Parameters
    ----------
    res : var() by Kanren
        DESCRIPTION.
    obj : string
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    aux1=var()
    return conde([parentescoAbuelo(aux1,obj),parentescos(aux1,res)])

#print (run(5,z,parentescoTio(hijos, "FreddyII"),parentescos(hijos,z)))


x = var()

# Definir la consulta con conde y un condicional OR
consulta = conde(
    [eq(x, 2)],
    [eq(x, 1)]
)

# Ejecutar la consulta
resultados = run(2, x, consulta)

# Imprimir los resultados
print(resultados)

x = var()

# Definir una consulta con una condición AND
consulta = conde(
    [eq(x, 2), eq(x, 3)],  # Esto es falso ya que hijos no puede ser 2 y 3 al mismo tiempo
    [eq(x, 2), eq(x, 2)]   # Esto es verdadero ya que hijos puede ser 2 y 2 al mismo tiempo
)

# Ejecutar la consulta y mostrar los resultados
resultados = run(1, hijos, consulta)
print(resultados)
