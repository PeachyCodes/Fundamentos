menores=0
mayores=0
nro=0
cantmay=0
cantmen=0

while nro!=999:
    nro=int(input("nro: "))
    if nro>=18:
        mayores=mayores+1
        cantmay=cantmay+nro
    else:
        menores=menores+1
        cantmen=cantmen+nro
    

print("El conteo ha finalizado")
print("menores: ", menores)
print("mayores: ", mayores-1)

if menores>0:
    print("El promedio de edad de menores es: ", cantmen//menores)
else:
    print("El promedio de edad de menores no figura")
    
if mayores>0:
    print("El promedio de edad de mayores es: ", (cantmay-999)//mayores)
else:
    print("El promedio de edad de mayores no figura")
    

