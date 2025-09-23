figura=input("Dime una figura geometrica (Triángulo, cuadrado, rectángulo, trapecio, paralelogramo, rombo, círculo, pentágono, hexágono, heptágono, octógono, eneágono y decágono.): ")

match figura:
    case "triangulo":
        base=int(input("Dime la base: "))
        altura=int(input("Dime la altura: "))
        print(f"El valor del area es {base*altura/2} y el perimetro es {base*3}")
    case "cuadrado":
        lado=int(input("Dime la base: "))
        print(f"El valor del area es {lado*lado} y el perimetro es {lado*4}")
    case "rectangulo":
        lado=int(input("Dime la altura: "))
        lado2=int(input("Dime el lado: "))
        print(f"El valor del area es {lado*lado} y el perimetro es {lado+lado+lado2+lado2}")

