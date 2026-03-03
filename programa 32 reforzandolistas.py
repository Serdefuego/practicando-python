''' ##Ejercicio 1
Crea una lista con 5 números y:
Imprime el primero
Imprime el último
Imprime la suma de todos
Ejemplo esperado: '''

lista=[]

def cargar (arreglo):
    for i in range (5):
        numero=int(input("ingrese numero"))
        lista.append(numero)

def imprimeSuma(arreglo):
    suma=0
    for i in range (len(arreglo)+1):
        suma+=i

    print("la suma de todos los numeros del arreglo es ",suma)

def imprimiPimero(arreglo):
    print("el primero del arreglo es ",arreglo[0])

def imprimeUltimo(arreglo):
    imprir=len(arreglo)
    print("el ultimo numero del arreglo es ",arreglo[imprir-1])

cargar(lista)

imprimiPimero(lista)
imprimeUltimo(lista)
imprimeSuma(lista)