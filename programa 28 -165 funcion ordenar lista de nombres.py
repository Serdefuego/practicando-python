def ordenar(arreglo):

    for i in range(len(arreglo)-1):
        for j in range(len(arreglo)-1):
            if arreglo[j]>arreglo[j+1]:
                aux=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=aux
    return(arreglo)



nombres=["marcos","pedro","gato","alda"]

ordenados=ordenar(nombres)
print(ordenados)
