usuario=int(input("Dime un numero: "))
total=1
for i in range(1,usuario+1):
    total*=i
print("El factorial de ", usuario," es: ", total)
