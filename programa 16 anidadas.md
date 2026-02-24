# 📋 Ejercicio: Lista de Listas en Python

## 📌 Descripción

Este programa crea una estructura de datos utilizando listas anidadas (lista de listas).

El usuario ingresa datos por teclado y el programa los organiza en una matriz de 3 filas y 2 columnas.

## 🧠 ¿Qué conceptos se practican?

- Listas en Python
- Listas anidadas
- Bucles `for`
- Uso de `range()`
- Entrada de datos con `input()`

## 🛠 Funcionamiento

1. Se crean 3 listas vacías dentro de una lista principal.
2. Se solicitan 2 datos para cada lista interna.
3. Los datos se almacenan en la estructura.
4. Finalmente se imprime la lista completa.

## 💻 Código

```python
personas = []

for i in range(3):
    datos = []
    for j in range(2):
        nombre = input("Ingrese nombre: ")
        datos.append(nombre)
    personas.append(datos)

print(personas)