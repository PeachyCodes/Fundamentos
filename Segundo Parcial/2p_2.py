def ingresarCodigo():
    codigo=int(input("ingrese codigo de producto (-1 para finalizar) :"))
    while (codigo<1000 and codigo != -1) or codigo>9999:
        codigo=int(input("Error. Vuelva a ingresar el codigo del producto: "))
    return codigo

def existe(lista,dato):
    pos=-1
    i=0
    while i<len(lista) and lista [i] != dato:
        i=i+1
    if i!= len(lista):
        pos=1
    return pos

def ordena (codigos, stock):
    for i in range (len(stock) -1 ):
        for j in range (i+1, len (stock)):
            if stock[i]>stock[j]:
                aux=stock [i]
                stock[i]=stock [j]
                stock[j]=aux
                aux =codigos[i]
                codigos[i]=codigos[i+1]
                codigos [i+1]=aux
    pos =0
    while pos<len(len(stock)) and stock[pos] <=0:
        pos=pos+1
    for i in range (pos,len(stock) -1 ):
        for j in range (i+1, len (stock)):
            if stock[i]<stock[j]:
                aux=stock [i]
                stock[i]=stock [j]
                stock[j]=aux
                aux =codigos[i]
                codigos[i]=codigos[i+1]
                codigos [i+1]=aux
                
codigos=[]
stock=[]
codigo=ingresarCodigo()
while codigo !=-1:
    cantidad=int (input("cantidades producidas o vendidas :"))
    pos=existe(codigos, codigo)
    if pos != -1:
        stock [pos]=stock [pos]+cantidad
    else:
        codigos.append(codigo)
        stock.append(cantidad)
    codigo=ingresarCodigo()

ordena (codigos,stock)
print("Listado: ")
for i in range (len(codigos)):
    print ("el codigo n° ", codigos[i], "tiene un stock de ", stock[i])


        
