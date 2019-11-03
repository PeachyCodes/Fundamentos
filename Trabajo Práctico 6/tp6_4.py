"""Ejercicio 4: Verificar si un número es par o impar,
devolviendo True o False respectivamente."""

#funcion
def paridad(a):
    i=0
    if a%2==0:
        i=True
    else:
        i=False
    return i

#programa

nro1=int(input("Ingrese nro para saber si es par o no: "))
resultado=paridad(nro1)
if resultado == True:
    print("el numero es par")
else:
    print("el nro es impar")
