a=int(input("a="))
b=int(input("b="))

if a!=b:
    if a<b:
        cont=a
        suma=0
        while cont<=b:
            suma=suma+cont 
            cont=cont+1
        print(suma)
        print("el mayor es: ", b)
        print("el menor es: ", a)
    else:
        cont=b
        suma=0
        while cont<=a:
            suma=suma+cont 
            cont=cont+1
        print(suma)
        print("el mayor es: ", a)
        print("el menor es: ", b)
else:
    print("los numeros son iguales perri")

 