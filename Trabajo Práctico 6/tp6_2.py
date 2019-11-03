"""Ejercicio 2: Dados dos parámetros enteros A y B,
obtener AB (A elevado a la B) mediante multiplicaciones
sucesivas, utilizando la función del ejercicio 1."""

#funcion sumulti
def multi (a,b):
    suma=1
    for i in range(0,b):
        suma=suma*a
    return suma

#programa

nro1=int(input("ingrese nro 1: "))
nro2=int(input("ingrese nro 2: "))

resultado=multi(nro1, nro2)
print("El nro1 multiplicado por el nro2 es: ", resultado)