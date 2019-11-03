"""Ejercicio 9: Desarrollar la función signo(n),
que reciba un número entero y devuelva un 1,
-1 o 0 según el valor recibido sea positivo,
negativo o nulo."""

def signo(n):
    if n>0:
        n="1"
    else:
        if n<0:
            n="-1"
        else:
            n="0"
    return n

nro=int(input("ingrese nro: "))
res=signo(nro)
print(res)