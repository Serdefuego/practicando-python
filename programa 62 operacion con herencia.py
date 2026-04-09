class Operacion():
    def __init__(self):
        self.valor1=int(input("ingrese valo 1"))
        self.valor2=int(input("ingrese valo 2"))

class Suma(Operacion):
    def __init__(self):
        super().__init__()
        self.sumar()
    def sumar(self):
        print("el resultado de la suma es")
        print(self.valor1+self.valor2)    

nuevaOperacion=Suma()