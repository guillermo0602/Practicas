usuario=int(input("Dime un numero y te doy sus divisores: "))

for i in range (1,usuario+1):
    if(usuario%i==0):
        print(i)
