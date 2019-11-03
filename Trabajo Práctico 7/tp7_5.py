"""Ejercicio 5: Escribir una función para devolver la posición que ocupa un valor pasado como parámetro,
utilizando búsqueda secuencial en una lista desordenada. La función debe devolver -1 si el elemento no se
encuentra en la lista."""

def dolist():
    listex=[]
    nro=int(input("ingrese nro: "))
    while nro!=-1:
        if nro>0 and nro<21:
            listex.append(nro)
        else:
            print("nro no valido")
        nro=int(input("ingrese nro: "))
    return (listex)

def posicion(a,b):
    i=0
    pos=[]
    if len(a)>0:
        while i<len(a):
            if (a[i])==b:
                pos.append(i+1)
                i=i+1
            else:
                i=i+1
        return pos
    else:
        i="Lista sin elementos para encontrar"
    return i

res=dolist()
orden=int(input("ingrese valor de lista para saber ubicación: "))
funcion=posicion(res,orden)
print (res)
print (funcion)

    