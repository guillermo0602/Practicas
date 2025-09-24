miLista=[]
while True:
    dato = input("Introduce un dato (o escribe 'fin' para terminar): ")
    if dato.lower() == 'fin':
        break
    miLista.append(dato)
    print(miLista)