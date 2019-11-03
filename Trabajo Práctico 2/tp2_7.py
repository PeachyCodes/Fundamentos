#TRABAJO PRÁCTICO Nº 2

#Ejercicio 7: inmobiliaria.

#Ingresos
vendedor=int(input("Ingrese el numero del vendedor: "))
num_ventas=int(input("Ingrese el numero de ventas: "))
val_ventas=int(input("El valor de las ventas es: "))

#Cálculos
sal_fijo=int(800)
comision=float(50*num_ventas)+(val_ventas*0.05)
sal=sal_fijo+comision

#Devolución
print("------------EXPRESADO EN VALORES MENSUALES--------------")
print("El número de vendedor es: ",vendedor)
print("Su salario es: %.2f" %sal)
print("La cantidad de ventas que realzó fueron: %.2f" %num_ventas)
print("El valor total de las ventas es: %.2f" %val_ventas)
print("La comisión por ventas es: %.2f" %comision)
