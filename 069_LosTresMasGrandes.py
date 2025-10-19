numeros=[10,30,15,2,45,60,5,100,35]

for i in range (len(numeros)):
    for j in range(len(numeros)-i-1):
        if numeros[j]>numeros[j+1]:
            aux=numeros[j+1]
            numeros[j+1]=numeros[j]
            numeros[j]=aux
print(numeros[-3:])