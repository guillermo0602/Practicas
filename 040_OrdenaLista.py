numeros=[5,2,9,1,5,6]
print(numeros)
for i in range (len(numeros)):
    for j in range(len(numeros)-i-1):
        if numeros[j]>numeros[j+1]:
            aux=numeros[j+1]
            numeros[j+1]=numeros[j]
            numeros[j]=aux
print("Lista ordenada: ",numeros)