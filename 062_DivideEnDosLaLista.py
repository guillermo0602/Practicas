lista=[3, 7, 12, 18, 25, 31, 37, 44, 50, 57, 63, 70, 77, 83, 90, 96,15,41,68,99]
mayor=[]
menor=[]
usuario=int(input("Dime un numero: "))

for i in lista:
    if i < usuario:
        menor.append(i)
    else:
        mayor.append(usuario)
        mayor.append(i)

print(f"Los numeros menores a {usuario} de la lista son {menor}")
print(f"Los numeros mayores a {usuario} de la lista son {mayor}")