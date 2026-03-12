import random

lista=[]
cinco=5
lista.append(cinco)

for i in range(4):
    numero=random.randint(0,4)
    lista.append(numero)

print(lista)

def cargar(arreglo):
    arreglo.clear()
    arreglo.append(5)
    for i in range(4):
        numero=random.randint(0,4)
        arreglo.append(numero)
    print("nueva lista:", arreglo)

def mezclar(arreglo):
    random.shuffle(arreglo)


if 1 in lista:

    while lista[0] != 1:
        mezclar(lista)
        print(lista)

else:

    cargar(lista)