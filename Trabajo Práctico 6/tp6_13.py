"""Ejercicio 13: Devolver los últimos N dígitos de un número entero pasado como parámetro.
El valor de N también debe ser pasado como parámetro.
Devolver el número completo si N es demasiado grande.
Ejemplo: ultimosdigitos(12345,3) devuelve 345, y
ultimosdigitos(12345,8) devuelve 12345."""

def ultimosdigitos(a,b):
    ultimo=0
    const=a
    multi=10
    if a>(10**(b)):
        for i in range (0,b):
            restando=(a//10)*multi
            ultimo=const-restando
            a=a//10
            multi=multi*10
        return ultimo
    else:
        return const

nro1=int(input("nro1: "))
nro2=int(input("nro2: "))
res=ultimosdigitos(nro1, nro2)
print(res)