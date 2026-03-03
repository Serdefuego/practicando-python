usuarios = []
condicion = "si"

while condicion == "si":
    empleado = {}
    clave = input("ingrese clave: ")
    nombre = input("ingrese nombre: ")
    ocupacion = input("ingrese ocupacion: ")
    sueldo = input("ingrese sueldo: ")
    empleado[clave] = [nombre, ocupacion, sueldo]
    usuarios.append(empleado)
    condicion = input("desea continuar (si/no): ")

def imprimir(arreglo):
    for persona in arreglo:
     
        for clave in persona.keys():
            datos = persona[clave]
            print(f"Clave: {clave}, Nombre: {datos[0]}, Ocupación: {datos[1]}, Sueldo: {datos[2]}")

imprimir(usuarios)

def modificar(arreglo):
    buscado=input("ingrese clave")

    for persona in arreglo:
        if (persona[clave]==buscado):
            persona[0]=input("ingrese nombre modificado")
            persona[1]=input("ingrese ocupacion")
            persona[2]=input("sueldo")
modificar(usuarios)
imprimir(usuarios)