"""Ejercicio 6: Ídem anterior, utilizando búsqueda binaria sobre una lista ordenada."""

def dolist():
    listex=[]
    nro=int(input("ingrese nro: "))
    while nro!=-1:
        if nro>=0:
            listex.append(nro)
            nro=int(input("ingrese nro: "))
        else:
            if nro==-1:
                return (listex)
            else:
                print("nro no valido")
                nro=int(input("ingrese nro: "))
            
def posicion(a,b):
    aum=0
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

    
