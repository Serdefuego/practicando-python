arreglo = []

def menu():
    while True:
        seleccione = input(
            "\nIngrese:\n"
            "1 - Cargar empleado\n"
            "2 - Imprimir empleados\n"
            "3 - Modificar empleado\n"
            "4 - Eliminar empleado\n"
            "5 - Salir\n"
        )

        if seleccione == "1":
            cargar(arreglo)
        elif seleccione == "2":
            imprimir(arreglo)
        elif seleccione == "3":
            modificar(arreglo)
        elif seleccione == "4":
            eliminar(arreglo)
        elif seleccione == "5":
            salir()
            break
        else:
            print("Opción inválida")


def cargar(arreglo):
    cantidad = int(input("Ingrese cantidad de empleados a subir: "))
    for i in range(cantidad):
        diccionario = {}
        diccionario["edad"] = input("Ingrese edad: ")
        diccionario["nombre"] = input("Ingrese nombre: ")
        diccionario["sueldo"] = input("Ingrese sueldo: ")
        arreglo.append(diccionario)


def imprimir(arreglo):
    if not arreglo:
        print("No hay empleados cargados.")
    else:
        for elemento in arreglo:
            print("Edad:", elemento["edad"],
                  "Nombre:", elemento["nombre"],
                  "Sueldo:", elemento["sueldo"])


def modificar(arreglo):
    buscar = input("Ingrese nombre de la persona a modificar: ")
    for personas in arreglo:
        if personas["nombre"] == buscar:
            personas["edad"] = input("Ingrese nueva edad: ")
            personas["nombre"] = input("Ingrese nuevo nombre: ")
            personas["sueldo"] = input("Ingrese nuevo sueldo: ")
            print("Empleado modificado correctamente.")
            return
    print("Empleado no encontrado.")


def eliminar(arreglo):
    buscar = input("Ingrese nombre de la persona a eliminar: ")
    for i in range(len(arreglo)):
        if arreglo[i]["nombre"] == buscar:
            arreglo.pop(i)
            print("Empleado eliminado correctamente.")
            return
    print("Empleado no encontrado.")


def salir():
    print("Gracias por utilizar el programa")


# Ejecutar programa
menu()