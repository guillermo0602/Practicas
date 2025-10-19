numeros=[5,6,7,8,1]
maximo=numeros[0]
i=1
while i<len(numeros):
    if numeros[i] > maximo:
        maximo=numeros[i]
    i+=1
print("El numero mayor de la lista es: ",maximo)