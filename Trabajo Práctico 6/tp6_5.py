"""Ejercicio 5: Devolver el máximo entre dos
números recibidos como parámetros."""

def mayor(a,b):
    mayor=0
    if a >b:
        mayor=a
    if b>a:
        mayor=b
    return mayor

nro1=int(input("Ingrese nro1: "))
nro2=int(input("Ingrese nro2: "))
res=mayor(nro1, nro2)
if res!=0:
    print(res)
else:
    print("son iguales")
        