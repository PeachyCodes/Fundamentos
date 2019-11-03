bruto=float(input("Ingrese sueldo bruto: "))
antiguedad=int(input("Ingrese antiguedad: "))
civil=str(input("Si es soltero/a, ingrese c: "))
bruto1=bruto+(bruto*0.05)*antiguedad
bruto2=bruto+(bruto*0.07)*antiguedad
jub1=(bruto1*0.11)
jub2=(bruto2*0.11)
social1=(bruto1*0.03)
social2=(bruto2*0.03)
sindicato1=(bruto1*0.03)
social2=(bruto2*0.03)

if civil == "c" or civil == "C":
    print("El sueldo neto seria de : %.2f" %(bruto1-(jub1+social1+sindicato1)))
else:
    print("El sueldo neto seria de :%.2f " %(bruto2-jub2-social2-sindicato2))