operacion=int(input("1.-SUMA 2.-RESTA 3.-MULTIPLICACION 4.-DIVISION" "Selecciona la operacion que quieres realizar: "))


match operacion:
    case 1:
        num1=int(input("Dime un numero: "))
        num2=int(input("Dime otro numero: "))
        resultado=num1+num2
        print("El resultado de la suma es: ", resultado)
    case 2:
        num1=int(input("Dime un numero: "))
        num2=int(input("Dime otro numero: "))
        resultado=num1-num2
        print("El resultado de la resta es: ", resultado)
    case 3:
        num1=int(input("Dime un numero: "))
        num2=int(input("Dime otro numero: "))
        resultado=num1*num2
        print("El resultado de la multiplicacion es: ", resultado)
    case 4:
        num1=int(input("Dime un numero: "))
        num2=int(input("Dime otro numero: "))

        resultado=num1/num2
        
        if num1 < num2:
            num1=int(input("Dime otro numero(el primer numero debe ser mayor al segundo): "))
            resultado=num1/num2
            print("El resultado de la division es: ", resultado)
        else:
            print("El resultado de la division es: ", resultado)