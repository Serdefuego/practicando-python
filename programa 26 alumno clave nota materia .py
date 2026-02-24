diccionario={}
def ingresaTres():
    for i in range(3):
        nombre=input("ingrese nombre")
        nota=int(input("ingrese nota"))
        materia=input("ingrese materia")
        valores=(nombre,materia,nota)
        diccionario[i]=valores
    print(diccionario)

ingresaTres()

print(diccionario[0][0])