lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numeros=[]
for i in range(len(lista)):
    if i % 2 ==0:
        numeros.append(i)
print(numeros)