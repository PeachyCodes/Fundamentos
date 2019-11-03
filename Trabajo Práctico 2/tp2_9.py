#TRABAJO PRACTICO Nº 2
#Ejercicio 9

#Paso 1: Crear variable del numero
Numero=int(input("Ingrese numero binario de cuatro cifras: "))

#Paso 2: Tomar numeros por separado
cifra3=Numero//1000
resto3=Numero%1000
cifra2=resto3//100
resto2=resto3%100
cifra1=resto2//10
resto1=resto2%10
cifra0=resto1

#Paso 3: Imprimir cifras tomadas
print(cifra3, cifra2, cifra1, cifra0)

#Paso 4: Calcular decimal de binario e imprimirlo
decimal=cifra3*(2**3)+cifra2*(2**2)+cifra1*(2**1)+cifra0*(2**0)
print(cifra3,"*(2**3) +",cifra2,"*(2**2) +",cifra1,"*(2**1) +",cifra0,"*(2**0)=",decimal)
print("El binario pasado a decimal es ", decimal)
