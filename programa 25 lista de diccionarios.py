
condicion="si"
actividades=[]

while condicion != "no":

    actividad=input("ingrese actividad")
    fecha=input("ingrese fecha")
    hora=input("ingrese hora")

    propuesta={fecha,(actividad,hora)}
    actividades.append(propuesta)
    condicion=input("desea seguir agregando")

if condicion=="no":
    print(actividades)
