valores=[]
resultado=0
for i in range(3):
    valor=int(input("ingrese numero"))
    valores.append(valor)

for i in valores:
    resultado+=i

print("la suma de los numeros ingresados es de: ",resultado)