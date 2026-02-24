🧩 Programa 5 – Juego con while y operador lógico or
📌 Descripción

Este programa simula un pequeño juego interactivo donde:

El usuario ingresa un número.

Si el número es 7 o 3, gana.

En cualquier otro caso, pierde.

Luego puede decidir si desea volver a intentarlo.

El programa utiliza un bucle while para mantener el juego activo hasta que el usuario decida salir.

🧠 Conceptos trabajados

Bucles while

Operadores lógicos (or)

Estructuras condicionales anidadas

Control de flujo

Interacción continua con el usuario

Reasignación de variables dentro de un ciclo

💻 Código
num = int(input("Ingrese numero: "))
condicion = "si"

while condicion == "si":
    if num == 7 or num == 3:
        print("Ganó")
        print("desea intentarlo nuevamente?")
        condicion = input("si/no")
        num = int(input("Ingrese numero: ")) 
    else:
        print("perdió") 
        print("desea intentarlo nuevamente?")
        condicion = input("si/no")
      
        if condicion != "si":
            print("gracias por juegar hasta luego")
        else:
            num = int(input("Ingrese numero: ")) 