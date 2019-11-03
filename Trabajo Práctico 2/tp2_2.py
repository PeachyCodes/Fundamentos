#TRABAJO PRACTICO Nº 2

#Ejercicio 2: Escribir un programa que permita ingresar tres numeros enteros, calcular y mostrar su promedio.

#Paso 1: Introducir tres variables de enteros
nro1=int(input("Ingrese un primer número entero: "))
nro2=int(input("Ingrese un segundo número entero: "))
nro3=int(input("Ingrese un tercer número entero: "))
                
#Paso 2: Devolver su promedio
print("El promedio entre los tres números es: ", ((nro1+nro2+nro3)/3))

print("Es decir,",nro1+nro2+nro3,"dividido 3 es igual a ",(nro1+nro2+nro3)/3)

#        Se usa la variable "int" para numeros enteros. Si ingresamos un número decimal, salta error.
#        Se usa la variable "float" para ingresar números decimales, y "str" para cadena de caracteres.
#        No se puede imprimir usando "int" porque las variables decimales no pueden interpretarse como enteras.
#        El promedio de un conjunto de números es la suma de ellos y su división por la cantidad de términos.
