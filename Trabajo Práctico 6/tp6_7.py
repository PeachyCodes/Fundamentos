"""Ejercicio 7: Dado un número entero,
calcular su factorial
Ejemplo: fact(4) = 4*3*2*1 = 24"""

def facto (a):
    sum=1
    i=1
    while i<=a:
        sum=sum*i
        i=i+1
    return sum
    
num=int(input("ingrese nro para saber su fact: "))
res=facto(num)
print (res)