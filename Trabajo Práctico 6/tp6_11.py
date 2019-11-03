"""Ejercicio 11: Adaptar el programa que utiliza
la fórmula de Newton para calcular la
raíz cuadrada de un número
positivo N (de la práctica anterior)
para que trabaje como una función."""

def newton(a):
    raizcuadrada=a**(1/2)
    return raizcuadrada

num1=int(input("ingrese un numero "))
resultado=newton(num1)
print("la raiz cuadrada es %.2f"%resultado)