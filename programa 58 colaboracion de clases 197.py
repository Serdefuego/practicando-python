import random
class Dado():
    def __init__(self):
        self.lanzar()
        self.imprimir()

    def lanzar(self):
            self.valor= random.randint(1,6)
            return self.valor               
    
    def imprimir(self):
        print(self.valor)
    


arregloDeDados=[]
# Tirar 3 dados
for i in range(3):
    dado = Dado()
    valor = dado.lanzar()
    arregloDeDados.append(valor)

# Mostrar resultados
print("Dados:", arregloDeDados)

# Verificar si son iguales
if arregloDeDados[0] == arregloDeDados[1] == arregloDeDados[2]:
    print("Ganaste, son todos iguales 🎉")
else:
    print("Perdiste 😢")