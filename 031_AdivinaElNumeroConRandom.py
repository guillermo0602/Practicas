import random
usuario=int(input("Adivina el numero(Tienes 6 intentos): "))
intentos=6
total=0

if usuario==random.randint(1,20):
    print("Encontrado")
else:
    for i in range (1,intentos):
        usuario=int(input("ERROR vuelve a intentarlo: "))
    print("FALLASTE")
