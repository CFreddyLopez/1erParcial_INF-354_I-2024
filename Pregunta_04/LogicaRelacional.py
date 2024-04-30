# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:30:26 2024

@author: fredd
"""

from kanren import var, eq, run, Relation, facts, conde, membero, rembero
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


padresAux=run(2,padres,parentescos(padres,"FreddyII"))
print(padresAux)
hijosAbuelo=var()
hijosAbuelo=run(5, tios, conde([parentescoAbuelo(abuelos,"FreddyII"),
                                parentescos(abuelos,tios)]
                               ))
print(hijosAbuelo)

print(run(0,tios,rembero(padresAux[0], hijosAbuelo, tios))[0])
tios=run(0,tios,rembero(padresAux[0], hijosAbuelo, tios))[0]
print(run(5,primos,parentescos(tios,primos)))


print("Mis Primos")

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
resultados = run(2, x, consulta)
print(resultados)
