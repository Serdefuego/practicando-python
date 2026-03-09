def cargar():
    lista=[]
    for i in range(10):
        numero=int(input("ingrese numero: "))
        lista.append(numero)
    return lista

valores = cargar()

def imprimir(valores):
    for i in range(len(valores)//2):
        print(valores[i])

imprimir(valores)