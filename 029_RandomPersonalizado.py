import random

num=int(input("Dime un dumero para el rango inferio: "))
num2=int(input("Dime el numero para el rango superior: "))
intentos=int(input("Dime cuantos numeros random quieres: "))

for i in range(intentos):
    numero_aleatorio = random.randint(num, num2)
    print(numero_aleatorio)