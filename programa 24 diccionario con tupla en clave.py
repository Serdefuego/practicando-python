productos = []

for i in range(3):
    nombre = input("Ingrese nombre del producto: ")
    valor = int(input("Ingrese valor del producto: "))
    cantidad = int(input("Ingrese cantidad del producto: "))

    info = (nombre, valor, cantidad)

    producto = {
        "info": info
    }

    productos.append(producto)

print("\nLista de productos:\n")

for paquete in productos:
    print(paquete)