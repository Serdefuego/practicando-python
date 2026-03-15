class Alumno:
    def crear(self,nom,nota):
        self.nombre=nom
        self.nota=nota

    
    def imprimir(self):
        print("mi nombre es", self.nombre ,"y me saqué un",self.nota)

    def estado(self,nota):
        suma=0
        for i in range(len(self.nota)):
            suma+=self.nota[i]

        promedio=suma/len(self.nota)
        print("el promedio es de ",promedio)

def salon():
    nombre=input("ingrese nombre")
    calificaciones=[]

    for i in range(3):
        nota=int(input("ingrese nota"))
        calificaciones.append(nota)

    Alumno.crear(nombre,calificaciones)
    Alumno.imprimir
    Alumno.estado

salon()