lista=[1,2,3,4,5,6,7,8,9]
num1=int(input("Dime el numero que quieres cambiar(1,2,3,4,5,6,7,8,9): "))
num2=int(input("Dime por que numero lo quieres cambiar: "))

for i in range(len(lista)):
    if num1==lista[i]:
        lista[i]=num2
print("Esta es la nueva lista con los valores nuevos: ",lista)