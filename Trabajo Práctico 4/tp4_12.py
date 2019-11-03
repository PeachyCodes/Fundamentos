#ENCUESTA

#defino iteración
i=1
#defino consumidor
costumer=1
#defino valores de verdad a y b
a=0
b=0
#cantidades
aa=0
bb=0
justa=0
justb=0
none=0
both=0


while i<=100:
    print("Bienvenido cliente Nro", costumer,"!")
    acca=int(input("Acepta A? Si=1 / No=0:  "))
    if acca==1:
        a=1
        aa=aa+1
    else:
        a=0
    accb=int(input("Acepta B? Si=1 / No=0:  "))
    if accb==1:
        b=1
        bb=bb+1
    else:
        b=0
    if a==1 and b==0:
        justa=justa+1
    if a==0 and b==1:
        justb=justb+1
    if a==0 and b==0:
        none=none+1
    if a==1 and b==1:
        both=both+1
    i=i+1
    costumer=costumer+1

print("cant a: ", aa) 
print("cant b: ", bb)
print("cant a y no b: ", justa)
print("cant b y no a: ", justb)
print("cant ninguna: ", none)
print("cant ambas: ", both)
