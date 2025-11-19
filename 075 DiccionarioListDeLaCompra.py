compras={"pan":5,"leche":2,"huevo":12,"cafe":5}
#items recorre la clave y valor del diccionario
for producto, cantidad in compras.items():
        print(f"{producto}: {cantidad}")