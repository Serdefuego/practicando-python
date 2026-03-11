lista=[]
for i in range (3):
    palabra=input("ingrese palabra")
    lista.append(palabra)

print(lista)

def intercambia(arreglo):
    aux=0
    aux=arreglo[-1]
    arreglo[-1]=arreglo[0]
    arreglo[0]=aux
    print (arreglo)

intercambia(lista)