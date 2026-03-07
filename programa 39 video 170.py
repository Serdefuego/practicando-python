meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")
def imprime(nombre,cantidad):
    print(nombre[0:cantidad])

def devuelvePorcion(mes):
    cantidad=int(input("ingrese la cantidad de caracteres que quiere ver impreso "))
    for nombre in mes:
        imprime(nombre,cantidad)
       

devuelvePorcion(meses)