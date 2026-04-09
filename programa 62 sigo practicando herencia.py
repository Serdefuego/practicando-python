class Figura():
    def __init__(self):
        self.valor1=int(input("ingrese valor 1 "))
        self.valor2=int(input("ingrese valor 2 "))
        self.mostrarResultado()
    

    

class Cuadrado(Figura):
  super().__init__()
    self.operar()
    
    def operar(self):
        print(self.valor1*self.valor2)


nuevo =Cuadrado()