"""

    Leer dos listas de numeros M y N , ambas ordenadas de menor a mayor.
    Generar e imprimir una tercera lista que resulte de intercalar todos los elementos de M y N.
    La nueva lista también debe quedar ordenada, sin usar ningun metodo de ordenamiento
    
                                                                                                    """

#Funciones
def generarLista():
    l=[]
    print("Ingrese numeros a su lista. (-1 para finalizar)")
    while len(l)==0:
        print("Debe ingresar por lo menos un valor a la lista")
        n=int(input("Ingrese numero: "))
        while n != (-1):
            l.append(n)
            n=int(input("Ingrese numero: "))
    return l

def seleccion(l):
    for i in range (len(l)-1):
        for j in range (i+1, len(l)):
            if l[i]>l[j]:
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
    return l

def maxMas1(l,k):
    largol=len(l)
    largok=len(k)
    valorl=l[largol-1]+1
    valork=k[largok-1]+1
    mayor=valorl
    if valorl<valork:
        mayor=valork
    return mayor   

def app0(l,n):
    l.append(n)
    return l

#Programa
#1)
print("------LISTA M------")
m=seleccion(generarLista())
print("------LISTA N------")
n=seleccion(generarLista())
#2)
ciego=maxMas1(m,n)
mrange=app0(m,ciego)
nrange=app0(n,ciego)
#3)
ñ=[]
vM=0
vN=0
while (vN<(len(n)-1)) or (vM<(len(m)-1)):
    if (m[vM])==(n[vN]):
        ñ.append(m[vM])
        ñ.append(n[vN])
        vM=vM+1
        vN=vN+1
    else:
        if (m[vM])>(n[vN]):
            ñ.append(n[vN])
            vN=vN+1
        else:
            if (m[vM])<(n[vN]):
                ñ.append(m[vM])
                vM=vM+1
#4
m=m.pop()
n=n.pop()
print("-------------------------------------------------------------")
print ("M=", mrange)
print ("N=", nrange)
print ("La lista intercalada es:  Ñ=", ñ)

"""
        Pseudocódigo

1) El usuario genera dos listas, M y N, previendo que no pueden quedar vacías.
    Se ordenan con Método de Selección.
2) A las listas se les agrega un "numero ciego".
    Se genera tomando el mayor valor de las listas y se le suma 1.
    Este numero ciego no se agrega a la lista final "Ñ", y sólo
    sirve para que no quede fuera de rango el programa que las une y ordena.
3) El programa principal almacena en la lista "Ñ" los valores de las 2 listas,
    de menor a mayor. Para ello, sigue los siguientes pasos:
    -Se genera un contador de subíndices por lista, iniciado en 0,
        que va a ir aumentando a medida que se agreguen valores de la lista M o N respectivamente.
    -Si los valores tomados son iguales, se agregan ambos y se aumentan ambos contadores.
        Si el valor tomado de la lista M es menor que el de la N, se agrega el de la M y
        se aumenta su contador. Obviamente, lo mismo sucede con los valores de la lista N.
4) Finalmente, se imprimen las listas M y N, ambas sin el numero ciego, y la lista Ñ.

                                                                                        """