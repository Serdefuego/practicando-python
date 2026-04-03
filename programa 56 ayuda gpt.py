arregloDeAlumno = []

class Alumnos:
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.notas = []
        self.cargarNota()

    def cargarNota(self):
        for i in range(3):
            nota = int(input("Ingrese nota: "))
            self.notas.append(nota)

    def aprobo(self):
        def aprobo(self):
         aprobo = False
         for nota in self.notas:
            if nota >= 7:
                aprobo = True
         return aprobo

# Cargar alumnos
for i in range(2):
    alumno = Alumnos()
    arregloDeAlumno.append(alumno)

# Mostrar los que aprobaron
for persona in arregloDeAlumno:
    if persona.aprobo():
        print(persona.nombre)
