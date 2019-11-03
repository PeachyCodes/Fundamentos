"""Ejercicio 8: Calcular el Máximo Común Divisor
de dos enteros no negativos, basándose en las
siguientes fórmulas matemáticas:
• MCD(X,X) = X
• MCD(X,Y) = MCD(Y,X)
• Si X > Y => MCD(X,Y) = MCD(X-Y,Y).
Ejemplo: MCD(40,15) devuelve 5."""

def mcd(a,b):
    maximo=0
    if a>b:
        for i in range(1,a):
            if a%i==0 and b%i==0:
                maximo=i
    if b>a:
         for i in range(1,b):
            if a%i==0 and b%i==0:
                maximo=i
    if a==b:
        maximo=a
    return maximo

num1=int(input("ingrese un numero "))
while num1<0:
    num1=int(input("numero no valido, ingrese un numero positivo "))
num2=int(input("ingrese otro numero "))
while num2<0:
    num2=int(input("numero no valido, ingrese un numero positivo "))
resultado=mcd(num1,num2)
print("el MCD es",resultado)