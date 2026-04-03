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

# Cargar alumnos
for i in range(2):
    alumno = Alumnos()
    arregloDeAlumno.append(alumno)

# Mostrar alumnos con notas >= 7
for persona in arregloDeAlumno:
    for nota in persona.notas:
        if nota >= 7:
            print(persona.nombre)
            break  # para no repetir el nombre varias veces