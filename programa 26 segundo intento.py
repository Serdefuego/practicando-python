condicion="s"
alumnos=[]
while condicion!="n":
    dni=input("ingrese dni")
    nombre=input("ingrese nombre")
    nota=input("ingrese nota")
    alumno={}
    alumno["documento"]=dni
    alumno["identidad"]=nombre
    alumno["calificacion"]=nota
    alumnos.append(alumno)
    condicion=input("quiere seguir agregando? s/n")
for estudiante in alumnos:
    print(estudiante["identidad"],estudiante["calificacion"])

def buscar():
    busqueda=input("ingrese nombre de persona que busca")
    for persona in alumnos:
        if(persona["identidad"]==busqueda):
            print("se encontro que ",busqueda,"tiene una calificacion de",persona["calificacion"])    
buscar()