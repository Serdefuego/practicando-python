🧩 Programa 17 Registro de estudiantes con calificaciones (listas anidadas)
📌 Descripción

Este programa permite:

Ingresar nombres de estudiantes.

Ingresar dos calificaciones por cada estudiante.

Almacenar los nombres y las notas en listas separadas.

Mostrar ambas estructuras al final.

Se trabaja con listas anidadas para representar datos relacionados.

🧠 Conceptos trabajados

Listas anidadas

Uso de índices en listas

Bucles for

Relación entre estructuras paralelas

Organización básica de datos

💻 Código
estudiantes = []
calificaciones = []

for i in range(3):
    estudiantes.append([])
    nombre = input("ingrese nombre")
    estudiantes[i].append(nombre)

for j in range(len(estudiantes)):
    nota_1 = int(input("ingrese primer notas"))
    nota_2 = int(input("ingrese nota 2"))
   
    calificaciones.append([nota_1, nota_2])

print(estudiantes)
print(calificaciones)