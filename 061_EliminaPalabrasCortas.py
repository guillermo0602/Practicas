lista=["hola","mundo","madrid","sol","posible"]

for i in lista:
    if len(i)<=4:
        lista.remove(i)
print(lista)