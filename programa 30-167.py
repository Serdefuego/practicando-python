empleado = []
condicion = "si"

while condicion == "si":
    #creo un diccionario vacio 
    usuario = {}
    #pido la clave y los demas datos
    clave = input("ingrese numero clave: ")
    nombre = input("ingrese nombre: ")
    profesion = input("ingrese profesion: ")
    sueldo = input("ingrese sueldo: ")
    #al diccionario le asigno el valor clave como nombre de  la propiedad
    #y ademas le inserto dentro una lista con los valores que pedi
    usuario[clave] = [nombre, profesion, sueldo]
    #agrego el diccionario al arreglo
    empleado.append(usuario)
    condicion = input("desea seguir agregando? si/no: ")

def imprimir(arreglo):
    #por cada persona en arreglo
    for personas in arreglo:
        #por clave,datos n persona.items()
        for clave, datos in personas.items():
            print(clave, datos[0], datos[1], datos[2])

def modificar(arreglo):
    buscar = input("clave para modificar el sueldo: ")
    for personas in arreglo:
        if buscar in personas:
            personas[buscar][2] = input("ingrese sueldo modificado: ")
            print("sueldo modificado")
    imprimir(arreglo)

imprimir(empleado)
modificar(empleado)