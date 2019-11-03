"""Ejercicio 12: Extraer un dígito de un número entero.
La función recibe como parámetros dos números enteros,
uno será del que se extraiga el dígito y el otro indica
qué cifra se desea obtener. La cifra de la derecha se
considera la número 0. Retornar el valor -1 si no existe
el dígito solicitado. Ejemplo: extraerdigito(12345,1)
devuelve 4, y extraerdigito(12345,8) devuelve -1."""

def cifrex(a,b):
    nro=0
    i=0
    for i in range (0, (b+1)):
        nro=a%10
        a=a//10
    if a==0 and nro==0:
        nro=-1
    return nro

nro=int(input("ingrese nro entero: "))
nrocif=int(input("ingrese el nro de cifra a extraer(empieza desde 0 en la dcha): "))
res=cifrex(nro, nrocif)
print(res)