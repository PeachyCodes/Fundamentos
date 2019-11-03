#TRABAJO PRACTICO Nº 2

#Ejercicio 6: Imprimir período de segundos expresado en cantidad de dìas, horas, minutos y segundos.

periodo=int(input("Ingrese período en segundos: "))

#Dias
dias=periodo//86400
resto_dias=periodo%86400
#Horas
horas=resto_dias//3600
resto_horas=resto_dias%3600
#Minutos
minutos=resto_horas//60
resto_minutos=resto_horas%60
#Segundos
segundos=resto_minutos
 
#Imprimir resultados
print("El período de", var1,"ss. expresada en días es:",dias)
print("El período de", var1,"ss. expresada en horas es:",horas)
print("El período de", var1,"ss. expresada en minutos es:",minutos)
print("El período de", var1,"ss. expresada en segundos es:",segundos)

#       En este ejercicio se trabaja con los restos que va dejando secuencialmente una variable modificada.
#       Para conocer el resto de una division entera se utiliza módulo "%" junto al mismo divisor.