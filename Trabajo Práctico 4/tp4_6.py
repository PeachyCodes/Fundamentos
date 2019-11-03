i=0
comp=0
while i<10:
    nro=int(input("ingrese hasta 10 nros enteros: "))
    if comp<=nro:
        comp=nro
    i=i+1
print("el mayor valor ingresado es: ", comp)