nro=int(input("Ingrese un nro positivo: "))

while nro<=0:
    print("el nro ingresado no es valido")
    nro=int(input("Ingrese un nro positivo: "))
    
    suma=0
    while nro>0:
        digito=nro%10
        suma=suma+digito
        nro=nro//10
    print("La suma de sus digitos es", suma)

while nro<=0:
    print("el nro ingresado no es valido")
    nro=int(input("Ingrese un nro positivo: "))