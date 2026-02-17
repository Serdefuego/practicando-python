personas=[]
for i in range (3):
    personas.append([])
for i in range(2):    
    for i in range(len(personas)):
        nombre=input("ingrese nombre")
        personas[i].append(nombre)
print(personas)
