a=int(input("Numero: "))
b=0
c=0

ter=int(input("Terminos: "))
i=0

suma=0

while i<ter:
    c=a+b
    print(c)
    suma=suma+c
    a=b
    b=c
    i=i+1
    
print("suma: ", suma)
