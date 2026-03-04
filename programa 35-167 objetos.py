arreglo=[]
def menu ():
    seleccione=input("ingrese 1 para cargar empleado /" \
                    "2 imprimir" \
                    "3 para modificar empleado" \
                    "4 para eliminar empleado" \
                    "5 para salir")
    if seleccione=="1":
        cargar(arreglo)
    elif seleccione=="2":
        imprimir(arreglo)
    elif seleccione=="3":
        modificar(arreglo)
    elif seleccione=="4":
        eliminar(arreglo):
    elif seleccione=="5":
        salir()

def cargar(arreglo):
    cantidad=int(input("ingrese cantidad de empleados a subir"))
    for i in range(cantidad):
        diccionario={}
        diccionario["edad"]=input("ingrese edad")
        diccionario["nombre"]=input("ingrese nombre")
        diccionario["sueldo"]=input("ingrese sueldo")
        arreglo.append(diccionario)
    menu()

def imprimir(arreglo):
    for elemento in arreglo:
        print("edad:",elemento["edad"],"nombre",elemento["nombre"],"sueldo",elemento["sueldo"])
    menu()


        
def modificar(arreglo):
    buscar=input("ingrese persona a modificar")

    for personas in arreglo:
        if personas["nombre"]==buscar:
            personas["edad"]=input("ingrese edad")
            personas["nombre"]=input("ingrese nombre")
            personas["sueldo"]=input("ingrese sueldo")
    menu()



def salir():
        print("gracias por utilizar el programa")

