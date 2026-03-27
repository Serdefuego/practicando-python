arregloDeAlumno=[]

class Alumnos:
     def __init__(self):
        self.nombre=input("ingrese nombre")
        self.notas=[]
        self.cargarNota(self.notas)
        
        def cargarNota(arreglo):
            for i in range(3):
                nota=int(input("ingrse nota"))
                arreglo.append(nota)

for i in range (2):
    alumno=Alumnos
    arregloDeAlumno.append(alumno)



