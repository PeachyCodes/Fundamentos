nro=int(input("ingrese nro del 1 al 100: "))
    if nro>0 and nro<=100:
        divisor=1
        sumadivi=0
        while divisor<=nro:
            if nro%divisor==0:
                print("divisor de ", nro, "es: ", divisor)
                sumadivi=sumadivi+divisor
                divisor=divisor+1
            else:
                divisor=divisor+1
        if sumadivi==nro:
             print("El nro es perfecto")
        else:
            if sumadivi>nro:
                print("El nro es abundante")
            else:
                print("el nro es decreciente")           
    else:
        print("El numero no pertenece al rango pedido")

nro=int(input("ingrese nro del 1 al 100: "))    