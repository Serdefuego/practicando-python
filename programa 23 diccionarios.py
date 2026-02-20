cantidad=int(input("ingrese cantidad de personas"))

personas=[]



""" def buscar(dni):

    for usuarios in personas:
        if usuarios["documento"]==dni:
            print("se ha encontrado que ",usuarios["nombre"],"coincide con el dni")
        else:
            print("no se encontro ningun usuario con ese dni") esta linea da multiples repeticiones por lo tanto
             se realiza con una bandera """

def buscar(dni):
    encontrado = False
    
    for usuarios in personas:
        if usuarios["documento"] == dni:
            print("Se ha encontrado que", usuarios["nombre"], "coincide con el dni")
            encontrado = True
            break
    
    if not encontrado:
        print("No se encontró ningún usuario con ese dni")

def imprimir(arregloDePersonas):
    print("estas son todas las personas del arreglo")
    for items in arregloDePersonas:
        print(items["nombre"])
        print(items["documento"])

for i in range(cantidad):
    objeto={
        "nombre":input("ingrese nombre"),
        "documento":int(input("ingrese dni"))
    }
    personas.append(objeto)

buscando=int(input("ingrese dni de la persona que desea encontrar"))

imprimir(personas)

buscar(buscando)