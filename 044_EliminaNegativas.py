lista=[-1,-2,-3,-4,-5,1,2,3,4,5,6,7,8,9,10]
positivos=[]
negativos=[]

for i in lista:
    if i>=0:
        positivos.append(i)
    if i<0:
        negativos.append(i)
print(negativos)
print(positivos)