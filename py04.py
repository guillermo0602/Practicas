import random
usuario=int(input("Adivina el numero(Tienes 6 intentos): "))
intentos=6
contador=0


if usuario==random.randint(1,20):
    print("Encontrado")
else:
    for i in range(intentos-1):
        usuario=int(input("Dime otro numero: "))
        contador=i+1
    print("FALLASTE")
