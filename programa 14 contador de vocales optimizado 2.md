🧩 Programa 12 – Conteo de vocales usando lista de referencia
📌 Descripción

Este programa toma una palabra predefinida ("MurciElagO"), la convierte a mayúsculas y cuenta cuántas vocales contiene utilizando una lista que almacena las vocales.

Cada vez que encuentra una vocal, incrementa el contador y muestra el valor acumulado.

🧠 Conceptos trabajados

Método .upper() para normalización

Listas como estructura de referencia

Operador in para pertenencia

Variable acumuladora

Recorrido directo sobre strings

Comparación eficiente

💻 Código
palabra = "MurciElagO"
mayuscula = palabra.upper()
vocales = ["A", "E", "I", "O", "U"]
cantidad = 0

for letras in mayuscula:
    if letras in vocales:
        cantidad += 1
        print(cantidad)