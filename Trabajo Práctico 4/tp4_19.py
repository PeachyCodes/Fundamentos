nro=int(input("ingrese nro positivo (-1 para salir): "))
binario="."
while nro!=-1:
    if nro>=0:
        if nro>=2:
            if nro%2==0:
                binario="0"+ binario
                nro=nro//2
            else:
                binario="1" + binario
                nro=nro//2
        else:
            if nro==1:
                binario="1"+binario
                nro=-1
            else:
                binario="0"+binario
                nro=-1
        print("el nro ingresado en binario es: ", binario)
    else:
        print("el numero ingresado no es positivo")

print("fin del conteo") 



