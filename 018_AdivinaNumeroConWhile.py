print("Adivina el número (tienes 6 intentos):")
secreto = 7
intentos = 6

for i in range(intentos):
    usuario = int(input(f"Intento {i+1}: "))
    if usuario == secreto:
        print("ENCONTRADO")
        break
    else:
        print("INCORRECTO")

if usuario != secreto:
    print("FALLASTE, el número secreto era", secreto)
