#TRABAJO PRACTICO Nº 2

#Ejercicio 5

var1=int(input("Ingrese medida en metros: "))
med_cm=var1*100

print("La medida de", var1,"m. expresada en PIES es: %.2f" %(med_cm/30.48))
print("La medida de", var1,"m. expresada en PULGADAS es: %.2f" %(med_cm/2.54))
print("La medida de", var1,"m. expresada en YARDAS es: %.2f" %(med_cm/91.44))
print("La medida de", var1,"m. expresada en CENTIMETROS es: %.2f" %(med_cm))