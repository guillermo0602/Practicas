ciudades={"Aranjuez":28300,"Madrid":28001,"Valdemoro":28343,"Pinto":28320}
ciudades2={}

for ciudad,codigo in ciudades.items():
    ciudades2[codigo]=ciudad
print(f"Diccionario actual: {ciudades}")
print(f"Diccionario invertido: {ciudades2}")
