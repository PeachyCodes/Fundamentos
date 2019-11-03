x=int(input("Ingrese el año: "))

a=x%19
b=x%4
c=x%7
d=((a*19)+24)%30
e=((b*2)+(c*4)+(d*6)+5)%7

pascua=((d+e)+22)

if pascua>31:
    print("Pascua se celebraria el", pascua-31, "de Abril")
else :
    print("Pascua se celebra el", pascua, "de Marzo")
    

