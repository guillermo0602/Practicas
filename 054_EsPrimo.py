usuario=int(input("Dime un numero y te dire si es primo o no: "))
primo=True

for i in range(2,usuario):
    if usuario%i==0:
        primo=False
if primo:
    print("Es numero primo")
else:
    print("El numero no es primo")