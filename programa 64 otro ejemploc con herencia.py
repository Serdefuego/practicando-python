class Personaje():
    def __init__(self):
        self.nombre=input("ingrese nombre")
        self.saludar()
    def saludar(self):
        print("hola mi nombre es", self.nombre,"soy un ",self.tipo)
        print("mi poder es de ",self.poder)
        

class Mago(Personaje):
    def __init__(self):
        super().__init__()  
        super().saludar()
        self.tipo="mago"
        self.poder=20

nuevo=Mago()