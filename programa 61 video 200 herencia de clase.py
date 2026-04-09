class Operacion():
    def __init__(self):
        self.valor1=int(input("ingrese primer valor "))
        self.valor2=int(input("ingrese segundo valor "))
        self.resultado()
    

class Suma():
    def __init__(self):
        super(Operacion).__init__()

        def resultado(self):
            print(self.valor1+self.valor2)

class Resta():
    def __init__(self):
        super(Operacion).__init__()

        def resultado(self):
            print(self.valor1-self.valor2)

nuevo=Resta()