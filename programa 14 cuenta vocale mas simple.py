palabra="MurciElagO"
mayuscula=palabra.upper()
vocales=["A","E","I","O","U"]
cantidad=0

for letras in mayuscula:
  if letras in vocales:
    cantidad+=1
    print(cantidad)
    
