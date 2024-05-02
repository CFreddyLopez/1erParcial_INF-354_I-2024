# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:30:26 2024

@author: fredd
"""

from kanren import var, eq, run, Relation, facts, conde, membero, rembero, neq

hijos=var()
padres=var()
abuelos=var()
tios=var()
primos=var()

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
    return conde([parentescos(res,aux),parentescos(aux,obj)])

def padresHijo(res,obj):
    return conde([parentescos(res,obj)])

def hijosAbuelo (res,obj):
    aux=var()
    return conde([parentescoAbuelo(aux,obj), parentescos(aux,res)])
    


tiosRun=run(5,tios,conde([membero(tios, run(5,tios, hijosAbuelo(tios,"FreddyII"))),
       neq(tios, padresList[0])])
              )
print(tiosRun)


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
    
    return conde([membero(tios, run(5,tios, hijosAbuelo(tios,obj))),
           neq(tios, padresList[0])])


print(run(5,primos,parentescoTio(tios, "FreddyII"),parentescos(tios,primos)))


