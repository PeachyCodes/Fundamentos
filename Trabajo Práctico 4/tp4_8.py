#Informar el ultimo numero par de la secuencia dada por teclado

#Funcion
def generarlista():
    lista = []
    cont = 0
    nro = int(input("Ingrese un numero: "))
    lista.append(nro)
    while  nro != -1:    #cont < n
        nro = int(input("Ingrese un numero: "))
        lista.append(nro)
        cont = cont + 1
    return lista

#Programa Principal
i = 0
lista = generarlista()
if (len(lista))%2 == 0:
    while i <= len(lista) and lista[i] != -1:
        i = i + 1
    print(lista)
    print("El ultimo valor par es : ", lista[i-2])
else:
    while i <= len(lista) and lista[i] != -1:
        i = i + 1
    print(lista)
    print("El ultimo valor par es : ", lista[i-1])