🧩 Programa 10 – Manipulación de Strings
📌 Descripción

Este programa solicita al usuario que ingrese un nombre y muestra distintas transformaciones del texto:

Todo en mayúsculas

Todo en minúsculas

Capitalizado (primera letra en mayúscula)

El objetivo es practicar métodos de manipulación de cadenas en Python.

🧠 Conceptos trabajados

Entrada de datos con input()

Métodos de strings:

.lower()

.upper()

.capitalize()

Almacenamiento en variables

Salida formateada en consola

💻 Código
nombre = input("ingrese nombre")

nombreMinuscula = nombre.lower()
nombreMayuscula = nombre.upper()
nombreCapitalizado = nombre.capitalize()

print("nombre en mayuscula")
print(nombreMayuscula)

print("nombre en minuscula")
print(nombreMinuscula)

print("nombre capitalizado")
print(nombreCapitalizado)