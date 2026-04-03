class Alumno:
    def __init__(self):
        self.nombre = []
        self.edad = []
        self.menu()

    def menu(self):
        print("\n1- Cargar")
        print("2- Mostrar")
        print("3- Editar")
        print("4- Mayores de 18")
        print("5- Salir")

        opcion = int(input("Ingrese opción: "))

        match opcion:
            case 1:
                self.cargar()
            case 2:
                self.mostrar()
            case 3:
                self.editar()
            case 4:
                self.mayores()
            case 5:
                print("Programa finalizado")
            case _:
                print("Opción incorrecta")
                self.menu()

    def cargar(self):
        for i in range(3):
            nombres = input("Ingrese nombre: ")
            edades = int(input("Ingrese edad: "))
            self.nombre.append(nombres)
            self.edad.append(edades)
        self.menu()

    def mostrar(self):
        for i in range(len(self.nombre)):
            print("Nombre:", self.nombre[i], "Edad:", self.edad[i])
        self.menu()

    def editar(self):
        nombreEditar = input("Ingrese nombre a editar: ")
        encontrado = False

        for i in range(len(self.nombre)):
            if self.nombre[i] == nombreEditar:
                self.nombre[i] = input("Ingrese nuevo nombre: ")
                self.edad[i] = int(input("Ingrese nueva edad: "))
                encontrado = True

        if not encontrado:
            print("No se encontró el alumno")

        self.menu()

    def mayores(self):
        hay_mayores = False

        for i in range(len(self.nombre)):
            if self.edad[i] > 18:
                print(self.nombre[i], "-", self.edad[i])
                hay_mayores = True

        if not hay_mayores:
            print("No hay mayores de edad")

        self.menu()


persona = Alumno()