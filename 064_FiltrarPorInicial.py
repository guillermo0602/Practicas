palabras = ["sol", "luna", "mar", "estrella", "cielo"]
letra=input("Dime una letra: ")
filtrar=[]

for i in palabras:
    if i.startswith(letra):
        filtrar.append(i)
print(filtrar)