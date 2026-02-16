while True:

    mail = input("Ingrese mail: ")

    if "@" in mail and "." in mail:
        print("Mail correcto")
        break
    else:
        print("Mail incorrecto")