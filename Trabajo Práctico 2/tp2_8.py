#TRABAJO PRACTICO Nº 2

#Ejercicio 6: Minimizar cantidad de billetes entregados

#variable
Numero=int(input("Ingrese monto: "))
#100 
pe100=Numero//100
resto100=Numero%100
print("En billetes de 100: ", pe100)
#50
pe50=resto100//50
resto50=resto100%50
print("En billetes de 50: ", pe50)
#10
pe10=resto50//10
resto10=resto50%10
print("En billetes de 10: ", pe10)
#5
pe5=resto10//5
resto5=resto10%5
print("En billetes de 5: ", pe5)
#1
pe1=resto5//1
resto1=resto5%1
print("En billetes de 1: ", pe1)