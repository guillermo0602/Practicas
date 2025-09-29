lista=[]
usuario=int(input("Dime de cuantos elementos quieres tu lista: "))
numeros=0

for i in range (usuario):
    lista.append(input("Dime un numero: "))
    numeros+=i
print(lista)