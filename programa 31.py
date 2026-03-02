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
        # Para cada diccionario, obtenemos su única clave
        for clave in persona.keys():
            datos = persona[clave]
            print(f"Clave: {clave}, Nombre: {datos[0]}, Ocupación: {datos[1]}, Sueldo: {datos[2]}")

imprimir(usuarios)