lista=[1,2,3,1,2,3,1,2,3,4,5,6]
lista2=[]

for i in lista:
    if i not in lista2:
        lista2+=[i]
        contador=0
        for j in lista:
            if j==i:
                contador+=1
        print(f"{i}:{contador}")