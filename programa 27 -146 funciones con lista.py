import random

arreglo = []

def cargarListas():
    for i in range(10):
        numero = random.randint(1, 100)
        arreglo.append(numero)

def cero():
    for i in range(len(arreglo)):
        if arreglo[i] > 50:
            arreglo[i] = 0

cargarListas()
print("Lista original:", arreglo)

cero()
print("Lista modificada:", arreglo)