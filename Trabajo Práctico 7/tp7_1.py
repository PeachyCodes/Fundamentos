"""Ejercicio 1: Escribir una función para ingresar desde el teclado
una serie de números entre 1 y 20 y guardarlos en una lista.
En caso de ingresar un valor fuera de rango el programa mostrará
un mensaje de error y solicitará un nuevo número.
Para finalizar la carga se deberá ingresar -1.
La función no recibe ningún parámetro, y devuelve la lista cargada
(o vacía, si el usuario no ingresó nada) como valor de retorno.
En los siguientes ejercicios utilice la función del ejercicio 1
para ingresar datos en una lista y:"""

pili=[]
nro=int(input("ingrese nro: "))
while nro!=-1:
    if nro>0 and nro<21:
        pili.append(nro)
    else:
        print("nro no valido")
    nro=int(input("ingrese nro: "))
print(pili)

