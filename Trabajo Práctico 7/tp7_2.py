#Ejercicio 2: Calcular la suma de los números de una lista.

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

res=dolist()
print(res, "=" ,len(res))
