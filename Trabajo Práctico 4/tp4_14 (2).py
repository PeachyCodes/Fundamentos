a=1
b=0
c=0
while c<10000:
    c=a+b
    b=a
    a=c
    print(b)