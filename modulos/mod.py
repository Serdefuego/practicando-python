def cargar(arreglo):
    for i in range(3):
        numero=int(input("ingrese numero"))
        arreglo.append(numero)

def sumar(arreglo):
    suma=0
    for i in range(len(arreglo)):
        suma+=arreglo[i]
    print("la suma de todo es: ",suma)

def maximo(arreglo):
    maximo=arreglo[0]
    for i in range(len (arreglo)):
        if arreglo[i]>maximo:
            maximo=arreglo[i]
    print("el valor mas grande es ",maximo)
