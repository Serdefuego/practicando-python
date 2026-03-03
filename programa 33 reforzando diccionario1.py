''' Ejercicio 2

Crea un diccionario así:

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "México"
}

Imprime solo el nombre

Cambia la edad a 35

Agrega una nueva clave llamada "ocupacion" '''

def persona():
    diccionario={}
    diccionario["nombre"]=input("ingrese nombre")
    diccionario["edad"]=input("ingrese edad")
    diccionario["ciudad"]=input("ingrese ciudad")
    return diccionario

nuevaPersona=persona()

print(nuevaPersona)