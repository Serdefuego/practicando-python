estudiantes=[]
calificaciones=[]


for i in range(3):
    estudiantes.append([])
    nombre=input("ingrese nombre")
    estudiantes[i].append(nombre)
for j in range(len(estudiantes)):
    nota_1=int(input("ingrese primer notas"))
    nota_2=int(input("ingrese nota 2"))
   
    calificaciones.append([nota_1,nota_2])
print(estudiantes)
print(calificaciones)