"""Ejercicio 14: Obtener el dígito central de un número entero pasado como parámetro,
sólo si la cantidad de dígitos es impar. Si la longitud fuera par devolver -1.
Ejemplo: digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1."""

def digitocentral(a):
    i=0
    par=-1
    const=a
    digito=0
    divmodu=0
    divent=0
    #si a es -, lo hago +.
    if a<0:
        a=a*(-1)
        const=a
    #si a tiene mas de 4 digitos, que se ejecute       
    if a>999:
    #contador verificar cant digitos
        while a>0:
            a=a//10
            i=i+1
        #si a es impar, se ejecuta
        if i%2==1:
            divmodu=(const//(10**((i//2)+1)))*(10**(i//2))
            divent=(10**(i//2))
            digito=(const%divmodu)//divent
        #si a es par, devuelve -1
        else:
            digito=par
    else:
        #si a tiene 3 digitos, que devuelva el del medio
        if a>99 and a<1000:
            digito=(const//10)%10
        else:
            #si a tiene 2 digitos, es par
            if a>9:
                digito=par
            #si a tiene 1 digito, se impar.
            else:
                digito=a
    return digito
           

i=1
while i==1:
    nro=int(input("inserte nro: "))
    res=digitocentral(nro)
    print(res)