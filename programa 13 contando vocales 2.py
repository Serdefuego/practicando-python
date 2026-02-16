palabra="MuRciElAGo"
vocales=["A","E","I","O","U",]
cantidad=0
mayuscula=palabra.upper()

for i in range(len(mayuscula)):
    for x in range(len(vocales)):
        if mayuscula[i]==vocales[x]:
            cantidad+=1
print(cantidad)