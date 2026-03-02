contactos=[]
def cargar(arreglo):
    condicion="s"
    while condicion!="n":
        persona={}
        persona["nombre"]=input("ingrese nombre")
        persona["telefono"]=input("ingrese telefono")
        contactos.append(persona)
        condicion=input("desea seguir agregando s/n")

def modificar(arreglo):
    busca=input("que contacto desea usted modificar")
    for usuario in arreglo:
        if busca==usuario["nombre"]:
            usuario["nombre"]=input("ingrese la modificacion del nombre")
            usuario["telefono"]=input("ingrese la modificacion del telefono")
        else:
            print("no se encuentra esa persona en la agenda")
        
                

def imprimir(arreglo):
    print("esta es su agenda")
    for usuarios in arreglo:
        print(usuarios["nombre"],usuarios["telefono"])
    condicion="n"
    while condicion!="n":
        modificar(arreglo)
    else:
        print("gracias por usar este programa")
cargar(contactos)
imprimir(contactos)
modificar(contactos)
imprimir(contactos)