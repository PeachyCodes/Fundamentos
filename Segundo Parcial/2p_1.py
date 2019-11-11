import random
def crearLista():
    lista=[]
    while len (lista) < 10:
        nro=random.randint(0,20)
        while nro!=0:
            lista.append(nro)
            nro=random.randint(0,20)
    return lista
def contar (lista,dato):
    cont=0
    for i in range (0,len(lista)):
        if lista[i]==dato:
            cont=cont+1
    return cont

numeros=crearLista()
print(numeros)
masRepe=0
cantRepe=0
for i in range(len(numeros)):
    cant = contar (numeros, numeros [i])
    if cant > cantRepe:
        cantRepe =cant
        masRepe=numeros[i]
if cantRepe!=1:
    print (masRepe, "es el elemento que se repite mas veces")
else:
    print("no hay elementos repetidos.")