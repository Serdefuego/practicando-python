import random
class Dado:

    def lanzar(self):
        self.valor=random.randint(1,6)
    def imprimir(self):
        print("el valor es ",self.valor)
    def retornar(self):
        return self.valor
class Juego:
    def __init__(self):
        dado1=Dado()
        dado1.lanzar()
        self.valor1=dado1.retornar()
        dado2=Dado()
        dado2.lanzar()
        self.valor2=dado2.retornar()
        dado3=Dado()
        dado3.lanzar()
        self.valor3=dado3.retornar()
        self.comparar()

    def comparar(self):
        if self.valor1==self.valor2 and self.valor1==self.valor3:
            print("ganaste, los 3 dados son iguales")
            print(self.valor1,self.valor2,self.valor3)
        else:
            print("perdiste los dados poseen valores distintos")
            print(self.valor1,self.valor2,self.valor3)        

#bloque principal
nuevo=Juego()