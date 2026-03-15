def capituca(palabra):
    largo=(len(palabra))
    similitudes=0
    for i in range(largo):
        if palabra[i]==palabra[-i-1]:
            similitudes+=1
    if similitudes==largo:
        print("es capicua")
    else:
        print("no es capicua")

ingreso=input("ingrese palabra")
capituca(ingreso)