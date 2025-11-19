diccionario={}
palabra=input(f"Dime una palabra(pulsa salir para salir): ")
contador=0
while palabra!="0":
    contador+=1
    diccionario[palabra]=contador
    palabra=input(f"Dime una palabra(pulsa salir para salir): ")
print(diccionario)