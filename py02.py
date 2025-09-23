mes=input("Dime tu mes de nacimiento: ")
dia=int(input("Dime tu dia de nacimiento: "))

match mes:
    case "enero":
        if dia <=19:
            print("Tu signo es capricornio")
        else:
            print("Tu signo es acuario")
    case "febrero":
        if dia <=19:
            print("Tu signo es acuario")
        else:
            print("Tu signo es piscis")
    case "marzo":
        if dia <=19:
            print("Tu signo es piscis")
        else:
            print("Tu signo es aries")
    case "abril":
        if dia <=19:
            print("Tu signo es aries")
        else:
            print("Tu signo es tauro")
    case "mayo":
        if dia <=19:
            print("Tu signo es tauro")
        else:
            print("Tu signo es geminis")
    case "junio":
        if dia <=19:
            print("Tu signo es geminis")
        else:
            print("Tu signo es cancer")
    case "julio":
        if dia <=19:
            print("Tu signo es cancer")
        else:
            print("Tu signo es leo")
    case "agosto":
        if dia <=19:
            print("Tu signo es leo")
        else:
            print("Tu signo es virgo")
    case "septiembre":
        if dia <=19:
            print("Tu signo es virgo")
        else:
            print("Tu signo es libra")
    case "octubre":
        if dia <=19:
            print("Tu signo es libra")
        else:
            print("Tu signo es escorpio")
    case "noviembre":
        if dia <=19:
            print("Tu signo es escorpio")
        else:
            print("Tu signo es sagitario")
    case "diciembre":
        if dia <=19:
            print("Tu signo es sagitario")
        else:
            print("Tu signo es capricornio")