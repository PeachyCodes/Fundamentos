"""Ejercicio 10: Escribir la función comparar(a,b)
que reciba como parámetros dos números enteros y
devuelva 1 si el primero es mayor que el segundo,
0 si son iguales o -1 si el primero es menor que el segundo.
Ejemplo: comparar(4,2) devuelve 1, y comparar(2,4) devuelve -1."""

def comparar(a,b):
    if a>b:
        n="1"
    else:
        if a<b:
            n="-1"
        else:
            n="0"
    return n

nro1=int(input("ingrese nro1: "))
nro2=int(input("ingrese nro2: "))
res=comparar(nro1, nro2)
print(res)