''' Ejercicio 3
Crea esta estructura:
empleados = [
    {"clave": "001", "nombre": "Ana", "sueldo": 5000},
    {"clave": "002", "nombre": "Luis", "sueldo": 7000}
]
Imprime todos los nombres
Encuentra el sueldo mayor
Busca por clave y muestra los datos '''
usuarios=[]
def persona():
    diccionario={}
    diccionario["clave"]=int(input("ingrese edad"))
    diccionario["nombre"]=input("ingrese nombre")
    diccionario["sueldo"]=float(input("ingrese sueldo"))
    usuarios.append(diccionario)

def mayorSueldo(persona):
    mayor=0
    for i in persona:
        if i["sueldo"]>mayor:
            mayor=i["sueldo"]
    for items in persona:
        if items["sueldo"]==mayor:
            print("el mayor es" ,items["nombre"],"con un sueldo de ",items["sueldo"])

def ingresos():
    cantidad=int(input("ingrese cantidad de usuarios"))
    for i in range (cantidad):
        persona()

ingresos()
mayorSueldo(usuarios)
    
