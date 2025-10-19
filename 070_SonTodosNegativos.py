numeros=[-10,30,15,-2,45,60,-5,100,35]
contador=0
num=[]

for i in numeros:
    if i<0:
        print(i)
        contador+=1
print(f"En la lista hay: {contador}")