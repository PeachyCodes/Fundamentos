"""Ejercicio 6: Devolver True si el número entero
recibido como primer parámetro es múltiplo
del segundo, o False en caso contrario.
Ejemplo: esmultiplo(40,8) devuelve True
y esmultiplo(50,3) devuelve False."""

def multo (a,b):
    multo=0
    if a%b==0:
        multo=True
    else:
        multo= False
    return multo

nro1=int(input("Ingrese nro1: "))
nro2=int(input("Ingrese nro2: "))
res=multo(nro1, nro2)
print(res)
