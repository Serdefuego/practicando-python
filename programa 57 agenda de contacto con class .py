agendaPersonal = []

class Agenda:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail


def menu():
    while True:
        opcion = int(input("\n1 cargar contacto\n2 editar contacto\n3 consultar\n4 borrar\n5 salir\n: "))

        match opcion:
            case 1:
                cargar()
            case 2:
                editar()
            case 3:
                consultar()
            case 4:
                borrar()
            case 5:
                print("Gracias por utilizar la agenda")
                break
            case _:
                print("Opción inválida")


def cargar():
    while True:
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese teléfono: ")
        mail = input("Ingrese mail: ")

        persona = Agenda(nombre, telefono, mail)
        agendaPersonal.append(persona)

        seguir = input("¿Desea seguir cargando? (si/no): ").lower()
        if seguir != "si":
            break


def consultar():
    if not agendaPersonal:
        print("Agenda vacía")
        return

    for persona in agendaPersonal:
        print("\n----------------")
        print("Nombre:", persona.nombre)
        print("Teléfono:", persona.telefono)
        print("Mail:", persona.mail)
        print("----------------")


def editar():
    buscar = input("Ingrese el nombre a editar: ")

    for persona in agendaPersonal:
        if persona.nombre == buscar:
            persona.telefono = input("Nuevo teléfono: ")
            persona.mail = input("Nuevo mail: ")
            print("Contacto editado")
            return

    print("Contacto no encontrado")


def borrar():
    buscar = input("Ingrese el nombre a borrar: ")

    for persona in agendaPersonal:
        if persona.nombre == buscar:
            agendaPersonal.remove(persona)
            print("Contacto eliminado")
            return

    print("Contacto no encontrado")


menu()