cantidad = int(input("Ingrese cantidad de familias: "))
familias = []
engendros = []

for i in range(cantidad):
    padre = input("Ingrese nombre del padre: ")
    madre = input("Ingrese nombre de la madre: ")

    familias.append([padre, madre])

    cantidad_hijos = int(input("Ingrese cantidad de hijos: "))
    hijos = []

    for j in range(cantidad_hijos):
        nombre_hijo = input("Ingrese nombre del hijo/a: ")
        hijos.append(nombre_hijo)

    engendros.append(hijos)

print("Familias:")
print(familias)

print("Hijos por familia:")
print(engendros)
