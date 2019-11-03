nro=int(input("nro positivo: "))
posicion=1
binario=0
digbin=0
if nro>0:
    while nro>0:
        digbin=nro%2
        binario=binario+(digbin*posicion)
        posicion=posicion*10
        nro//2
    print("el nro binario es: ", binario)
    
else:
    print("el nro no es valido")
    nro=int(input("nro: "))

