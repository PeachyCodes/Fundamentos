año=int(input("Ingrese el año: "))

if año%4==0 and año%100==0 and año%400==0:
    print("El año es biciesto")
else :
    if año%4==0 and año%100==0:
        print("El año no es biciesto")
    