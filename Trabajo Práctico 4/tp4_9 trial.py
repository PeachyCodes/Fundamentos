#imprima impares de 3 cifras usando ciclo

nro=int(input("nro: "))

while nro!=0:
    if nro>=1:
        if nro>99 and nro<1000:
            if nro%2==0:
                print=("El nro ", nro, " es par.")
                nro=int(input("nro: "))
            else:
                print("El nro ", nro, " es impar.")
                nro=int(input("nro: "))
        else:
            print("El nro no tiene 3 cifras")
            nro=int(input("nro: "))
    else:
        print("El numero ", nro, "no es natural")
        nro=int(input("nro: "))

nro=int(input("nro: "))
