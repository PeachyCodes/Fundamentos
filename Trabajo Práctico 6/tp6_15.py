"""Ejercicio 15: Escribir una función que reciba como parámetros
dos números enteros y devuelva la concatenación de ambos.
Por ejemplo concatenar(123,456) devuelve 123456."""

def dos_seguidos(a,b):
    i=0
    constb=b
    nro=0
    while b>0:
        b=b//10
        i=i+1
    nro=a*(10**i)+constb
    return nro

nro1=int(input("Nro1: "))
nro2=int(input("Nro2: "))
res=dos_seguidos(nro1,nro2)
print(res)

