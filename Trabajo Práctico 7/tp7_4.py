#Ejercicio 4: Invertir aquellos valores ubicados en posiciones impares de una lista.

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

def invertidex(a):
    largo=len(a)
#va saltando de a dos desde la primera hasta la ultima cifra de la lista
    for i in range(1,largo,2):
        a[i]=a[i]*-1
    return a    

lista=dolist()
res=lista
print(res)
invertida=invertidex(res)
print(invertida)