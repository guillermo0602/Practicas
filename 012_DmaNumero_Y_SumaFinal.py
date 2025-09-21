usuario=int(input("Dime un numero: "))
contador=0
while usuario != 0:
    contador=contador+usuario
    usuario=int(input("Dime un numero: "))
print("La suma de los numeros es: ",contador)