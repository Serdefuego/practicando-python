cantidad=int(input("ingrese cantidad de personas"))

personas=[]

for i in range(cantidad):
    objeto={
        "nombre":input("ingrese nombre"),
        "edad":int(input("ingrese edad"))
    }
    personas.append(objeto)

for elementos in personas:
    print(elementos["nombre"])