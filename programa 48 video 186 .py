class Alumno:
    
    def crear(self, nom, nota):
        self.nombre = nom
        self.nota = nota

    def imprimir(self):
        print("mi nombre es", self.nombre, "y mis notas son", self.nota)

    def estado(self):
        suma = 0
        for i in range(len(self.nota)):
            suma += self.nota[i]

        promedio = suma / len(self.nota)
        print("el promedio es", promedio)


def salon():
    nombre = input("ingrese nombre: ")
    calificaciones = []

    for i in range(3):
        nota = int(input("ingrese nota: "))
        calificaciones.append(nota)

    alumno1 = Alumno()           # crear objeto
    alumno1.crear(nombre, calificaciones)

    alumno1.imprimir()           # llamar métodos
    alumno1.estado()

