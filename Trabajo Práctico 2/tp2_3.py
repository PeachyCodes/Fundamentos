#TRABAJO PRACTICO Nº 2

#Ejercicio 3: Una empresa fabrica cortinas de baño en color verde, blanco y azul.
#             Escribir un programa que permita ingresar la cantidad de cortinas fabricadas
#             en cada uno de los colores e informe el porcentaja que fabricó en cada uno de ellos.

#Paso 1: Introducir tres variables enteras
nro1=int(input("Ingrese cantidad de cortinas color verde: "))
nro2=int(input("Ingrese cantidad de cortinas color blanco: "))
nro3=int(input("Ingrese cantidad de cortinas color azul: "))

#Paso 2: Realizar los "cálculos intermedios"
total=nro1+nro2+nro3

#Paso 3: Calcular y devolver porcentaje
print("El porcentaje de cortinas color verde es: %.2f" %((nro1*100)/total), "%")
print("El porcentaje de cortinas color blanco es: %.2f" %((nro2*100)/total), "%")
print("El porcentaje de cortinas color azul es: %.2f"%((nro3*100)/total), "%")

#      En este ejercicio, se ingresan variables enteras, porque no fabricamos media cortina,
#         y luego se efectúa la división real.
#      Imput tiene como valor asociasdo el string, por eso hay que asignarle valor int.
#      Al realizar un cálculo intermedio, se simplifica la codificación posterior.
#      Se utilia la función "round(   [, ndigits])" para redondear el número a decimal, o bien...
#         //print("..... %.[ndigits]f" %[variable]) ------> SIN COMA!!
#      Para calcular el porcentaje se lo multiplica por 100 y luego se lo divide por el total de ingresos.
