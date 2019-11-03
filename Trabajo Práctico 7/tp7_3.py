#Ejercicio 3: Determinar si una lista es capicúa.

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
long=len(res)
ciclo=0
i=0
cc=0
if long!=0:
    cifa=res[i]
    cifb=res[long-(1+i)]
    if long%2==0:
        ciclo=long//2
    else:
        ciclo=(long//2)+1
    while ciclo>0:
        ciclo=ciclo-1
        if cifa==cifb:
            cifa=res[i-1]
            cifb=res[long-(1+i)]
            cc=1
    if cc==1:
        print("la lista es capicua")
    else:
        print("la lista no es capicua")
else:
    print("La lista no contiene elementos.")

