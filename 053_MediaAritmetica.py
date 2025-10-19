numeros=[3, 7, 12, 18, 25, 31, 37, 44, 50, 57, 63, 70, 77, 83, 90, 96,15,41,68,99]
media=0

for i in range(len(numeros)):
    media+=numeros[i]
    media=media/len(numeros)
print("La media de la lista es: ", media)