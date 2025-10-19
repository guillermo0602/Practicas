palabras=["sol", "luna", "mar", "estrella", "cielo"]
letra=input("Dime una letra: ").lower()
lista=[]

for i in palabras:
    if i[0]==letra:
        lista.append(i)
print(lista)