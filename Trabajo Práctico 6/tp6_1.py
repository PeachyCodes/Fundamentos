"""Ejercicio 1: Dados dos parámetros numéricos,
calcular y devolver el resultado de la multiplicación
de ambos utilizando sólo sumas."""

#funcion sumulti
def sumulti (a,b):
    suma=0
    for i in range(0,b):
        suma=suma+a
    return suma

#programa

nro1=int(input("ingrese nro 1: "))
nro2=int(input("ingrese nro 2: "))

resultado=sumulti(nro1, nro2)
print("El nro1 multiplicado por el nro2 es: ", resultado)