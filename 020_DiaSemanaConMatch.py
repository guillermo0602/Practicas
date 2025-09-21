usuario=input("Dime un dia de la semana: ")
match usuario:
    case "sabado"|"domingo":
        print("Es fin de semana")
    case "lunes"|"martes"|"miercoles"|"jueves"|"viernes":
        print("Este dia es laborable.")
    case _:
        print("ERROR")