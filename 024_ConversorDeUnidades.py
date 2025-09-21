valor = float(input("Introduce el valor: "))
unidad = input("Introduce la unidad (km, m, cm): ")

match unidad:
    case "km":
        print(f"{valor} km = {valor * 1000} m")
    case "m":
        print(f"{valor} m = {valor} m")
    case "cm":
        print(f"{valor} cm = {valor / 100} m")
    case _:
        print("Unidad no válida")