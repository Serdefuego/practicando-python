cantidad=int(input("ingrese cantidad de familias a confeccionar"))
familias=[]
engendros=[]
for i in range(cantidad):
    padre=input("ingrese nombre de padre")
    madre=input("ingrese nombre de madre")
    familias.append([padre,madre])


for x in range(len(familias)):
       cantidadDHijos=int(input("ingrese cant de hijos"))
       for j in range(cantidadDHijos):
        engendros.append([])
        nombre=input("ingrese nombre de hijx")
        engendros[j].append(nombre)
print(familias)
print(engendros)