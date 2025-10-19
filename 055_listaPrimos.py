usuario=int(input("Dime un numero: "))
lista=[]

for i in range(2,usuario+1):
    primo=True
    for j in range(2,i):
        if i%j==0:
            primo=False

    if primo:
        lista.append(i)
print(lista)


