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
    buscado = input("Ingrese clave a modificar: ")
    for persona in arreglo:
        if buscado in persona:
            persona[buscado][0] = input("Ingrese nombre modificado: ")
            persona[buscado][1] = input("Ingrese ocupacion modificada: ")
            persona[buscado][2] = input("Ingrese sueldo modificado: ")
            print("Empleado modificado correctamente.")
            return
    print("Clave no encontrada.")

modificar(usuarios)
imprimir(usuarios)