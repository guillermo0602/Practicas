usuario=input("Ingresa un caracter(puede ser vocal, constante o caracter especial): ")
vocales=("aeiouAEIOU")
especial=("!@#$~%&/()=?¿'¡^*¨Ç,.-_")

match True:
    case _ if usuario in vocales:
            print("El caracter es vocal")
    case _ if usuario ==especial:
            print("El caracter es un caracter especial")
    case _:
        print("El caracter es consonante")
