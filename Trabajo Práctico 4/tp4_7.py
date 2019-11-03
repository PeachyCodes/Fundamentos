num=int(input("Ingrese un numero: "))

primero=num

while num!=-1:
    num=int(input("ingrese un numero: "))
    if num!=-1:
        ultimo=num
    else:
        print("fin")        
print(primero, ultimo)
