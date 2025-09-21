usuario=input("Dime una palabra: ")
vocales="aeiouAEIOU"
contador=0

for i in usuario:
    if i in vocales:
        contador=contador+1
print(contador)