🧩 Programa 4 – Condicional con Operador Lógico and
📌 Descripción

Este programa solicita al usuario su edad y sexo, y determina si puede ingresar sin pagar según una condición específica:

Debe ser mayor o igual a 18 años

Debe ser de sexo femenino

Si ambas condiciones se cumplen, puede ingresar sin pagar.

🧠 Conceptos trabajados

Entrada de datos con input()

Conversión de tipos (int)

Operadores relacionales (>=)

Operadores lógicos (and)

Comparación de strings

Evaluación de múltiples condiciones

💻 Código
edad = int(input("ingrese edad"))
sexo = input("masculino/femenino")

if edad >= 18 and sexo == "femenino":
    print("puede ingresar sin pagar")
else:
    print("no puede ingresar")