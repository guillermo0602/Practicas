lista=[1,2,3,4,5,6,7,8,9,5]
moda=lista[0]
contador=0
maximo=0

for i in lista:
    for j in lista:
        if j==i:
            contador+=1
    if contador>maximo:
        maximo=contador
        moda=i
print(moda)