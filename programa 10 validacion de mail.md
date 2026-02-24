🧩 Programa 9 – Validación básica de email
📌 Descripción

Este programa solicita al usuario que ingrese un correo electrónico y valida que contenga los caracteres "@" y ".".

El programa continúa solicitando el correo hasta que el formato sea considerado válido.

🧠 Conceptos trabajados

Bucle infinito while True

Uso de break

Validación de datos

Operador in para búsqueda en strings

Control de flujo condicional

Manejo de entrada del usuario

💻 Código
while True:

    mail = input("Ingrese mail: ")

    if "@" in mail and "." in mail:
        print("Mail correcto")
        break
    else:
        print("Mail incorrecto")