import random
''' creo una lista donde inserto el 5 '''
lista=[]
cinco=5
lista.append(cinco)

''' le agrego 4 numeros random a la lista '''
for i in range(4):
    numero=random.randint(0,4)
    lista.append(numero)

print(lista)

''' defino la funcion para cargar el arreglo con numeros nuevos limpiando la lista previa '''
def cargar(arreglo):
    arreglo.clear()
    arreglo.append(5)
    for i in range(4):
        numero=random.randint(0,4)
        arreglo.append(numero)
    print("nueva lista:", arreglo)

''' defino la funcion para mezclar '''
def mezclar(arreglo):
    random.shuffle(arreglo)

''' si 1 esta incluido en la lista hacer... '''
'''  mientras que la lista en la posicion 0 sea!= de 1 '''
if 1 in lista:
    while lista[0] != 1:
        mezclar(lista)
        print(lista)

else:
    cargar(lista)