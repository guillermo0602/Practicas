numeros = [1, 2, 2, 3, 4, 4, 4, 5]
usuario=int(input("Dime el numero por el que quieres multiplicar la lista: "))

for i in range (len(numeros)):
    numeros[i]=numeros[i]*usuario
print(numeros)