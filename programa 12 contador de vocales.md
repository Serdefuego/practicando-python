🧩 Programa 11 – Contador de Vocales
📌 Descripción

Este programa solicita al usuario que ingrese una frase y calcula cuántas veces aparece cada vocal (a, e, i, o, u).

Primero convierte la frase a minúsculas para evitar problemas con mayúsculas y luego recorre el texto carácter por carácter contando cada vocal.

🧠 Conceptos trabajados

Manipulación de strings

Método .lower()

Recorrido por índice con range(len())

Estructura condicional if / elif

Variables acumuladoras

Procesamiento carácter por carácter

💻 Código
frase = input("ingrese frase")
preparado = frase.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for x in range(len(preparado)):
    if preparado[x] == "a":
        a += 1
    elif preparado[x] == "e":
        e += 1
    elif preparado[x] == "i":
        i += 1
    elif preparado[x] == "u":
        u += 1    
    elif preparado[x] == "o":
        o += 1

print("tu frase contiene ", a ," :a ", e ," :e ", i ," :i ", o ," :o ", u ," :u ")