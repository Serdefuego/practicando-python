🧩 Programa 7 – Lista de nombres con for
📌 Descripción

Este programa permite al usuario ingresar tres nombres, almacenarlos en una lista y luego mostrarlos en pantalla.

Se utiliza un bucle for para capturar los datos y otro para recorrer la lista e imprimir los valores almacenados.

🧠 Conceptos trabajados

Listas ([])

Método .append()

Bucle for

Función range()

Función len()

Recorrido de estructuras de datos

Almacenamiento dinámico

💻 Código
nombres = []

for i in range(3):
    nombre = input("ingrese nombre: ")
    nombres.append(nombre)

for i in range(len(nombres)):
    print(nombres[i])