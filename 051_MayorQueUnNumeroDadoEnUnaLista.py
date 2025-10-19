numeros = [3, 7, 12, 18, 25, 31, 37, 44, 50, 57, 63, 70, 77, 83, 90, 96,15,41,68,99]
lista=[]
usuario=int(input("Dime un numero: "))

for i in range(len(numeros)):
    if usuario < numeros[i]:
        lista.append(numeros[i])
lista.sort()
print(lista)