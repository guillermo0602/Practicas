usuario=int(input("Ingrese su nota: "))

match usuario:
    case 0|1|2:
        print("Muy deficiente")
    case 3|4:
        print("Suspenso")
    case 5:
        print("Aprobado")
    case 6:
        print("Bien")
    case 7|8:
        print("Muy bien")
    case 9:
        print("Sobresaliente")
    case 0|1|2:
        print("Matricula de honor")