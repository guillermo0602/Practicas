usuario=int(input("Dime un numero de 1 a 3 digitos: "))
primo=usuario
total=[]
divisor=2

while usuario>1:
    if usuario % divisor ==0:
        total+=[divisor]
        usuario=usuario//divisor
    else:
        divisor+=1

print(primo,"=","x".join(str(x)for x in total))



