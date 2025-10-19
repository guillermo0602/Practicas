usuario=input("Dime una frase: ")
suma=0

palabra=usuario.split()
for i in palabra:
    suma+=1

print("La palabra tiene ",suma," palabras. ")