import random
arreglo=[]

for i in range(10):
    numero=random.randint(0,10)
    arreglo.append(numero)

print (arreglo)

def mezclar(arreglo):
  
    for i in range(10):
        posicion=random.randint(0,9)
        aux=arreglo[i]
        arreglo[i]=arreglo[posicion]
        arreglo[posicion]=aux
mezclar(arreglo)
print(arreglo)