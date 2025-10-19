usuario=int(input("Dime un numero y te dire sus multiplos: "))
rango=int(input("Dime cuantos multiplos quieres: "))
lista=[]
numero=0

for i in range(rango):
    numero=usuario*(i+1)
    lista.append(numero)

print(lista)