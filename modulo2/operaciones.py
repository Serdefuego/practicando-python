def mayor(arreglo):
    mayor = arreglo[0]
    for i in range(len(arreglo)):
        if arreglo[i] > mayor:
            mayor = arreglo[i]

    print("el mayor es", mayor)


def menor(arreglo):
    menor = arreglo[0]
    for i in range(len(arreglo)):
        if arreglo[i] < menor:
            menor = arreglo[i]

    print("el menor es", menor)