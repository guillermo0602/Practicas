lista=[1,2,3,4,5,6,7,8,9,10]
num=len(lista)

if num%2==1:
    media=lista[num//2]
else:
    media=(lista[num//2-1]+lista[num//2])/2

print(f"La media de la lista de numeros {lista} es: {media}")