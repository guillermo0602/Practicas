lista=[]
suma=0
usuario=int(input("Dime un numero(ingresa 0 para salir): "))

while usuario!=0:
    lista.append(usuario)
    usuario=int(input("Dime un numero(ingresa 0 para salir): "))

for i in lista:
    if i%2==0:
        pares=i
    else:
        suma+=i
print(f"La suma de los numeros impares de la lista {lista} es: {suma}")