usuario=int(input("Dime un numero: "))
a=0
b=1

for i in range (0,usuario):
    total=a
    a=b
    b=a+total
    print(a,end=" ")